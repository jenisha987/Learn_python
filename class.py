#--Class and Object in Python--

#Creating Class
class Student: 
    name = "Jenisha Shrestha"

s1 = Student()
s1.name = "Ram"
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    color = "Blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

#__init__ Function

class Student:
    def __init__(self): #default constructors
       pass
    def __init__(self, name, marks): #parameterized Constructor
        self.name = name
        self.marks = marks
        print("Creating New Student in Database")
s1 = Student("Karan", 88) #call __init__ function ech time object is created
print(s1.name, s1.marks)

s2 = Student("Arjun", 45)
print(s2.name, s2.marks)

#--Class and Instance Attributes
class Student:
    college = "Khwopa College"
    name = "Ram" #class attribute
    def __init__(self, name, marks): #parameterized Constructor
        self.name = name #object attribute > Class attribute
        self.marks = marks
        print("Creating New Student in Database")
s1 = Student("Karan", 88) #()used to call __init__ function
print(s1.name, s1.marks)

s2 = Student("Arjun", 45)
print(s2.name, s2.marks)
print(s2.college)
print(Student.college) #48 and 49 are same

#Methods
class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def welcome(self):
        print("Welcome,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 98)
s1.welcome()
print(s1.get_marks())

#--Access Specifiers/Modifiers--
#Private
class Employee:
    def __init__(self):
        self.__name = "Jenisha"
a = Employee()
# print(a.__name) #Can't access directly
print(a._Employee__name) #Can access indirectly

#Protected
class Student:
    def __init__(self):
        self._name = "Jenisha"
    def _funName(self):  #Protected Method
        return "Jenisha Shrestha"  
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)  #calling by ibject of Student Class
print(obj._funName())
print(obj1._name) #calling by ibject of Subject Class
print(obj1._funName())


#--Let's Practice--
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(self.name, "your average is", sum/3)
s1 = Student("Ram", [99,98,97])
s1.get_avg()

s1.name = "hari" #attribute value can be manipulted 
s1.get_avg()

#--Static Methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #decorator
    def hello():
        print("Hello")

s1 = Student("Ram", [99,98,97])
s1.hello()

#Abstration
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 = Car()
car1.start()

#--Let's Practice--
class Account:
    def __init__(self, bal, acc): 
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)



#--del Keyword--
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("jenisha")
del s1 #delete object
print(s1.name) #delete object ko attribute
del s1.name
print(s1.name)

#Private (like) attributes and methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()
p1 = Person()
print(p1.welcome())









#--Let's Practice--

#calculate area and perimeter using constructor
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius * self.radius
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
r = Circle(21)
print(r.area())
print(r.perimeter())

#Q2
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetail(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "70,000")

eng1 = Engineer("Elon Musk", 50)

e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetail()
eng1.showDetail()

#Q3
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > ord2.price


ord1 = Order("Chips", 40)
ord2 = Order("Tea", 20)

print(ord1 > ord2)



