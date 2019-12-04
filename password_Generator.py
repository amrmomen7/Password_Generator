# Password Generator
# By:   Amr momen
#######################################

import random
import string

numbers = []
lowerStr = []
upperStr = []
special = []
lists = []

for i in range(0, 10):
    numbers.append(str(i))

lowerStr = list(string.ascii_lowercase)
upperStr = list(string.ascii_uppercase)

s = "!@#$%^&*()_+"
special = list(s)

print("Do you want to add Special Characters to your password ? y/n")
if input() == "y":
    lists = lowerStr + upperStr + numbers + special
elif input() == "n":
    lists = lowerStr + upperStr + numbers

print("Enter Password Length: ( Should be more than 10 characters )")
length = input()

password = random.choices(lists, k=int(length))
x = ''.join(password)
print("Your Password is : ")
print(x)

