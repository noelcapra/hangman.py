# Hangman Game in Python

A classic Hangman game where the player tries to guess a randomly chosen word, letter by letter, within a certain number of attempts.

## How to Run
1. Ensure you have Python installed.
2. Download `hangman.py`.
3. Run the program from the terminal using the command: `python hangman.py`
4. Follow the instructions and guess letters.

## What I Learned / Concepts Demonstrated
* Using the `random` module (`random.choice`) to randomly select a word from a list.
* String manipulation and working with lists (e.g., to represent the hidden word with `_` and to store incorrectly guessed letters).
* `while` loops to control the game's flow (continue as long as the word isn't guessed and attempts remain).
* `for` loops to iterate through the word and check guesses.
* `if/elif/else` statements to handle different game logic (correct guess, incorrect guess, out of attempts).
* Handling user input and converting to lowercase (`.lower()`).
* Updating and displaying the game's status (hidden word, attempts left, incorrect letters).
