import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play (word)
    word_completion = "_" * len (word)
    guess = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to hangman. Let's play!")
    print(display_hangman(tries))
    print(word completion)
    print("\n")
    while not guessed and tries > 0: 
        guess = input("Please guess a letter, or the whole word: ").upper()
        if len(guess) == 1 and guess.isalpha():
        
        elif len(guess) == len(word) and guess.isalpha():

        else: 
            print("Not a valid guess.")


    

