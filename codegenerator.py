import random
import pyperclip

decodeList = []
textList = []

def TextEncoder(inputText):
    textList = []
    for letter in inputText:
        newLetter = (ord(letter) + 3)
        textList.append(chr(newLetter))
    encodedText = ("".join((textList)))
    return encodedText
def TextDecoder(decodeText):
    decodeList = []
    for dLetter in decodeText:
        oldLetter = (ord(dLetter) - 3)
        decodeList.append(chr(oldLetter))
    decodedText = ("".join((decodeList)))
    return decodedText

w = 1
while w == 1:
    start = input ("Would you like to decode or encode text?")
    if start == "encode":
        w = 0
        encodeText = input ("Write the text you would like to encode here:")
        encodedText = (TextEncoder(encodeText))
        pyperclip.copy(encodedText)
        print(encodedText)
        print ("Encoded text has been copied to the keyboard!")
        w = 1

    if start == "decode":
        w = 0
        decodeText = input ("Paste the text you would like to decode here:")    
        decodedText = (TextDecoder(decodeText))
        pyperclip.copy(decodedText)
        print(decodedText)
        print ("Decoded text has been copied to the keyboard!")
        w = 1