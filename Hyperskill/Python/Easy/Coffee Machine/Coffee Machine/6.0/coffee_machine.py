def main():
    coffee_machine = CoffeeMachine()

    while coffee_machine.state != "exit":
        coffee_machine.__setstate__(input())


class CoffeeMachine:

    states = ["on", "buy", "fill", "take", "remaining", "off"]
    coffee_types = [["espresso", 250, 0, 16, 4], ["latte", 350, 75, 20, 7], ["cappuccino", 200, 100, 12, 6]]

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.state = "on"

    def __setstate__(self, state):
        self.state = state

        if self.state == "buy":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if choice == "back":
                return
            else:
                self.make(self.coffee_types[int(choice) - 1])

        if self.state == "fill":
            water = int(input("Write how many ml of water do you want to add:\n"))
            milk = int(input("Write how many ml of milk do you want to add:\n"))
            beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
            cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

            self.fill(water, milk, beans, cups)

        if self.state == "take":
            print(f"I gave you {self.take()}")

        if self.state == "remaining":
            self.__str__()

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        payout = self.money
        self.money = 0
        return payout

    def make(self, coffee):

        water = coffee[1]
        milk = coffee[2]
        beans = coffee[3]
        price = coffee[4]

        if self.has_supply(water, milk, beans, 1):
            print("I have enough resources, making you a coffee!")
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += price
        elif self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.beans < beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")

    def has_supply(self, water, milk, beans, cups):
        return self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= cups

    def __str__(self):
        print(f"""
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money""")

main()
