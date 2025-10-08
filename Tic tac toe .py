board = [' ' for _ in range(9)]

def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)

def player_move(icon):
    if icon == 'X':
        player = 1
    else:
        player = 2

    print("Player {}'s turn".format(player))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == ' ':
        board[choice-1] = icon
    else:
        print("That space is already taken!")

def is_victory(icon):
    return ((board[0] == board[1] == board[2] == icon) or
            (board[3] == board[4] == board[5] == icon) or
            (board[6] == board[7] == board[8] == icon) or
            (board[0] == board[3] == board[6] == icon) or
            (board[1] == board[4] == board[7] == icon) or
            (board[2] == board[5] == board[8] == icon) or
            (board[0] == board[4] == board[8] == icon) or
            (board[2] == board[4] == board[6] == icon))

def is_draw():
    return ' ' not in board

while True:
    print_board()
    player_move('X')
    if is_victory('X'):
        print_board()
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break

    print_board()
    player_move('O')
    if is_victory('O'):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break
