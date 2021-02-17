# read animals.txt
# and write animals_new.txt

old = open('animals.txt', 'r')
animals = old.readlines()

new = open('animals_new.txt', 'w')

for animal in animals:
    new.write(animal.replace('\n', ' '))


old.close()
new.close()
