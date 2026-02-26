"""
Erfahrungsspeicher V9.4 mit hierarchischem Coarse-Speicher,
vollständiger Thread-Safety und Multi-Source-Merge.

Architektur:
  - Offline-Training schreibt nach: trade_experience_offline.csv
  - Live-Trading schreibt nach:     trade_experience_live.csv
  - Merge erzeugt:                  trade_experience_weighted.csv
  - Policy liest immer:             trade_experience_weighted.csv
  - Coarse-Speicher:                trade_experience_coarse.csv
"""
import csv
from pathlib import Path
from threading import Lock
from typing import Dict, Tuple, Optional

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Hauptspeicher — Policy liest hieraus
EXPERIENCE_CSV = DATA_DIR / "trade_experience_weighted.csv"

# Getrennte Speicher für parallelen Betrieb
EXPERIENCE_OFFLINE_CSV = DATA_DIR / "trade_experience_offline.csv"
EXPERIENCE_LIVE_CSV = DATA_DIR / "trade_experience_live.csv"

# Coarse-Speicher für hierarchische Erfahrung
EXPERIENCE_COARSE_CSV = DATA_DIR / "trade_experience_coarse.csv"

_lock = Lock()


def load_experience(path: Optional[Path] = None) -> dict:
    target = path or EXPERIENCE_CSV
    exp: Dict[Tuple[str, str], int] = {}
    with _lock:
        if not target.exists():
            return exp
        try:
            with target.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = (row["chain"], row["result"])
                    exp[key] = int(row["count"])
        except Exception as e:
            print(f"[Experience] Warnung beim Laden von {target.name}: {e}")
    return exp


def persist_experience(exp: dict, path: Optional[Path] = None):
    target = path or EXPERIENCE_CSV
    with _lock:
        DATA_DIR.mkdir(exist_ok=True)
        tmp_path = target.with_suffix(".tmp")
        try:
            with tmp_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["chain", "result", "count"])
                for (chain, result), count in exp.items():
                    writer.writerow([chain, result, count])
            tmp_path.replace(target)
        except Exception as e:
            print(f"[Experience] Fehler beim Speichern nach {target.name}: {e}")
            if tmp_path.exists():
                tmp_path.unlink()


def add_experience(chain: str, result: str, exp: dict):
    key = (chain, result)
    with _lock:
        exp[key] = exp.get(key, 0) + 1


def decay_experience(exp: dict, decay_factor: float = 0.98, min_threshold: int = 1):
    with _lock:
        to_delete = []
        for key, count in list(exp.items()):
            new_count = int(count * decay_factor)
            if new_count < min_threshold:
                to_delete.append(key)
            else:
                exp[key] = new_count
        for key in to_delete:
            del exp[key]


# ===== Coarse-Speicher =====

def load_experience_coarse(path: Optional[Path] = None) -> dict:
    return load_experience(path=path or EXPERIENCE_COARSE_CSV)


def persist_experience_coarse(exp: dict, path: Optional[Path] = None):
    persist_experience(exp, path=path or EXPERIENCE_COARSE_CSV)


# ===== Multi-Source Merge =====

def merge_experience(
    live_weight: float = 0.8,
    offline_weight: float = 1.0,
    output_path: Optional[Path] = None,
) -> dict:
    """
    V9.4: Merge Offline + Live → Weighted.

    Gewichtung korrigiert: Offline ≥ Live, weil Live-Feedback
    durch 1-Perioden-Bewertung rausch-dominiert ist.
    Live-Erfahrung fließt ein, aber dominiert nicht.
    """
    target = output_path or EXPERIENCE_CSV

    offline_exp = load_experience(EXPERIENCE_OFFLINE_CSV)
    live_exp = load_experience(EXPERIENCE_LIVE_CSV)

    print(f"[Merge] Offline: {len(offline_exp)} Einträge (Gewicht {offline_weight}x), "
          f"Live: {len(live_exp)} Einträge (Gewicht {live_weight}x)")

    merged: Dict[Tuple[str, str], int] = {}

    for key, count in offline_exp.items():
        weighted = max(1, int(count * offline_weight))
        merged[key] = merged.get(key, 0) + weighted

    for key, count in live_exp.items():
        weighted = max(1, int(count * live_weight))
        merged[key] = merged.get(key, 0) + weighted

    persist_experience(merged, path=target)

    total_entries = len(merged)
    total_counts = sum(merged.values())
    print(f"[Merge] Ergebnis: {total_entries} Einträge, "
          f"{total_counts} Gesamtzähler → {target.name}")

    return merged


def merge_status():
    for name, path in [
        ("Offline", EXPERIENCE_OFFLINE_CSV),
        ("Live", EXPERIENCE_LIVE_CSV),
        ("Merged", EXPERIENCE_CSV),
        ("Coarse", EXPERIENCE_COARSE_CSV),
    ]:
        if path.exists():
            exp = load_experience(path)
            total_counts = sum(exp.values())
            success = sum(v for (_, r), v in exp.items() if r == "success")
            failure = sum(v for (_, r), v in exp.items() if r == "failure")
            draw = sum(v for (_, r), v in exp.items() if r == "draw")
            print(f"  {name:8s}: {len(exp):6d} Einträge, "
                  f"{total_counts:8d} Zähler "
                  f"(S:{success} F:{failure} D:{draw})")
        else:
            print(f"  {name:8s}: — nicht vorhanden —")