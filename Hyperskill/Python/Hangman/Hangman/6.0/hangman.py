import random


def play():
    words = ["python", "java", "kotlin", "javascript"]
    word = random.choice(words)
    revealed = ""
    found = set()
    lives = 8

    print("H A N G M A N")

    while lives > 0:
        print()
        revealed = generate_display(word, found)
        print(revealed)
        if revealed == word:
            "You guessed the word!"
            break
        guess = input("Input a letter: ")

        if guess in word:
            if guess in found:
                print("No improvements")
                lives -= 1
            else:
                found.add(guess)
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

    if lives > 0:
        print("You survived!")
    else:
        print("You lost!")


def generate_display(word, found):
    display = ""
    for c in word:
        if c in found:
            display += c
        else:
            display += "-"
    return display


play()
