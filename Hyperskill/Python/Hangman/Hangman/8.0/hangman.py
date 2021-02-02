import random


def start():

    choice = ""

    while True:
        choice = input('Type "play" to play the game, "exit" to quit:')

        if choice == "play" or choice == "exit":
            break

    if choice == "play":
        play()
    elif choice == "exit":
        pass


def play():
    words = ["python", "java", "kotlin", "javascript"]
    word = random.choice(words)
    guessed = set()
    lives = 8

    print("H A N G M A N")

    while lives > 0:
        print()
        revealed = generate_display(word, guessed)
        print(revealed)

        if revealed == word:
            "You guessed the word!"
            break

        guess = input("Input a letter: ")

        if not valid_guess(guess, guessed):
            continue

        guessed.add(guess)

        if guess not in word:
            print("That letter doesn't appear in the word")
            lives -= 1

    if lives > 0:
        print("You survived!")
    else:
        print("You lost!")

    start()


def valid_guess(guess, guessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(guess) != 1:
        print("You should input a single letter")
        return False

    if guess not in alphabet:
        print("Please enter a lowercase English letter ")
        return False

    if guess in guessed:
        print("You've already guessed this letter")
        return False

    return True


def generate_display(word, found):
    display = ""
    for c in word:
        if c in found:
            display += c
        else:
            display += "-"
    return display


start()
