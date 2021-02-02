import random


def play():
    words = ["python", "java", "kotlin", "javascript"]
    word = random.choice(words)
    found = set()

    print("H A N G M A N")
    print()

    for i in range(8):
        print(generate_display(word, found))
        guess = input("Input a letter: ")

        if guess in word:
            found.add(guess)
        else:
            print("That letter doesn't appear in the word")
        print()

    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")


def generate_display(word, found):
    display = ""
    for c in word:
        if c in found:
            display += c
        else:
            display += "-"
    return display


play()
