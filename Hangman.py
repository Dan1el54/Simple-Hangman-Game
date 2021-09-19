
#! note: this is the hangman game
from tkinter import *
from wordlist import word
import random
import time
import image



print (image.hangman[0])
word = random.choice(word)
length = len(word)
check = length * " _ "
print(check)
print ("length of the word is", length)
list_of_guess = []
lives = 6
wrong = 0
gameEnd = False #we need to define this. when the gameEnd is true or false

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
        elif guess == ["?", ">", "!", "#", "=", "%", "*", "$", ".", ","]: #? it'snot working with 2 '='
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
                    print (image.hangman[wrong])
                    break
        #* oh and you making so much errors all the time. can you run it again?
        #  yes wait
    else:
        while len(guess) == 0 or len(guess) > 1:
            if guess not in word:
                print ("enter only 1 letter or a whole word") 
            if len(guess) == len(word):
                if guess == word:
                    gameWon()
                else:
                    wrong += 1
                    print(image.hangman[wrong])
                    lives -= 1
                    print("Wrong guess. Remaining lives:", lives)
                    break                    
                    
gameWon()
#* because everywhere errors...
#* wait i need to eat now and i will make a new live share to make all changes
#  clear. okay