import itertools

# first_names = ['Anna', 'Catarina']
# middle_names = ['Luisa', 'Maria']

for name in itertools.product(first_names, middle_names):
    print(*name)
