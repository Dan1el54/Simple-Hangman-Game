#? this is the hangman game
from tkinter import *
from wordlist import word
import random
import time
from image import hangman
import Main

#! can you run this?

print (hangman[0])
word = random.choice(word)
length = len(word)
check = length * " _ "
print(check)
print ("length of the word is", length)
list_of_guess = []
lives = 6
wrong = 0
gameEnd = False #we need to define this. when the gameEnd is true or false

#! which one is the hangman file? this one


def gameWon(gameEnd):
    if guess == word:
        gameEnd = True
        print ("Congratulation! You won!")
    if lives == 0:
        gameEnd = True
        print ("Game Over. The word is:", word)
    else:
        gameEnd = False
  
while gameEnd == False and lives > 0:
    guess = input("guess a letter or a word: ")
    time.sleep (0.1)
    
    if guess in list_of_guess:
        print ("You already guess that letter/word. Enter a new letter or word")
        list_of_guess.append(guess)
        break
  
    if len(guess) == 1:
        if guess.isnumeric():
            print("You enter a numeric! Enter only a letter")
        elif guess == ["?", ">", "!", "#", "=", "%", "*", "$", ".", ","]:
            print("Input invalid. Enter a letter or a word") 
        else:
            for i in range(length):
                right_letter = i
                if word[i] == guess: #? this is not working at all
                    print(i, end = "")  
                if guess not in word:
                    lives -= 1
                    print ("Wrong guess. Remaining lives:", lives)
                    wrong += 1
                    print (hangman[wrong])
        
    else:
        while len(guess) == 0 or len(guess) > 1:
            if guess not word:
                print ("enter only 1 letter or a whole word") 
            if len(guess) == len(word):
                if guess == word:
                    gameWon()
                else:
                    wrong += 1
                    print (hangman[wrong])
                    lives -= 1
                    print("Wrong guess. Remaining lives:", lives)
    gameWon()
