from goodPractices.abstractClass import GoodPractice


class IgnoreErrors(GoodPractice):
    def __init__(
        self,
        name="ignore errors",
        criticity="HIGHEST",
        grade=0,
        maxgrade=0,
        comment="",
    ):
        self.grade = grade
        self.maxgrade = maxgrade
        self.name = name
        self.criticity = criticity
        self.comment = comment

    def evaluate(self):
        print("Evaluating Good Practice " + self.__class__.__name__)
        print("Found use of  " + str(self.grade) + " ignore erros")
        return 100 - (self.grade / self.maxgrade) * 100 

    def parse(self, filelist):


        for file in filelist:
            length = len(filelist)
        print("Evaluating " + str(length) + " files...")
        counter = 0
        badGradeCounter = 0
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            for line in f:
                    if "ignore_errors" in line:
                        print(
                            "Detected usage of ignore errors"
                            
                            + " in file "
                            + file
                        )
                        badGradeCounter += 1
            counter += 1

        self.maxgrade = counter
        self.grade = badGradeCounter

    def generateComment(self):
        return
