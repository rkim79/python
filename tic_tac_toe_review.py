from random import randint

# display game board
def display_board(board):
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')
    print('------------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('------------')
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')

# select marker for each player
def marker_choice():
    while True:
        p1_mark = input('Choose your marker, O or X: ').lower()
        if p1_mark != 'o' and p1_mark != 'x':
            print('Wrong input, choose either O or X...')
            continue
        else:
            if p1_mark == 'o':
                return ('O', 'X') # this will exit the func, so no break will be needed
            else:
                return ('X', 'O')

# show each player's marker
def confirm_marker(player1, player2):
    print(f'Player 1\'s marker: {player1}\nPlayer 2\'s marker: {player2}')

# randomize the first player
def random_first():
    first_player = randint(1, 2)
    if first_player == 1:
        return 'player1'
    else:
        return 'player2'

# check if the place is empty
def vacant_check(board, position):
    return board[position].isdigit()

# place marker on the board
def make_move(board, player_marker, turn):
    while True:
        user_input = input(f'{turn}({player_marker}), Choose your position : ')
        if user_input.isalpha():
            print('Please provide a number from 1 to 9...')
            continue
        else:
            position = int(user_input)
            if position < 0 or position > 9:
                print('Out of range, try again...')
                continue
            else:
                if vacant_check(board, position):
                    board[position] = player_marker
                    break
                else:
                    print(f'{position} is already occupied, try again...')
                    continue

# check if the board is full which means the game is a draw
def full_board_check(board):
    for i in range(1, 10):
        if vacant_check(board, i):
            return False
    return True

# check if someone wins the game
def win_check(b, marker):
    if ((b[1] == b[2] == b[3] == marker) or (b[4] == b[5] == b[6] == marker) or
        (b[7] == b[8] == b[9] == marker) or (b[1] == b[4] == b[7] == marker) or
        (b[2] == b[5] == b[8] == marker) or (b[3] == b[6] == b[9] == marker) or
        (b[1] == b[5] == b[9] == marker) or (b[3] == b[5] == b[7] == marker)):
        return marker
        # multiple line statement can be written with parentheses
        # example a = (b
        #               + c)

# game function
def game(board, player, turn):
    make_move(board, player, turn)

    display_board(board)

    if win_check(board, player) == player:
        print(f'{turn} has won the game!')
        return (False, turn)
    elif full_board_check(board):
        print('No more space, Draw!')
        return (False, turn)
    else:
        if turn == 'player1':
            return(True, 'player2')
        else:
            return(True, 'player1')

# replay
def wanna_replay():
    while True:
        answer = input('Play Again?[yes/no] ').lower()
        if answer[0] != 'y' and answer[0] != 'n':
            print('Answer again, Yes or No?')
            continue
        elif answer[0] == 'y':
            return True
        else:
            return False

# game itself
while True:
    print('Welcome to tic-tac-toe game!\n')

    board = [str(cell) for cell in range(10)]
    game_on = True

    display_board(board)

    player1, player2 = marker_choice()

    confirm_marker(player1, player2)

    turn = random_first()

    while game_on:
        if turn == 'player1':
            game_on, turn = game(board, player1, turn)
        elif turn == 'player2':
            game_on, turn = game(board, player2, turn)

    # replay
    if wanna_replay():
        continue
    else:
        break