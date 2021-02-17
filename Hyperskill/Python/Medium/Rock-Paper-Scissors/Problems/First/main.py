# read test_file.txt

file = open('test_file.txt', 'r', encoding='utf-16')
lines = file.readlines()
print(lines[0])

file.close()
