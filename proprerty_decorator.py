#--Property Decorator--

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

std1 = Student(97,98,99)
print(std1.percentage)

std1.phy = 86 #phy ko marks change hunxa but percentage nikalda paila kai value ma calculate vayera aauxa, so inorder to print the actual percentage we make a new function
print(std1.phy)
std1.calcPercentage()
print(std1.percentage) 

#above progarm in better way using property
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"    

std1 = Student(97,98,99)
print(std1.percentage)

std1.phy = 86
print(std1.phy)
print(std1.percentage) 

#--Polymorphism
print(1 + 2) #3
print("Jen" + "stha") #concatenate
print([1, 2, 3] + [4, 5, 6]) #merge