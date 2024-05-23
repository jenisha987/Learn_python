#Loops in Python

#While Loop
i = 1
while i <= 5:
    print("hello")
    i += 1

j = 1
while j <= 5:
    print(j)
    j += 1

k = 5
while k >= 1:
    print(k)
    k  -= 1



#For loop

nums = [1,2,3,4] #print individual element
for val in nums:
    print(val)


veggies = ["potato", "aalu"]
for val in veggies:
    print(val)


str = "Jenisha"
for char in str:
    if(char == 'n'):
        print("Found")
        break
else:
    print("END")