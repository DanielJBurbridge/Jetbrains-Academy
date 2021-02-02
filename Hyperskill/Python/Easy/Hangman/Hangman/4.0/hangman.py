import random
words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
display = word[0:3] + '-' * (len(word) - 3)
print("H A N G M A N")
print(f"Guess the word {display}:")
guess = input("Guess the word: ")

if word == guess:
    print("You survived!")
else:
    print("You lost!")
