# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Table of Contents
 1. [Project Description](#project-description)
 2. [Installation Instructions](#installation-instructions)
 3. [Usage Instructions](#usage-instructions)
 4. [File Structure of the Project](#file-structure-of-the-project)
 5. [License Information](#license-information)

# Project Description
This project is an implementation of a Hangman game using Python.
The program randomly selects a word from a word list. The user starts with 5 lives and then they need to enter a letter as their guess - this input is validated to ensure that only a single letter can be entered and the letter has not been asked already.
If the input is valid the guess is checked against the random word. If the letter is in the word the position of the letter is displayed for example:
['_', '_', 'a', '_', '_']

The process is repeated until the user either guesses the word or loses all of their lives.

This project has reinforced my understanding of object oriented programaming as well as using git and git hub.

# Installation Instructions
The project uses the standard Python installation.

# Usage Instructions
The project can be tested using the file milestone_5.py

# File Structure of the Project
**milestone_3.py** has two functions. Ask_for_input which validates the user input to ensure a single letter is entered. If a single letter is entered it then calls the check_guess function to see if the letter is in the randomly selected word.

**milestone_4.py** creates a Hangman class with the following attributes:
1. word: The word to be guessed, picked randomly from the word_list. 
2. word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
3. num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
4. num_lives: int - The number of lives the player has at the start of the game.
5. word_list: list - A list of words
6. list_of_guesses: list used to capture guesses already made

Methods check_guess and ask_for_input have been implemented using the structure from milestone_3.py

**milestone_5.py** builds on milestone_4.py to run the game. This checks the number of lives and the number of letters. If the number of lives reaches 0 the game ends with the player losing. If the number of letters reaches 0 (without the number of lives reaching 0) the player wins.

# License Information
This program has been developed as part of the AiCore training programme.