"""Export von Resonanzzeitpunkten als CSV."""

from __future__ import annotations

import csv


def export_resonances(filename: str, resonance_history: list[float]) -> None:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Resonanzzeitpunkt'])
        for t_res in resonance_history:
            writer.writerow([t_res])
    print(f"Resonanzereignisse exportiert nach {filename}")