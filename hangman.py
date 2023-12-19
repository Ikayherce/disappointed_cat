import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    """this is the play function"""
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # show welcome message
    print("Welcome to hangman. Let's play!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0: 
        guess = input("Please guess a letter, or the whole word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter!", guess)
            elif guess not in word:
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
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True 
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word: 
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
            else:
                 guessed = True 
                 word_completion = word
        else:
            word_length = len(word)
            print("Your guess is not valid.")
            print(f"It needs to be a letter or a word of {word_length} length")
                    
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congratulations, you guessed the word! You can be proud!")
    else:
        print("Oh no! You ran out of tries.")
        print(f"The word was {word}. Better luck next time!")


        

def display_hangman(tries):
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
    word = get_word()
    play(word)
    while input("Do you want to play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
