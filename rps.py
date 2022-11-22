import random
import time

rps = input ("rock paper or scissors?")

if rps == "rock":
    opp = random.randint(1, 3)
    if opp == 1:
        print ("Opponent chose rock! Its a draw")
    elif opp == 2:
        print ("Opponent chose paper! You lose")
    elif opp == 3:
        print ("Opponent chose scissors! Yuo win")
if rps == "paper":
    opp = random.randint(1, 3)
    if opp == 1:
        print ("Opponent chose rock! You win")
    elif opp == 2:
        print ("Opponent chose paper! draw")
    elif opp == 3:
        print ("Opponent chose scissors! you lose")
if rps == "scissors":
    opp = random.randint(1, 3)
    if opp == 1:
        print ("Opponent chose rock! You lose")
    elif opp == 2:
        print ("Opponent chose paper! you win")
    elif opp == 3:
        print ("Opponent chose scissors! you draw")