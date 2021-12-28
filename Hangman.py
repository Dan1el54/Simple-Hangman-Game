
# #note: this is the hangman game
# from tkinter import *
# import wordlist
# import random
# import time
# import image


# print(image.hangman[0])
# word = random.choice(wordlist.word)
# length = len(word)
# check = length * " _ "
# print(check)
# print("length of the word is", length)
# list_of_guess = []
# lives = 6
# wrong = 0
# gameEnd = False  #note: we need to define this. When the gameEnd is True or False


# def gameEnd(gameEnd):
#     if gameEnd == True:
#         print(" You Won! ")

# #note
# #+chat2
# ##chat1
# #warning
# #error
# #question
# #todo


# def gameWon():  # note: name of define is gameWon. gameEnd is true if:
#     if guess == word:  # note: True if guess is word: Win. Code finish running
#         gameEnd = True
#         print("Congratulation! You won!")
#     elif lives == 0:  # note: True if lives = 0: lose. Code finish running
#         gameEnd = True
#         print("Game Over. The word is:", word)
#     else:  # note: False if anything else other than those 2 True condition. Then code while loop will run.
#         gameEnd = False


# while gameEnd == False and lives > 0:
#     guess = input("guess a letter or a word: ")
#     time.sleep(0.1)

# note: condition 1: guess word that already in the list will not reduce lives and return (print)
#     if guess in list_of_guess:
#         print("You already guess that letter/word. Enter a new letter or word")

#     elif len(guess) == 0:  # note: condition 2: if guess is "(no letter)", lives will not reduce
#         print("Enter a letter or a word")

#     elif len(guess) == 1:  # note: condition 3: length of guess is exactly 1 letter
#         if guess.isnumeric():  # note: UNDER CONDITION 3: BUT in numeric. Will not reduce lives
#             print("You enter a numeric! Enter only a letter")
#         elif guess == ["?", ">", "!", "#", "=", "%", "*", "$", ".", ","]:  # warning: not working
#             print("Input invalid. Enter a letter or a word")
#         else:  # note: UNDER CONDITION 3: letter is alphabet
#             for i in range(length):
#                 right_letter = i
#                 if word[i] == guess:  # warning: not working
#                     print(i, end="")
#                 if guess not in word:
#                     lives -= 1
#                     print("Wrong guess. Remaining lives:", lives)
#                     wrong += 1
#                     print(image.hangman[wrong])
#                     break

#     else: # note: condition 4, if guess length is as much as word length
#         while len(guess) > 1:
# note: UNDER CONDITION 4: ONLY works if length guess is exactly as much as length word
#             if len(guess) == len(word):
#                 if guess == word:  # note: > guess is word: win
#                     gameWon()
#                 else:  # note: UNDER CONDITION 4: guess is not word: lose
#                     wrong += 1
#                     print(image.hangman[wrong])
#                     lives -= 1
#                     print("Wrong guess. Remaining lives:", lives)
#                     gameWon()
# note: UNDER CONDITION 4: length guess is more than 1 (but not exactly as much as word length)
#             if guess not in word:
#                 print("enter only 1 letter or a whole word")
#                 break
# note: append function will add variable (guess) to the list_of_guess. have to be added at the last code so that the first guess will not be filtered
#     list_of_guess.append(guess)
