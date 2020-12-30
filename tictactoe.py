import random;

board = ["1","2","3","4","5","6","7","8","9"]

user_symbol="x"
computer_symbol="o"
winner_symbol=""

def print_board():
    for i in range(0, len(board), 3):
        print('  '.join(map(str, board[i:i+3])))

def validate_input():
    while True:
        user=input("Enter your move (position 1-9) : ")
        try:
            if int(user)-1>=0 and int(user)-1<=8:
                break
        except ValueError:
            print("Invalid Input")
            pass
    return int(user)

def user_input():
    user_move=validate_input()
    while board[user_move-1]==user_symbol or board[user_move-1]==computer_symbol:
        print("Enter a valid input")
        user_move=validate_input()
    board[user_move-1]=user_symbol
           

def computer_input():
    x=random.randint(0,8)
    while board[x]==user_symbol or board[x]==computer_symbol:
        x=random.randint(0,8)  
    board[x]=computer_symbol

def is_tie():
    for item in board:
        if item == user_symbol or item ==computer_symbol:
            tie = True
        else:
            tie = False
            return tie
    return tie

def has_won(player_symbol):
    if board[0]==board[1]==board[2]==player_symbol :
        return True
    elif board[3]==board[4]==board[5]==player_symbol :
        return True
    elif board[6]==board[7]==board[8]==player_symbol :
        return True
    elif board[0]==board[3]==board[6]==player_symbol :
        return True
    elif board[1]==board[4]==board[7]==player_symbol :
        return True
    elif board[2]==board[5]==board[8]==player_symbol :
        return True
    elif board[0]==board[4]==board[8]==player_symbol :
        return True
    elif board[2]==board[4]==board[6]==player_symbol :
        return True
    else:
        return False

user_symbol=input("Choose symbol X or O: ")
while user_symbol!="X" and user_symbol!="O":
    print("Please enter a valid input")
    user_symbol=input("Choose symbol X or O only: ")
if user_symbol=="X":
    computer_symbol="O"
else:
    computer_symbol="X"

print_board()

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