import random

def play(x):
    for i in range(x):
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])
        r, p , s = 'r' , 'p', 's'   
        print('computer: ' +computer)
        if user == computer:
             print('It\`s a tie')
        
        if is_win(user, computer):
            print ('You won!')
        else:
            print ('You lost!')

def is_win(player, opponent):
    r, p , s = 'r' , 'p', 's' 
    if (player == r and opponent == s) or \
        (player == p and opponent == r) or (player == s and opponent == p):
        return True

x = int(input("please enter how many games you wanna play: "))
play(x)