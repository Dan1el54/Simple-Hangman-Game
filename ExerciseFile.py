#! don't delete thisss

# Search Engine

# Youre working on a search engine. Watch your back Google!

# The given code takes a text and a word as input and passes them to a function called search().

# The search() function should return:
#! The search() function should return "Word found" if the word is present in the text, or "Word not found", if its not. (this is the key word)
#? word must be present in text 
#* yes but present in this case is the if 
#*if word is present in text
#* you see in blue? they say i need to define search()

# Sample Input
# "This is awesome"
# "awesome"

# Sample Output
# Word found

#NOTE: Define the search() function, so that the given code works as expected.


def search(text,word):  
    if word in text:
        return("Word found")
    else:
        return("Word not found")
    
text = input() 
word = input()            
print (search(text, word))

#* im eating lunch and then we can continue