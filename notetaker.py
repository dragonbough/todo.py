notesDict = {}

def DisplayNote(note):
    print (note + ": \n")
    print (notesDict[note])

def CreateNote():
    noteName = input ("What would you like to call your note?: ")
    print (noteName)
    lines = []
    print ("Press enter for a new line\n ")
    while True:
        text = input (str(len(lines)+1) + " ")
        if text == "\end":
            break
        lines.append(text)
    note = lines.join(" ")
    DisplayNote(note)
    
CreateNote()