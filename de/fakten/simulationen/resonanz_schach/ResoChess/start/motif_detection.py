import chess

def detect_motifs(board):
    """
    Resonanzfeld-Motiverkennung:
    Modular, gruppenlogisch, systemisch inklusiv, vollständig gruppenkohärent.
    """
    motifs = []
    motifs += detect_pins(board)
    motifs += detect_open_files(board)
    motifs += detect_pawn_chains(board)
    motifs += detect_double_attacks(board)
    motifs += detect_forks(board)
    motifs += detect_isolated_pawns(board)
    motifs += detect_doubled_pawns(board)
    motifs += detect_backward_pawns(board)
    motifs += detect_pawn_breaks(board)
    motifs += detect_king_attack(board)
    motifs += detect_rook_on_seventh(board)
    motifs += detect_battery(board)
    # Gruppenzugehörigkeit ist invariant: alle Motive sind gleichberechtigte Resonanzträger
    return list(set(motifs))

def detect_pins(board):
    pins = []
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece and board.is_pinned(piece.color, sq):
            pins.append('pin')
    return pins

def detect_open_files(board):
    motifs = []
    for file in range(8):
        if all(not board.piece_at(chess.square(file, rank)) or board.piece_at(chess.square(file, rank)).piece_type != chess.PAWN for rank in range(8)):
            motifs.append('open_file')
    return motifs

