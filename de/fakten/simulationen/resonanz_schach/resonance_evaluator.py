import chess
import numpy as np

def king_zone(square):
    """Gibt alle Felder des 3x3-Quadrats um square zurück (inkl. Randprüfung)."""
    rank = chess.square_rank(square)
    file = chess.square_file(square)
    zone = []
    for dr in [-1, 0, 1]:
        for df in [-1, 0, 1]:
            r = rank + dr
            f = file + df
            if 0 <= r < 8 and 0 <= f < 8:
                zone.append(chess.square(f, r))
    return zone

def king_safety(board, color):
    """Bewerte die Feldkohärenz um den eigenen König: Nähe verbündeter Figuren, Distanz zu feindlichen Angreifern."""
    king_square = board.king(color)
    if king_square is None:
        return -999  # Matt

    # Verbündete um den König
    allied_mask = np.zeros(64)
    for sq in chess.SQUARES:
        if board.color_at(sq) == color and sq != king_square:
            allied_mask[sq] = 1
    king_neighbors = king_zone(king_square)
    allied_shield = sum(allied_mask[sq] for sq in king_neighbors)

    # Feindliche Angreifer auf den König
    enemy_attackers = board.attackers(not color, king_square)
    pressure = len(enemy_attackers)

    # Resonanzwert: Mehr Schutz = besser, mehr Druck = schlechter
    return allied_shield - 2 * pressure

def king_pressure(board, color):
    """Bewerte den Angriffsdruck auf den gegnerischen König."""
    enemy_king_square = board.king(not color)
    if enemy_king_square is None:
        return 999  # Matt gesetzt

    # Eigene Angreifer auf den gegnerischen König
    attackers = board.attackers(color, enemy_king_square)
    pressure = len(attackers)

    # Nähe: Je näher eigene Figuren am König, desto höher der Druck
    proximity = 0
    for sq in attackers:
        dist = chess.square_distance(sq, enemy_king_square)
        proximity += max(0, 3 - dist)  # Bonus für Nähe bis 3 Felder

    return pressure + proximity

def evaluate_resonance(board, move):
    """
    Feldlogische Gesamtbewertung eines Zuges: 
    𝓡(z) = Schutz eigener König + Druck auf gegnerischen König
    """
    color = board.turn
    board_push = board.copy(stack=False)
    board_push.push(move)

    safety = king_safety(board_push, color)
    pressure = king_pressure(board_push, color)

    resonance = safety + pressure
    return resonance, {"king_safety": safety, "king_pressure": pressure}