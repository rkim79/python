from random import randint

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(10)] # not sure about self.board

    def display_board(self):
        print('   |   |')
        print(f' {self.board[7]} | {self.board[8]} | {self.board[9]}')
        print('   |   |')
        print('------------')
        print('   |   |')
        print(f' {self.board[4]} | {self.board[5]} | {self.board[6]}')
        print('   |   |')
        print('------------')
        print('   |   |')
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]}')
        print('   |   |')

    def mark(self, position, marker):
        if self.board[position].isdigit():
            self.board[position] = marker
            return True
        else:
            return False

    def win_check(self, marker):
        if ((self.board[1] == self.board[2] == self.board[3] == marker) or
            (self.board[4] == self.board[5] == self.board[6] == marker) or
            (self.board[7] == self.board[8] == self.board[9] == marker) or
            (self.board[1] == self.board[4] == self.board[7] == marker) or
            (self.board[2] == self.board[5] == self.board[8] == marker) or
            (self.board[3] == self.board[6] == self.board[9] == marker) or
            (self.board[1] == self.board[5] == self.board[9] == marker) or
            (self.board[3] == self.board[5] == self.board[7] == marker)):
            return marker 

    def full_board_check(self):
        for cell in self.board[1:]:
            if cell.isdigit():
                return False
        return True

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
                if board.mark(position, player_marker):
                    break
                else:
                    print(f'{position} is already occupied, try again...')
                    continue

# game function
def game(board, player, turn):
    make_move(board, player, turn)

    board.display_board()
    print(board.full_board_check())

    if board.win_check(player) == player:
        print(f'{turn} has won the game!')
        return (False, turn)
    elif board.full_board_check():
        print('No more space! Draw!')
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

    new_board = Board()
    game_on = True

    new_board.display_board()

    player1, player2 = marker_choice()

    confirm_marker(player1, player2)

    turn = random_first()

    while game_on:
        if turn == 'player1':
            game_on, turn = game(new_board, player1, turn)
        elif turn == 'player2':
            game_on, turn = game(new_board, player2, turn)

    # replay
    if wanna_replay():
        continue
    else:
        break