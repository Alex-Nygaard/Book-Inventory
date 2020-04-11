fName = input("What's your FIRST name? ")
lName = input("What's your LAST name? ")
num = int(input("How many emails (between 1-99)? "))

# Check if num is within range
if num > 99:
    num = 99
elif num < 1:
    num = 1

# File output
f = open('emails.txt','w')
for i in range(1, num+1):
    email = f"{fName}.{lName}{i}@uwcisak.jp\n"
    f.write(email)
f.close()
