import chess
import numpy as np
import hashlib
import pickle

class ResonancePatternBank:
    """
    Systemische Sammlung typischer Feldmuster (Templates, Cluster, Wellen).
    Jedes Muster ist eine Kombination aus:
        - Brett-Hash (Topologie)
        - Feldspannungsvektor (z.B. Angriffsdruck, Schutzstruktur)
        - Klassifikation & Meta-Tags (z. B. Angriff, Festung, Bruch, Wave)
    """
    def __init__(self):
        self.patterns = {}  # key: hash, value: dict with meta

    def _position_hash(self, board, mode="minimal"):
        """
        Erzeugt einen systemisch invarianten Hash für die aktuelle Stellung.
        mode="minimal": Nur Stellung und Zugrecht.
        """
        fen = board.board_fen()
        stm = "w" if board.turn else "b"
        # Systemische Invarianz: Nur relevante Feldstruktur, keine Zählwerte
        key = f"{fen}_{stm}"
        return hashlib.sha1(key.encode("utf-8")).hexdigest()

    def store_pattern(self, board, resonance_vector, tags=None, comment=""):
        """
        Füge ein Muster hinzu (mit Topologie, Resonanzvektor, Tags).
        """
        pattern_hash = self._position_hash(board)
        self.patterns[pattern_hash] = {
            "fen": board.fen(),
            "resonance_vector": resonance_vector,
            "tags": tags or [],
            "comment": comment
        }

    def match_pattern(self, board, resonance_vector, tolerance=0.1):
        """
        Suche nach ähnlichen Mustern. Systemisch: Feldvektoren vergleichen.
        Gibt Liste (hash, dist, meta) zurück – sortiert nach Ähnlichkeit.
        """
        matches = []
        for k, v in self.patterns.items():
            vec_ref = v["resonance_vector"]
            # Systemische Feldabstandsmetrik (z.B. L2-Norm)
            dist = np.linalg.norm(np.array(resonance_vector) - np.array(vec_ref))
            if dist <= tolerance:
                matches.append((k, dist, v))
        matches.sort(key=lambda x: x[1])
        return matches

    def save_bank(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.patterns, f)

    def load_bank(self, path):
        with open(path, "rb") as f:
            self.patterns = pickle.load(f)

def extract_resonance_vector(board):
    """
    Extrahiere einen systemisch-invarianten Resonanzvektor:
    - Angriffsdruck pro Feld (flach, 64 Werte)
    - Schutzstruktur um beide Könige (lokale Masken)
    Rückgabe: 64+18 = 82-dim Vektor (Beispiel)
    """
    vec = []
    for color in [chess.WHITE, chess.BLACK]:
        # Angriffsdruck gesamt
        for sq in chess.SQUARES:
            vec.append(len(board.attackers(color, sq)))
        # Königsschutz: 3x3-Umgebung
        king_sq = board.king(color)
        if king_sq is not None:
            zone = chess.SquareSet(chess.SQUARES_3X3[king_sq])
            for sq in zone:
                val = 1 if board.color_at(sq) == color else -1 if board.color_at(sq) == (not color) else 0
                vec.append(val)
        else:
            # Kein König: Matt
            vec += [0]*9
    return vec

# --- Beispiel für Integration in die Hauptengine ---

def meta_learn_on_move(board, pattern_bank, tags=None, comment=""):
    """
    Wird nach jedem Zug aufgerufen: Muster extrahieren und ggf. speichern.
    """
    resonance_vec = extract_resonance_vector(board)
    pattern_bank.store_pattern(board, resonance_vec, tags=tags, comment=comment)

def recognize_pattern(board, pattern_bank, tolerance=2.0):
    """
    Erkenne, ob aktuelle Stellung einem bekannten Muster entspricht.
    """
    resonance_vec = extract_resonance_vector(board)
    matches = pattern_bank.match_pattern(board, resonance_vec, tolerance=tolerance)
    return matches

# --- Beispiel für Nutzung ---

if __name__ == "__main__":
    bank = ResonancePatternBank()
    board = chess.Board()

    # Schritt 1: Musterbank aufbauen
    # (Beispiel: erste Züge, typische Muster speichern)
    for i in range(2):
        meta_learn_on_move(board, bank, tags=["opening"], comment=f"Zug {i}")
        move = list(board.legal_moves)[0]
        board.push(move)

    # Schritt 2: Aktuelle Stellung abgleichen
    board.reset()
    matches = recognize_pattern(board, bank)
    print("Gefundene Muster:", matches)
    bank.save_bank("resonance_patterns.pkl")