import csv
import os

DATA_DIR = os.path.join(".", "data")
CSV_PATH = os.path.join(DATA_DIR, "experience_weighted.csv")

def add_conscious_experience(chain, result, experience_set):
    """
    Fügt einen neuen Erfahrungseintrag oder erhöht dessen Gewichtung.
    - chain: Zugkette mit Farbmarkierung, z.B. "w:e4|b:e5"
    - result: "success", "failure" oder "draw"
    - experience_set: dict, wird als Frequenzspeicher aktualisiert
    """
    key = (chain, result)
    if key in experience_set:
        experience_set[key] += 1
    else:
        experience_set[key] = 1

def persist_experience_set(experience_set):
    """
    Persistiert den Erfahrungsspeicher in experience_weighted.csv.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(CSV_PATH, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["chain", "result", "count"])
        for (chain, result), count in experience_set.items():
            writer.writerow([chain, result, count])

def load_weighted_experience_set():
    """
    Lädt den gewichteten Erfahrungsspeicher (wenn vorhanden).
    """
    experience_set = {}
    if os.path.isfile(CSV_PATH):
        with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = (row["chain"], row["result"])
                experience_set[key] = int(row["count"])
    return experience_set