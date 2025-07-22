import os
import csv
import re
import matplotlib.pyplot as plt
import numpy as np
from glob import glob

SNAPSHOT_DIR = "./snapshots"
OUTPUT_CSV = "learning_progress.csv"
OUTPUT_PNG = "learning_curve.png"
SNAPSHOT_PATTERN = re.compile(r"experience_weighted_(\d{4})\.csv")
# Für legacy/alternative Namensschemata:
ALT_SNAPSHOT_PATTERN = re.compile(r"experience_snapshot_(\d{5})\.csv")

# Setze hier das gewünschte Qualitätsmaß – Spaltenname im CSV
QUALITY_FIELDS = ["move_quality_score", "score", "reward", "weight"]  # Fallback-Liste

def find_quality_field(header):
    for field in QUALITY_FIELDS:
        if field in header:
            return field
    return None

def get_snapshots_sorted():
    # Alle passenden Files finden (verschiedene Formate akzeptieren)
    files = []
    for pattern in [SNAPSHOT_PATTERN, ALT_SNAPSHOT_PATTERN]:
        for f in os.listdir(SNAPSHOT_DIR):
            m = pattern.match(f)
            if m:
                files.append((int(m.group(1)), os.path.join(SNAPSHOT_DIR, f)))
    files.sort()
    return files

def evaluate_snapshots():
    if not os.path.isdir(SNAPSHOT_DIR):
        print(f"Snapshot-Verzeichnis '{SNAPSHOT_DIR}' nicht gefunden.")
        return

    snapshots = get_snapshots_sorted()
    if not snapshots:
        print("Keine Snapshot-Dateien gefunden.")
        return

    results = []

    for snap_num, snap_path in snapshots:
        try:
            with open(snap_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if not rows:
                    print(f"[Warnung] Snapshot {snap_path} ist leer – übersprungen.")
                    continue
                header = reader.fieldnames
                quality_field = find_quality_field(header)
                if not quality_field:
                    print(f"[Warnung] Keine Qualitäts-Spalte in {snap_path} gefunden – übersprungen.")
                    continue
                # Extrahiere Qualitätswerte (nur numerische, ggf. filtern)
                values = []
                for row in rows:
                    try:
                        val = float(row[quality_field])
                        values.append(val)
                    except (ValueError, KeyError, TypeError):
                        continue
                if not values:
                    print(f"[Warnung] Keine gültigen Qualitätswerte in {snap_path} – übersprungen.")
                    continue
                mean = np.mean(values)
                std = np.std(values)
                n = len(values)
                # Spielanzahl schätzen: SNAPSHOT_INTERVAL * SnapNum (konservativ)
                total_games = snap_num * 100
                results.append({
                    "snapshot_num": snap_num,
                    "filename": os.path.basename(snap_path),
                    "games_total": total_games,
                    "mean_quality": mean,
                    "std_quality": std,
                    "n": n
                })
        except Exception as e:
            print(f"[Fehler] Snapshot {snap_path} konnte nicht gelesen werden: {e}")

    if not results:
        print("Keine auswertbaren Snapshots gefunden.")
        return

    # Ergebnisse als CSV speichern
    with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["snapshot_num", "filename", "games_total", "mean_quality", "std_quality", "n"])
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    print(f"[OK] Aggregierte Metriken gespeichert in '{OUTPUT_CSV}'.")

    # Lernkurve plotten
    xs = [r["games_total"] for r in results]
    ys = [r["mean_quality"] for r in results]
    yerr = [r["std_quality"] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(xs, ys, marker="o", label="∅ Move-Qualität")
    plt.fill_between(xs, np.array(ys)-np.array(yerr), np.array(ys)+np.array(yerr), color="#cce6ff", alpha=0.5, label="Std-Abweichung")
    # Optional: Glättung
    if len(ys) >= 5:
        from scipy.ndimage import uniform_filter1d
        ys_smooth = uniform_filter1d(ys, size=3)
        plt.plot(xs, ys_smooth, "--", color="orange", label="Gleitender Mittelwert")

    plt.title("Lernfortschritt der Resonanz-KI")
    plt.xlabel("Spiele gesamt")
    plt.ylabel("∅ Move-Qualität")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig(OUTPUT_PNG)
    print(f"[OK] Lernkurve gespeichert als '{OUTPUT_PNG}'.")

if __name__ == "__main__":
    evaluate_snapshots()