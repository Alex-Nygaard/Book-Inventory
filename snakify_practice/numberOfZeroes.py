# Read an integer:
N = int(input())

howMany = 0

for i in range(N):
    a = int(input())
    if a == 0:
        howMany += 1

print(howMany)
