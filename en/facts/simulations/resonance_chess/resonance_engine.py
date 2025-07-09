import chess
from resonance_evaluator import evaluate_resonance

def select_best_move(board, depth=1):
    """Wähle den Zug mit maximalem Resonanzwert, ggf. mit Minimax-Suche."""
    if depth == 1:
        # Nur aktuelle Stellung
        best_move = None
        best_value = -float('inf')
        best_details = None
        for move in board.legal_moves:
            value, details = evaluate_resonance(board, move)
            if value > best_value:
                best_value = value
                best_move = move
                best_details = details
        return best_move, best_value, best_details
    else:
        # Minimax-Suche mit Resonanzbewertung
        move, value, details = minimax_root(board, depth, is_maximizing=board.turn)
        return move, value, details

def minimax_root(board, depth, is_maximizing):
    """Finde den besten Zug mit Minimax bis gegebener Tiefe."""
    best_move = None
    best_value = -float('inf') if is_maximizing else float('inf')
    best_details = None
    for move in board.legal_moves:
        board_push = board.copy(stack=False)
        board_push.push(move)
        value = minimax(board_push, depth-1, not is_maximizing)
        if is_maximizing and value > best_value:
            best_value = value
            best_move = move
            best_details = {"minimax": value}
        elif not is_maximizing and value < best_value:
            best_value = value
            best_move = move
            best_details = {"minimax": value}
    return best_move, best_value, best_details

def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        # Wertung aus Sicht des aktuellen Spielers (WHITE = +, BLACK = -)
        move = next(iter(board.legal_moves), None)
        if move:
            value, _ = evaluate_resonance(board, move)
            return value if board.turn == chess.WHITE else -value
        else:
            return 0
    values = []
    for move in board.legal_moves:
        board_push = board.copy(stack=False)
        board_push.push(move)
        values.append(minimax(board_push, depth-1, not is_maximizing))
    return max(values) if is_maximizing else min(values)