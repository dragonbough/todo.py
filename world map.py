import keyboard


row1 = [".", ".", "."]
row2 = [".", ".", "."]
row3 = [".", ".", "."]

rows = [row1, row2, row3]

def drawMap():
    print (*row1)
    print (*row2)
    print (*row3)
    
positionXY = [2, 2]

def clearPosition():
    for row in rows:
        for i in row:
            if i == "I":
                return "B"
                
def updateMap():
    if positionXY[0] == 1:
        clearPosition()
        row1[positionXY[1] - 1] = "I"
    elif positionXY[0] == 2:
        clearPosition()
        row2[positionXY[1] - 1] = "I"
    elif positionXY[0] == 3:
        clearPosition()
        row3[positionXY[1] - 1] = "I"
    drawMap()

updateMap()

check = "yes"

while check == "yes":
    if keyboard.is_pressed("w"):
        check = "no"
        positionXY[0] -= 1
        updateMap()
check = "yes"

