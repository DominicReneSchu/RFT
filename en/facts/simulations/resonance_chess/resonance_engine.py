import chess
from resonance_evaluator import evaluate_resonance

def select_best_move(board, depth=1):
    """
    Wähle den Zug mit maximalem Resonanzwert, priorisiere Mattsetzung,
    berücksichtigt Wertigkeiten aller Figuren und Schutzstruktur.
    """
    if depth == 1:
        best_move = None
        best_value = -float('inf')
        best_details = None
        for move in board.legal_moves:
            value, details = evaluate_resonance(board, move)
            # Priorisiere Mattsetzung maximal
            board_push = board.copy(stack=False)
            board_push.push(move)
            if board_push.is_checkmate():
                value = float('inf')
                details["matt"] = True
            elif board_push.is_stalemate():
                value = 0
                details["pat"] = True
            if value > best_value:
                best_value = value
                best_move = move
                best_details = details
        return best_move, best_value, best_details
    else:
        move, value, details = minimax_root(board, depth, is_maximizing=board.turn)
        return move, value, details

def minimax_root(board, depth, is_maximizing):
    """
    Minimax-Startknoten: Durchsucht alle legalen Züge, priorisiert Mattsetzung,
    berücksichtigt Wertigkeit und Schutzstrukturen.
    """
    best_move = None
    best_value = -float('inf') if is_maximizing else float('inf')
    best_details = None
    for move in board.legal_moves:
        board_push = board.copy(stack=False)
        board_push.push(move)
        value = minimax(board_push, depth-1, not is_maximizing, matthunter=True)
        details = {"minimax": value}
        # Priorisiere kürzesten Mattweg
        if board_push.is_checkmate():
            value = float('inf') - (depth * 100)  # Je schneller Matt, desto höher
            details["matt"] = True
        elif board_push.is_stalemate():
            value = 0
            details["pat"] = True
        if is_maximizing and value > best_value:
            best_value = value
            best_move = move
            best_details = details
        elif not is_maximizing and value < best_value:
            best_value = value
            best_move = move
            best_details = details
    return best_move, best_value, best_details

def minimax(board, depth, is_maximizing, matthunter=False):
    """
    Rekursive Minimax-Logik mit Resonanzbewertung:
    - Priorisiert Mattsetzung (kürzeste Wege)
    - Bewertet Material (Wertigkeit), Angriffs- und Schutzfelder (über evaluate_resonance)
    """
    if depth == 0 or board.is_game_over():
        if board.is_checkmate():
            # Matt für den Zugausführenden = Niederlage
            return -float('inf') if board.turn == chess.WHITE else float('inf')
        elif board.is_stalemate():
            return 0
        move = next(iter(board.legal_moves), None)
        if move:
            value, _ = evaluate_resonance(board, move)
            # Für das Minimax: Wert aus Sicht des aktuellen Spielers
            return value if board.turn == chess.WHITE else -value
        else:
            return 0
    values = []
    for move in board.legal_moves:
        board_push = board.copy(stack=False)
        board_push.push(move)
        # Mattjäger-Logik: Kürzester Mattweg zählt höher
        if matthunter and board_push.is_checkmate():
            val = float('inf') - (depth * 100)
        elif matthunter and board_push.is_stalemate():
            val = 0
        else:
            val = minimax(board_push, depth-1, not is_maximizing, matthunter)
        values.append(val)
    return max(values) if is_maximizing else min(values)