import unittest
from unittest.mock import patch

from tictactoe import BOARD, draw_current_board, get_all_moves, is_valid_move, select_move, \
    check_for_winner


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        # for testing drawing the game board with variety of player's moves
        self.players_moves_and_game_boards = [
            ({'x': [], 'o': []},
             '   |   |   \n ---------- \n   |   |   \n ---------- \n   |   |  '),
            ({'x': [5], 'o': []},
             '   |   |   \n ---------- \n   | x |   \n ---------- \n   |   |  '),
            ({'x': [5, 3, 9], 'o': [1, 7]},
             ' o |   | x \n ---------- \n   | x |   \n ---------- \n o |   | x'),
            ({'x': [5, 3, 9, 4], 'o': [1, 7, 6, 2]},
             ' o | o | x \n ---------- \n x | x | o \n ---------- \n o |   | x')
        ]
        # for testing the sequence of moves in a single game
        self.moves_in_game = [
            (("x", [], {'x': [], 'o': []}),  {'x': [5], 'o': []}),
            (("o", [], {'x': [5], 'o': []}), {'x': [5], 'o': [1]}),
            (("x", [5], {'x': [5], 'o': [1]}), {'x': [5, 6], 'o': [1]}),
            (("o", [1], {'x': [5, 6], 'o': [1]}), {'x': [5, 6], 'o': [1, 4]}),
            (("x", [5, 6], {'x': [5, 6], 'o': [1, 4]}), {'x': [5, 6, 7], 'o': [1, 4]}),
            (("o", [1, 4], {'x': [5, 6, 7], 'o': [1, 4]}), {'x': [5, 6, 7], 'o': [1, 4, 2]}),
            (("x", [5, 6, 7], {'x': [5, 6, 7], 'o': [1, 4, 2]}), {'x': [5, 6, 7, 3], 'o': [1, 4, 2]}),
        ]
        # for testing varying game results
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
            {'x': [4, 5, 3, 8, 6], 'o': [1, 2, 7, 9]},
        ]

    def test_draw_current_board(self):
        for players_moves, game_board in self.players_moves_and_game_boards:
            expected_board = game_board
            actual_board = draw_current_board(BOARD, players_moves)
            self.assertEqual(expected_board, actual_board)

    def test_get_all_moves(self):
        expected_moves = [4, 5, 3, 8, 6, 1, 2, 7, 9]
        actual_moves = get_all_moves(self.x_wins[3])
        self.assertEqual(expected_moves, actual_moves)

    def test_is_valid_move_space_taken(self):
        players_moves = {'x': [5], 'o': []}
        select_space_that_is_already_taken = is_valid_move(5, players_moves)
        self.assertFalse(select_space_that_is_already_taken)

    def test_is_valid_move_bad_input(self):
        players_moves = {'x': [], 'o': []}
        select_space_that_is_not_on_board = is_valid_move(0, players_moves)
        self.assertFalse(select_space_that_is_not_on_board)
        select_space_that_is_not_on_board = is_valid_move(10, players_moves)
        self.assertFalse(select_space_that_is_not_on_board)

    @patch('builtins.input', side_effect=['5', '1', '6', '4', '7', '2', '3'])
    def test_select_move(self, mock_input):
        for move, next_move in self.moves_in_game:
            expected_next_move = next_move
            actual_next_move = select_move(*move)
            self.assertEqual(expected_next_move, actual_next_move)

    def check_for_game_result(self, expected_game_result, result_type):
        for game in result_type:
            game_result = check_for_winner(game)
            self.assertEqual(expected_game_result, game_result)

    def test_tie_games(self):
        self.check_for_game_result("It's a tie!", self.tie_games)

    def test_o_wins(self):
        self.check_for_game_result("o wins!", self.o_wins)

    def test_x_wins(self):
        self.check_for_game_result("x wins!", self.x_wins)


if __name__ == '__main__':
    unittest.main()
