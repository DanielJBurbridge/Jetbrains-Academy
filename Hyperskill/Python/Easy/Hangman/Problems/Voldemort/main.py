import random


# work with this variable
n = int(input())
string = "Voldemort"

random.seed(n)
print(random.choice(string))
