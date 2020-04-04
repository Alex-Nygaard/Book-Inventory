age = int(input("What is the dog's age (in dog years)? "))

if age == 1:
    dogAge = 10.5
elif age == 2:
    dogAge = 21
else:
    dogAge = 21 + 4*(age-2)

print("The dog's age in dog years is", dogAge)
