from tkinter import *
from wordlist import word
import random
import time
import Main



word = random.choice(word)
length = len(word)
check = list(length * "_")
print(check)
lives = 6
gameWon = False


def Won():
  if gameWon == True:
    print("Congratulation! You're a champ")
    time.sleep(0.1)

while gameWon is False or lives > 0:
  guess = input ("guess a letter or word: ")
  time.sleep(0.1)

  if len(guess) == 1 and guess in word:
    for i in range (0, length):
      check = word[i]
      check[i] = guess
  elif guess not in word:
        lives -= 1
  elif lives == 0:
      print("Game Over")
      time.sleep(0.1)
      Main.response()

