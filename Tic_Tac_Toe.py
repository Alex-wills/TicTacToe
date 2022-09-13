from random import randrange

# players class
'''whenever you need to interact with board you must step into Board b with b.board'''

''' player methods could be static right now, need to make it so they either are static or use objects sign'''


# board class

class Board:
    def __init__(self):
        self.board = [['empty' for column in range(3)] for row in range(3)]

    def display_board(self):
        # The function accepts one parameter containing the board's current status
        # and prints it out to the console.

        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|  ', self.board[0][0], '  |  ', self.board[0][1], '  |  ', self.board[0][2], '  |')
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|  ', self.board[1][0], '  |  ', self.board[1][1], '  |  ', self.board[1][2], '  |')
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|  ', self.board[2][0], '  |  ', self.board[2][1], '  |  ', self.board[2][2], '  |')
        print('|       |       |       |')
        print('+-------+-------+-------+')

    def make_list_of_free_fields(self):
        # The function browses the board and builds a list of all the free squares;
        # the list consists of tuples, while each tuple is a pair of row and column numbers.
        free_fields = []

        # scan
        for row in range(3):
            for column in range(3):
                if self.board[row][column] != 'X' and self.board[row][column] != '0':
                    free_fields.append((row, column))
                else:
                    free_fields.append('full')

        num_to_pos = {}

        for i in range(len(free_fields)):
            if free_fields[i] != 'full':
                num_to_pos[str(i + 1)] = free_fields[i]

        return num_to_pos

    def fill_board(self):
        # initialise board
        # board[row][column]
        '''
        [0][0]  [0][1]  [0][2]

        [1][0]  [1][1]  [1][2]

        [2][0]  [2][1]  [2][2]
        '''

        dic = self.make_list_of_free_fields()

        for key, value in dic.items():
            self.board[value[0]][value[1]] = key

        self.board[1][1] = 'X'


class Player:

    def __init__(self, sign):
        self.sign = sign

    def enter_move(self, b, sign):
        # The function accepts the board's current status, asks the user about their move,
        # checks the input, and updates the board according to the user's decision.

        num_to_pos = b.make_list_of_free_fields()

        usr_inp = input('Enter your move: ').upper()
        move = num_to_pos[usr_inp]
        b.board[move[0]][move[1]] = sign

        return b

    def draw_move(self, b, sign):
        # The function draws the computer's move and updates the board.
        cpu_inp = randrange(1, 10)

        num_to_pos = b.make_list_of_free_fields()

        while str(cpu_inp) not in num_to_pos:
            cpu_inp = randrange(1, 10)
        move = num_to_pos[str(cpu_inp)]
        b.board[move[0]][move[1]] = sign

        return b

    def victory_for(self, b, sign):
        # The function analyzes the board's status in order to check if
        # the player using 'O's or 'X's has won the game

        # checks####################################################################################
        # horizontal check
        def h_check(b, sign, row, column):
            if b.board[row][column + 1] == sign and b.board[row][column + 2] == sign:
                return True
            else:
                return False

        # vertical check
        def v_check(b, sign, row, column):
            if b.board[row + 1][column] == sign and b.board[row + 2][column] == sign:
                return True
            else:
                return False

        # positive diagonal check
        def pd_check(b, sign, row, column):
            if b.board[row - 1][column + 1] == sign and b.board[row - 2][column + 2] == sign:
                return True
            else:
                return False

        # negative diagonal check
        def nd_check(b, sign, row, column):
            if b.board[row + 1][column + 1] == sign and b.board[row + 2][column + 2] == sign:
                return True
            else:
                return False

        ##########################################################################################

        # negative diagonal checks for top left field
        if b.board[0][0] == sign:
            if nd_check(b, sign, 0, 0):
                return True

        # positive diagonal checks for bottom left field
        if b.board[2][0] == sign:
            if pd_check(b, sign, 2, 0):
                return True

        for row in range(3):
            for column in range(3):
                # skip the middle as there is no need to check from this
                if row == 1 and column == 1:
                    continue

                # perform checks

                # vertical checks for top row only
                if row == 0 and b.board[row][column] == sign:
                    if v_check(b, sign, 0, column):
                        return True
                # horizontal checks for left column only
                if column == 0 and b.board[row][column] == sign:
                    if h_check(b, sign, row, 0):
                        return True
                else:
                    continue


if __name__ == '__main__':
    user = Player('0')
    cpu = Player('X')
    b = Board()
    b.fill_board()
    num_of_moves = 1

    #
    while num_of_moves < 9:
        b.display_board()
        user.enter_move(b, user.sign)
        b.display_board()
        if user.victory_for(b, user.sign):
            print("Well done you win!!!!!")
            break
        cpu.draw_move(b, cpu.sign)
        b.display_board()
        if cpu.victory_for(b, cpu.sign):
            print("Unlucky Computer wins!!!!!")
            break

        num_of_moves += 2

    print("*****************************")
    print("*********GAME OVER***********")
    print("*****************************")
    quit()
