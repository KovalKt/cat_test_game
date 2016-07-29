
EMPTY = ""


def check_winner(board_size, board, diagonals):
    if board_size == 3:
        return winner3(board, diagonals)
    if board_size == 5:
        return winner5(board, diagonals)

def winner3(board, diagonals):
    if not diagonals:
        WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5),
                       (6, 7, 8), (0, 3, 6),
                       (1, 4, 7), (2, 5, 8))
    else:
        WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5),
                       (6, 7, 8), (0, 3, 6),
                       (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner, (row[0], row[1], row[2])
        if not len(possible_moves(board)):
            return "Tie", None
    return None, None

def winner5(board, diagonals):
    pass

def possible_moves(board):
    return [indx for (indx, cell) in enumerate(board) if cell == '']

def get_computer_move(board_size, board, computer_sign, user_sign, diagonals):
    board = board[:]

    if diagonals:
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    else:
        BEST_MOVES = (4, 1, 7, 3, 5, 0, 6, 2, 8)
    for move in possible_moves(board):
        board[move] = computer_sign
        if check_winner(board_size, board, diagonals) == computer_sign:
            return move
        board[move] = EMPTY
    for move in possible_moves(board):
        board[move] = user_sign
        if check_winner(board_size, board, diagonals) == user_sign:
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in possible_moves(board):
            return move
