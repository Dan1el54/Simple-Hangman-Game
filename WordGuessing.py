from tkinter import *
import wordlist 
import time
import Main
#NOTE This is only for the beginning, we will do a Window where the magic will happen


#todo: the word to guess like _ _ _ _ is not printed in terminal i told


word = input(wordlist) 
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
        if len(guess) == 1 and guess in word:
             for i in range (0, length): 
                  if guess == word[i]:
                       check[i] = guess
                  elif "_" not in check:                     
                        return Won() 
             
play()
def Won():
        if gameWon == True:
          print ("Congratulation! You're a champ")
          return Main.response()
        else:
          print ("Game Over")
          time.sleep (1)
          return Main.response()
Won()













