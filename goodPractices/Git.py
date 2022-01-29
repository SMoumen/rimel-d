import os

from goodPractices.abstractClass import GoodPractice


class GitGP(GoodPractice):
    def __init__(self, name="Git", criticity="MEDIUM", grade=0, maxgrade=1, comment=""):
        self.name = name
        self.criticity = criticity
        self.grade = grade
        self.maxgrade = maxgrade
        self.comment = comment

    def evaluate(self):
        print("Grade " + str(self.grade) + " / " + str(self.maxgrade))
        return self.grade / self.maxgrade

    def parse(self, path):
        if ".git" in os.listdir(path):
            self.grade += 1
