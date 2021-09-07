import random
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
boardReset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def showBoard():
    print("----------TIC TAC TOE--------")
    print("Player 1 : X \nPlayer 2 : O")
    print("__________________")
    print("|  %c  |  %c   | %c  |" %(board[1], board[2], board[3]))
    print("|-----|------|----|")
    print("|  %c  |  %c   | %c  |" %(board[4], board[5], board[6]))
    print("|-----|------|----|")
    print("|  %c  |  %c   | %c  |" %(board[7], board[8], board[9]))
    print("-------------------")

def dicission():
    if(board[1] == board[2] and board[2] == board[3]):
        return 1
    elif(board[4] == board[5] and board[5] == board[6]):
        return 1
    elif(board[7] == board[8] and board[8] == board[9]):
        return 1
    elif(board[1] == board[4] and board[4] == board[7]):
        return 1
    elif(board[2] == board[5] and board[5] == board[8]):
        return 1
    elif(board[3] == board[6] and board[6] == board[9]):
        return 1
    elif(board[1] == board[5] and board[5] == board[9]):
        return 1
    elif(board[3] == board[5] and board[5] == board[7]):
        return 1
    else:
        return 0
def play():
    i = 1
    showBoard()
    while(i <= 9):
        player = (i % 2 == 1) and 1 or 2
        try:
            choice = int(input("Player {} : ".format(player)))
            if(choice <= 0 or choice >= 10 or board[choice] == 'X' or board[choice] == 'O' ):
                print("Wrong choice, try again")
            else:
                if(player == 1):
                    board[choice] = 'X'
                else:
                    board[choice] = 'O'
                showBoard()
                if(i >= 5):
                    if(dicission() == 1):
                        print("Player {} won".format(player))#The current player won
                        break
                if(i == 9):
                    print("Match draw")
                    break
                i = i + 1
        except:
            print("Invalid input, try again")
# play()

