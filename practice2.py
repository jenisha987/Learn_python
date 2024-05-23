#Loops in Python


#--Practice Questions

# print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

#print numbers from 100 to 1
j = 100
while j >= 1:
    print(j)
    j -= 1

#print multiplication table of a number n
x = int(input("x : "))
i = 1
while i <= 10:
    print(x*i)
    i += 1

#print elements of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1

#search for a number x in this tuple:
number = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to be searched : "))
i = 0
while i < len(number):
    if(number[i] == x):
        print("Found at",i)
        break
    i += 1





#Let's Practice
#Print the elements of the list using loop

list = [1,4,9,16,25,36,49,81,100]
for val in list:
    print(val)

#Search the number in the tuple

tup = (1,4,9,16,25,36,49,81,100,16)
i = 0
x = int(input("Enter the item to be searched : "))
for val in tup:
    if(val == x):
        print("Found at index", i)
    i += 1







#Let's Practice
#find the sum of first n numbers

#using while loop
n = int(input("Enter the value of n : "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)

#using for loop
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#find the factorial of first n numbers

#using for loop
n = int(input("Enter the value of n : "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(fact)

#using while loop
n = n = int(input("Enter the value of n : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

