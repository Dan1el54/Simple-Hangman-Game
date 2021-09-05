from tkinter import *
import wordlist
import random
import time
import Main

#todo: the word to guess like _ _ _ _ printed in terminal

word = random.choice(wordlist)
length = len(word)
check = list(length * "_")
print(check)
lives = 6
gameWon = False

def play():
     while gameWon == False and lives > 0:
        guess = input ("guess a letter or word: ", )
        if guess == wordlist:
          gameWon = True
          Won()
        elif len(guess) == 1 and guess in word:
          for i in range (0, length): 
               if guess == word[i]:
                    check[i] = guess
                    #"_" not in check:                   
     else:
          Won()  
play()

def Won():
        if gameWon == True:
          print ("Congratulation! You're a champ")
          return Main.response()
        else:
          print ("Game Over")
          time.sleep (1)
          return Main.response()
