import csv
from collections import defaultdict
from pathlib import Path

SEQUENCE_LENGTH = 10
USER_CSV = Path("user_experience.csv")
CONSCIOUS_CSV = Path("conscious_experience.csv")

def extract_sequences():
    sequences = []
    current_game = []
    current_result = None
    with USER_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            # Erkenne Start einer neuen Partie
            if row["Zugnummer"] == "1" and current_game:
                # Sliding Window über die abgeschlossene Partie
                if len(current_game) >= SEQUENCE_LENGTH:
                    for i in range(len(current_game) - SEQUENCE_LENGTH + 1):
                        sequences.append((tuple(current_game[i:i+SEQUENCE_LENGTH]), current_result))
                current_game = []
            current_game.append(row["Zug"])
            current_result = row["Ergebnis"]
        # Sliding Window für die letzte (evtl. laufende) Partie
        if current_game and len(current_game) >= SEQUENCE_LENGTH:
            for i in range(len(current_game) - SEQUENCE_LENGTH + 1):
                sequences.append((tuple(current_game[i:i+SEQUENCE_LENGTH]), current_result))
    print(f"[DEBUG] Extrahierte {len(sequences)} Sequenzen aus allen Partien.")
    return sequences

def score_result(result):
    # Skala: 10 = Sieg, 1 = Niederlage, 5 = Remis, 3 = Sonstiges
    if "1-0" in result:
        return 10
    elif "0-1" in result:
        return 1
    elif "1/2-1/2" in result:
        return 5
    return 3

def build_conscious_experience():
    seq_stats = defaultdict(list)
    sequences = extract_sequences()
    for seq, result in sequences:
        seq_stats[seq].append(score_result(result))
    conscious_list = []
    for seq, scores in seq_stats.items():
        avg_score = sum(scores) / len(scores)
        conscious_list.append({
            "sequence": " ".join(seq),
            "count": len(scores),
            "avg_score": round(avg_score, 2)
        })
    conscious_list.sort(key=lambda x: (-x["avg_score"], -x["count"]))
    with CONSCIOUS_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sequence", "count", "avg_score"], delimiter=";")
        writer.writeheader()
        for row in conscious_list:
            writer.writerow(row)
    print(f"[DEBUG] Bewusstseinsfeld aktualisiert: {len(conscious_list)} Sequenzen gespeichert.")

if __name__ == "__main__":
    build_conscious_experience()