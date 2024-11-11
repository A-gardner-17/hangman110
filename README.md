# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Table of Contents

# Project Description
This project is an implementation of a Hangman game using Python.

# Installation Instructions

# Usage Instructions

# File Structure of the Project
** milestone_3.py ** has two functions. Ask_for_input which validates the user input to ensure a single letter is entered. If a single letter is entered it then calls the check_guess function to see if the letter is in the randomly selected word.

** milestone_4.py ** creates a Hangman class with the following attributes:
1. word: The word to be guessed, picked randomly from the word_list. 
2. word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
3. num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
4. num_lives: int - The number of lives the player has at the start of the game.
5. word_list: list - A list of words
6. list_of_guesses: list used to capture guesses already made

Methods check_guess and ask_for_input have been implemented using the structure from milestone_3.py


# License Information
