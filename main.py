#this is the first file of this project
#NOTE: strftime is string, so need to use (" "),  yeah right
#NOTE: %Y:year, %m:month, %d;day, %H:hours, #M:minutes, #S:seconds
#NOTE: PAY ATTENTION TO THE CAPITAL LETTER. Same like True!=true, False!=false
#NOTE: i think % is for the format. Or maybe it is some kind of function to call the (idk the what XD)

from datetime import datetime
now = datetime.now()  # variable 1; current date and time


def Date():
    year = now.strftime ("%Y") #variable 2    
    month = now.strftime("%m") #variable 3    
    day = now.strftime("%d") #variable 4 :why the color of %d is different than others?    
    return(day,month,year)

def time_now():    
    time = now.strftime("%H:%M:%S")    
    return(time)


print(Date(),time_now())

#? let's continue this tomorrow okay. im really sleepy
#* yeah no problem sleep well tere :D
#? night
