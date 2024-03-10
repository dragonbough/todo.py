import random
import string

password = []

def Generate(length, rules):
    global password
    for i in range(length):
        rule = random.randint(len(rules))
        if rule == "u":
            password.append(string.ascii_uppercase[random.randint(1, len(string.ascii_uppercase)-1)])
        if rule == "l":
            password.append(string.ascii_lowercase[random.randint(1, len(string.ascii_lowercase)-1)])
        if rule == "p":
            password.append(string.punctuation[random.randint(1, len(string.punctuation)-1)])
    return "".join(password)

enabled = []
length = int(input ("How long do you want your password to be?"))
while True:
    i = 0
    if i // 4 == 0:
        print ("Uppercases [U] Lowercases [L] Digits [D] Punctuation [P]")
        print ("GENERATE [G]")
    choice = input ("")
    enabled.append(choice)
    if choice.lower() == "g":
        Generate(length, enabled)
    