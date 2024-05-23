#WAP capable of greeting you with GM, GA, GE using time module

import time
t = time.strftime('%H:%M:%S')
# print(timestamp)
# hour = int(time.strftime('%H'))
hour = int(input("Enter hour : "))
print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning!")
elif(hour >= 12 and hour < 17):
    print("Good Afternoon!")
elif(hour >= 17):
    print("Good Night!")
else:
    print("Fine!")


#--Time Module--
import time

time.time()
print(time.time())

time.sleep()
print(4)
time.sleep(3)
print("This is printed after 3 seconds")

time.strftime()
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)  





#For loop with else #While loop
for i in range(6):
    print(i) #yo complete vayesi else ma janxa
    if i == 4:
        break #break vayo vani else execute hudaina
else:
    print("No i") #same in while loop also





#Raising Custom Error
a = int(input("Enter any value between 5 and 9"))
if(a < 5 or a > 9):
    raise ValueError("value should be between 5 and 9")

quick = int(input("Enter any value : "))
if(quick != "quit"):
    raise ValueError("wrong")









