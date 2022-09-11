import unittest

# would usually be a class so fewer references
from Tic_Tac_Toe import victory_for, create_board

class TestTicTacToe(unittest.TestCase):

    def test_left_vert_win(self):
        board = create_board()

        board[0][0] = '0'
        board[1][0] = '0'
        board[2][0] = '0'

        victory_for(board, '0')

        self.assertEqual(victory_for(board, '0'), True)

    def test_right_vert_win(self):
        board = create_board()

        board[0][2] = '0'
        board[1][2] = '0'
        board[2][2] = '0'

        victory_for(board, '0')

        self.assertEqual(victory_for(board, '0'), True)

    def test_top_hori_win(self):
        board = create_board()

        board[0][0] = '0'
        board[0][1] = '0'
        board[0][2] = '0'

        victory_for(board, '0')

        self.assertEqual(victory_for(board, '0'), True)

    def test_bottom_hori_win(self):
        board = create_board()

        board[2][0] = '0'
        board[2][1] = '0'
        board[2][2] = '0'

        victory_for(board, '0')

        self.assertEqual(victory_for(board, '0'), True)

    def test_nd_win(self):
        board = create_board()

        board[0][0] = 'X'
        board[1][1] = 'X'
        board[2][2] = 'X'

        victory_for(board, 'X')

        self.assertEqual(victory_for(board, 'X'), True)

    def test_pd_win(self):
        board = create_board()

        board[2][0] = 'X'
        board[1][1] = 'X'
        board[0][2] = 'X'

        victory_for(board, 'X')

        self.assertEqual(victory_for(board, 'X'), True)


if __name__ == '__main__':
    unittest.main()
