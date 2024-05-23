

#Set in Python
collection = {1,2,3,4}
print(collection)
print(type(collection))

dup = {1,2,2,"hello", "world", "world"}
print(dup) #duplicate ites lai ignore garxa
print(len(dup)) # duplicate lai count gardaina so length will be 4

#create empty set
set  = {} #empty dictionary not a set so to create empty set do:
sets = set() #empty set; syntax set()

#Sets Methods
code = set()
code.add(1)
code.add("Jenisha")
code.add((1,2,3))
# code.add([1,2,3]) #error as lists cannot be added
code.add(2)
code.add(2)
code.remove(1)
# code.remove(6) #error as element doesnot exist

code.clear()
print(code)
print(len(code))

print(code.pop()) #pops random values

set1 = {1,2,5,3}
set2 = {3,4,5}
print(set1.union(set2)) 
print(set1.intersection(set2))


