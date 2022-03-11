from goodPractices.abstractClass import GoodPractice


class NoLocalAction(GoodPractice):
    def __init__(self, grade=0, badGradeCounter=0):
        self.grade = grade
        self.badGradeCounter = badGradeCounter
        self.criticity = "MEDIUM"

    def parse(self, filelist):
        print("Evaluating " + str(len(filelist)) + " files...")
        badGradeCounter = 0
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            linecounter = 0
            for line in f:
                linecounter += 1
                if "local_action" in line:
                    print(
                        "Presence of local_action detected on line "
                        + str(linecounter)
                        + " in file "
                        + file
                    )
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
            + " files that contained local action in task"
        )
        return str(self.grade - self.badGradeCounter) + " // " + str(self.grade)
    
    def evaluate_percentage(self):
        return str(100 - (self.badGradeCounter / self.grade) * 100) + "%"
        
