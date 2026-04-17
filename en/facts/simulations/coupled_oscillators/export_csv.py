"""Export of resonance time points as CSV."""

from __future__ import annotations

import csv


def export_resonances(filename: str, resonance_history: list[float]) -> None:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Resonance Time'])
        for t_res in resonance_history:
            writer.writerow([t_res])
    print(f"Resonance events exported to {filename}")
