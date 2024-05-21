#--Enumerate function in Python--


a = [12, 6, 44, 77]
print(list(enumerate(a)))
for index, marks in enumerate(a):
    print(index, marks) 
    if(index == 1):
        print("Hello")

#Changing the start index

for index, marks in enumerate(a, start = 1):
    print(index, marks) 
    if(index == 1):
        print("Hello")