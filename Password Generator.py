
#*Password Generator

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]()-!?/&$%+"

all = lower + upper + number + symbol
length = 26
password = "".join(random.sample(all,length))

print(password)
