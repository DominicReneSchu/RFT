import chess
import math

def dynamic_piece_value(piece_type, board, color):
    """
    Dynamischer Wert einer Figur abhängig vom Spielfeld-Zustand.
    Exponentielles Wachstum: Je weniger Figuren, desto wertvoller wird jede einzelne.
    Die Dame ist einzigartig und wird besonders stark gewichtet.
    """
    base = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    own_pieces = [p for p in board.piece_map().values() if p.color == color and p.piece_type != chess.KING]
    n = len(own_pieces)
    # Exponentieller Wachstumsfaktor
    k = 0.13
    expo = math.exp(k * (15 - n))
    # Dame erhält zusätzlichen Multiplikator für Einzigartigkeit und Bedeutung im Endspiel
    if piece_type == chess.QUEEN:
        expo *= 1.7
    # Bauern werden im Endspiel ebenfalls systemisch wertvoller
    if piece_type == chess.PAWN and n < 7:
        expo *= 1.25
    return base[piece_type] * expo

def evaluate_resonance(board, move):
    board_cp = board.copy()
    board_cp.push(move)
    color = board.turn
    opp_color = not color

    # Dynamische Materialbewertung
    my_material = sum(
        dynamic_piece_value(p.piece_type, board_cp, color)
        for p in board_cp.piece_map().values() if p.color == color and p.piece_type != chess.KING
    )
    opp_material = sum(
        dynamic_piece_value(p.piece_type, board_cp, opp_color)
        for p in board_cp.piece_map().values() if p.color == opp_color and p.piece_type != chess.KING
    )
    material_diff = my_material - opp_material

    # Gefolgschaft (Anzahl + Typen der verbleibenden Figuren)
    my_figures = [sq for sq in chess.SQUARES if (
        (p := board_cp.piece_at(sq)) and p.color == color and p.piece_type != chess.KING)]
    opp_figures = [sq for sq in chess.SQUARES if (
        (p := board_cp.piece_at(sq)) and p.color == opp_color and p.piece_type != chess.KING)]
    gefolgschaft = len(my_figures) - len(opp_figures)

    # Mobilität
    my_mob = sum(1 for m in board_cp.legal_moves if board_cp.piece_at(m.from_square) and board_cp.piece_at(m.from_square).color == color)
    opp_mob = sum(1 for m in board_cp.legal_moves if board_cp.piece_at(m.from_square) and board_cp.piece_at(m.from_square).color == opp_color)
    mobilitaet = my_mob - opp_mob

    # Synergie
    my_synergy = sum(
        sum(1 for sq2 in chess.SQUARES if board_cp.is_attacked_by(color, sq2) and board_cp.piece_at(sq2) and board_cp.piece_at(sq2).color == color)
        for sq in my_figures
    )
    opp_synergy = sum(
        sum(1 for sq2 in chess.SQUARES if board_cp.is_attacked_by(opp_color, sq2) and board_cp.piece_at(sq2) and board_cp.piece_at(sq2).color == opp_color)
        for sq in opp_figures
    )
    synergie = my_synergy - opp_synergy

    # Königssicherheit: Wie viele eigene Figuren decken Felder um den König
    king_sq = next(sq for sq in chess.SQUARES if (p := board_cp.piece_at(sq)) and p.color == color and p.piece_type == chess.KING)
    king_zone = [sq for sq in chess.SQUARES if chess.square_distance(sq, king_sq) == 1]
    king_safe = sum(1 for sq in king_zone if board_cp.is_attacked_by(color, sq))

    # Gesamtbewertung: Dynamisches Material dominiert exponentiell, Rest systemisch verschränkt
    value = 8.0 * material_diff + 2.0 * gefolgschaft + 1.2 * mobilitaet + 0.8 * synergie + 1.0 * king_safe

    details = {
        "material_diff": material_diff,
        "gefolgschaft": gefolgschaft,
        "mobilitaet": mobilitaet,
        "synergie": synergie,
        "king_safe": king_safe
    }
    return value, details