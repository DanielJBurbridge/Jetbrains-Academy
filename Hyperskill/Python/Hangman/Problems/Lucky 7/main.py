n = int(input())
inputs = []

for _ in range(n):
    inputs.append(int(input()))

for x in inputs:
    if (x % 7) == 0:
        print(x * x)
