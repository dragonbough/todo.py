row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

def Display():
    print (*row1)
    print (*row2)
    print (*row3)

def FindRow(location, symbol):
    if location in row1:
        row1[location - 1] = symbol
    if location in row2:
        row2[location - 4] = symbol
    if location in row3:
        row3[location - 7] = symbol

def CheckWin():
    if any(i == ("X", "X", "X") for i in (row1, row2, row3)):
        win = x
    if all(i == ("X") for i in (row1[0], row2[0], row3[0)):
        win = x
    if all(i == ("X") for i in (row1[1], row2[1], row3[1)):
        win = x
    if all(i == ("X") for i in (row1[2], row2[2], row3[2])):
        win = x
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        win = x
    elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        win = x
    elif any(i == ("O", "O", "O") for i in (row1, row2, row3)):
        win = o
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        win = x
    elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        win = x
    elif row1 != (
        
turn = 0

while win = null:
    if turn == 0:
        Display()
        l = int(input ("Input location of X"))
        FindRow(l, "X")
        turn += 1 

    if turn == 1:
        Display()
        l = int(input ("Input location of O"))
        FindRow(l, "O")
        turn += 1

    if turn > 1:
        turn = 0
        
