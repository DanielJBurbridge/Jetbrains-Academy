# put your python code here
numbers = input().split()
key = input()

positions = [str(i) for i, n in enumerate(numbers) if n == key]

print(" ".join(positions) or "not found")
