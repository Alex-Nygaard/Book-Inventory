# Read an integer:
n = int(input()) # Kilometers per day
m = int(input()) # Route length

if m % n > 0:
    print((m // n) + 1)
else:
    print(m // n)
