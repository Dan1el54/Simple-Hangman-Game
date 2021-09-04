from tkinter import *
import Hangman
import NumberGuessing
import WordGuessing


window = Tk()
window.title('PythonGuides')
window.geometry('400x300')
window.config(bg='#A67449')

message = '''
This is Test Text for a box. 
CCOOOLLLLLL
'''
text_box = Text(
    window,
    height=13,
    width=40
)
text_box.pack(expand=True)
text_box.insert('end', message)
message2 = '''
This is Test Text for a box. 
CCOOOLLLLLL
'''
text_box2 = Text(
    window,
    height=20,
    width=40
)
text_box2.pack(expand=True)
text_box2.insert('end', message2)
window.mainloop()




print(" Welcome to our GameHub! \n")
print("Please write your name: ")
name = input ()
print("Glad to know you " + name)
print("After this you decide which of the 3 Games you want to Play:")
Menu()
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
        return window()
        #note back to game
    else:
      window()

        