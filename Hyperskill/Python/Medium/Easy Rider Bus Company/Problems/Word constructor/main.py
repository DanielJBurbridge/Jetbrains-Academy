string1 = input()
string2 = input()

word = ''
for letter1, letter2 in zip(string1, string2):
    word += letter1+letter2

print(word)
