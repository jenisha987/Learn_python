# #--Secret Code Langauge--


st = input("Enter Message : ")
words = st.split(" ")
coding = input("1 for coding and 0 for decoding : ")
coding = True if coding == "1" else False
print(coding)
if(coding):
    newwords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "sde"
            r2 = "rew"
            stnew = r1 + word[1:] + word[0] + r2
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))

else:
    newwords = []
    for word in words:
        if(len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))