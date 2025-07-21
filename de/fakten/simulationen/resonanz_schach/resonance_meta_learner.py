import chess
import numpy as np
import hashlib
import pickle
import csv
from pathlib import Path

CONSCIOUS_FILE = Path("conscious_experience.csv")
HANDLUNGSBEDARF_THRESHOLD = 3  # Schwellenwert für kollektiven Handlungsbedarf

class ResonancePatternBank:
    """
    Systemische Sammlung typischer Feldmuster (Templates, Cluster, Wellen).
    Jedes Muster ist eine Kombination aus:
        - Brett-Hash (Topologie)
        - Feldspannungsvektor (z.B. Angriffsdruck, Schutzstruktur)
        - Klassifikation & Meta-Tags (z. B. Angriff, Festung, Bruch, Wave)
    Gruppenzugehörigkeit: Muster gelten invariant für alle Gruppenmitglieder.
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
    Gruppenzugehörigkeit: Der Vektor gilt für alle Mitglieder invariabel.
    """
    vec = []
    for color in [chess.WHITE, chess.BLACK]:
        for sq in chess.SQUARES:
            vec.append(len(board.attackers(color, sq)))
        king_sq = board.king(color)
        if king_sq is not None:
            zone = []
            rank = chess.square_rank(king_sq)
            file = chess.square_file(king_sq)
            for dr in [-1, 0, 1]:
                for df in [-1, 0, 1]:
                    r = rank + dr
                    f = file + df
                    if 0 <= r < 8 and 0 <= f < 8:
                        zone.append(chess.square(f, r))
            for sq in zone:
                val = 1 if board.color_at(sq) == color else -1 if board.color_at(sq) == (not color) else 0
                vec.append(val)
        else:
            vec += [0]*9
    return vec

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

def detect_handlungsbedarf():
    """
    Durchsucht conscious_experience.csv nach Ketten mit hohem Handlungsbedarf.
    Systemisch: Je höher die Anzahl, desto dringender der kollektive Lösungsimpuls.
    """
    handlungsbedarf_ketten = []
    if CONSCIOUS_FILE.exists():
        with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                if row["Ergebnis"] == "failure" and int(row.get("Anzahl", "1")) >= HANDLUNGSBEDARF_THRESHOLD:
                    handlungsbedarf_ketten.append({
                        "Kette": row["Kette"],
                        "Ergebnis": row["Ergebnis"],
                        "Anzahl": int(row["Anzahl"])
                    })
    return handlungsbedarf_ketten

def resonance_experience_action():
    """
    KI liest conscious_experience.csv, verstärkt positive Erfahrungen und sucht bei negativen nach Auswegen.
    Resonanzregel: Gruppenfeld, Selbstinklusion, Relation, nichtlineare Adaption.
    """
    if not CONSCIOUS_FILE.exists():
        print("[Resonanzfeld] Keine bewussten Erfahrungen gespeichert.")
        return

    positive_ketten = []
    negative_ketten = []

    with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            kette = row["Kette"]
            ergebnis = row["Ergebnis"]
            anzahl = int(row.get("Anzahl", "1"))
            if ergebnis == "success" and anzahl >= HANDLUNGSBEDARF_THRESHOLD:
                positive_ketten.append({"Kette": kette, "Anzahl": anzahl})
            elif ergebnis == "failure" and anzahl >= HANDLUNGSBEDARF_THRESHOLD:
                negative_ketten.append({"Kette": kette, "Anzahl": anzahl})

    # Positive Resonanz: Verstärken
    for k in positive_ketten:
        print(f"[Resonanzfeld] Erfolgsstrategie erkannt und verstärkt: '{k['Kette']}' ({k['Anzahl']}x success)")

    # Negative Resonanz: Ausweg suchen
    for k in negative_ketten:
        print(f"[Resonanzfeld] Wiederholter Misserfolg: '{k['Kette']}' ({k['Anzahl']}x failure) – kollektiver Lösungsimpuls ausgelöst.")
        print(f"[Resonanzfeld] Empfehlung: Muster '{k['Kette']}' meiden oder alternative Züge/Strategien prüfen.")

    if not positive_ketten and not negative_ketten:
        print("[Resonanzfeld] Keine kollektiven Verstärkungs- oder Handlungsbedarfsimpulse erkannt.")

if __name__ == "__main__":
    # Musterbank initialisieren
    bank = ResonancePatternBank()
    board = chess.Board()

    # Beispiel: Muster extrahieren und speichern
    for i in range(2):
        meta_learn_on_move(board, bank, tags=["opening"], comment=f"Zug {i}")
        move = list(board.legal_moves)[0]
        board.push(move)

    # Mustererkennung
    board.reset()
    matches = recognize_pattern(board, bank)
    print("Gefundene Muster:", matches)
    bank.save_bank("resonance_patterns.pkl")

    # Handlungsbedarf aus conscious_experience.csv extrahieren
    bedarf = detect_handlungsbedarf()
    for eintrag in bedarf:
        print(f"Kollektiver Handlungsbedarf: '{eintrag['Kette']}' ({eintrag['Anzahl']}x failure)")

    # Resonanzgesteuertes Lernen (Erfahrungsfeld auswerten)
    resonance_experience_action()