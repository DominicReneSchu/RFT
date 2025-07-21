import json
import csv
from pathlib import Path
import os

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
    # Nach Speicherung: CSV-Datei löschen (systemisch invariant)
    delete_user_experience_csv()

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

def delete_user_experience_csv():
    if CSV_FILE.exists():
        try:
            os.remove(CSV_FILE)
            print("user_experience.csv nach Erfahrungsspeicherung gelöscht (systemisch invariant).")
        except Exception as e:
            print(f"Fehler beim Löschen von user_experience.csv: {e}")

def load_user_experience():
    if EXPERIENCE_FILE.exists():
        try:
            with EXPERIENCE_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warnung: Konnte user_experience.json nicht laden: {e}")
    return []

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
        # Prüfe auf Anzahl-Spalte, ergänze falls nötig
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
    Führt kollektive Speicherung und Zählung in conscious_experience.csv aus.
    Jede Wiederholung verstärkt die Zählspalte 'Anzahl' systemisch invariant.
    """
    if not chain:
        print("add_conscious_experience: Leere Kette, nichts gespeichert.")
        return
    chain_str = "|".join(chain)
    entries = []
    found = False

    # Lade alle Einträge und erhöhe Anzahl bei Wiederholung
    if CONSCIOUS_FILE.exists():
        with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                # Falls Anzahl fehlt, initialisiere mit 1
                if "Anzahl" not in row or not row["Anzahl"]:
                    row["Anzahl"] = "1"
                # Prüfe auf Wiederholung
                if row["Kette"] == chain_str and row["Ergebnis"] == result:
                    row["Anzahl"] = str(int(row["Anzahl"]) + 1)
                    found = True
                entries.append(row)
    if not found:
        # Neue Kette: initialisiere Zählspalte
        entries.append({"Kette": chain_str, "Ergebnis": result, "Anzahl": "1"})
        print("add_conscious_experience: Bewusste Erfahrung gespeichert.")
    else:
        print("add_conscious_experience: Anzahl erhöht – kollektive Verstärkung.")
    # Schreibe alle Einträge zurück
    with CONSCIOUS_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Kette", "Ergebnis", "Anzahl"], delimiter=";")
        writer.writeheader()
        for row in entries:
            writer.writerow(row)

def _load_conscious_experience_set():
    """
    Lädt alle bewussten Erfahrungen als Set von (Kette, Ergebnis) für schnelle Duplikat-Prüfung.
    Systemisch gruppenfähig, da alle Ketten invariant wirken.
    """
    exp_set = set()
    if CONSCIOUS_FILE.exists():
        with CONSCIOUS_FILE.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                exp_set.add((row["Kette"], row["Ergebnis"]))
    return exp_set

def blacklist_faulty_chain(chain):
    # Gibt eine Menge von Zug-Ketten (als Strings) zurück, die als Blacklist fungieren
    return set(["|".join(chain)])

def analyze_causal_chain(games, loss_index):
    """
    Analysiert rückwärts ab loss_index die Kausalkette bis zum letzten Nicht-Verlust.
    Gibt die Kette als Liste von Zügen zurück.
    Systemisch: Kausalketten werden invariant für alle Mitglieder erfasst.
    """
    chain = []
    i = loss_index
    while i >= 0:
        history = games[i].get("history", [])
        result = games[i].get("result", "")
        chain = history + chain  # prepend history
        if result != "loss":
            break
        i -= 1
    return chain

# Optional: Initialisierung beim Start
if __name__ == "__main__":
    initialize_conscious_file()