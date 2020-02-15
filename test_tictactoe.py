import unittest

from tictactoe import check_for_winner


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tie_games = [
            {'x': [5, 7, 2, 4, 9], 'o': [1, 3, 8, 6]},
            {'x': [5, 3, 9, 2, 4], 'o': [1, 7, 6, 8]},
            {'x': [5, 1, 6, 2, 7], 'o': [3, 9, 4, 8]},
        ]
        self.o_wins = [
            {'x': [1, 3, 8, 9], 'o': [5, 2, 4, 6]},
            {'x': [4, 3, 7, 2], 'o': [9, 8, 1, 5]},
            {'x': [1, 2, 6, 4], 'o': [5, 9, 8, 7]}
        ]
        self.x_wins = [
            {'x': [5, 1, 2, 8], 'o': [9, 4, 3]},
            {'x': [1, 5, 3, 2], 'o': [9, 6, 7]},
            {'x': [1, 3, 2], 'o': [9, 5]},
        ]

    def check_for_game_result(self, expected_game_result, result_type):
        for game in result_type:
            game_result = check_for_winner(game)
            self.assertEqual(expected_game_result, game_result)

    def test_tie_games(self):
        self.check_for_game_result("It's a tie!", self.tie_games)  # should strs be constants?

    def test_o_wins(self):
        self.check_for_game_result("o wins!", self.o_wins)

    def test_x_wins(self):
        self.check_for_game_result("x wins!", self.x_wins)


if __name__ == '__main__':
    unittest.main()
