#--Super Method--


class Car:
    def __init__(self, type):
        self.type = type
   
    @staticmethod
    def start():
        print("car Started..")
    
    @staticmethod
    def stop():
        print("Car Stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("pirus", "electric")
print(car1.type)

#Example of Super() keyword

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, language):
        # self.name = name
        # self.id = id  #instead of these two lines perform super() to call the parent class ko name and id so that no repeatition
        super().__init__(name, id)
        self.language = language
rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry Boy", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.language)