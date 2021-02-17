# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
lines = file.readlines()
print(len(lines))
file.close()