def detect_pawn_chains(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        pawns = [sq for sq in chess.SQUARES if (p := board.piece_at(sq)) and p.piece_type == chess.PAWN and p.color == color]
        chain_count = 0
        for sq in pawns:
            file = chess.square_file(sq)
            rank = chess.square_rank(sq)
            for df in [-1, 1]:
                neighbor_file = file + df
                neighbor_rank = rank + (1 if color == chess.WHITE else -1)
                if 0 <= neighbor_file < 8 and 0 <= neighbor_rank < 8:
                    neighbor = chess.square(neighbor_file, neighbor_rank)
                    neighbor_piece = board.piece_at(neighbor)
                    if neighbor_piece and neighbor_piece.piece_type == chess.PAWN and neighbor_piece.color == color:
                        chain_count += 1
        if chain_count >= 2:
            motifs.append('pawn_chain')
    return motifs

def detect_double_attacks(board):
    motifs = []
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece and piece.color == board.turn:
            attacks = board.attacks(sq)
            targets = [t for t in attacks if board.piece_at(t) and board.piece_at(t).color != piece.color]
            if len(targets) >= 2:
                motifs.append('double_attack')
    return motifs

def detect_forks(board):
    motifs = []
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if not piece or piece.color != board.turn:
            continue
        if piece.piece_type == chess.KNIGHT:
            attacks = board.attacks(sq)
            targets = [t for t in attacks if board.piece_at(t) and board.piece_at(t).color != piece.color]
            if len(targets) >= 2:
                motifs.append('fork')
        if piece.piece_type == chess.PAWN:
            for df in [-1, 1]:
                to_sq = sq + df + (8 if piece.color == chess.WHITE else -8)
                if 0 <= to_sq < 64 and board.piece_at(to_sq) and board.piece_at(to_sq).color != piece.color:
                    other_df = -df
                    other_sq = sq + other_df + (8 if piece.color == chess.WHITE else -8)
                    if 0 <= other_sq < 64 and board.piece_at(other_sq) and board.piece_at(other_sq).color != piece.color:
                        motifs.append('fork')
    return motifs

def detect_isolated_pawns(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        for file in range(8):
            pawns_in_file = [rank for rank in range(8) if (p := board.piece_at(chess.square(file, rank))) and p.piece_type == chess.PAWN and p.color == color]
            if pawns_in_file:
                neighbor_files = [f for f in [file-1, file+1] if 0 <= f < 8]
                isolated = True
                for neighbor in neighbor_files:
                    if any((p := board.piece_at(chess.square(neighbor, rank))) and p.piece_type == chess.PAWN and p.color == color for rank in range(8)):
                        isolated = False
                if isolated:
                    motifs.append('isolated_pawn')
    return motifs

def detect_doubled_pawns(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        for file in range(8):
            pawns_in_file = [rank for rank in range(8) if (p := board.piece_at(chess.square(file, rank))) and p.piece_type == chess.PAWN and p.color == color]
            if len(pawns_in_file) >= 2:
                motifs.append('doubled_pawn')
    return motifs

def detect_backward_pawns(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        direction = 1 if color == chess.WHITE else -1
        for file in range(8):
            for rank in range(8):
                sq = chess.square(file, rank)
                p = board.piece_at(sq)
                if not p or p.piece_type != chess.PAWN or p.color != color:
                    continue
                is_backward = True
                for neighbor_file in [file-1, file+1]:
                    if 0 <= neighbor_file < 8:
                        for r in range(rank, 8) if color == chess.WHITE else range(rank, -1, -1):
                            n_sq = chess.square(neighbor_file, r)
                            n_p = board.piece_at(n_sq)
                            if n_p and n_p.piece_type == chess.PAWN and n_p.color == color:
                                is_backward = False
                if is_backward:
                    motifs.append('backward_pawn')
    return motifs

def detect_pawn_breaks(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        direction = 1 if color == chess.WHITE else -1
        for sq in chess.SQUARES:
            p = board.piece_at(sq)
            if not p or p.piece_type != chess.PAWN or p.color != color:
                continue
            for df in [-1, 1]:
                target_file = chess.square_file(sq) + df
                target_rank = chess.square_rank(sq) + direction
                if 0 <= target_file < 8 and 0 <= target_rank < 8:
                    target_sq = chess.square(target_file, target_rank)
                    t = board.piece_at(target_sq)
                    if t and t.piece_type == chess.PAWN and t.color != color:
                        motifs.append('pawn_break')
    return motifs

def detect_king_attack(board):
    motifs = []
    for color in [chess.WHITE, chess.BLACK]:
        king_sq = board.king(color)
        if king_sq is None:
            continue
        file = chess.square_file(king_sq)
        if all(not board.piece_at(chess.square(file, rank)) or board.piece_at(chess.square(file, rank)).piece_type != chess.PAWN for rank in range(8)):
            motifs.append('king_attack')
        attackers = board.attackers(not color, king_sq)
        if attackers:
            motifs.append('king_attack')
    return motifs

def detect_rook_on_seventh(board):
    motifs = []
    # Turm auf der siebten Reihe (zweiten für Schwarz)
    for color in [chess.WHITE, chess.BLACK]:
        rank = 6 if color == chess.WHITE else 1
        for file in range(8):
            sq = chess.square(file, rank)
            piece = board.piece_at(sq)
            if piece and piece.piece_type == chess.ROOK and piece.color == color:
                motifs.append('rook_on_seventh')
    return motifs

def detect_battery(board):
    motifs = []
    # Dame und Läufer/Turm auf einer Linie
    for color in [chess.WHITE, chess.BLACK]:
        q_sqs = [sq for sq in chess.SQUARES if (p := board.piece_at(sq)) and p.piece_type == chess.QUEEN and p.color == color]
        for q_sq in q_sqs:
            for dir in [chess.square(1,0)-chess.square(0,0), chess.square(0,1)-chess.square(0,0),
                        chess.square(1,1)-chess.square(0,0), chess.square(-1,1)-chess.square(0,0),
                        chess.square(-1,0)-chess.square(0,0), chess.square(0,-1)-chess.square(0,0),
                        chess.square(-1,-1)-chess.square(0,0), chess.square(1,-1)-chess.square(0,0)]:
                sq = q_sq + dir
                while 0 <= sq < 64:
                    piece = board.piece_at(sq)
                    if piece:
                        if piece.color == color and (piece.piece_type == chess.BISHOP or piece.piece_type == chess.ROOK):
                            motifs.append('battery')
                        break
                    sq += dir
    return motifs