from goodPractices.abstractClass import GoodPractice

class PlaybookExtension(GoodPractice):
    def __init__(self, grade=0, badGradeCounter=0):
        self.grade = grade
        self.badGradeCounter = badGradeCounter
        self.criticity = "MEDIUM"

    def parse(self, filelist):
        print("Evaluating " + str(len(filelist)) + " files...")
        badGradeCounter = 0
        for file in filelist:
            if not (str(file).endswith(".yml") or str(file).endswith(".yaml")):
                print("The file " + file + " does not have the extension .yml or .yaml (malaise)\n")
                badGradeCounter += 1
        self.badGradeCounter = badGradeCounter
        self.grade = len(filelist)

    def evaluate(self):
        print("Evaluating Good Practice " + self.__class__.__name__)
        print(
            "Found "
            + str(self.badGradeCounter)
            + " / "
            + str(self.grade)
            + " files that contained wrong extension "
        )
        return 100 - (self.badGradeCounter / self.grade) * 100
        
