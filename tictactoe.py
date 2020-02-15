import itertools

SPACES_ON_BOARD = (1,2,3,4,5,6,7,8,9)  # todo: use range

WINNING_COMBOS = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (1,4,7),
    (2,5,8),
    (3,6,9),
    (1,5,9),
    (3,5,7)
)

# tie
# players_moves = {
#     'x': [5,7,2,4,9],
#     'o': [1,3,8,6],
# }

players_moves = {
    'x': [],
    'o': [],
}


def check_for_winner(players_moves):
    all_moves = [move for moves in players_moves.values() for move in moves]  # could use itertools chain
    if all(move in all_moves for move in SPACES_ON_BOARD):
        return "It's a tie!"
    for player, moves in players_moves.items():
        for combo in WINNING_COMBOS:
            if all(move in moves for move in combo):
                return player + ' wins'
print(check_for_winner(players_moves))
board = " 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9"
# print(board)

game_instructions = """Welcome to Command Line Tic Tac Toe!

Enter a number from 1-9 to place your move on the board in the corresponding space:

{}
""".format(board)

def draw_current_board(board, players_moves):
    for player, moves in players_moves.items():
        for move in moves:
            if str(move) in board:
                board = board.replace(str(move), player)
    for space in SPACES_ON_BOARD:
        if str(space) in board:
            board = board.replace(str(space), ' ')

    return board

# print(draw_current_board(board, players_moves))

if __name__ == "__main__":
    print(game_instructions)

    playing_game = True

    while playing_game:

        for player, moves in players_moves.items():

            current_board = "Current board: \n\n{}\n\n".format(draw_current_board(board, players_moves))
            print(current_board)

            move = input("Player {}, enter your move.\n".format(player))
            moves.append(int(move))
            # print(players_moves)
            if check_for_winner(players_moves):
                print(check_for_winner(players_moves))
                playing_game = False
                break  # break out of for loop