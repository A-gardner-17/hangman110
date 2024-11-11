import random

word_list = ["apple","orange","banana","grape","strawberry"]

# Class creation
class Hangman():
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = len(self.word)*["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.list_of_guesses = []
    
    # Method to check the user guess
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for position in range(len(self.word)):
                if self.word[position] == guess:
                    self.word_guessed[position] = guess
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)        
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    # Method to capture valid user input
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


play = Hangman(word_list, num_lives=5)
play.ask_for_input()
