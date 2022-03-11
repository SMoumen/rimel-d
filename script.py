import os
from pathlib import Path
from goodPractices.BecomeUserCheck import BecomeUserWithoutBecome
from goodPractices.BooleanCompare import BooleanCompare
from goodPractices.DeprecatedModules import DeprecatedModules
from goodPractices.EmptyStrCompare import EmptyStringCompare
from goodPractices.Git import GitGP
from goodPractices.IgnoreErrors import IgnoreErrors
from goodPractices.NoLocalActionInTask import NoLocalAction
from goodPractices.NoTabs import NoTabs
from goodPractices.TaskHasName import GPHasName
from goodPractices.PlaybookExtension import PlaybookExtension
import xlsxwriter
import xlwt
import pandas as pd
import xlwings as xw


class Answer:
    def __init__(self, goodPractice) -> None:
        self.goodPractice = goodPractice

    def printAnswer(self):
        print(
            "Evaluated Good Practice: %s" % self.goodPractice.name
            + " grade"
            + str(self.goodPractice.grade)
            + "\n criticity : "
            + self.goodPractice.criticity
            + self.goodPractice.comment
        )


class Parser:
    def parseDirectoryForTasks(self, directory):
        pathlist = Path(directory).glob("**/*.yml")
        bannedList = ["\.github", ".travis.yml", "\\meta\\", "\\.circleci\\", "\\.ci\\"]
        L = []
        for path in pathlist:
            # because path is object not string
            path_in_str = str(path)
            if any(ext in path_in_str for ext in bannedList):
                continue
            L.append(path_in_str)
        return L


parser = Parser()


def parseAndSlash(classNameList):
    for className in classNameList:
        e = className
        e.parse(parser.parseDirectoryForTasks(abs_path))
        print(e.evaluate)


ROOT_FOLDER = "repo_database/"
data = []
cols = [
    "",
    "TaskHasName",
    "Git",
    "Deprecated Modules",
    "NoTabs",
    "NoLocalAction",
    "PlaybookExtension",
    "EmptryString",
    "IgnoreErrors",
    "BooleanCompare",
    "BecomeUserWithoutBecome"
]
for dir_path in os.listdir(ROOT_FOLDER):
    print("Parsing in progress project directory:", dir_path)
    if dir_path == "ansible-cmdb":
        continue
    abs_path = ROOT_FOLDER + dir_path
    L = []
    L.append(dir_path)

    c = GPHasName("Task naming", "Lowest")
    c.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(c.evaluate())

    t = GitGP()
    t.parse(abs_path)
    L.append(t.evaluate())

    d = DeprecatedModules()
    d.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(d.evaluate())

    tabs = NoTabs()
    tabs.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(tabs.evaluate())

    nolocal = NoLocalAction()
    nolocal.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(nolocal.evaluate())

    playbookExtension = PlaybookExtension()
    playbookExtension.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(playbookExtension.evaluate())

    emptyStr = EmptyStringCompare()
    emptyStr.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(emptyStr.evaluate())

    ignore_error = IgnoreErrors()
    ignore_error.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(ignore_error.evaluate())

    bool_compare = BooleanCompare()
    bool_compare.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(bool_compare.evaluate())

    become_user = BecomeUserWithoutBecome()
    become_user.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(become_user.evaluate())
    data.append(L)

print("successfully parsed " + str(len(os.listdir(ROOT_FOLDER))) + " ansible projects")
df = pd.DataFrame(data, columns=cols)
wb = xw.Book("Example.xls")
sheet = wb.sheets["Example"]
sheet.range('A1').value = df
sheet.range('A1').options(pd.DataFrame, expand='table').value
#sht1.range("B2").value = 45
#for i in range(len(data)):
#    for j in range(len(data[i])):
#        sht1.write(i, j, data[i][j])

wb.save()
