
EMPTY = ""


def check_winner(board_size, board, diagonals):
    if board_size == 3:
        return winner3(board, diagonals)
    if board_size == 5:
        return winner5(board, diagonals)

def winner3(board, diagonals):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5),
                   (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8))
    if diagonals:
        WAYS_TO_WIN += ((0, 4, 8), (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner, (row[0], row[1], row[2])
        if not len(possible_moves(board)):
            return "Tie", None
    return None, None

def winner5(board, diagonals):
    WAYS_TO_WIN = ((0, 1, 2, 3, 4), (5, 6, 7, 8, 9),
                   (10, 11, 12 ,13, 14), (15, 16, 17, 18, 19),
                   (20, 21, 22, 23, 24), (0, 5, 10, 15, 20),
                   (1, 6, 11, 16, 21), (2, 7, 12, 17, 22),
                   (3, 8, 13, 18, 23), (4, 9, 14, 19, 24))
    if diagonals:
        WAYS_TO_WIN += ((0, 6, 12, 18, 24),(4, 8, 12, 10, 20))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] == board[row[3]] == board[row[4]] != EMPTY:
            winner = board[row[0]]
            return winner, (row[0], row[1], row[2], row[3], row[4])
        if not len(possible_moves(board)):
            return "Tie", None
    return None, None


def possible_moves(board):
    return [indx for (indx, cell) in enumerate(board) if cell == '']

def get_computer_move(board_size, board, computer_sign, user_sign, diagonals):
    board = board[:]

    BEST_MOVES = give_best_moves(board_size, diagonals)
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

def give_best_moves(board_size, diagonals):
    if board_size == 3:
        if diagonals:
            return (4, 0, 2, 6, 8, 1, 3, 5, 7)
        else:
            return (4, 1, 7, 3, 5, 0, 6, 2, 8)
    elif board_size == 5:
        if diagonals:
            return (12, 0, 4, 8, 16, 24, 1, 5, 11, 17, 23,
                    2, 6, 10, 18, 22, 3, 7, 13, 15, 21, 9,
                    14, 19, 20)
        else:
            return (12, 0, 6, 18, 24, 4, 8, 16, 20, 1, 2,
                    3, 5, 7, 9, 10, 11, 13, 14, 15, 17, 19,
                    21, 22, 23)