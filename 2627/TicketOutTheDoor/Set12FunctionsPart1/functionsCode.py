import random
gameBoard = [""]+[" "]*9
player = "x"
computer = "o"

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print("**************************************************")
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    

def startGame():
    global player
    player = input("Do you want to be x or o?")
    if(player == "o"):
        global computer
        computer = "x"
        
    turn = random.randint(0,1)  
    return turn
    

def checkWin(board):
    if((board[7] == board[8] == board[9] != " ") or 
    (board[4] == board[5] == board[6] != " ") or
    (board[1] == board[2] == board[3] != " ") or
    (board[7] == board[4] == board[1] != " ") or
    (board[8] == board[5] == board[2] != " ") or
    (board[9] == board[6] == board[3] != " ") or
    (board[7] == board[5] == board[3] != " ") or
    (board[1] == board[5] == board[9] != " ")):
         return True
    return False

def isFreeSpace(board):
    for s in board:
          if(s == " "):
                return True
    return False

def playerMove():
    move = input("Where do you want to play?")
    gameBoard[int(move)] = player

def computerMove():
    for s in range(len(gameBoard)):
        if(gameBoard[s] == " "):
            gameBoard[s] = computer
            return

turn = startGame()


while(checkWin(gameBoard)==False and isFreeSpace(gameBoard)==True):
    print("**************************************************")
    if(turn == 0):
        print("Computer turn")
        computerMove()
        drawBoard(gameBoard)
        if(checkWin(gameBoard)):
            print("**************************************************")
            print("LOSER LOSER!")
        turn = 1
    else:
        print("Your turn")
        drawBoard(gameBoard)
        playerMove()
        if(checkWin(gameBoard)):
            print("**************************************************")
            print("WINNER WINNER!")
        turn = 0


drawBoard(gameBoard)   


 












