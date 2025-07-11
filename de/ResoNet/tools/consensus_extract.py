"""
ResonanzNet Konsens-Extraktion – GPT-kompatible Zusammenfassung
Systemisch: Extrahiert, normalisiert und exportiert Meinungen für KI-gestützte Konsensfindung.
"""

import json
from pathlib import Path
from collections import Counter
from datetime import datetime

DATA_PATH = Path("../data/opinions.json")
EXPORT_PATH = Path("../data/consensus_export.json")

def load_opinions():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def extract_topics(opinions):
    return list(set(op["topic"] for op in opinions))

def group_by_topic(opinions):
    topics = {}
    for op in opinions:
        t = op["topic"]
        topics.setdefault(t, []).append(op)
    return topics

def export_for_gpt(grouped):
    export = []
    for topic, ops in grouped.items():
        export.append({
            "topic": topic,
            "opinions": [op["opinion"] for op in ops],
            "authors": [op["author"] for op in ops],
            "signatures": [op.get("signature", "") for op in ops],
            "count": len(ops)
        })
    return export

def main():
    opinions = load_opinions()
    grouped = group_by_topic(opinions)
    export = export_for_gpt(grouped)
    EXPORT_PATH.parent.mkdir(exist_ok=True)
    with open(EXPORT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "topics": export
        }, f, ensure_ascii=False, indent=2)
    print(f"Konsens-Export gespeichert unter {EXPORT_PATH}")

if __name__ == "__main__":
    main()