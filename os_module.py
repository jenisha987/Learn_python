#--How import works in Python--

import math as m
res = m.sqrt(16)
res = math.sqrt(16)
print(res)

# --dir function--
import math
print(dir(math)) #math vitra k k functions and variables haru xa herna pauxa
print(math.nan)


#--OS Module--


import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}") #source,destination

folders = os.listdir("data")
print(folders) #print all the folders of data directory
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))  #print all files inside each folder

print(os.getcwd())


# --Clear the Clutter-- Exercise

import os
files = os.listdir("clutterFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterFolder/{file}", f"clutterFolder/{i}.png")
        i = i + 1