def playAgainstComputer():
    i = 1
    showBoard()
    while(i <= 9):
        player = (i % 2 == 1) and 1 or 2
        try:
            if(player == 1):
                choice = int(input("Player1(You) : "))
                if(choice <= 0 or choice >= 10 or board[choice] == 'X' or board[choice] == 'O' ):
                    print("Wrong choice, try again")
                    i = i - 1
                else:
                    board[choice] = 'X'
            else:
                if(board[1] == 'O' and board[2] == 'O' and board[3] != 'X'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                elif(board[1] == 'O' and board[2] != 'X' and board[3] == 'O'):
                    board[2] = 'O'
                    print("Player2(Computer) : 2")
                elif(board[1] != 'X' and board[2] == 'O' and board[3] == 'O'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[4] == 'O' and board[5] == 'O' and board[6] != 'X'):
                    board[6] = 'O'
                    print("Player2(Computer) : 6")
                elif(board[4] == 'O' and board[5] != 'X' and board[6] == 'O'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[4] != 'O' and board[5] == 'O' and board[6] == 'O'):
                    board[4] = 'O'
                    print("Player2(Computer) : 4")
                elif(board[7] == 'O' and board[8] == 'O' and board[9] != 'X'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[7] == 'O' and board[8] != 'X' and board[9] == 'O'):
                    board[8] = 'O'
                    print("Player2(Computer) : 8")
                elif(board[7] != 'X' and board[8] == 'O' and board[9] == 'O'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[1] == 'O' and board[4] == 'O' and board[7] != 'X'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[1] == 'O' and board[4] != 'X' and board[7] == 'O'):
                    board[4] = 'O'
                    print("Player2(Computer) : 4")
                elif(board[1] != 'X' and board[4] == 'O' and board[7] == 'O'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[2] == 'O' and board[5] == 'O' and board[8] != 'X'):
                    board[8] = 'O'
                    print("Player2(Computer) : 8")
                elif(board[2] == 'O' and board[5] != 'X' and board[8] == 'O'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[2] != 'X' and board[5] == 'O' and board[8] == 'O'):
                    board[2] = 'O'
                    print("Player2(Computer) : 2")
                elif(board[3] == 'O' and board[6] == 'O' and board[9] != 'X'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[3] == 'O' and board[6] != 'X' and board[9] == 'O'):
                    board[6] = 'O'
                    print("Player2(Computer) : 6")
                elif(board[3] != 'X' and board[6] == 'O' and board[9] == 'O'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                elif(board[1] == 'O' and board[5] == 'O' and board[9] != 'X'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[1] == 'O' and board[5] != 'X' and board[9] == 'O'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[1] != 'X' and board[5] == 'O' and board[9] == 'O'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[3] == 'O' and board[5] == 'O' and board[7] != 'X'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[3] == 'O' and board[5] != 'X' and board[7] == 'O'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[3] != 'X' and board[5] == 'O' and board[7] == 'O'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                elif(board[1] == 'X' and board[2] == 'X' and board[3] != 'O'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                elif(board[1] == 'X' and board[2] != 'O' and board[3] == 'X'):
                    board[2] = 'O'
                    print("Player2(Computer) : 2")
                elif(board[1] != 'O' and board[2] == 'X' and board[3] == 'X'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[4] == 'X' and board[5] == 'X' and board[6] != 'O'):
                    board[6] = 'O'
                    print("Player2(Computer) : 6")
                elif(board[4] == 'X' and board[5] != 'O' and board[6] == 'X'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[4] != 'O' and board[5] == 'X' and board[6] == 'X'):
                    board[4] = 'O'
                    print("Player2(Computer) : 4")
                elif(board[7] == 'X' and board[8] == 'X' and board[9] != 'O'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[7] == 'X' and board[8] != 'O' and board[9] == 'X'):
                    board[8] = 'O'
                    print("Player2(Computer) : 8")
                elif(board[7] != 'O' and board[8] == 'X' and board[9] == 'X'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[1] == 'X' and board[4] == 'X' and board[7] != 'O'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[1] == 'X' and board[4] != 'O' and board[7] == 'X'):
                    board[4] = 'O'
                    print("Player2(Computer) : 4")
                elif(board[1] != 'O' and board[4] == 'X' and board[7] == 'X'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[2] == 'X' and board[5] == 'X' and board[8] != 'O'):
                    board[8] = 'O'
                    print("Player2(Computer) : 8")
                elif(board[2] == 'X' and board[5] != 'O' and board[8] == 'X'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[2] != 'O' and board[5] == 'X' and board[8] == 'X'):
                    board[2] = 'O'
                    print("Player2(Computer) : 2")
                elif(board[3] == 'X' and board[6] == 'X' and board[9] != 'O'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[3] == 'X' and board[6] != 'O' and board[9] == 'X'):
                    board[6] = 'O'
                    print("Player2(Computer) : 6")
                elif(board[3] != 'O' and board[6] == 'X' and board[9] == 'X'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                elif(board[1] == 'X' and board[5] == 'X' and board[9] != 'O'):
                    board[9] = 'O'
                    print("Player2(Computer) : 9")
                elif(board[1] == 'X' and board[5] != 'O' and board[9] == 'X'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[1] != 'O' and board[5] == 'X' and board[9] == 'X'):
                    board[1] = 'O'
                    print("Player2(Computer) : 1")
                elif(board[3] == 'X' and board[5] == 'X' and board[7] != 'O'):
                    board[7] = 'O'
                    print("Player2(Computer) : 7")
                elif(board[3] == 'X' and board[5] != 'O' and board[7] == 'X'):
                    board[5] = 'O'
                    print("Player2(Computer) : 5")
                elif(board[3] != 'O' and board[5] == 'X' and board[7] == 'X'):
                    board[3] = 'O'
                    print("Player2(Computer) : 3")
                else:
                    if(board[5] == '5'):
                        board[5] = 'O'
                        print("Player2(Computer): 5")
                    else:
                        choice_computer = random.randrange(1,10)
                        # if(board[choice_computer] != 'O'):
                        #     if(board[choice_computer] != 'X'):
                        #         board[choice_computer] = 'O'
                        #         print("Player2(Computer x): {}".format(choice_computer))
                        #     else:
                        #         i = i - 1
                        # else:
                        #     if(board[choice_computer] != 'X'):                            
                        #         board[choice_computer] = 'O'
                        #         print("Player2(Computer o): {}".format(choice_computer))
                        #     else:
                        #         i = i - 1
                        if(board[choice_computer] == 'X' or board[choice_computer] == 'O'):
                            i = i - 1
                        else:
                            board[choice_computer] = 'O'
                            print("Player2(Computer ): {}".format(choice_computer))
            showBoard()
            if(i >= 5):
                if(dicission() == 1):
                    if(player == 1):
                        print("Player1(you) won")
                        break
                    else:
                        print("Player2(computer) won")
                        break
            if(i == 9):
                print("Match draw")
                break
            i = i + 1
        except:
            print("Invalid input, try again")

def resetBoard():
    j = 0
    for val in boardReset:
        board[j] = val
        j = j + 1

def main():
    while(True):
        resetBoard()
        print("\nMenu\n1.Play against your friend\n2.Play against computer\n3.exit")
        choice = int(input("Enter your choice : "))
        if(choice == 1):
            play()
        elif(choice == 2):
            playAgainstComputer()
        elif(choice == 3):
            break
        else:
            print("Wrong choice given")

main()