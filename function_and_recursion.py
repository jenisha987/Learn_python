#Functions and Recursion

#--Functions in Python--
def sum(a,b):
    s = a + b
    return s
print(sum(2,3))

def calc_sum(a,b):
    return a + b
sum = calc_sum(4,5)
print(sum)

def print_hello():
    print(f"Hello World!")
print_hello()
print_hello()
print_hello()

def hello():
    print("hello")
output = hello()
print(output)  #none because the function is not returning anything

#average of 3 numbers
def avg(a,b,c):
    average = (a+b+c)/3
    print(average)
    return average   
avg(2,3,5)



#--Recusrion in Python--

n = int(input("Enter n : "))
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(n)

n = int(input("Enter n : ")) #Factorial using recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(n))

#calculate the sum of first n natural numbers
n = int(input("enter n : "))
def  sum_of_natural_numbers(n):
    if (n==0):
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)
sum = sum_of_natural_numbers(n)
print(sum)

#print all elements in list
name = ["ram", "hari", "syma", "syam"]
def print_list(list,index):
    if(index < len(list)):
        print(list[index])
        print_list(list, index + 1)
print_list(name,0)







