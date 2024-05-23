#--Magic/Dunder Methods--

class Employee:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
e = Employee("Harry")
print(str(e))


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(4, 6)
num2.showNumber()
# num3 = num1.add(num2) #without using dunder function just add()
# num3.showNumber()
num3 = num1 + num2 #after using dunder function -- __add__()
num3.showNumber()

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, v):
        return Vector(self.i + v.i, self.j + v.j, self.k + v.k)
v1 = Vector(3, 5, 6)
v2 = Vector(1, 2, 9)
print(v1 +v2)