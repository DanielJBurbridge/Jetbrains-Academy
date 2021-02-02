Stage 7/8: Error_
Description
Now that we are done with the basics, let's work on perfecting some details.

In the previous stage, if the user entered the same letter twice, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn’t seem fair to the player, does it? They gain no additional information about the situation on the field yet the program still reduces their remaining attempts. Let's fix it!

Objectives
If the user enters the same letter twice, then the program should output You've already guessed this letter . This message should also be printed if the user inputs a letter that doesn't appear in the word. The number of attempts shouldn't be decreased in this case.
Also, you should check to make sure the player entered an English lowercase letter. If not, the program should print Please enter a lowercase English letter .
You should also check if the player entered exactly one letter. If not, the program should print You should input a single letter . Remember that zero is also not one!
Note that none of these three errors should reduce the number of remaining attempts!
Please, make sure that your program's output formatting precisely follows the output formatting in the example. Pay attention to the empty lines between tries and in the end.