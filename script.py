import os
from pathlib import Path
from goodPractices.DeprecatedModules import DeprecatedModules
from goodPractices.Git import GitGP
from goodPractices.NoLocalActionInTask import NoLocalAction
from goodPractices.NoTabs import NoTabs
from goodPractices.TaskHasName import GPHasName


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
        L = []
        for path in pathlist:
            # because path is object not string
            path_in_str = str(path)
            L.append(path_in_str)
        return L


parser = Parser()

ROOT_FOLDER = "repo_database/"

for dir_path in os.listdir(ROOT_FOLDER):
    print("Parsing in progress project directory:", dir_path)
    abs_path = ROOT_FOLDER + dir_path
    c = GPHasName("Task naming", "Lowest")
    c.parse(parser.parseDirectoryForTasks(abs_path))
    print(c.evaluate())

    t = GitGP()
    t.parse(abs_path)
    print(t.evaluate())

    d = DeprecatedModules()
    d.parse(parser.parseDirectoryForTasks(abs_path))
    d.evaluate()

    tabs = NoTabs()
    tabs.parse(parser.parseDirectoryForTasks(abs_path))
    tabs.evaluate()
    
    nolocal = NoLocalAction()
    nolocal.parse(parser.parseDirectoryForTasks(abs_path))
    nolocal.evaluate()


a = Answer(c)
a.printAnswer()
