from goodPractices.abstractClass import GoodPractice


class BooleanCompare(GoodPractice):
    def __init__(
        self,
        name="BooleanCompare",
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
        print("Found use of  " + str(self.grade) + " deprecated modules")
        return (self.grade / self.maxgrade) * 100 

    def parse(self, filelist):

        banned_list = [
            "== True",
            "== False",
            "== false",
            "== true",
            "!= True",
            "!= False",
            "!= false",
            "!= true",
        ]
        for file in filelist:
            length = len(filelist)
        print("Evaluating " + str(length) + " files...")
        counter = 0
        badGradeCounter = 0
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            for line in f:
                for i in banned_list:
                    if i + ":" in line:
                        print(
                            "Detected usage of boolean comparison "
                            + i
                            + " in file "
                            + file
                        )
                        badGradeCounter += 1
            counter += 1

        self.maxgrade = counter
        self.grade = badGradeCounter

    def generateComment(self):
        return
