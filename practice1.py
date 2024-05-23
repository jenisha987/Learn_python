# Wap to input 2 numbers and print their sum

num1 = int(input("num1:"))
num2 = int(input("num2:"))
sum = num1 + num2
print("Sum =", sum)

# Wap to input side of a square and print its area

l = float(input("Enter side : "))
area = l*l
print("Area =", area) # print("Area =", l ** 2)

# input 2 floating point number and print their average

n1 = float(input("num1:"))
n2 = float(input("num2:"))
avg = (n1 + n2)/2
print("Average =", avg)

# input 2 numbers a and b. print ture if a>=b else false

a = int(input("Enter a :"))
b = int(input("Enter b :"))
print("True") if a >= b else print("False") #print(a>=b)


# input user's first name and print its length

name = input("First name :")
print(len(name))

str = "Hello $ can you be$ here$"
print(str.count("$")) # count '$' symbol in the string

#check if the number entered is even or odd
num = int(input("Enter number:"))
if(num%2 == 0):
    numb = "Even"
else:
    numb = "Odd"
print("Number is", numb)

     