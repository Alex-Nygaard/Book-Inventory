# Read an integer:
N = int(input())

inputs = []

for i in range(N-1):
    inputs.append(int(input()))
    
for i in range(1, N+1):
    if i not in inputs:
        print(i)
