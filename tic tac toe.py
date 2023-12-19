from operator import indexOf

def initBoard():
    print (board[0], board[1], board[2])
    print (board[3], board[4], board[5])
    print (board[6], board[7], board[8])

def checkBoard():
    #for X
    #down checks
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return "X"
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        return "X" 
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        return "X"
    #across checks
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return "X"
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        return "X" 
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        return "X"
    #diagonal checks
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return "X"
    if board[6] == "X" and board[4] == "X" and board[2] == "X":
        return "X"
    #for O
    #down checks
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        return "O"
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        return "O" 
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        return "O"
    #across checks
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        return "O"
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        return "O"
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        return "O"
    #diagonal checks
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        return "O" 
    if board[6] == "O" and board[4] == "O" and board[2] == "O":
        return "O"

board = [0,1,2,
         3,4,5,
         6,7,8]

turn = 0

while True:
    initBoard()
    if turn == 0:
        coord = int(input ("Player 1, enter number of box you want to change"))
        if coord in board:
            board[board.index(coord)] = "X"
            if checkBoard() == "X":
                print ("Player 1 has won!")
                break
            turn = 1
        else:
            print ("Invalid selection")
            continue
    elif turn == 1:
        coord = int(input ("Player 2, enter number of box you want to change"))
        if coord in board:
            board[board.index(coord)] = "O"
            if checkBoard() == "O":
                print ("Player 2 has won!")
                break
            turn = 0
        else:
            print ("Invalid selection")
            continue


