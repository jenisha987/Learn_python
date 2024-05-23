#--Class Method--

class Person:
    name = "anonymmous"

    # def changeName(self, name):
    #     # self.name = name #changes the name of the object's attribute not class's attribute
    #     # Person.name = name #changes the name of the both class's attribute and object's attribute as RK
    #     self.__class__.name = "R" #same as 261  

    @classmethod
    def changeName(cls, name):
        cls.name = name #directly changes the name of the class's attribute
    
p1 = Person()
p1.changeName("RK")
print(p1.name)
print(Person.name)

#--Class Method as Alternative Constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
string = "John-1200"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromString(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
person = Person.fromString("John Doe,45")
print(person.name, person.age)


