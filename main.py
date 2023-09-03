import chess


def evaluate(state):
    return 'x'


def generate_moves(board, player):
    return board.legal_moves


def apply_move(board, move):
    return board.push_uci(move)


def minimax(board, depth, player):
    if depth == 0:
        return get_best_move(board)

    best_move = None
    best_value = -float('inf') if player == 1 else float('inf')
    legal_moves = generate_moves(board, player)
    for legal_move in legal_moves:
        new_board = apply_move(board, legal_move)
        value = minimax(new_board, depth - 1, -player)

        if player == 'white':
            if value > best_value:
                best_value = value
                best_move = legal_move
        else:
            if value < best_value:
                best_value = value
                best_move = legal_move

    return best_move


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = chess.Board('8/8/8/8/8/2K5/5R2/1k6 w - - 0 1')
    move = minimax(board, 10, 'white')
