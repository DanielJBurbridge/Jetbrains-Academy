# the list "walks" is already defined
# your code here

total_distance = 0
for walk in walks:
    total_distance += walk.get("distance")
print(int(total_distance / len(walks)))

