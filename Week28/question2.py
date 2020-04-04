length = int(input("Input the length of the dictionary: "))

d = {}

for i in range(1, length+1):
    d[str(i)] = i*i

print(d)
