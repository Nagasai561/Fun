import random
import time

#Our initial configuration of board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]



#All positions refer to a cell in the board according to the direction they define (NW means North-West)
position = {
    "N": (0,1),
    "S": (2,1),
    "E": (1,2),
    "W": (1,0),
    "C": (1,1),
    "NW": (0, 0),
    "NE": (0,2),
    "SW": (2,0),
    "SE": (2,2)
}

symbol_list = ['X', 'O']
turn = 2

#prints the board in a nice format
def print_board():
    print("")
    for i in range(3):
        for j in range(3):
            print(" ", board[i][j], " ", end="")
            if(j != 2):
                print("|", end="")
        print("")
        if(i != 2):
            for k in range(17):
                print("-", end="")
            print("")
    print("")        
    
#This function gives a random valid move
def computer_move_random():
    available = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                available.append((i, j))
    choice = random.choice(available)
    return choice

#This function returns the optimal move
def computer_move_engine(symb_ind):
    return computer_move_bruteforce(symb_ind)[:-1]

#helper function for the above function which goes through all the possibilites
#to find the optimal move
#it returns [i, j, k] where i and j are indices of optimal position on board
#k defines what type of move it is
#k = 1, means upon making that move, we are guaranteed to win
#k = 0, guaranteed to draw
#k = -1, guaranteed to lose
def computer_move_bruteforce(symb_ind):
    draw = [None, None, 0]
    lose = [None, None, -1]
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '): #checking if the spot is available to make the move
                board[i][j] = symbol_list[symb_ind]
                if(matched_symbol() == symbol_list[symb_ind]):  #if it matched then return i, j
                    board[i][j] = ' '
                    return (i, j, 1)
                opp = computer_move_bruteforce(1-symb_ind) #now it's opponent turn
                board[i][j] = ' '
                match opp[2]:
                    case 1:     #opponent wins 
                        lose = [i, j, -1]
                    case -1:    #opponent loses
                        return [i, j, 1]
                    case 0:     #game is draw
                        draw = [i, j, 0]
    if((draw[0] == None) and (lose[0] == None)):
        return [1,1,0]
    elif(draw[0] != None):
        return draw
    else:
        return lose

                


#This checks if any symbol has matched. If some symbol is matching then it returns that symbol
def matched_symbol():
    for i in range(3):  #checking for matching along rows
        for j in range(3):
            if(board[i][0] != board[i][j]):
                break
            if(j == 2):
                return board[i][0]
    for j in range(3):  #checking for matching along colums
        for i in range(3):
            if(board[i][j] != board[0][j]):
                break
            if(i == 2):
                return board[0][j]
    if((board[1][1] == board[0][0]) and (board[1][1] == board[2][2])):  #checking for \ diagonal
        return board[1][1]
    if((board[1][1] == board[0][2]) and (board[1][1] == board[2][0])):  #checking for / diagonal
        return board[1][1]
    return ' '


#Taking input from user
def user_move():
    while ((move:=input("Your move: ").upper()) not in position) or board[position[move][0]][position[move][1]] != ' ':
        print("Please enter a valid position to play")
        print("Valid moves are N, W, S, E, C, NW, NE, SW, SE! Each representing the direction of box!")
    return position[move]
        



if __name__ == "__main__":

    print_board()
    #Asking the user to select the symbol 
    while ((user_symbol := input("Which symbol you want to play? Enter 'X' or 'O': ").upper()) != 'X') and (user_symbol != 'O'):
        print("Please select a valid symbol to play ('X' or 'O')!")
        print("")

    turn = 0
    user_turn = True if(user_symbol == 'X') else False
    computer_symbol = 'X' if(user_symbol == 'O') else 'O'

    while turn < 9:
        if(user_turn):
            curr_move = user_move()
            board[curr_move[0]][curr_move[1]] = user_symbol
            time.sleep(1)
        else:
            curr_move = computer_move_engine(0 if computer_symbol == 'X' else 1)

            # curr_move = computer_move_random() #Uncomment this and comment above line to make computer choose the choice randomly
            board[curr_move[0]][curr_move[1]] = computer_symbol
            print("Computer's move: ")
            print("Computer is thinking........")
            time.sleep(1)

        print_board()
        user_turn = not user_turn
        turn += 1
        win = matched_symbol()
        if(win != ' '):
            if(win == user_symbol):
                print("Hooray! You have won!!!!!")
            else:
                print("Awww!! You have lost! Better luck next time!!")
            break
        if(turn == 9):
            print("It's a Draw!!!")

