
# note: HANGMAN TESTFILE

import wordlist
import random
import time
import image
import Main

#todo: we need to figure out how to import stuff from a other folder.



def attr():
    print(image.hangman[0])
    word = random.choice(wordlist.list_of_word)
    length = len(word)
    check = length * " _ "
    list_of_guess = []
    lives = 6
    wrong = 0
    return (length, check, list_of_guess, lives, wrong, word)

def gameStart():
    print(attr.check)
    print("length of the word is", attr.length)
    return attr.length

def gameWon():  
    if attr.guess == attr.word: 
        print("Congratulation! You won!")
    elif attr.lives == 0: 
        print("Game Over. The word is:", attr.word)
    end()

def end():
    yes = 1
    no = 0
    inp = input("You want to go back to the Main Menu?")
    if inp == yes:
        Main()
    else:
        exit()

def invalid():
    if attr.guess.isnumeric():
        print("You enter numeric! Only letters allowed")
    elif len(attr.guess) == 0:  
        print("Enter a letter or a word")
    else:
        print("Input invalid. Enter a letter or a word")

def gamePlay():
    while attr.lives > 0: 
        guess = input("guess a letter or a word: ") 
        time.sleep(0.1)                             
        if attr.guess in attr.list_of_guess:
            print("You already guess that letter/word. Enter a new letter or word")
        elif len(attr.guess) >= 1: #warning: this will not works
            for i in range(attr.length):
                right_letter = ""
                if attr.word[i] == guess:  
                    guess = right_letter
                    print(i, end="")
                    print()
                else:
                    attr.lives -= 1
                    print("Wrong guess. Remaining lives:", attr.lives)
                    attr.wrong += 1
                    print(image.hangman[attr.wrong])
                    attr()
                    
    attr.list_of_guess.append(attr.guess)
    gameWon()         
    invalid()
gameStart()
gamePlay()
# note: append function will add variable (guess) to the list_of_guess. have to be added at the last code so that the first guess will not be filtered

