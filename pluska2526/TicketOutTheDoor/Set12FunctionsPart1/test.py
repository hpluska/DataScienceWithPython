import random
player = "x"
computer = "o"
turn = ""

def startGame():
    choice = input("Do you want to be x or o?")
    if(choice == "o"):
        global computer
        global player

        computer = "x"
        player = "o"
        if(random.random() < 0.5):
            global turn
            turn = computer
        

startGame()
