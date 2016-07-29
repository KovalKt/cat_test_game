
EMPTY = ""
game_board = []

def check_winner(board_size, board):
    if board_size == 3:
        return winner3(board)
    if board_size == 5:
        return winner5(board)

def winner3(board):
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

def possible_moves(board):
    # moves = [x.id for x in board if x.value == '']
    # cells_num 
    # for cell in range(len(board)):
    #     if board[square] == EMPTY:
    #         moves.append(square)
    # print [x for x in enumerate(board)]
    return [indx for (indx, cell) in enumerate(board) if cell == '']

def get_computer_move(board_size, board, computer_sign, user_sign):
    #copy for checking
    board = board[:]

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for move in possible_moves(board):
        board[move] = computer_sign
        if check_winner(board_size, board) == computer_sign:
            # print (move)
            return move
        board[move] = EMPTY
    for move in possible_moves(board):
        board[move] = user_sign
        if check_winner(board_size, board) == user_sign:
            # print (move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in possible_moves(board):
            # print (move)
            return move
