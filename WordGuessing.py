from tkinter import *
from wordlist import word
import random
import time
import Main

word = random.choice(word)
length = len(word)
check = length * ['_']
wrong_guess = 0
guess_letter = []
print(check)
lives = 6
gameWon = False  

def Won():
  if gameWon == True:   
    print("Congratulation! You're a champ")
    time.sleep(0.1)
  else:
    print("Game Over")
    time.sleep(1)
    print ("The word is ", word)
    time.sleep(0.1)
    Main.response()
    
    

def right():
  for i in check:
    print(i, end = " ")
   
while gameWon is False or lives > 0:
  guess = input ("guess a letter or word: ")
  time.sleep(0.1)
  if guess == word or len(guess) == length:
    gameWon == True
    Won ()
  for i in word:
    if guess in word:
      index=0
      if i == guess:
        check[index]=guess
        index += 1
      right()
      
  if len(guess) == 1 and guess.isalpha:
    if guess not in word:
      print ("you guessed wrong")
      lives -= 1
      print ("you have remaining lives: ", lives)
    if lives == 0:
      gameWon == False
      Won()

#note: if you debug, click for exit: control+f2
