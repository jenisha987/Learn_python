#--Random Password Generator--

import random
import string #collection of string constants

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(charValues)

#Using list comprehension [function for i in range(n)]
# password = "".join([random.choice(charValues) for i in range(pass_len)])

print("Your random password is :", password)

