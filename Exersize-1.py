import random 
from time import time
from colorama import Fore
from termcolor import colored

text=["X","O"]

def show_board():
    print()
    for row in range(3):
        for column in range(3):
            if board[row][column]=='X':
                print(Fore.RED + 'X', end=' ')
                print(Fore.WHITE, end='')
            elif board[row][column]=='O':
                print(Fore.CYAN + 'O', end=' ')
                print(Fore.WHITE, end='')
            else:
                print('-', end=' ')
        print()

def check_pos(x, y):
    if x <= 2 and y <= 2:
        return True
    else:
        return False

def is_empty(x, y):
    if board[x][y] == '-':
        return True
    else:
        return False

def gp(name, sign):
    while True:
        print("It\s turn of " , name ," : ")
        x = abs(int(input("Please enter the row of your choice (1 or 2 or 3) : ")))
        y = abs(int(input("Please enter the column of your choice (1 or 2 or 3) : ")))
        x -= 1
        y -= 1
        if check_pos(x, y):
            if is_empty(x, y):
                board[x][y] = sign
                return
            else:
                print('This position is already filled & you can\'t store here! Please try again.')
        else:
            print('This position is not true so you can\'t store here! Please try again.')

def win_match():
    for i in range(3):
        cnt_user1 = 0 
        cnt_user2 = 0
        for j in range(3):
            test = board[i][j]
            if test=='X':
               cnt_user2+=1
            elif test=='O':
                cnt_user1+=1
        if cnt_user2==3 or cnt_user1==3:
            return True


    for i in range(3):
        cnt_user1 = 0 
        cnt_user2 = 0
        for j in range(3):
            test = board[j][i]
            if test == 'X':
                cnt_user2 += 1
            elif test =='O':
                cnt_user1+=1
        if cnt_user2 == 3 or cnt_user1 == 3:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '-':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != '-':
        return True
    return False
    
def is_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':
                return False
    return True

def check():
    if win_match():
        return 'win'
    elif is_draw():
        return 'draw'
    else:
        return 'nothing'

def end_game(state, name):
    if state == 'win':
        print("The : ", name, " wins the game !")
    elif state == 'draw':
        print('Game had been draw.')

def start_game(a):
    sign1 = random.choice(text)
    player1 = input('player 1 name : ')
    if sign1 == 'O' :
        sign2 = 'X' 
    else :
        sign2 = 'O'
    if a =='2' :
         player2 = input('player2 name : ')
    else : 
        player2 = 'computer'
    turn = random.choice(text)
    while True:
        turn = sign1
        show_board()
        gp(player1, turn)
        test = check()
        if test == 'win' or test == 'draw':
            show_board()
            end_game(test, player1)
            break
        show_board()
        turn = sign2
        if a == '2':
            gp(player2, turn)
        else:
            while True:
                randomrow = random.randint(0, 2)
                randomcolumn = random.randint(0, 2)
                if is_empty(randomrow, randomcolumn):
                    board[randomrow][randomcolumn] = turn
                    break

        test = check()
        if test == 'win' or test == 'draw':
            end_game(test, player2)
            break
while True:
    board = [['-']*3, ['-']*3, ['-']*3]
    choice_menu = input('Please choose one of iteams \n 1.play with computer\n 2.Play with 2 players\n3.exit\n')

    if choice_menu=='1' :
        t1 = time()
        start_game('1')
        print(" time is : " ,round(time() - t1, 2) , "sec")
        
    elif choice_menu=='2':
        t1 = time()
        start_game('2')
        print(" time :" ,round(time() - t1, 2) , "sec")
        
    elif choice_menu=='3':
        exit()