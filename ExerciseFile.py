
from ast import In


text = input()
word = input()

def search(text,word):
    
    if word in text:
        return "Word Found"
    else:
       return "Word not Found"
    
print(search(text, word))

