# Write your code here

required_water = 200
required_milk = 50
required_beans = 15

water = int(input("write how many ml of water the coffee machine has:\n"))
milk = int(input("write how many ml of milk the coffee machine has:\n"))
beans = int(input("write how many grams of coffee beans the coffee machine has:\n"))
available = int(min(water/required_water, milk/required_milk, beans/required_beans))


cups = int(input("Write how many cups of coffee you will need:\n"))

if cups == available:
    print("Yes, I can make that amount of coffee")
elif cups > available:
    print(f"No, I can make only {available} cups of coffee")
else:
    print(f"Yes, I can make that amount of coffee (and even {available - cups} more than that")
