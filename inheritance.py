#--Inheritance--

#single inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

#multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

#--multiple inheritance--
#Example 1
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

# Example 2
class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")
class Dancer:
    def __init__(self, dance):
        self.dance = dance
        def show(self):
            print(f"The dance is {self.dance}")
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() #jun class paila xa ni line 270 tyo matra call garxa
print(DancerEmployee.mro()) #mro() defines kunai pani aauta method le kata kata khojxa vanera in order

#--Hybrid Inheritance--
class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1, Derived2):
    pass

#--Hierarchical Inheritance--
class BaseClass:
    pass
class D1(BaseClass):
    pass
class D2(BaseClass):
    pass
class D3(D1):
    pass
