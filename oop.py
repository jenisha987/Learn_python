
#--'is' VS '=='
a = 4
b = "4"
print(a is b) #exact location of memory
print(a == b) #value



#--OOP--

# Library Management System
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    
    def addBooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are :")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBooks("Harry Porter1")
l1.addBooks("Harry Porter2")
l1.addBooks("Harry Porter3")
l1.addBooks("Harry Porter4")
l1.addBooks("Harry Porter5")
l1.showInfo()



#--OOP--

#dir(), __dict__, help()
#dir()
x = [1, 2, 3]
print(dir(x)) #gives all the methods that can be done to any object
print(x.__add__)

#__dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("John", 30)
print(p.__dict__)   #self. garera j object banako xa tyo __dict__ ma aauxa and then they are printed in the form of dictioanry

#help()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("John", 30)
print(help(Person)) 





#--Creating Command Line Utility in Python--

#--Walrus Operator in Python--
a = True
# print(a = False) #Not Possible
print(a := False) #Usinf walrus operator it's possible

#walrus in while loop
numbers = [1, 2, 3, 4, 5]
while(n := len(numbers)) > 0:
    print(numbers.pop())

happy = True
print(happy)

print(happy := True)
foods = list()
while (food := input("What food do you like? : ")) != "quit":
    foods.append(food)
print(foods)

#--Shutil Module in Python--
import shutil
shutil.copy("CWH2.py", "CHW21.py")

shutil.copytree("clutterFolder", "mytutorial")

shutil.move("clutterFolder/file.file", "file.file")

shutil.rmtree("mytutorial") #delete the directory
    
