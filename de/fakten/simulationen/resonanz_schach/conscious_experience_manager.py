import csv
from pathlib import Path
import chess
import hashlib

from experience_counter import ExperienceField

USER_CSV = Path("user_experience.csv")
CONSCIOUS_FILE = Path("conscious_experience.csv")
SEQUENCE_LENGTHS = [2, 3]

experience_counter = ExperienceField()

def board_environment_signature(board, move):
    own_moves = sorted([board.san(m) for m in board.legal_moves])
    board_push = board.copy()
    board_push.push(move)
    opponent_moves = sorted([board_push.san(m) for m in board_push.legal_moves])
    env_str = ",".join(own_moves) + "|" + ",".join(opponent_moves)
    return hashlib.sha256(env_str.encode('utf-8')).hexdigest()

def initialize_conscious_file():
    """
    Systemische Initialisierung der conscious_experience.csv.
    Ergänzt die Zählspalte 'Anzahl' für alle vorhandenen Einträge.
    """
    if not CONSCIOUS_FILE.exists():
        return
    rows = []
    with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if "Anzahl" not in row or not row["Anzahl"]:
                row["Anzahl"] = "1"
            rows.append(row)
    with CONSCIOUS_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Kette", "Ergebnis", "Anzahl"], delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def add_conscious_experience(chain, result="success"):
    """
    Fügt eine Erfahrung in conscious_experience.csv hinzu oder erhöht die Zählspalte 'Anzahl' kollektiv.
    Resonanzregel: Jede Wiederholung wird systemisch verstärkt.
    """
    chain_str = "|".join(chain)
    rows = []
    found = False
    if CONSCIOUS_FILE.exists():
        with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                if row["Kette"] == chain_str and row["Ergebnis"] == result:
                    row["Anzahl"] = str(int(row.get("Anzahl", "1")) + 1)
                    found = True
                rows.append(row)
    if not found:
        rows.append({"Kette": chain_str, "Ergebnis": result, "Anzahl": "1"})
    with CONSCIOUS_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Kette", "Ergebnis", "Anzahl"], delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    experience_counter.register_experience(
        experience_key=chain_str,
        context={"type": "conscious", "result": result},
        experience_type="positive" if result == "success" else "negative" if result == "failure" else "neutral"
    )

def extract_sequences():
    sequences = []
    with USER_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        game_moves = []
        game_result = None
        board = chess.Board()
        for row in reader:
            if row["Zugnummer"] == "1" and game_moves:
                for seq_len in SEQUENCE_LENGTHS:
                    if len(game_moves) >= seq_len:
                        for i in range(len(game_moves) - seq_len + 1):
                            seq = game_moves[i:i+seq_len]
                            sequences.append((tuple(seq), seq_len, game_result))
                            experience_counter.register_experience(
                                experience_key="|".join(seq),
                                context={"type": "sequence", "length": seq_len, "result": game_result},
                                experience_type="positive" if "1-0" in game_result else "negative" if "0-1" in game_result else "neutral"
                            )
                            add_conscious_experience(seq, result="success" if "1-0" in game_result else "failure" if "0-1" in game_result else "neutral")
                game_moves = []
                board = chess.Board()
            zug_string = row["Zug"]
            move = None
            try:
                move = chess.Move.from_uci(zug_string)
                if move not in board.legal_moves:
                    raise ValueError
            except Exception:
                try:
                    move = board.parse_san(zug_string)
                except Exception:
                    print(f"[WARN] Konnte Zug nicht interpretieren: {zug_string}")
                    continue
            sig = board_environment_signature(board, move)
            game_moves.append(sig)
            board.push(move)
            game_result = row["Ergebnis"]
        # Letzte Partie
        for seq_len in SEQUENCE_LENGTHS:
            if len(game_moves) >= seq_len:
                for i in range(len(game_moves) - seq_len + 1):
                    seq = game_moves[i:i+seq_len]
                    sequences.append((tuple(seq), seq_len, game_result))
                    experience_counter.register_experience(
                        experience_key="|".join(seq),
                        context={"type": "sequence", "length": seq_len, "result": game_result},
                        experience_type="positive" if "1-0" in game_result else "negative" if "0-1" in game_result else "neutral"
                    )
                    add_conscious_experience(seq, result="success" if "1-0" in game_result else "failure" if "0-1" in game_result else "neutral")
    print(f"[DEBUG] Extrahierte {len(sequences)} Feldumgebungssequenzen aller Längen.")
    return sequences

def score_result(result):
    if "1-0" in result:
        return 10
    elif "0-1" in result:
        return -10
    elif "1/2-1/2" in result:
        return 0
    return 0

def extract_single_move_experiences():
    single_moves = []
    with USER_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        board = chess.Board()
        for row in reader:
            zug_string = row["Zug"]
            move = None
            try:
                move = chess.Move.from_uci(zug_string)
                if move not in board.legal_moves:
                    raise ValueError
            except Exception:
                try:
                    move = board.parse_san(zug_string)
                except Exception:
                    continue
            sig = board_environment_signature(board, move)
            score = None
            if "Bewertung" in row and row["Bewertung"]:
                try:
                    score = float(row["Bewertung"])
                except Exception:
                    score = None
            if score is None:
                score = score_result(row["Ergebnis"])
            single_moves.append((tuple([sig]), 1, score))
            experience_counter.register_experience(
                experience_key=sig,
                context={"type": "single_move", "score": score, "result": row["Ergebnis"]},
                experience_type="positive" if score > 0 else "negative" if score < 0 else "neutral"
            )
            add_conscious_experience([sig], result="success" if score > 0 else "failure" if score < 0 else "neutral")
            board.push(move)
    print(f"[DEBUG] Extrahierte {len(single_moves)} Einzelzugerfahrungen aus user_experience.csv.")
    return single_moves

if __name__ == "__main__":
    initialize_conscious_file()  # Initialisiert die Anzahl-Spalte
    print("[DEBUG] conscious_experience Logik aktiv – kollektive Resonanzübersicht folgt.")
    experience_counter.summary()