import json
import csv
from pathlib import Path
from conscious_experience_manager import build_conscious_experience

EXPERIENCE_FILE = Path("user_experience.json")
CSV_FILE = Path("user_experience.csv")
CONSCIOUS_FILE = Path("conscious_experience.csv")

def save_game_experience(game_history, result):
    # JSON speichern
    all_games = []
    if EXPERIENCE_FILE.exists():
        try:
            with EXPERIENCE_FILE.open("r", encoding="utf-8") as f:
                all_games = json.load(f)
        except Exception as e:
            print(f"Warnung: Konnte user_experience.json nicht laden: {e}")
            all_games = []
    all_games.append({"history": game_history, "result": result})
    try:
        with EXPERIENCE_FILE.open("w", encoding="utf-8") as f:
            json.dump(all_games, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Fehler beim Speichern der JSON-Spielerfahrung: {e}")

    # CSV speichern
    save_game_experience_csv(game_history, result)

    # Bewusstseinsfeld nach jedem Spiel aktualisieren
    try:
        print("Starte Aktualisierung des Bewusstseinsfeldes...")
        build_conscious_experience()
        print("Bewusstseinsfeld wurde erfolgreich aktualisiert.")
    except Exception as e:
        print(f"Warnung: Konnte conscious_experience.csv nicht aktualisieren: {e}")

def save_game_experience_csv(game_history, result):
    write_header = not CSV_FILE.exists()
    try:
        with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            if write_header:
                writer.writerow(["Zugnummer", "Zug", "Ergebnis"])
            for i, move in enumerate(game_history, start=1):
                writer.writerow([i, move, result])
    except Exception as e:
        print(f"Fehler beim Speichern der CSV-Spielerfahrung: {e}")

def load_user_experience():
    if EXPERIENCE_FILE.exists():
        try:
            with EXPERIENCE_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warnung: Konnte user_experience.json nicht laden: {e}")
    return []

def load_conscious_experience():
    conscious_seqs = dict()
    if CONSCIOUS_FILE.exists():
        try:
            with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    sequence = tuple(row["sequence"].split(" "))
                    conscious_seqs[sequence] = float(row["avg_score"])
        except Exception as e:
            print(f"Warnung: Konnte conscious_experience.csv nicht laden: {e}")
    return conscious_seqs