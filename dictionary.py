#--Dictionary in Python--

dict = {
    "key" : "value",
    "subject" : ['python','c','js'],
    "list" : ('a','b'),
    "ok" : True,
    "age" : 35,
    "marks" : 89.9
}
print(dict)

#--accessing value of dictionary--
print(dict["key"])
print(dict["subject"])
print(dict["list"])

#--assign new value to key --
dict["key"] = "Jenisha"
print(dict)

#--add new key and its value--
dict["surname"] = "Shrestha"
print(dict)

#nestetd dictioanary
student = {
    "name" : "Jenisha",
    "score" : {
        "chem" : 98,
        "maths" : 95,
        "phy" : 80
    }
}

print(student) #accessing the dictioanry
print(student["name"]) #accessing only some values of dictioanry
print(student["score"]["chem"]) #accessing values vitra ko values only

#Dictionary Methods
student = {
    "name" : "Jenisha",
    "score" : {
        "chem" : 98,
        "maths" : 95,
        "phy" : 80
    }
}

print(student.keys()) #returs all keys
print(list(student.keys())) #converts keys into list
print(len(student)) #returns number of items in dictionary

print(student.values()) #return all values

print(student.items())  # returns a list of tuples with (key,value) pairs
pairs = list(student.items())
print(pairs[0]) #accessing individual tuples

print(student["name"])
print(student.get("name")) #returns value according to the key

# # but if difference between both
print(student["name2"]) #error
print(student.get("name2")) #no error -> none

student.update({"city" : "Kathmandu"})
print(student)
#OR
std = {
    "city" : "Kathmamndu", "age" : 20
}
student.update(std)
print(student)
