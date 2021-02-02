Stage 5/8: Keep trying
Description
Let's make the game iterative. Now it's time to make the game resemble the classic version of Hangman a bit more. The player should now guess letters in the word instead of typing the entire word all at once. If the player guesses a letter, it should be uncovered in the word. For now, start by building the defeat condition and add 8 tries to guess a letter that appears in the word. When the player runs out of attempts, the game ends.

Later we will determine the winning conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

Objectives
Now your game should work as follows:

A player has exactly 8 tries and enters letters. Nothing changes if a player has more tries left but they have already guessed the word.
If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.
Also, the word should be selected from our list: 'python', 'java', 'kotlin', 'javascript', so that your program can be tested more reliably.
Please, make sure that your program's output formatting precisely follows the example. Pay attention to the empty lines between tries and at the end.