import random
from words import word_list
print("Welcome to Sad Kitty. Guess a letter or word right - don't make kitty sad!")# show welcome message

class Level:
    """
    Level class :  checks if user wants to play level easy, medium or hard
    """
    def __init__(self, level):
        self.level = level

    def decide_level(self):   
        if self.level == "1":
            return "Easy"
        elif self.level == "2":
            return "Medium"
        elif self.level == "3":
            return "Hard"


def validate_level(value):
    """
    Checks user gives valid data (1,2 or 3) to choose level
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed {value}"
            )
    except ValueError as e:
        print(f"Invalid data:{e}, please try again\n")
        return False
    return True

"""returns chosen word depending on chosen level """
def get_level():
    while True:
        chosen_level = input(
            "Choose your level:\n\n 1. Easy\n 2. Medium\n 3. Hard\n")
        level_instance = Level(chosen_level)  
        level = level_instance.decide_level()  
        
        if validate_level(chosen_level):
            filtered_list = filter_words(word_list, level)
            chosen_word = random.choice(filtered_list)
            return chosen_word



def filter_words(words, level):
    """
    Filters words by length into separate lists depending on chosen level
    """
    if level == "Easy":
        easy = [word for word in words if len(word) < 5]
        return easy
    elif level == "Medium":
        medium = [word for word in words if 5 <= len(word) < 10]
        return medium
    elif level == "Hard":
        hard = [word for word in words if len(word) >= 10]
        return hard


def get_word():
    """This is the get word function. It gets a random word for the user to guess from the word list in words.py"""
    word = random.choice(word_list)
    return word.upper()

def play(word):
    """ 
    this is the play function. It checks and stores data provided by the user and gives feedback accordingly
    """
    word_completion = " _ " * len(word)
    guessed = False
    guessed_letters = [] #stores guessed letters
    guessed_words = [] #stores guessed words
    tries = 6 #number of tries before the whole sad kitty is on full display
    print(display_sad_kitty(tries))
    print(word_completion)
    print("\n")

    word_letters = list(word)

    while not guessed and tries > 0:
        #guess = input("Please guess a letter, or the whole word:\n ").upper()
        guess = input("Please guess a letter, or the whole word:\n ").lower()

        # check that user data is one letter or a word of the riht length
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters: #warns user letter has been already guessed
                print("You already guessed this letter!", guess.upper)
            #elif guess not in word:
            elif guess.lower() not in word: 
                print("Oh no!", guess, "is not in the word.")
                tries -= 1  #substract tries by 1 when guess is wrong
                guessed_letters.append(guess)
      

            else:
                print("Well done,", guess, "is in the word.")#print feedback to user when guess is correct
                guessed_letters.append(guess)
                #displays right guesses to user by replacing underscore by correctly guessed letter
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)#if all underscores are replaced by  letters, word is guessed

        

            '''conditional block checks if word is guessed, if letter is already guessed 
            and whether letter is or is not in the word. '''
            if "_" not in word_completion:
                guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess.upper)
            elif guess != word:
                print(guess.upper, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word  
        else:
            #if user has not provided a letter or word of correct length they get feedback that guess is invalid
            word_length = len(word)
            print("Your guess is not valid.")
            print(f"It needs to be a letter or a word of {word_length} length")
            #print display of sad kitty and of word completion
            print(display_sad_kitty(tries))
            print(word_completion)  
            print("\n")
    
    #check if user guessed or ran out of tries,print right feedback to user that they have won or lost the game
    if guessed:
        print("Congratulations, you guessed the word! Kitty is proud of you!")
    else:
        print("Oh no! You ran out of tries. Kitty is sad :( ")
        print(f"The word was {word}. Kitty wishes you better luck next time!")


def display_sad_kitty(tries):
    """
    This is the display function. 
    It displays the different stages of display of the disappointed cat, one stage for each failed try. 
    """
    stages = [  # final state: head, torso, paws, tail. kitty is disappointed in you
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
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]        

def main():
    """
    This function runs the game and asks the user if they want to play again when the game is over.
    """
    word = get_level()  
    play(word)
    
    while input("Do you want to play again? (Y/N): ")() == "Y":
        word = get_level()  
        play(word)

#code fragment so game runs by running the script on the command line
if __name__ == "__main__":
    main()
 












