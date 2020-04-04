string = input("Please input a string: ")

letters = 0
numbers = 0

for i in string:
    if i.isalpha(): # Checks if a letter
        letters += 1
    elif i.isdigit(): # Checks if digit
        numbers += 1 

print("Letters:", letters)
print("Numbers:", numbers)

