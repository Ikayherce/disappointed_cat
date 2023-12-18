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
                print("Oh no!" , guess, "is not in the word.")
                tries -= 1 
                guessed_letters.append(guess)
            else: 
                print("Well done", guess, "is in the word." )
                guessed_letters.append(guess)
                word_as_list = list(word_completion) 
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess 
                word_completion = ""join.(word_as_list)
                if "_" not in word_completion:
                    guess = True 
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                elif guess != word: 
                    print(guess, "is not the word.")

        else: 
            print("Your guess is not valid")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

        


    

