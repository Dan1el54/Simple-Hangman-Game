from tkinter import *
from wordlist import word
import random
import time
from image import hangman


print (hangman[0])
word = random.choice(word)
length = len(word)
check = length * "_"
print(check)
print ("length of the word is", length)
lives = 6
wrong = 0
gameEnd = False

def gameEnd():
  return 11


def gameWon(gameEnd):
  if guess == word:
    gameEnd = True
    print ("Congratulation! You won!")
    print (hangman[lives])
  if lives == 0:
    gameEnd = True
    print ("Game Over. The word is:", word)
  else:
    gameEnd = False
  
while gameEnd == False and lives > 0:
  guess = input("guess a letter or word: ")
  time.sleep (0.1)

  if guess.isnumeric:
    print("You enter a numeric! Enter only a letter")
  elif len(guess) == 0:
    print ("enter only 1 letter or a whole word") 
  elif len(guess) == len(word):
    if guess == word:
      gameWon()
    else:
      lives -= 1
      wrong += 1
      print (hangman[wrong])
      print("wrong guess")
      print ("you have remaining lives:", lives)
  else:
    print("input invalid. enter a letter or a word") 
    
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