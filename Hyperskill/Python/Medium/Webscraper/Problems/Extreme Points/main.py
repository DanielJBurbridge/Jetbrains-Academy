# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'

maximum = max(test_dict, key= lambda k: test_dict[k])
minimum = min(test_dict, key= lambda k: test_dict[k])

print(f"min: {minimum}")
print(f"max: {maximum}")
