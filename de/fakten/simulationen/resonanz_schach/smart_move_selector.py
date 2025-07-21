import chess
import random
from motif_detection import detect_motifs

def get_recent_chain(board, n=2, relative=False, semantic_map_func=None):
    """
    Extrahiert die letzten n Züge als SAN-Zugkette mit Farbmarkierung (z.B. "w:e4|b:e5").
    Für relative=True: explizite Farbmarkierung und Platzhalter für zukünftige semantische Abstraktion.
    Optional: semantic_map_func ermöglicht weitere Musterabstraktion.
    """
    if not board.move_stack:
        return ""
    san_list = []
    temp_board = chess.Board()
    for move in board.move_stack:
        color = 'w' if temp_board.turn else 'b'
        san = temp_board.san(move)
        if semantic_map_func:
            san = semantic_map_func(san, temp_board)
        san_list.append(f"{color}:{san}")
        temp_board.push(move)
    last_n_san = san_list[-n:]
    return "|".join(last_n_san)

def select_learned_move(board, experience_set, max_chain_n=4):
    """
    Resonanzlogische Zugauswahl: Kumuliert Zugketten- und Motivresonanz.
    Alle Kettenlängen (max_chain_n bis 2), Motive als gleichwertige Resonanzträger.
    Score = Erfolg + Motivbonus − Fehler, Länge als Tiebreaker.
    Zufall nur bei Gleichstand (Exploration).
    """
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None

    move_scores = []
    for move in legal_moves:
        temp_board = board.copy()
        temp_board.push(move)
        best_score = None
        motif_bonus = 0
        motifs = detect_motifs(temp_board)
        if motifs:
            motif_chain = "|".join(sorted(motifs))
            motif_bonus += experience_set.get((f"motif:{motif_chain}", "success"), 0)
            motif_bonus -= experience_set.get((f"motif:{motif_chain}", "failure"), 0)
        for n in range(max_chain_n, 1, -1):
            chain = get_recent_chain(temp_board, n=n, relative=True)
            success = experience_set.get((chain, "success"), 0)
            failure = experience_set.get((chain, "failure"), 0)
            score = (success + motif_bonus, -failure, n)
            if (best_score is None) or (score > best_score):
                best_score = score
        if best_score is None:
            best_score = (motif_bonus, 0, 0)
        move_scores.append((move, best_score))

    move_scores.sort(key=lambda x: x[1], reverse=True)
    top_score = move_scores[0][1]
    top_moves = [move for move, score in move_scores if score == top_score]
    return random.choice(top_moves)