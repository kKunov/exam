import unittest
import TicTacToe


class TestTicTac(unittest.TestCase):
    def setUp(self):
        self.table = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def test_is_good_input(self):

        self.assertFalse(TicTacToe.is_good_input(0, 2, self.table))
        self.assertFalse(TicTacToe.is_good_input(1, 4, self.table))

        self.table[0][1] = 'x'

        self.assertFalse(TicTacToe.is_good_input(0, 1, self.table))
        self.assertTrue(TicTacToe.is_good_input(1, 1, self.table))

    def test_count_free(self):
        self.assertEqual(TicTacToe.count_free(self.table), 9)
        self.table[1][1] = 'x'
        self.assertEqual(TicTacToe.count_free(self.table), 8)
        self.table[1][2] = 'x'
        self.assertEqual(TicTacToe.count_free(self.table), 7)

    def test_free_pos_8(self):
        self.table[1][1] = 'x'
        returns = []

        for index in range(100):
            returns.append(TicTacToe.free_pos_8(self.table, 8))

        self.assertTrue([0, 2] in returns)
        self.assertTrue([2, 0] in returns)
        self.assertTrue([2, 2] in returns)
        self.assertTrue([0, 0] in returns)

        self.table[1][1] = ' '
        self.table[0][2] = 'x'

        self.assertEqual(TicTacToe.free_pos_8(self.table, 8), [1, 1])

        self.assertFalse(TicTacToe.free_pos_8(self.table, 4))

    def test_check_rows(self):
        self.table[1][1] = 'x'
        self.table[0][0] = 'x'
        self.table[2][0] = 'o'

        self.assertEqual(TicTacToe.check_rows(self.table, [], 'x'), [])

        self.table[0][0] = ' '
        self.table[1][0] = 'x'

        self.assertEqual(TicTacToe.check_rows(self.table, [], 'x'), [[1, 2]])

        self.table[1][0] = ' '
        self.table[1][2] = 'x'

        self.assertEqual(TicTacToe.check_rows(self.table, [], 'x'), [[1, 0]])

        self.table[1][1] = ' '
        self.table[1][0] = 'x'

        self.assertEqual(TicTacToe.check_rows(self.table, [], 'x'), [[1, 1]])

    def test_check_col(self):
        self.table[1][1] = 'x'
        self.table[0][0] = 'x'
        self.table[2][0] = 'o'

        self.assertEqual(TicTacToe.check_col(self.table, [], 'x'), [])

        self.table[0][0] = ' '
        self.table[2][1] = 'x'

        self.assertEqual(TicTacToe.check_col(self.table, [], 'x'), [[0, 1]])

        self.table[2][1] = ' '
        self.table[0][1] = 'x'

        self.assertEqual(TicTacToe.check_col(self.table, [], 'x'), [[2, 1]])

        self.table[1][1] = ' '
        self.table[2][1] = 'x'

        self.assertEqual(TicTacToe.check_col(self.table, [], 'x'), [[1, 1]])

    def test_check_diagonals(self):
        self.table[1][1] = 'x'
        self.table[0][0] = 'x'
        self.table[2][0] = 'o'

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[2, 2]])

        self.table[1][1] = ' '
        self.table[2][2] = 'x'

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[1, 1]])

        self.table[0][0] = ' '
        self.table[1][1] = 'x'

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[0, 0]])

        self.table[2][0] = 'x'
        self.table[2][2] = 'o'

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[0, 2]])

        self.table[0][2] = 'x'
        self.table[2][0] = ' '

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[2, 0]])

        self.table[2][0] = 'x'
        self.table[1][1] = ' '

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [[1, 1]])

        self.table[2][0] = ' '

        self.assertEqual(TicTacToe.check_diagonals(self.table, [], 'x'),
                         [])

    def test_pcs_if_pc_can_win(self):
        self.table[0][0] = 'o'
        self.table[0][1] = 'o'

        self.assertEqual(TicTacToe.pc(self.table), [0, 2])

if __name__ == '__main__':
    unittest.main()
