import chess
import random

def get_recent_chain(board, n=2, relative=False):
    """
    Extrahiert die letzten n Züge als SAN-Zugkette mit Farbmarkierung (z.B. "w:e4|b:e5").
    Für relative=True Platzhalter für zukünftige semantische Abstraktion.
    """
    if not board.move_stack:
        return ""
    san_list = []
    temp_board = chess.Board()
    for move in board.move_stack:
        color = 'w' if temp_board.turn else 'b'
        san = temp_board.san(move)
        if relative:
            # Platzhalter für Muster, z.B. f"{color}:piece_center"
            san_list.append(f"{color}:{san}")  # später abstrahieren
        else:
            san_list.append(f"{color}:{san}")
        temp_board.push(move)
    last_n_san = san_list[-n:]
    return "|".join(last_n_san)

def select_learned_move(board, experience_set, max_chain_n=4):
    """
    Wählt anhand von Erfahrung und Gewichtung.
    - Berücksichtigt alle Kettenlängen von max_chain_n bis 2 (je länger, desto vorrangig)
    - Bevorzugt Züge mit hoher 'success'-Gewichtung, meidet 'failure'
    - Bei Gleichstand: Zufallswahl
    """
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None

    move_scores = []
    for move in legal_moves:
        temp_board = board.copy()
        temp_board.push(move)
        best_score = None
        for n in range(max_chain_n, 1, -1):
            chain = get_recent_chain(temp_board, n=n)
            success = experience_set.get((chain, "success"), 0)
            failure = experience_set.get((chain, "failure"), 0)
            if success or failure:
                score = (success, -failure, n)
                if (best_score is None) or (score > best_score):
                    best_score = score
        if best_score is None:
            best_score = (0, 0, 0)
        move_scores.append((move, best_score))

    # Sortiere nach Success, dann wenig Failure, dann längste Kette
    move_scores.sort(key=lambda x: x[1], reverse=True)
    top_score = move_scores[0][1]
    top_moves = [move for move, score in move_scores if score == top_score]
    return random.choice(top_moves)