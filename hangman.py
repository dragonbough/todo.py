from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)
import random

mode = "normal"
redraw = "no"
wordlen = []
letters = []
guesscheck = []
win = "null"
stage = 0
draw = "yes"
count = 0

def drawHangman():
    if stage == 7:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|        -|-")
        print("|        ""/ \\")
        print("|")
        print("\nH A N G M A N!\n")
    elif stage == 6:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|        -|-")
        print("|        /")
        print("|")
        print("\nH A N G M A\n")
    elif stage == 5:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|        -|-")
        print("|")
        print("|")
        print("\nH A N G M\n")
    elif stage == 4:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|        -|")
        print("|")
        print("|")
        print("\nH A N G\n")
    elif stage == 3:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|         |")
        print("|")
        print("|")
        print("\nH A N\n")
    elif stage == 2:
        print("-----------")
        print("|         |")
        print("|         @")
        print("|")
        print("|")
        print("|")
        print("\nH A\n")
    elif stage == 1:
        print("-----------")
        print("|         |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("\nH\n")
    elif stage == 0:
        print("-----------")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\n")
     
#Gets a random word from the word list (sets are unordered so you cannot take a word from an index, but
#rather iterate 
word = list(web2lowerset)[0]
for i in word:
    wordlen.append("_")
    letters.append(i)

print ("\nWELCOME TO H A N G M A N")
print ("Play")
print ("Options")
select = input ("")
if select == "options":
    print ("What mode do you want to play the game in?")
    print ("normal or debug?")
    mode = input ("")
    print ("Redraw hangman even when guess is correct (or has been entered already)?")
    print ("Yes or no?")
    redraw = input ("")

while win == "null":
    if redraw == "no":
        drawHangman()
    elif draw == "yes":
        drawHangman()
        draw = "no"
    print ("The word is:")
    print(" ".join(wordlen))
    if mode == "debug":
        print (word)
        print (letters)
    guess = input ("\nGuess a letter: ")
    if guess not in guesscheck:
        if guess in letters:
            guesscheck.append(guess)
            for i in range(len(letters)):
                if letters[i - 1] == guess:
                    wordlen[i - 1] = guess
        elif guess == "".join(letters):
            win = "win"
        else:
            guesscheck.append(guess)
            stage += 1
            if redraw == "yes":
                draw = "yes"
    else:
        print ("\nYou have already guessed this letter.")
        if redraw == "yes":
            draw = "no"
        continue
    if "_" not in wordlen:
        win = "win"
    if stage == 7:
        drawHangman()
        win = "loss"
if win == "win":
    print ("\nYOU WIN!!")
if win == "loss":
    print ("\nYOU LOSE!!")
    print ("The word was: ", "".join(letters))

               
        

