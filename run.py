import random
from words import word_list
# show welcome message
print("Welcome to Sad Kitty. Guess right - don't make kitty sad!")


def get_word():
    """function to get random word from word list in separate file"""
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    this is the play function.
    it displays underscores according to the length of the word to guess.
    it validates user input, as well as subtracting points when guess
    is not correct.
    This function prints feedback to the user and displays word completion
    according to user's guesses.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # show welcome message
    print(display_sad_kitty(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter, or the whole word: ").upper()
        # check that user data is one letter or a word of the riht length
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                # warns user letter has been already guessed
                print("You already guessed the letter", guess)
            elif guess not in word:
                print("Oh no!", guess, "is not in the word, kitty might cry")
                # substract tries by 1 when guess is wrong
                tries -= 1
                guessed_letters.append(guess)
            else:
                # print feedback to user when guess is correct
                print("Kitty says well done!", guess, "is in the word.")
                guessed_letters.append(guess)
                # replaces underscore by correctly guessed letter
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                    ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # if all underscores are replaced by letters, word is guessed
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # conditional block checks if word or letter is already guessed.
            # and whether letter is or is not in the word.
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word. Come on, you can do it!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            # feedback when input is not a letter or word of right length
            word_length = len(word)
            print("Your guess is not valid.")
            print(f"It needs to be a letter or a word of {word_length} letters' length")
        # print display of hangman and of word completion
        print(display_sad_kitty(tries))
        print(word_completion)
        print("\n")

    # check if user guessed or ran out of tries
    # print right feedback to user that they have won or lost the game
    if guessed:
        print("Congratulations, you guessed the word! Kitty is proud of you!")
    else:
        print("Oh no! You ran out of tries. Kitty is now sad")
        print(f"The word was {word}. Kitty wishes you better luck next time!")


def display_sad_kitty(tries):
    """
    This function displays the different stages of display
    of the disappointed cat, one stage for each failed try.
    """
    stages = [  # final state: head, torso, paws, tail
                """
                          ／＞　 フ
                         | 　_　_| 
                       ／` ミ＿xノ 
                      /　　　　 |
                     /　 ヽ　　 ﾉ
                    │　　|　|　|
                ／￣|　　 |　|　|
                 (￣ヽ＿_ヽ_)__)
                  ＼二)

                               
                """,
                # head, torso and paws
                """
                  
                                         ／＞　 フ  
                                        | 　_　_| 
                                      ／` ミ＿xノ 
                                     /　　　　 |
                                    /　 ヽ　　 ﾉ
                                   │　　|　|　|

                """,
                # head and full torso
                """
                                         ／＞　 フ
                                        | 　_　_| 
                                      ／` ミ＿xノ 
                                     /　　　　 |
                                    /　 ヽ　　 ﾉ
                                   
                """,
                # head and some torso
                """
                           ／＞　 フ
                          | 　_　_| 
                        ／` ミ＿xノ 
                       /　　　　 |
                      
                """,
                # head
                """
                        ／＞　 フ
                       | 　_　_| 
                     ／` ミ＿xノ 
                      
                """,
                # ears and eyes
                """
                 ／＞　 フ
                | 　_　_| 
               
                """,
                # ears
                """
                  ／＞　 フ
                """,
                 # initial empty state
                """
                """
    ]

    return stages[tries]


def main():
    """
    This function runs the game and asks user whether
    they want to play again
    """
    word = get_word()
    play(word)

    while input("Do you want to play again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)


# code fragment so game runs by running the script on the command line
if __name__ == "__main__":
    main()
