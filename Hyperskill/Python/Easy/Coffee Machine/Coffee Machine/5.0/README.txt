Stage 5/6: Keep track of the supplies
Description
Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types "buy", "fill" or "take", then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type "exit". The program should terminate on this command. Also, when the user types "remaining", the program should output all the resources that the coffee machine has.

Objectives
Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.