#--File I/O in Python--

f = open("demo.txt", "r")
data = f.read()
# data = f.readline() #reads one line at a time + extra line
# data = f.read(5) #print first 5 characters
print(data)
print(type(data))
f.close()

f = open("demo.txt", "w")
f.write("Hello I am Jenisha Shrestha.") #overwrites the existing data of the file
f.close()

f = open("demo.txt", "a")
f.write("\nI am very hungry.") #adds at the end of the data of the file
f.close()

f = open("demo.txt", "r+") #r+ mode overwrites the data from first
f.write("Ram")
f.close()

#WITH Syntax
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("New Data")

#Deleting a file
import os
os.remove("demo.txt")

#--Let's Practice--
f = open("practice.txt", "w")
f.write("Hi everyone\nwe are learning File I/O\nusing Python.\nI like programming in Python.")
f.close()

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Python.\nI like programming in Python.")


#replace all occurences of "Python" with "Py"
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Python", "Py")
print(new_data)
with open("practice.txt", "w") as f:
    f.write(new_data)


#search if the word "learning" exists in the file or not
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word)): #data.find("learning") #if(word in data), the better one
            print("Found")
        else:
            print("Not Found")
check_for_word()


#find in which line the word "learning" occurs
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1
print(check_for_line())


#print the count of even numbers
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data) #data are in string format , so need to covert in int values

    num = ""  #basic way
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]



nums = data.split(",") #better way --splits -> splits the list with comma
for value in nums:
    if(int(value) % 2 == 0):
        count += 1
print(count)
    

