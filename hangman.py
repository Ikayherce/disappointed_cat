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
            if guess in guessed_letters:
                print("You already guessed this letter!", guess)
            elif guess is not in word:
                print(guess, "is not in the word.")
                tries -= 1 
                guessed_letters.append(guess)
            else: 
        
        elif len(guess) == len(word) and guess.isalpha():

        else: 
            print("Your guess is not valid")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

        


    

