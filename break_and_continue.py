#Break and Continue


#Break
i = 1
while i <= 5:
    print(i)
    if(i == 3): #no further execution 1,2,3
        break
    i += 1

#Continue
i = 0
while i <= 5:
    if(i == 3): #0,1,2,4,5 -- 3 lai skip garxa
        i += 1
        continue
    print(i)
    i += 1