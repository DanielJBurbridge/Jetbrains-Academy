# Write your code here
from random import randint
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class Person:
    def __init__(self):
        self.bank_cards = []
        for line in cur.fetchall():
            self.bank_cards.append([line[1], line[2]])
        print(self.bank_cards)

    def add_bank_card(self):
        bank_card = BankCard()
        bank_card_numbers = bank_card.generate_card()

        while not self.unique_card(bank_card_numbers):
            bank_card_numbers = bank_card.generate_card()

        self.bank_cards.append(bank_card_numbers)
        cur.execute(f'INSERT INTO card VALUES(1, {bank_card_numbers[0]}, {bank_card_numbers[1]}, 0)')
        conn.commit()
        return self.bank_cards[-1]

    def unique_card(self, bank_card):
        card_numbers = []
        for card in self.bank_cards:
            card_number = card[0]
            card_numbers.append(card_number)
        if bank_card[0] in card_numbers:
            return False
        else:
            return True

    def check_for_card(self, bank_card):
        return bank_card in self.bank_cards


class BankCard:
    def __init__(self):
        self.iin = 0
        self.account_number = 0
        self.check_sum = 0
        self.pin = 0

    def generate_card(self):
        self.iin = 400000
        self.account_number = randint(0, 999999999)

        digits = str(self.iin) + str(self.account_number).zfill(9)
        count = 0
        for index, digit in enumerate(digits):
            if (index + 1) % 2 != 0:
                temp = int(digit) * 2
                if temp >= 10:
                    temp -= 9
                count += temp
            else:
                count += int(digit)

        if count % 10 == 0:
            self.check_sum = 0
        else:
            self.check_sum = 10 - (count % 10)

        print(count)
        print(count % 10)
        print (self.check_sum)
        self.pin = randint(0, 9999)

        return [str(self.iin) + str(self.account_number).zfill(9) + str(self.check_sum), str(self.pin).zfill(4)]


def logged_in_loop(person):

    while True:
        action = input(f"1. Balance\n"
                       f"2. Log out\n"
                       f"0. Exit\n")

        if action == '1':
            print("Balance: 0")
        elif action == '2':
            print("You have successfully logged out!")
            break
        elif action == '0':
            print("Bye!")
            exit()


def action_loop(person):
    while True:
        action = input(f"1. Create an account\n"
                       f"2. Log into account\n"
                       f"0. Exit\n")
        if action == '1':
            bank_card = person.add_bank_card()
            print(f'Your card has been created\n'
                  f'Your card number:\n{bank_card[0]}\n'
                  f'Your card PIN:\n{bank_card[1]}\n')
        elif action == '2':
            usr_card_number = input("Enter your card number:\n")
            usr_pin_number = input("Enter your PIN:\n")

            if person.check_for_card([usr_card_number, usr_pin_number]):
                print("You have successfully logged in!")
                logged_in_loop(person)
            else:
                print("Wrong card number or PIN!")
        elif action == '0':
            print("Bye!")
            exit()


cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
conn.commit()

p = Person()
action_loop(p)

