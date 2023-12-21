
# Sad Kitty

Sad Kitty is a classic hangman game with a twist. Instead of seeing a dangling man displayed when you guess wrong, you see a cat who is disappointed in you. 
Sad Kitty is my porftolio project 3 for Code Insitute, coded with Python. 

[Link to live site] 

![amIresponsive image](assets/images/readmeimages/amiresponsive.png)


## Index - Table of Contents

- [Planning](#planning)

- [UX](#ux)
    - [Programm Goals](#programm-goals)
    - [User Stories](#user-stories)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [Data Model](#data-model)

- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Testing User Stories](#testing-user-stories-functionality)

- [Debugging](#debugging)
    - [Fixed bugs](#fixed-bugs)
    - [Unfixed bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Credits](#credits)
    - [Data](#data)
    - [Code](#code)
    - [Styling](#styling)

## Planning

My plan consisted in designing a simple hangman application that would have a main play function to handle data input from user and give feedback, and a display function to display the different visual stages of Sad Kitty depending on the number of failed answers. After this logic was put in place I decided to add the level class in order to make it possible for the user to play choosing among three different levels (easy, medium or hard).

## UX 
### Program goals 

The goal of this program is to entertain the user with a simple hangman console game, and at the same time amuse with the twist of a sad cat instead of the classic stick figure. By being able to choose a level of difficulty, the user can play the game several times with variation. 

### User stories 
#### The user wants to
- see the introduction text
- see brief instruction
- choose a level of difficulty (easy, medium or hard)
- get feedback on correct and incorrect guesses
- get feedback on when given data is invalid
- get feedback and see the correct word displayed after losing a game
- get feedback when game is won and see word displayed
- get the option to choose whether they want to play again or not 


## Features
### Existing features
- Welcome message
- Level choice 
- Feedback "invalid data" when user gives invalid input
- Feedback when user replies correctly
- Feedback when user replies incorrectly
- Sad Kitty display
- Feedback for won or lost game
- Option to play again or exit the game

### Possible future features
 - Adding colors to the design and more forms of visual appeal to the game. 
 - A logo display at the beginning of the game 

## Debugging

### Fixed bugs
 - Game wouldn't return a correct answer feedback even when user introduced right letter. This happened because the list of words in words.py was in lower case, while the code was expecting upper case letters. This was fixed by converting the input from the user into lowercase. 
### Unfixed bugs 
- User doesn't get correct number of guesses .
- Game doesn't run again when user gives input "y" 
## Deployment 
- The code has been created in the IDE Gitpod, stored and pushed to Github's repository and then deployed in Heroku via Github, using Code Institute's mockterminal.  
In order to deploy in Heroku, I used the instructions provided by Code Institute for this project, see below: 

* When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows: 1. `heroku/python` 2. `heroku/nodejs`
* You must then create a _Config Var_ called `PORT`. Set this to `8000`
* If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
* Connect your GitHub repository and deploy as normal. 


## Testing
https://pep8ci.herokuapp.com/

Lighthouse

Manual testing
## Credits
### Code ### 
Project on Github by fellow Code Institute student:
https://github.com/Kathrin-ddggxh/CI-PP3_hangman 

Youtube Tutorials: 
https://www.youtube.com/watch?v=JNXmCOumNw0

https://www.youtube.com/watch?v=TWLD2OKmSCQ

https://www.youtube.com/watch?v=cJJTnI22IF8

https://www.youtube.com/watch?v=m4nEnsavl6w 

https://www.youtube.com/watch?v=pFvSb7cb_Us

### README file ### 
Inspired by https://github.com/Kathrin-ddggxh/CI-PP3_hangman 

### List of words (content) ###
The list of words stored in words.py was created with help of chat GPT