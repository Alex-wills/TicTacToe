import unittest
from unittest.mock import patch


from Tic_Tac_Toe import Board, Player


class TestTicTacToe(unittest.TestCase):

    def test_left_vert_win(self):
        b = Board(3, 3)
        user = Player('0')

        b.board[0][0] = '0'
        b.board[1][0] = '0'
        b.board[2][0] = '0'

        self.assertEqual(user.victory_for(b), True)

    def test_right_vert_win(self):
        b = Board(3, 3)
        user = Player('0')

        b.board[0][2] = '0'
        b.board[1][2] = '0'
        b.board[2][2] = '0'

        self.assertEqual(user.victory_for(b), True)

    def test_top_hori_win(self):
        b = Board(3, 3)
        user = Player('0')

        b.board[0][0] = '0'
        b.board[0][1] = '0'
        b.board[0][2] = '0'

        self.assertEqual(user.victory_for(b), True)

    def test_bottom_hori_win(self):
        b = Board(3, 3)
        user = Player('0')

        b.board[2][0] = '0'
        b.board[2][1] = '0'
        b.board[2][2] = '0'

        self.assertEqual(user.victory_for(b), True)

    def test_nd_win(self):
        b = Board(3, 3)
        cpu = Player('X')

        b.board[0][0] = 'X'
        b.board[1][1] = 'X'
        b.board[2][2] = 'X'

        self.assertEqual(cpu.victory_for(b), True)

    def test_pd_win(self):
        b = Board(3, 3)
        cpu = Player('X')

        b.board[2][0] = 'X'
        b.board[1][1] = 'X'
        b.board[0][2] = 'X'

        self.assertEqual(cpu.victory_for(b), True)


# Test broken as it gets stuck in infinite loop of '5 is already taken, pick again'

# @patch('builtins.input', lambda *args: '5')
# def test_pick_chosen_block(self):
#     b = Board(3, 3)
#     user = Player('0')
#     b.board[1][1] = 'X'  # Equivalent to choosing position 5
#
#     user.enter_move(b)  # @patch enters 5


if __name__ == '__main__':
    unittest.main()
