# List practice

## 1. Even indices
```.py
# Read a list:
l = input().split(" ") # Split the string into a list

# Print every other (only even) indices
for i in range(0, len(l), 2):
    print(l[i])
```

## 2. Even Elements
```.py
# Read a list:
l = [int(i) for i in input().split(" ")] # Split the string into a list of ints

# Print every even value
for i in l:
    if i % 2 == 0:
        print(i)
```


## 3. Greater Than Previous
```.py
# Read a list:
l = [int(i) for i in input().split(" ")] # Split the string into a list of ints

# Compares previous element to next
for i in range(1, len(l)):
    if l[i-1] < l[i]:
        print(l[i])
```


## 4. Neighbors of the same sign
```.py
# Read a list:
l = [int(i) for i in input().split(" ")] # Split the string into a list of ints

# Checks every pair, prints and breaks if sign is same
for i in range(1, len(l)):
    if l[i-1] > 0 and l[i] > 0 or l[i-1] < 0 and l[i] < 0:
        print(l[i-1], l[i])
        break
```


## 5. Greater than neighbours
```.py
# Read a list:
l = [int(i) for i in input().split(" ")] # Split the string into a list of ints

# Checks every number (except first and last) of list against its neighbors
quantity = 0
for i in range(1, len(l) - 1):
    if l[i-1] < l[i] > l[i+1]:
        quantity += 1

print(quantity)
```



