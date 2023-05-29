print('----------------------')
print("Let's play Py-Pac-Poe!")
print('----------------------')

winner = False
tie = False

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


init_game()

def print_board():
    print('     A     B     C')
    print('')
    print('1)  ', board['a1'] or ' ', ' | ', board['b1'] or ' ', ' | ', board['c1'] or ' ')
    print('    ---------------')
    print('2)  ', board['a2'] or ' ', ' | ', board['b2'] or ' ', ' | ', board['c2'] or ' ')
    print('    ---------------')
    print('3)  ', board['a3'] or ' ', ' | ', board['b3'] or ' ', ' | ', board['c3'] or ' ')
    print('    ---------------')

print_board()


def get_winner():
    global winner
    for combo in winning_combos:
        if set(combo).issubset(set(move_x_combos)):
            winner = True
            print('Player X wins!')
            init_game()
            return
        elif set(combo).issubset(set(move_o_combos)):
            winner = True
            print('Player O wins!')
            init_game()
            return
    if len(move_x_combos) + len(move_o_combos) == 9:
        winner = True
        print("Another tie!")
        init_game()

    if winner == True:
        init_game()



def get_move():
    global move_x, move_o, winner, move_x_combos, move_o_combos
    move_x_combos = []
    move_o_combos = []
    turn = 'X'

    while winner == False:
        while turn == 'X':
            move_x = input("Player X's move (example B2): ").lower()

            if move_x in board and board[move_x] == None:
                board[move_x] = 'X'
                print_board()
                move_x_combos.append(move_x)
                # print(move_x_combos)

                get_winner()

                if winner == True:
                    break
                turn = 'O'
            else:
                print('Bogus move! Try again...')
                continue

        while turn == 'O':
            move_o = input("Player O's turn (example B2): ").lower()

            if move_o in board and board[move_o] == None:
                board[move_o] = 'O'
                print_board()
                move_o_combos.append(move_o)
                # print(move_o_combos)

                get_winner()

                turn = 'X'
            else:
                print('Bogus move! Try again...')
                continue

        # print(move_x)
        # print(move_o)

get_move()