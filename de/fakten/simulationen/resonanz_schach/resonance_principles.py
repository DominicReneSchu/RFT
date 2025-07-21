import chess

def king_safety(board):
    """
    Bonus für rochierten König, Malus für König im Zentrum nach 10 Zügen,
    Malus für offene Linien oder wenige Bauern vor dem König.
    """
    score = 0.0
    # Rochade-Status
    if board.has_kingside_castling_rights(chess.WHITE) or board.has_queenside_castling_rights(chess.WHITE):
        if board.king(chess.WHITE) in [chess.G1, chess.C1]:
            score += 1.2
    if board.has_kingside_castling_rights(chess.BLACK) or board.has_queenside_castling_rights(chess.BLACK):
        if board.king(chess.BLACK) in [chess.G8, chess.C8]:
            score -= 1.2
    # König im Zentrum nach 10 Zügen
    if board.fullmove_number > 10:
        for color in [chess.WHITE, chess.BLACK]:
            king_sq = board.king(color)
            if king_sq in [chess.E4, chess.D4, chess.E5, chess.D5]:
                score += 0.8 if color == chess.WHITE else -0.8
    # Bauern vor dem König
    for color in [chess.WHITE, chess.BLACK]:
        king_sq = board.king(color)
        if king_sq is not None:
            file = chess.square_file(king_sq)
            ranks = range(1, 4) if color == chess.WHITE else range(6, 7)
            cnt = 0
            for offset in [-1, 0, 1]:
                f = file + offset
                if 0 <= f < 8:
                    for r in ranks:
                        sq = chess.square(f, r)
                        piece = board.piece_at(sq)
                        if piece and piece.piece_type == chess.PAWN and piece.color == color:
                            cnt += 1
            if cnt < 2:
                score += -0.5 if color == chess.WHITE else 0.5
    return score

def center_control(board):
    """
    Bonus für Bauern und Figuren, die zentrale Felder (d4, e4, d5, e5) kontrollieren.
    """
    score = 0.0
    center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    for color in [chess.WHITE, chess.BLACK]:
        for sq in center_squares:
            attackers = board.attackers(color, sq)
            bonus = 0.2 * len(attackers)
            score += bonus if color == chess.WHITE else -bonus
            piece = board.piece_at(sq)
            if piece and piece.color == color:
                score += 0.3 if color == chess.WHITE else -0.3
    return score

def development(board):
    """
    Bonus für entwickelte Leichtfiguren (Springer, Läufer) in den ersten 10 Zügen.
    Malus, wenn Figuren auf Ausgangsfeldern verharren.
    """
    score = 0.0
    if board.fullmove_number > 12:
        return 0.0
    minor_pieces = {chess.KNIGHT, chess.BISHOP}
    white_developed, black_developed = 0, 0
    white_home = [chess.B1, chess.G1, chess.C1, chess.F1]
    black_home = [chess.B8, chess.G8, chess.C8, chess.F8]
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if not piece or piece.piece_type not in minor_pieces:
            continue
        if piece.color == chess.WHITE:
            if sq not in white_home:
                white_developed += 1
            else:
                score -= 0.2
        else:
            if sq not in black_home:
                black_developed += 1
            else:
                score += 0.2
    score += 0.5 * (white_developed - black_developed)
    return score

def pawn_structure(board):
    """
    Minuspunkte für Doppelbauern, isolierte Bauern, rückständige Bauern.
    Bonus für verbundene Freibauern.
    """
    score = 0.0
    for color in [chess.WHITE, chess.BLACK]:
        pawns = board.pieces(chess.PAWN, color)
        files = [chess.square_file(sq) for sq in pawns]
        # Doppelbauern
        for f in range(8):
            count = files.count(f)
            if count > 1:
                score += -0.3 * (count - 1) if color == chess.WHITE else 0.3 * (count - 1)
        # Isolierte Bauern
        for f in range(8):
            if files.count(f) > 0:
                neighbor_files = []
                if f > 0:
                    neighbor_files += [i for i, file in enumerate(files) if file == f - 1]
                if f < 7:
                    neighbor_files += [i for i, file in enumerate(files) if file == f + 1]
                if not neighbor_files:
                    score += -0.2 if color == chess.WHITE else 0.2
        # Freibauern
        for sq in pawns:
            if is_passed_pawn(board, sq, color):
                score += 0.3 if color == chess.WHITE else -0.3
    return score

