string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for c in string:
    if c in vowels:
        count += 1

print(count)
