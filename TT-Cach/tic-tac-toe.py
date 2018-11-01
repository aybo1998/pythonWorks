
import os
import random as rd

board = [" "," "," "," "," "," "," "," "," "]
computer_board = ['1', '2', '3', '4', '5', '6', '7', '8','9']

empty_error = False
wrong_place = False
wrong_input = False

player = 'X'
choice = None

def print_header():
    print('''

 _____  _  ____     _____  ____  ____     _____  ____  _____ 
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/         1|2|3   
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \           4|5|6   
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_          7|8|9
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\            
                                                                                      
    ''')


def print_board():
    print(" | | ")
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("_|_|_")
    print(" | | ")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("_|_|_")
    print(" | | ")
    print(board[6]+"|"+board[7]+"|"+board[8])
    print(" | | ")

def print_error():
    global empty_error,wrong_place,wrong_input
    if empty_error :
        print("\nPlease enter a value.\n")
        empty_error = False
    elif wrong_place:
        print("\nPlease enter a correct place.\n")
        wrong_place = False
    elif wrong_input:
        print("\nPlease enter a correct value.\n")
        wrong_input = False

def print_mode(mode):
    if mode == "p_to_c":
        print("\nPerson To Comouter Mode\n")
    else:
        print("\nPerson To Person Mode\n")

def repeat_or_exit(status='win'):
    print_header()
    print_board()
    if status == "win":
        print("\n"+ player +" win !\n")
    elif status == "tie":
        print("\n Tie !! \n")
    while True:
        answer = input("To repeat the game press Enter and to exit enter exit")
        if(len(answer)==0):
            global board , computer_board
            board = [" "," "," "," "," "," "," "," "," "]
            computer_board = ['1', '2', '3', '4', '5', '6', '7', '8','9']
            break
        elif answer == "exit":
            exit()

def is_winner(player):
    global board
    if((board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player) or \
       (board[0] == player and board[4] == player and board[8] == player)):
           return True

def check_error():
    global empty_error,wrong_place,wrong_input,choice
    if choice == "":
        empty_error = True
        return True
    elif choice not in ['1', '2', '3', '4', '5', '6', '7', '8','9']:
        wrong_input = True
        return True
    elif board[int(choice)-1] != " ":
        wrong_place = True
        return True

def computer_move():
    global computer_board,board

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if is_winner("X"):
                board[i] = " "
                return str(i+1)
            board[i] = " "
            
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if is_winner("O"):
                board[i] = " "
                return str(i+1)
            board[i] = " "
    if len(computer_board) == 9:
        if board[4] == " ":
            return "5"
    elif len(computer_board) == 7:
        if board[0] == " ":
            return "1"
        elif board[2] == " ":
            return "3"
        elif board[6] == " ":
            return "7"
        elif board[8] == " ":
            return "9"
    elif len(computer_board) == 5:
        if board[4] == " ":
            return "5"
    else:
        if board[0] == " ":
            return "1"
        elif board[2] == " ":
            return "3"
        elif board[6] == " ":
            return "7"
        elif board[8] == " ":
            return "9"

    choice = rd.choice(computer_board)
    return choice

def play(mode):
    computer_turn = True
    global choice,computer_board,player, board,empty_error,wrong_place,wrong_input
    while True:
        
        
        if mode == "p_to_p" or computer_turn == False :
            os.system("clear")
            print_header()
            print_mode(mode)
            print_board()
            print_error()
            choice = input("Enter  the place of your "+player+" :")
        elif computer_turn :
            choice = computer_move()
            print(choice)
            computer_board.remove(choice)
        # check user input 
        if(check_error()):
            continue
        
        
        if mode == "p_to_c":
            if computer_turn == False:
                computer_board.remove(choice)
        computer_turn = not(computer_turn)
        board[int(choice)-1] = player


        # to check there is a winner or it's tie
        if(is_winner(player)):
            repeat_or_exit()
        elif " " not in board:
            repeat_or_exit("tie")

            
                
        # change the player        
        player = "O" if player == "X" else "X"


while True:
    print_header()
    print(("{:^60}").format("Welcome to Tic-Tac-Toe Game"))
    print(("{:^60}").format("The Menu"))
    print("\n    1- play person vs person.")
    print("    2- play person vs computer.")
    print("    3- exit.\n")
    game_mode = input("Enter your choice: ")
    if game_mode == "1":
        play("p_to_p")
    elif game_mode == "2":
        play("p_to_c")
    elif game_mode == "3":
        break
    else:
        continue
        
    
     