def is_passed_pawn(board, sq, color):
    """
    Prüft, ob ein Bauer ein Freibauer ist.
    """
    file = chess.square_file(sq)
    rank = chess.square_rank(sq)
    direction = 1 if color == chess.WHITE else -1
    for df in [-1, 0, 1]:
        f = file + df
        if 0 <= f < 8:
            test_sq = chess.square(f, rank + direction)
            while 0 <= chess.square_rank(test_sq) < 8:
                piece = board.piece_at(test_sq)
                if piece and piece.piece_type == chess.PAWN and piece.color != color:
                    return False
                test_sq = chess.square(f, chess.square_rank(test_sq) + direction)
    return True

def rook_connection(board):
    """
    Bonus, wenn Türme verbunden sind (keine Figuren zwischen den Türmen auf der Grundreihe).
    """
    score = 0.0
    for color in [chess.WHITE, chess.BLACK]:
        back_rank = 0 if color == chess.WHITE else 7
        rook_files = [f for f in range(8) if board.piece_at(chess.square(f, back_rank)) and board.piece_at(chess.square(f, back_rank)).piece_type == chess.ROOK and board.piece_at(chess.square(f, back_rank)).color == color]
        if len(rook_files) == 2:
            between = rook_files[1] - rook_files[0] - 1
            blocked = False
            for f in range(rook_files[0]+1, rook_files[1]):
                if board.piece_at(chess.square(f, back_rank)):
                    blocked = True
            if not blocked:
                score += 0.5 if color == chess.WHITE else -0.5
    return score

def open_file_for_rook(board):
    """
    Bonus für Türme auf offenen oder halboffenen Linien.
    """
    score = 0.0
    for color in [chess.WHITE, chess.BLACK]:
        for sq in board.pieces(chess.ROOK, color):
            file = chess.square_file(sq)
            own_pawn = False
            opp_pawn = False
            for r in range(8):
                piece = board.piece_at(chess.square(file, r))
                if piece and piece.piece_type == chess.PAWN:
                    if piece.color == color:
                        own_pawn = True
                    else:
                        opp_pawn = True
            if not own_pawn and not opp_pawn:
                score += 0.3 if color == chess.WHITE else -0.3  # offene Linie
            elif not own_pawn and opp_pawn:
                score += 0.15 if color == chess.WHITE else -0.15  # halboffen
    return score

def knight_on_rim(board):
    """
    Malus für Springer auf dem Rand (a/h-Linie oder 1/8 Reihe).
    """
    rim_squares = [chess.A1, chess.H1, chess.A8, chess.H8, chess.A2, chess.H2, chess.A7, chess.H7]
    score = 0.0
    for sq in rim_squares:
        piece = board.piece_at(sq)
        if piece and piece.piece_type == chess.KNIGHT:
            score += -0.25 if piece.color == chess.WHITE else 0.25
    return score

def tempo_penalty(board):
    """
    Malus für mehrfache Züge derselben Figur in der Eröffnung.
    """
    # Diese Regel kann nur mit zusätzlicher Zugliste (move history) sauber umgesetzt werden.
    # Platzhalter: Kein Beitrag.
    return 0.0

def evaluate_all_principles(board):
    """
    Aggregiert alle Grundsatzregeln zu einer Gesamtbewertung.
    """
    total = 0.0
    total += king_safety(board)
    total += center_control(board)
    total += development(board)
    total += pawn_structure(board)
    total += rook_connection(board)
    total += open_file_for_rook(board)
    total += knight_on_rim(board)
    total += tempo_penalty(board)
    return total