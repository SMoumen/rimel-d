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
        return (self.grade / self.maxgrade) * 100

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
        badGradeCounter = 0
        badTokens = ['#', '---']
        for file in filelist:

            f = open(file, "r", encoding="utf8")
            strname = "name:"
            flag = False
            line_counter = 0
            for line in f:
                line_counter += 1
                if  any(ext in line for ext in badTokens):
                    continue 
                if line == '\n' and flag == False: 
                    flag = True
                    counter += 1 # task identified on next line 
                    continue
                if flag and strname in line and line.split("name:", 1)[1] != "":
                    flag = False
                    gradeCounter += 1
                    continue
                if flag and ((strname not in line) or (strname in line and line.split("name:", 1)[1] == "")):
                    badGradeCounter += 1
                    #print("Unamed task found on line " + str(line_counter) + "file " + file)
                    flag = False
                    continue

        self.maxgrade = counter
        self.grade = gradeCounter
        self.generateComment()
