def get_time_limit(board, last_move=None):
    # Kritische Stellungen: Schach, wenige Züge, Endspiel, Materialschwankung, Königszug
    if last_move:
        piece = board.piece_at(last_move.to_square)
        if piece and piece.piece_type == chess.KING:
            return 300  # 5 Minuten bei Königszug
    if board.is_check():
        return 300  # 5 Minuten bei Schach
    if len(list(board.legal_moves)) < 8:
        return 240  # 4 Minuten bei Endspiel/Kritik
    if sum(1 for p in board.piece_map().values() if p.color == board.turn) < 5:
        return 180  # 3 Minuten bei wenig Material
    return 120  # 2 Minuten Standard (unkritisch)