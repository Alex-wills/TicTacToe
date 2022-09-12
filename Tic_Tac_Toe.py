from random import randrange


def create_board():
    # initialise board
    # board[row][column]
    '''
    [0][0]  [0][1]  [0][2]

    [1][0]  [1][1]  [1][2]

    [2][0]  [2][1]  [2][2]
    '''

    board = [['empty' for column in range(3)] for row in range(3)]

    spaces = make_list_of_free_fields(board)

    for key, value in spaces.items():
        board[value[0]][value[1]] = key

    board[1][1] = 'X'
    return board


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print(board)
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[0][0], '  |  ', board[0][1], '  |  ', board[0][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[1][0], '  |  ', board[1][1], '  |  ', board[1][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', board[2][0], '  |  ', board[2][1], '  |  ', board[2][2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    num_to_pos = make_list_of_free_fields(board)

    usr_inp = input('Enter your move: ').upper()
    move = num_to_pos[usr_inp]
    board[move[0]][move[1]] = '0'

    return board


def draw_move(board):
    # The function draws the computer's move and updates the board.
    cpu_inp = randrange(1, 10)

    num_to_pos = make_list_of_free_fields(board)

    while str(cpu_inp) not in num_to_pos:
        cpu_inp = randrange(1, 10)
    move = num_to_pos[str(cpu_inp)]
    board[move[0]][move[1]] = 'X'

    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []

    # scan
    for row in range(3):
        for column in range(3):
            if board[row][column] != 'X' and board[row][column] != '0':
                free_fields.append((row, column))
            else:
                free_fields.append('full')

    num_to_pos = {}

    for i in range(len(free_fields)):
        if free_fields[i] != 'full':
            num_to_pos[str(i + 1)] = free_fields[i]

    return num_to_pos


# horizontal check
def h_check(board, sign, row, column):
    if board[row][column + 1] == sign and board[row][column + 2] == sign:
        return True
    else:
        return False


# vertical check
def v_check(board, sign, row, column):
    if board[row + 1][column] == sign and board[row + 2][column] == sign:
        return True
    else:
        return False


# positive diagonal check
def pd_check(board, sign, row, column):
    if board[row - 1][column + 1] == sign and board[row - 2][column + 2] == sign:
        return True
    else:
        return False


# negative diagonal check
def nd_check(board, sign, row, column):
    if board[row + 1][column + 1] == sign and board[row + 2][column + 2] == sign:
        return True
    else:
        return False


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    win = False

    # negative diagonal checks for top left field
    if board[0][0] == sign:
        if nd_check(board, sign, 0, 0):
            return True

    # positive diagonal checks for bottom left field
    if board[2][0] == sign:
        if pd_check(board, sign, 2, 0):
            return True

    for row in range(3):
        for column in range(3):
            # skip the middle as there is no need to check from this
            if row == 1 and column == 1:
                continue

            # perform checks

            # vertical checks for top row only
            if row == 0 and board[row][column] == sign:
                if v_check(board, sign, 0, column):
                    return True
            # horizontal checks for left column only
            if column == 0 and board[row][column] == sign:
                if h_check(board, sign, row, 0):
                    return True
            else:
                continue


board = create_board()
num_of_moves = 1

#
while num_of_moves < 9:
    display_board(board)
    enter_move(board)
    display_board(board)
    if victory_for(board, '0'):
        print("Well done you win!!!!!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Unlucky Computer wins!!!!!")
        break

    num_of_moves += 2

print("*****************************")
print("*********GAME OVER***********")
print("*****************************")
quit()