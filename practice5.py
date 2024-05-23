#Functons and Recursion

#--Let's Practice--
#WAF to print the length of list, list is the parameter
cities = ["Ktm", "Pokhara", "Bhkt", "Lalitpur"]
fruits = ["Apple", "Mango", "Orange"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(fruits)

#WAF to print the elements of a list in single line
def print_line(list):
    for item in list:
        print(item, end = " ")
print_line(cities)
print()
print_line(fruits)

#WAF to find the factorial of a number
n = int(input("Enter n : "))
def calc_fact(n):
    fact = 1
    for i  in range(1, n + 1):
        fact  = fact * i
    print(fact)
calc_fact(n)

#WAF to convert USD to NPR
usd = float(input("Enter amount in USD : "))
def usd_to_npr(usd):
    rate = 132.19 
    npr = usd * rate
    print(usd, "USD =", "Rs", npr)
usd_to_npr(usd)

#WAF to input one number and check if it is odd or even, if odd print odd else return even
num = int(input("Entr num : "))
def  check_odd_even(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")
check_odd_even(num)