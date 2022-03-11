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
data_percentage = []
cols = [
    "Files with good practices",
    "TaskHasName",
    "Git",
    "Deprecated Modules",
    "NoTabs",
    "NoLocalAction",
    "PlaybookExtension",
    "EmptryString",
    "IgnoreErrors",
    "BooleanCompare",
    "BecomeUserWithoutBecome",
]
for dir_path in os.listdir(ROOT_FOLDER):
    print("Parsing in progress project directory:", dir_path)
    if dir_path == "ansible-cmdb":
        continue
    abs_path = ROOT_FOLDER + dir_path
    L = []
    L_percentage = []
    L.append(dir_path)
    L_percentage.append(dir_path)

    c = GPHasName("Task naming", "Lowest")
    c.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(c.evaluate())
    L_percentage.append(c.evaluate_percentage())

    t = GitGP()
    t.parse(abs_path)
    L.append(t.evaluate())
    L_percentage.append(t.evaluate_percentage())

    d = DeprecatedModules()
    d.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(d.evaluate())
    L_percentage.append(d.evaluate_percentage())

    tabs = NoTabs()
    tabs.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(tabs.evaluate())
    L_percentage.append(tabs.evaluate_percentage())

    nolocal = NoLocalAction()
    nolocal.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(nolocal.evaluate())
    L_percentage.append(nolocal.evaluate_percentage())

    playbookExtension = PlaybookExtension()
    playbookExtension.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(playbookExtension.evaluate())
    L_percentage.append(playbookExtension.evaluate_percentage())

    emptyStr = EmptyStringCompare()
    emptyStr.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(emptyStr.evaluate())
    L_percentage.append(emptyStr.evaluate_percentage())

    ignore_error = IgnoreErrors()
    ignore_error.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(ignore_error.evaluate())
    L_percentage.append(ignore_error.evaluate_percentage())

    bool_compare = BooleanCompare()
    bool_compare.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(bool_compare.evaluate())
    L_percentage.append(bool_compare.evaluate_percentage())

    become_user = BecomeUserWithoutBecome()
    become_user.parse(parser.parseDirectoryForTasks(abs_path))
    L.append(become_user.evaluate())
    data.append(L)
    L_percentage.append(become_user.evaluate_percentage())
    data_percentage.append(L_percentage)

print("successfully parsed " + str(len(os.listdir(ROOT_FOLDER))) + " ansible projects")

df = pd.DataFrame(data, columns=cols)
df2 = pd.DataFrame(data_percentage, columns=cols)

wb = xw.Book("Example.xls")
sheet = wb.sheets["Example"]
sheet.range("A1").value = df
sheet.range("A1").options(pd.DataFrame, expand="table").value

sheet.range("A40").value = df2
sheet.range("A40").options(pd.DataFrame, expand="table").value
# sht1.range("B2").value = 45
# for i in range(len(data)):
#    for j in range(len(data[i])):
#        sht1.write(i, j, data[i][j])

wb.save()
