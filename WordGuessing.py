from tkinter import *
from wordlist import word
import random
import time
from image import hangman


print (hangman[0])
word = random.choice(word)
length = len(word)
check = length * " _ "
print(check)
print ("length of the word is", length)
list_of_guess = []
lives = 6
wrong = 0
gameEnd = False
if gameEnd:
 print() 

def gameWon():
  if guess == word or " _ " not in check:
    return "gg"

def gameEnd():
  return 11


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
  
  if len(guess) == 1:
    if guess.isnumeric():
      print("You enter a numeric! Enter only a letter")
    if guess in list_of_guess:
      print ("You already guess that letter")
    elif guess = ["?", ">", "!", "#", "=", "%", "*", "$", ".", ","]
    #note why there are two of this file? idk. is this from pygame? yes. ill
    #delete the other later whhich one of them
      print("Input invalid. Enter a letter or a word") 
  elif len(guess) == 0 or len(guess) > 1 :
    print ("enter only 1 letter or a whole word") 
  if len(guess) == len(word):
    if guess == word:
      gameWon()
    if guess in list_of_guess:
      print ("you already guess that word")
    else:
      wrong += 1
      print (hangman[wrong])
      lives -= 1
      print("Wrong Guess")
      print ("You have remaining lives:", lives)
  
    
  for i in range(length):
    right_letter = i
    if word[i] == guess:
      print(i, end="")  
    if guess not in word:
      lives -= 1
      print ("Wrong guess. Remaining lives:", lives)
      wrong += 1
      print (hangman[wrong])
    break
gameWon()