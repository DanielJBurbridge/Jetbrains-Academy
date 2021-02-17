# Write your code here
from random import randrange
options = ["rock", "paper", "scissors"]

while True:
    usr_input = input()
    ai_input = options[randrange(3)]
    choices = {"player": usr_input, "AI": ai_input}

    if choices["player"] == "scissors":
        if choices["AI"] == "scissors":
            print(f"There is a draw ({choices['AI']})")
        elif choices["AI"] == "rock":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
    elif choices["player"] == "rock":
        if choices["AI"] == "rock":
            print(f"There is a draw ({choices['AI']})")
        elif choices["AI"] == "paper":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
    elif choices["player"] == "paper":
        if choices["AI"] == "paper":
            print(f"There is a draw ({choices['AI']})")
        elif choices["AI"] == "scissors":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
    elif choices["player"] == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")


