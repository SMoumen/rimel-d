from abc import ABC, abstractmethod


class Answer :
    
    def __init__(self,goodPractice) -> None:
        self.goodPractice = goodPractice

    
    def printAnswer(self) :
        print("EVALUATED GOOD PRACTICE : " + self.goodPractice.name + " grade : " + str(self.goodPractice.grade) + "\n criticity : " + self.goodPractice.criticity + self.goodPractice.comment)
    
    
   

class GoodPractice(ABC) :
    

    @abstractmethod
    def evaluate(self) : return 0
    
    @abstractmethod
    def parse(self) : return 
    
    @abstractmethod 
    def generateComment(self) : return


class GPHasName(GoodPractice) :
    
    
    def __init__(self,name,criticity,grade =0 ,maxgrade = 0,comment = "") : 
        self.grade = grade
        self.maxgrade = maxgrade
        self.name = name
        self.criticity =criticity
        self.comment = comment
    def evaluate(self) : return self.grade/self.maxgrade       
    
    def generateComment(self) : 
        if(self.grade == self.maxgrade) : self.comment = " You have correctly respected the " + self.name + " good practice! "
        elif(self.grade < self.maxgrade / 2) : self.comment = " Warning ! You should name your rule files in the main.yml file" 
          
    def parse(self) : 
        f = open("main.yml","r")
        str = "name:"
        counter = 0
        gradeCounter = 0
        for line in f : 
            if(str not in line) : continue
            if(line.split("- name:",1)[1] != ""):
                #print("name isnt empty : " + line.split("- name:",1)[1])
                gradeCounter += 1
            counter += 1
            
        self.maxgrade = counter
        self.grade = gradeCounter
        self.generateComment()
        

        
   
   




c = GPHasName("Naming","Lowest")
c.parse()
print(c.evaluate())
a = Answer(c)
a.printAnswer()

        
    
    


