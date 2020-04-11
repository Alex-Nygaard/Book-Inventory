import random
import string

num = int(input("How many passwords? "))

# Make a string with all letters, digits and special characters
allCharacters = string.ascii_letters + string.digits + string.punctuation
passwordLength = 20

# Generate the passwords
for i in range(num):
    password = "".join([random.choice(allCharacters) for i in range(passwordLength)])
    print(password)

