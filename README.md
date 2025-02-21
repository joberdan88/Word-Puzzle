# Word-Puzzle
Overview
Many games and puzzles require iteration where a person (or a computer) repeats the same steps for each piece in the game or each spot in a puzzle. For this assignment, you will create an interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.

Wordle is a web-based word game that became popular online in the early part of 2022. (You can learn more about it from the Wordle Wikipedia page. If you want, you can play it online for free from the New York Times page.)

For this assignment, you'll create a puzzle game that follows a similar pattern.

Project Description
The program contains a hidden secret word stored in a variable. This word can have any number of letters in it. When the program runs, the user is shown underscores ( _ ) for each letter of the word.

The user then enters a guess. If the guess is correct, the user wins and the game is over.

If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

The game continues prompting the user for new guesses and showing them hints until they guess the word correctly. When the game is over, the program displays the number of guesses that were made.

The guess must be the same number of letters as the secret word. If the guess has a different numbers of letters, the user is given a message explaining this, and no hint is provided.

The hint shows the letters of the guess, but each letter is rendered in a special way as follows:

An underscore _ indicates that the letter was not present in the secret word.

A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)
"""
