
from ast import Return
from tkinter import *
import Hangman
import NumberGuessing
import WordGuessing
import time
import WordGuessing

gameNR = 0

print(" Welcome to our GameHub! \n")
time.sleep(1)
print("Please write your name: ")
name = input ()
print("Glad to know you " + name)
time.sleep(1)
print("After this you decide which of the 3 Games you want to Play:")

ans=True
while ans:
      print("""
      1.Hangman
      2.Guess the Number
      3.Guess the Word
      4.Exit/Quit
      """)
gameNR = input("What would you like to do? ", )
breakpoint()
if gameNR == "1":
      Hangman()
elif gameNR == "2":
       NumberGuessing()
elif gameNR == "3":
       WordGuessing()
elif gameNR == "4":
      print("\n Goodbye")
      ans = False
else:
      print("\n Not Valid Choice Try again")

#* idk why its looping i need to find the key. it is if loops.
#?  need a break point. waitt, it;s running on my local drive
#* and? but i save   commee heerreeeeee chat is bad inside of
#  the code blocks
#* we cant use ans  for the menu.
#* its a boolean not an int or float









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
