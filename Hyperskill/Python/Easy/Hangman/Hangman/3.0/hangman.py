import random
words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
print("H A N G M A N")
guess = input("Guess the word: ")

if word == guess:
    print("You survived!")
else:
    print("You lost!")
