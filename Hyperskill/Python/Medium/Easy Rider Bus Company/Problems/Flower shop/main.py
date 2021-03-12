import itertools

for i in range(1, 4):
    for combination in itertools.combinations(flower_names, i):
        print(combination)
