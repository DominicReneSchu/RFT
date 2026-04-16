from __future__ import annotations

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SCRIPT_DIR, "publication_results", "publication_results.json"), 'r') as f:
    data = json.load(f)

# main_results Struktur
print("=== main_results['1.02'] ===")
print(json.dumps(data['main_results']['1.02'], indent=2, default=str)[:500])

print("\n=== systematik['0.3'] ===")
print(json.dumps(data['systematik']['0.3'], indent=2, default=str)[:500])

print("\n=== seed_variation['1.02'] ===")
print(json.dumps(data['seed_variation']['1.02'], indent=2, default=str)[:500])