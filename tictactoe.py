from itertools import chain

SPACES_ON_BOARD = range(1, 10)

WINNING_COMBOS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
)

BOARD = " 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9"

VALIDATION_ERROR_MESSAGE = "Not a valid move. Please select a space between 1 and 9 that is available on the board."

game_instructions = """Welcome to Command Line Tic Tac Toe!

Enter a number from 1-9 to place your move on the board in the corresponding space:

{}
""".format(BOARD)


def draw_current_board(board, players_moves):
    for player, moves in players_moves.items():
        for move in moves:
            if str(move) in board:
                board = board.replace(str(move), player)
    for space in SPACES_ON_BOARD:
        if str(space) in board:
            board = board.replace(str(space), ' ')
    return board


def select_move(player, moves, players_moves):
    selecting_move = True

    while selecting_move:
        move = input("Player {}, enter your move.\n".format(player))

        try:
            move = int(move)
        except ValueError:
            print(VALIDATION_ERROR_MESSAGE)
            continue

        if not is_valid_move(move, players_moves):
            print(VALIDATION_ERROR_MESSAGE)
        else:
            moves.append(move)
            selecting_move = False

    players_moves[player] = moves

    return players_moves


def get_all_moves(players_moves):
    return list(chain.from_iterable(players_moves.values()))


def is_valid_move(move, players_moves):
    return move in SPACES_ON_BOARD and move not in get_all_moves(players_moves)


def check_for_winner(players_moves):
    all_moves = get_all_moves(players_moves)

    for player, moves in players_moves.items():
        for combo in WINNING_COMBOS:
            if all(move in moves for move in combo):
                return player + ' wins!'

    if all(move in all_moves for move in SPACES_ON_BOARD):
        return "It's a tie!"


def main():
    players_moves = {
        'x': [],
        'o': [],
    }

    print(game_instructions)

    playing_game = True

    while playing_game:

        for player, moves in players_moves.items():

            current_board = "Current board: \n\n{}\n\n".format(draw_current_board(BOARD, players_moves))
            print(current_board)

            players_moves = select_move(player, moves, players_moves)

            if check_for_winner(players_moves):
                print(check_for_winner(players_moves))
                print(draw_current_board(BOARD, players_moves))
                playing_game = False
                break


if __name__ == "__main__":
    main()
