#--Practice Questions--
#Question1

jen = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(jen)

#Question2
subjects = {"python","java","C++","python","JS","java","python","java","C++","C"}
print(len(subjects))

#Question3
marks = {}

x = int(input("Enter phy : "))
marks.update({"phy" : x})

x = int(input("Enter phy : "))
marks.update({"chem" : x})

x = int(input("Enter phy : "))
marks.update({"maths" : x})

print(marks)

#Question4 -- store 9 and 9.0 as separate values in the set
values = {9, 9.0} #treats both as same value
print(values)

value = {9, "9.0"} #one possible way
print(value)

val = { #next possible way
    ("float", 9.0),
    ("int", 9)
}
print(val)