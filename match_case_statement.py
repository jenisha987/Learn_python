#Match Case Statement


x = int(input("Enter the value of x : "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    # case _: #default case
    #     print(x)
        
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x!= 80:
        print(x, "is not 80")
    case _: #default case
        print(x)