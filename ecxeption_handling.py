#Exception Handling

a = input("Enter the number : ")
print(f"Multiplication table of {a} is : ")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e: #except:
    print("Invalid Input")
print("Some imp lines of code")
print("End of Program ")



#Finally Keyword 
def func1():
    try:
        l = [1,2,3,6]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executing")
x = func1()
print(x)