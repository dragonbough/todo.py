import keyboard

playerDigit = "X"

row1 = ["a", "b", "c"]
row2 = ["d", "e", "f"]
row3 = ["g", "h", "i"]

uRow1 = ["_", "_", "_"]
uRow2 = ["_", "_", "_"]
uRow3 = ["_", "_", "_"]

rows = [row1, row2, row3]

def DrawMap():
    print (*uRow1)
    print (*uRow2)
    print (*uRow3)
    
position = 0
                
def UpdateMap():
    if position == "a":
        uRow1[row1.index("a")] = playerDigit
    elif position == "b":
        uRow1[row1.index("b")] = playerDigit
    elif position == "c":
        uRow1[row1.index("c")] = playerDigit
    elif position == "d":
        uRow2[row2.index("d")] = playerDigit
    elif position == "e":
        uRow2[row2.index("e")] = playerDigit
    elif position == "f":
        uRow2[row2.index("f")] = playerDigit
    elif position == "g":
        uRow3[row3.index("g")] = playerDigit
    elif position == "h":
        uRow3[row3.index("h")] = playerDigit
    elif position == "i":
        uRow3[row3.index("i")] = playerDigit 
    DrawMap()

UpdateMap()

while True:
    if keyboard.is_pressed("a"):
        position = "a"
        UpdateMap()

        

