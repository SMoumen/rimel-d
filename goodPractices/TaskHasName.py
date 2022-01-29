from goodPractices.abstractClass import GoodPractice


class GPHasName(GoodPractice):
    def __init__(self, name, criticity, grade=0, maxgrade=0, comment=""):
        self.grade = grade
        self.maxgrade = maxgrade
        self.name = name
        self.criticity = criticity
        self.comment = comment

    def evaluate(self):
        print("Evaluating Good Practice " + self.__class__.__name__)
        print("Grade " + str(self.grade) + " / " + str(self.maxgrade))
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
