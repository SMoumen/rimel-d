from goodPractices.abstractClass import GoodPractice


class BecomeUserWithoutBecome(GoodPractice):
    def __init__(
        self,
        name="BecomeUserWithoutBecome",
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
        return str(self.maxgrade - self.grade) + " // " + str(self.maxgrade)

    def evaluate_percentage(self):
        return str(100 - (self.grade / self.maxgrade) * 100) + "%"

    def parse(self, filelist):

        for file in filelist:
            length = len(filelist)
        print("Evaluating " + str(length) + " files...")
        counter = 0
        badGradeCounter = 0
        flag = False
        previous_line = False
        for file in filelist:
            f = open(file, "r", encoding="utf8")
            for line in f:
                previous_line = False
                if "become:" in line:
                    flag = True
                    previous_line = True
                if "become_user" in line and flag == False:
                    print(
                        "Detected usage of become_users without become"
                        + " in file "
                        + file
                    )
                    badGradeCounter += 1
                if previous_line == False:
                    flag = False

            counter += 1

        self.maxgrade = counter
        self.grade = badGradeCounter

    def generateComment(self):
        return
