name = input("name : ")
age = int(input("age : "))
price = float(input("prince : "))

print("My name is", name, "and I am", age, "years old")

#lists in python

marks = [12,45,78,90.9,30]
print(marks)

print(marks[0]) #accessing index of lists
print(marks[2])

print(len(marks))

student = ["Ram", 45, "Ktm"]
print(student)

#input three names from user and store in a list

x = input("name1: ")
y = input("name2: ")
z = input("name3: ")
list = [x,y,z]
print(list)

# OR
name = []
x = input("name1: ")
y = input("name2: ")
z = input("name3: ")
name.append(x)
name.append(y)
name.append(z)
print(name)

# OR
name =[]
name.append(input("name1: "))
name.append(input("name2: "))
name.append(input("name3: "))
print(name)

#extend() method in list
list = [1,2,3,4]
m = [600,877,800]
k = list + m
print(k) #concatenation of list and m but print(list) gives only the original one
print(list)
# list.extend(m) #list ko value haru paxadi m ko value rakhxa
print(list) #original ma nai change aauxa


#check if a list contain a palindrome of elements

list = [1,2,3,2,1]
copy = list.copy()
copy.reverse()
if(list == copy):
    print("Palindrome")
else:
    print("Not Palindrome")


# count the number of students with the "A" grade in following tuple

student = ("C","D","A","B","A","B","A")
print(student.count("A"))

#store the above values in a list and sort them from "A" to "D"

student = ["C","D","A","B","A","B","A"]
student.sort()
print(student)