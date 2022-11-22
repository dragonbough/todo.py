import random
import math
import string
import time
import pyperclip

passDigAmount = int(input ("How many digits do you want your password to be? Enter number:"))
password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = passDigAmount))
print ("Your generated password is:", password)
pyperclip.copy(password)
print ("Password copied to clipboard!")
time.sleep(5)    