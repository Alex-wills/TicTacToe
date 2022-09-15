from random import randrange

# board class
'''
This class initialises an NxN board and places an appropriate number in any free spaces within the board.

(Board class generalised apart from display_board() would need a different display format)
'''


class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [['empty' for column in range(col)] for row in range(row)]
        self.fieldNum = [str(num) for num in range(1, (self.row * self.col) + 1)]


    '''
    This method fills the NxN board with a corresponding number to each
    empty space after the board has been initialised - board[row][column]
    
        [0][0]  [0][1]  [0][2]

        [1][0]  [1][1]  [1][2]   ...

        [2][0]  [2][1]  [2][2]
                   .
                   .
                   .
    
    '''
    def fill_board(self):


        ctr = 0
        for row in range(self.row):
            for column in range(self.col):
                self.board[row][column] = str(self.fieldNum[ctr])
                ctr += 1


    '''
    This method browses the board and builds a list of all the free squares, 
    then creates a dictionary for each square's corresponding number to its position.
    '''
    def make_list_of_free_fields(self):
        # The function browses the board and builds a list of all the free squares;
        # the list consists of tuples, while each tuple is a pair of row and column numbers.
        free_fields = []
        num_to_pos = {}

        # scan
        for row in range(self.row):
            for column in range(self.col):
                if self.board[row][column] in self.fieldNum:
                    free_fields.append((row, column))
                else:
                    free_fields.append('full')

        for i in range(len(free_fields)):
            if free_fields[i] != 'full':
                num_to_pos[str(i + 1)] = free_fields[i]

        return num_to_pos

    '''
    This method prints the Board instance to the terminal in the format of 3x3 tic-tac-toe.
     This will have to be overridden if another game board is required to be displayed
    '''
    def display_board(self):

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


# players class


'''
Player class initiates a player with their chosen a single sign to play with. A Player instance can 
enter a specific move on the Board through enter_move or enter a random move through draw_move.
 
(victory conditions specific to 3x3 tic tac toe) 
'''


class Player:

    def __init__(self, sign):
        self.sign = sign

    '''
    This method accepts the board's current status, asks the user about their move,
    checks the input, and updates the board according to the user's decision.
    '''

    def enter_move(self, b):

        num_to_pos = b.make_list_of_free_fields()
        valid = False
        move = (0,0)

        while not valid:
            try:
                usr_inp = input('Enter your move: ')
                move = num_to_pos[usr_inp]
            except KeyError as e:
                print(e.args[0], " is already taken, pick again")
                continue
            else:
                valid = True

        b.board[move[0]][move[1]] = self.sign

    '''
    This method accepts the board's current status, computes a possible move, and 
    updates the board according to the random empty position chosen.
    '''

    def draw_move(self, b):
        cpu_inp = randrange(1, 10)

        num_to_pos = b.make_list_of_free_fields()

        while str(cpu_inp) not in num_to_pos:
            cpu_inp = randrange(1, 10)
        move = num_to_pos[str(cpu_inp)]
        b.board[move[0]][move[1]] = self.sign

    '''
    This method checks the possible winning positions of that player's sign on the given Board, 
    returning a True if the player has won, and a False if the game has yet to be won by the player.
    
    (The victory conditions are specific to a 3x3 tic-tac-toe game, for another game this method 
    will have to be overridden).
    '''

    def victory_for(self, b):
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
        if b.board[0][0] == self.sign:
            if nd_check(b, self.sign, 0, 0):
                return True

        # positive diagonal checks for bottom left field
        if b.board[2][0] == self.sign:
            if pd_check(b, self.sign, 2, 0):
                return True

        for row in range(3):
            for column in range(3):
                # skip the middle as there is no need to check from this
                if row == 1 and column == 1:
                    continue

                # perform checks

                # vertical checks for top row only
                if row == 0 and b.board[row][column] == self.sign:
                    if v_check(b, self.sign, 0, column):
                        return True
                # horizontal checks for left column only
                if column == 0 and b.board[row][column] == self.sign:
                    if h_check(b, self.sign, row, 0):
                        return True


if __name__ == '__main__':
    user = Player('0')
    cpu = Player('X')
    b = Board(3, 3)
    b.fill_board()
    num_of_moves = 0

    #
    while num_of_moves < 9:
        b.display_board()
        user.enter_move(b)
        b.display_board()
        if user.victory_for(b):
            print("Well done you win!!!!!")
            break
        cpu.draw_move(b)
        b.display_board()
        if cpu.victory_for(b):
            print("Unlucky Computer wins!!!!!")
            break

        num_of_moves += 2

    print("*****************************")
    print("*********GAME OVER***********")
    print("*****************************")
    quit()
