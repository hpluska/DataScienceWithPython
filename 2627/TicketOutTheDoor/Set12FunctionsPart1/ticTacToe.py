import random

#define variables
player = "x"
computer = "o"
turn = "computer"
gameBoard = [""] + [" "]*9

def startGame():
     global player
     global computer
     global turn
     choice = input("Do you want to be x or o?")
     if(choice == "o"):
        player = "o"
        computer = "x"
     if(random.random() < 0.5):
        turn = player
        
#better to use parameter
def playerMove(board):
     move = input("Where do you want to play?")
     move = int(move)
     board[move] = player

def drawBoard(board):
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

#better to use parameter
def computerMove(board):
     for space in range(len(board)):
          if(board[space] == " "):
               board[space] = computer
               break
             

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
    else:
         return False

def isFreeSpace(board):
     for space in board:
          if(space == " "):
               return True 
     return False

startGame()
playerMove(gameBoard)
computerMove(gameBoard)
drawBoard(gameBoard)
print(checkWin(gameBoard))
print(isFreeSpace(gameBoard))

#while(checkWin(gameBoard) == False and isFreeSpace(gameBoard) == True):
     #keep playing
     #if(turn == computer)

