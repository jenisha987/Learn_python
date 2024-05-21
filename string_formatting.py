#String formatting in Python


txt = "For only {price:.2f} dollars!"
print(txt.format(price=35.9056))

letter = "Hey my name is {} and I am from {}" 
country = "Nepal"
name  = "Jenisha"
print(letter.format(name, country))

# f-string
letter = "Hey my name is {0} and I am from {1}" #Old method
country = "Nepal"
name  = "Jenisha"
print(letter.format(name, country))

country = "Nepal"
name = "Jenisha"
print(f"Hey I am {name} from {country}")
print(f"Hey I am {{name}} from {{country}}")

print(f"{2 * 30}")

#docstring in Python
def square(n):
    '''Takes in a number n, returns the square of n''' #docstring that can be ignored
    print(n ** 2)
square(5)
print(square.__doc__) #prints the docstring also
