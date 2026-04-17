from __future__ import annotations

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SCRIPT_DIR, "publication_results", "publication_results.json"), 'r') as f:
    data = json.load(f)
print("Top-level keys:", list(data.keys()))
for key in data.keys():
    val = data[key]
    if isinstance(val, dict):
        print(f"  {key}: dict with keys {list(val.keys())[:10]}")
    elif isinstance(val, list):
        print(f"  {key}: list with {len(val)} entries")
        if val and isinstance(val[0], dict):
            print(f"    First entry keys: {list(val[0].keys())}")
    else:
        print(f"  {key}: {type(val).__name__} = {str(val)[:100]}")
