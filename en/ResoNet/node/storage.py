import json
from pathlib import Path

DATA_PATH = Path("../data/opinions.json")

def load_opinions():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_opinions(opinions):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(opinions, f, ensure_ascii=False, indent=2)