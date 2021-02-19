# Write your code here
from random import randrange
import math


class Game:

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_name = ""
        self.ratings = {}

    def get_user_name(self):
        self.user_name = input("Enter your name: ")

    def greet(self):
        print(f"Hello, {self.user_name}")

    def set_choices(self):
        custom_choices = input()

        if len(custom_choices) > 0:
            self.choices = custom_choices.split(',')

    def start(self):
        self.get_user_name()
        self.greet()
        self.set_choices()

        self.load_ratings()

        if self.user_name not in self.ratings:
            self.ratings[self.user_name] = 0

        print("Okay, let's start")
        self.game_loop()

    def game_loop(self):

        while True:
            usr_choice = input()
            ai_choice = self.choices[randrange(0, len(self.choices))]

            outcome = self.determine_winner_v2(usr_choice, ai_choice)
            if outcome == "win":
                print(f"Well done. The computer chose {ai_choice} and failed")
                self.increase_rating(100)
            elif outcome == "draw":
                print(f"There is a draw ({ai_choice})")
                self.increase_rating(50)
            elif outcome == "lose":
                print(f"Sorry, but the computer chose {ai_choice}")
            elif outcome == "!exit":
                self.end()
                break
            elif outcome == "!rating":
                self.print_ratings()
            else:
                print("Invalid input")

    def determine_winner_v2(self, usr_choice, ai_choice):
        outcome = ""

        if usr_choice in self.choices:
            array_minus_choice = self.choices[self.choices.index(usr_choice) + 1:] + self.choices[0:self.choices.index(usr_choice)]
            winning_choices = array_minus_choice[0:math.floor(len(array_minus_choice) / 2)]
            losing_choices = array_minus_choice[math.ceil(len(array_minus_choice) / 2):]
        else:
            return usr_choice

        if ai_choice not in array_minus_choice:
            outcome = "draw"
        elif ai_choice in winning_choices:
            outcome = "lose"
        elif ai_choice in losing_choices:
            outcome = "win"

        return outcome

    def end(self):
        print("Bye!")
        self.save_ratings()

    def increase_rating(self, amount):
        self.ratings[self.user_name] += amount

    def print_ratings(self):
        print(f"Your rating: {self.ratings[self.user_name]}")

    def load_ratings(self):
        ratings_file = open("rating.txt", 'r')

        for line in ratings_file:
            rating = line.split(" ")
            self.ratings[rating[0]] = int(rating[1])

        ratings_file.close()

    def save_ratings(self):
        ratings_file = open("rating.txt", 'w')

        for player in self.ratings:
            print(f"{player} {self.ratings[player]}", file=ratings_file)

        ratings_file.close()


game = Game()
game.start()
