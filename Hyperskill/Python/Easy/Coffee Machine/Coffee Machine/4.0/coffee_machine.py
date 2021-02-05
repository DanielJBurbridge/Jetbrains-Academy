def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.stock_report()
    choice = input("Write action (buy, fill, take):\n")

    if choice == "buy":
        buy(coffee_machine)

    if choice == "fill":
        fill(coffee_machine)

    if choice == "take":
        take(coffee_machine)


def buy(coffee_machine):
    coffee_machine = coffee_machine
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")

    if choice == "1":
        coffee_machine.make(250, 0, 16, 4)
    if choice == "2":
        coffee_machine.make(350, 75, 20, 7)
    if choice == "3":
        coffee_machine.make(200, 100, 12, 6)

    coffee_machine.stock_report()


def fill(coffee_machine):
    coffee_machine = coffee_machine
    water = int(input("Write how many ml of water do you want to add:\n"))
    milk = int(input("Write how many ml of milk do you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    coffee_machine.fill(water, milk, beans, cups)
    coffee_machine.stock_report()


def take(coffee_machine):
    coffee_machine = coffee_machine
    print(f"I gave you {coffee_machine.take()}")
    coffee_machine.stock_report()


class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        payout = self.money
        self.money = 0
        return payout

    def make(self, water, milk, beans, price):
        if self.has_supply(water, milk, beans, 1):
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += price

    def has_supply(self, water, milk, beans, cups):
        return self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= cups

    def stock_report(self):
        print(f"""{self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")


main()
