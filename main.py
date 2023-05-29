print('----------------------')
print("Let's play Py-Pac-Poe!")
print('----------------------')

winner = False

winning_combos = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2'],
    ['a3', 'b3', 'c3'],
    ['a1', 'b2', 'c3'],
    ['a3', 'b2', 'c1']
]


def init_game():
    global board, turn
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None
    }
    turn = 'X'
    # init_game(print(board['a1'], '|', board['a2'], '|', board['a3']))
    # print('      A      B      C')
    # print('')
    # print('1)  ', board['a1'], '|', board['a2'], '|', board['a3'])
    # print('    -------------------')
    # print('2)  ', board['b1'], '|', board['b2'], '|', board['b3'])
    # print('    -------------------')
    # print('3)  ', board['c1'], '|', board['c2'], '|', board['c3'])
    # print('    -------------------')

init_game()

def print_board():
    print('      A      B      C')
    print('')
    print('1)  ', board['a1'], '|', board['b1'], '|', board['c1'])
    print('    -------------------')
    print('2)  ', board['a2'], '|', board['b2'], '|', board['c2'])
    print('    -------------------')
    print('3)  ', board['a3'], '|', board['b3'], '|', board['c3'])
    print('    -------------------')

print_board()

def get_winner():
    global winner
    if winner == True:
        init_game()
    if move_x_combos in winning_combos:
        winner = True
        print('Player X wins!')
    elif move_o_combos in winning_combos:
        winner = True
        print('Player O Wins!')

def get_move():
    global move_x, winner, move_x_combos, move_o_combos
    move_x_combos = []
    move_o_combos = []
    while winner == False:
        move_x = input("Player X's turn: ")
        if move_x in board:
            board[move_x] = 'X'
            print_board()
            turn = 'O'
            move_x_combos.append(move_x)
            print(move_x_combos)
            get_winner()
        move_o = input("Player O's turn: ")
        if move_o in board:
            board[move_o] = 'O'
            print_board()
            move_o_combos.append(move_o)
            turn = 'X'
            print(move_o_combos)
            get_winner()
        # get_move()
        print(move_x)
        print(move_o)

get_move()

# def get_winner():
#     if move_x_combos in winning_combos:
#         winner == True
#         print('Player X wins!')

# def get_winner():
#     if move_x_combos in winning_combos:
#         print('Player X wins!')

# get_winner()