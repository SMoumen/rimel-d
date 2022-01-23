from abc import ABC, abstractmethod
from pathlib import Path
import string


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


class GoodPractice(ABC):
    @abstractmethod
    def evaluate(self):
        return 0

    @abstractmethod
    def parse(self):
        return

    @abstractmethod
    def generateComment(self):
        return


class GPHasName(GoodPractice):
    def __init__(self, name, criticity, grade=0, maxgrade=0, comment=""):
        self.grade = grade
        self.maxgrade = maxgrade
        self.name = name
        self.criticity = criticity
        self.comment = comment

    def evaluate(self):
        print("Grade " +  str(self.grade) + " / " + str(self.maxgrade))
        return self.grade / self.maxgrade

    def generateComment(self):
        if self.grade == self.maxgrade:
            self.comment = (
                " You have correctly respected the " + self.name + " good practice! "
            )
        elif self.grade < self.maxgrade / 2:
            self.comment = (
                " Warning ! You should name your rule files in the main.yml file"
            )

    def parse(self, filelist):
        length = len(filelist)
        print("Evaluating " + str(length) + " files...")
        counter = 0
        gradeCounter = 0
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            strname = "name:"

            for line in f:
                if strname not in line:
                    continue
                if line.split("- name:", 1)[1] != "":
                # print("name isnt empty : " + line.split("- name:",1)[1])
                    gradeCounter += 1
                counter += 1

        self.maxgrade = counter
        self.grade = gradeCounter
        self.generateComment()


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
c = GPHasName("Task naming", "Lowest")
c.parse(parser.parseDirectoryForTasks("repo_examples"))
print(c.evaluate())
a = Answer(c)
a.printAnswer()
