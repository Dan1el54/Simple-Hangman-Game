from tkinter import *
import random
#NOTE This is only for the beginning, we will do a Window where the magic will happen
#? okay

def thirdGame():
    
    guess = ["january", "february", "flower", "tree", "cloud", "snow", "book", "picture", "laptop", "sheep",
         "printer", "phone", "pencil", "mouth", "camera", "glasses", "telenovela", "television", "rain"]
    word = random.choice(guess)
    count = 0
    length = len(word)
    display = "_" * length
    print("guess the word" + length)

