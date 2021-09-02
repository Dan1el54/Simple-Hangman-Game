from tkinter import *
import Hangman
import NumberGuessing
import WordGuessing


Frame(width=400, height=250)
text_box1 = Text(width=50, height=20)

print(" Welcome to our GameHub! \n")
print("Please write your name: ")
name = input ()
print("Glad to know you " + name)
print("After this you decide which of the 3 Games you want to Play:")

def Menu(ans=True): 
    while ans:
        print("""
        1.Hangman
        2.Guess the Number
        3.Guess the Word
        4.Exit/Quit
        """)
    ans = input("What would you like to do? ")
    if ans == "1":
      Hangman()
    elif ans == "2":
      NumberGuessing()
    elif ans == "3":
      WordGuessing
    elif ans == "4":
      print("\n Goodbye")
      ans = False
    else:
       print("\n Not Valid Choice Try again")


def replay():
    response = input("play again? enter 'yes' or 'no'")

    if response == "yes":
        return "fff"
        #NOTE back to game
    
