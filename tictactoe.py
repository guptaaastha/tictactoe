import random;

board = [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]

user_symbol="X"
computer_symbol="O"
winner_symbol=""

def print_board():
    for row in board:
        for item in row:
            print(item, end=" ")
        print("\n")

def user_input():
    user_move = input("Enter your move x , y space-separated: ")
    user_move = list(map(int, user_move.split()))
    while board[user_move[0]][user_move[1]]==user_symbol or board[user_move[0]][user_move[1]]==computer_symbol:
        print("Invalid Input. Try Again !!")
        user_move = input("Enter your move x , y space-separated: ")
        user_move = list(map(int, user_move.split()))
    board[user_move[0]][user_move[1]]=user_symbol
           

def computer_input():
    x=random.randint(0,2)
    y=random.randint(0,2)
    while board[x][y]==user_symbol or board[x][y]==computer_symbol:
        x=random.randint(0,2)
        y=random.randint(0,2)  
    board[x][y]=computer_symbol

def is_tie():
    for row in board:
        for item in row:
            if item == user_symbol or item ==computer_symbol:
                tie = True
            else:
                tie = False
                return tie
    return tie

def has_won(player_symbol):
    if board[0][0]==board[0][1]==board[0][2]==player_symbol :
        return True
    elif board[1][0]==board[1][1]==board[1][2]==player_symbol :
        return True
    elif board[2][0]==board[2][1]==board[2][2]==player_symbol :
        return True
    elif board[0][0]==board[1][0]==board[2][0]==player_symbol :
        return True
    elif board[0][1]==board[1][1]==board[2][1]==player_symbol :
        return True
    elif board[0][2]==board[1][2]==board[2][2]==player_symbol :
        return True
    elif board[0][0]==board[1][1]==board[2][2]==player_symbol :
        return True
    elif board[0][2]==board[1][1]==board[2][0]==player_symbol :
        return True
    else:
        return False

user_symbol=input("Choose symbol X or O: ")
if user_symbol=="X":
    computer_symbol="O"
else:
    computer_symbol="X"

while not has_won(user_symbol) and not has_won(computer_symbol) and not is_tie():
    user_input()
    print_board()
    if not has_won(user_symbol) and not is_tie():
        print("Computer's move:")
        computer_input()
        print_board()

if has_won(user_symbol):
    print("You WON :D !!!")
elif has_won(computer_symbol):
    print("You Lost, Better luck next time :)") 
else:
    print("It's a tie :|")


