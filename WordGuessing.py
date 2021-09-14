from tkinter import *
from wordlist import word
import random
import time
import Main
from image import hangman


print (hangman[0])
word = random.choice(word)
length = len(word)
check = length * " _ "
print(check)
guessed_letter = []
lives = 6
wrong = 0
gameWon = False


def Won():
  if gameWon == False:
    print ("Game Over")
    time.sleep(0.5)
    print ("the word is:", word)
  else:
    print ("Congratulation! You are a Champ")



while lives > 0:
  guess = input ("guess a letter or word: ")
  time.sleep(0.1)
  if guess == word:
    gameWon = True
    Won()
    
  for i in range(length):
    right_letter = word[i] #! New variable. contains only guessed letter that store in word
    if guess == word [i]:
      guessed_letter == guess #! still not working
    elif guess not in word:
      wrong += 1
      print (hangman [wrong])
      print ("you guess wrong")
      lives -= 1
      print ("you have remaining lives: ",lives)
      if lives == 0:
        gameWon = False
        Won()
      break
  