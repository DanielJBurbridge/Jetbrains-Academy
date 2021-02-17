# Write your code here
from random import randrange
options = ["rock", "paper", "scissors"]

# load ratings and players

ratings_file = open("rating.txt", 'r')
ratings_array_raw = ratings_file.readlines()
ratings_array = []
for rating in ratings_array_raw:
    ratings_array.append(rating.split(" "))

ratings_file.close()

ratings_obj = {}

for ratings_pair in ratings_array:
    ratings_obj[ratings_pair[0]] = int(ratings_pair[1])

player_name = input("Enter your name")
print(f"Hello, {player_name}")

if player_name not in ratings_obj:
    ratings_obj[player_name] = 0

while True:
    usr_input = input()
    ai_input = options[randrange(3)]
    choices = {"player": usr_input, "AI": ai_input}

    if choices["player"] == "scissors":
        if choices["AI"] == "scissors":
            print(f"There is a draw ({choices['AI']})")
            ratings_obj[player_name] += 50
        elif choices["AI"] == "rock":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
            ratings_obj[player_name] += 100
    elif choices["player"] == "rock":
        if choices["AI"] == "rock":
            print(f"There is a draw ({choices['AI']})")
            ratings_obj[player_name] += 50
        elif choices["AI"] == "paper":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
            ratings_obj[player_name] += 100
    elif choices["player"] == "paper":
        if choices["AI"] == "paper":
            print(f"There is a draw ({choices['AI']})")
            ratings_obj[player_name] += 50
        elif choices["AI"] == "scissors":
            print(f"Sorry, but the computer chose {choices['AI']}")
        else:
            print(f"Well done. The computer chose {choices['AI']}")
            ratings_obj[player_name] += 100
    elif choices["player"] == "!exit":
        print("Bye!")
        ratings_file = open("rating.txt", 'w')

        for player in ratings_obj:
            print(f"{player} {ratings_obj[player]}", file= ratings_file)

        ratings_file.close()
        break
    elif choices["player"] == "!rating":
        print(f"Your rating: {ratings_obj[player_name]}")
    else:
        print("Invalid input")



