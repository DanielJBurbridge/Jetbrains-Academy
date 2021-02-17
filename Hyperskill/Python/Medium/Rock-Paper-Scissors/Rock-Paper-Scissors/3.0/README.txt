Stage 3/5: Endless game
Description
Wasn't that pretty cool?

But the game is really short so far: nobody plays just a single shot of rock-paper-scissors. We need to do some literally unstoppable game for unstoppable players. Not literally unstoppable, of course: let's implement a way to stop your program.

Improve your program so it would take an unlimited number of inputs until the user enters !exit. After entering !exit the program should print Bye! and terminate. Also, let's try to handle invalid inputs: your program should be ready that there may be a typo in user's input, or that a user may just enter complete gibberish instead of a normal command. So, in case the input doesn't correspond to any known command (option name or !exit), your program should output the line Invalid input

Objectives
Your program should:

Take an input from the user
If the input is !exit, output Bye! and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
If the input corresponds to anything else, output Invalid input
Do it all over again
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.