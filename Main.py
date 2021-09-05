
from ast import Break, Return
from tkinter import *
import Hangman
import NumberGuessing
import WordGuessing
import time
import WordGuessing

print(" Welcome to our GameHub! \n")
time.sleep(1)
print("Please write your name: ")
name = input()
print("Glad to know you " + name)
time.sleep(1)
print("After this you decide which of the 3 Games you want to Play:")

gameNR = 0 

ans=True
ans = print("""
      
      1.Hangman
      2.Guess the Number
      3.Guess the Word
      4.Exit/Quit\n
      """)

gameNR = input("What would you like to do? ", )

if gameNR == "1":
      Hangman()
elif gameNR == "2":
       NumberGuessing()
elif gameNR == "3":
       WordGuessing
elif gameNR == "4":
      print("\n Goodbye \n")
      ans = False
      Break
else:
      print("\n Not Valid Choice Try again")




# def window():
      # window = Tk()
      # window.title('PythonGuides')
      # window.geometry('400x300')
      # window.config(bg='#A67449')

      # message = '''
      # This is Test Text for a box.
      # CCOOOLLLLLL
      # '''
      # text_box = Text(
      #     window,
      #     height=5,
      #     width=40
      # )
      # text_box.pack(expand=True)
      # text_box.insert('end', message)
      # message2 = '''
      # This is Test Text for a box.
      # CCOOOLLLLLL
      # '''
      # text_box2 = Text(
      #     window,
      #     height=5,
      #     width=40
      # )
      # text_box2.pack(expand=True)
      # text_box2.insert('end', message2)
      # window.mainloop()
