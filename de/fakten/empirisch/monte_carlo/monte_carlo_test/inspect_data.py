"""Schnelle Inspektion des Dielectron-Datensatzes."""

from __future__ import annotations

import pandas as pd
import numpy as np

df = pd.read_csv("dielectron.csv")
print(f"Spalten: {list(df.columns)}")
print(f"\nAnzahl Zeilen: {len(df)}")
print(f"\nStatistik der Spalte 'M':")
print(df["M"].describe())
print(f"\nPerzentile:")
for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
    print(f"  {p}%: {df['M'].quantile(p/100):.2f} GeV")
print(f"\nNaN-Werte: {df['M'].isna().sum()}")
print(f"Werte < 2 GeV: {(df['M'] < 2).sum()}")
print(f"Werte 2-5 GeV: {((df['M'] >= 2) & (df['M'] < 5)).sum()}")
print(f"Werte 5-20 GeV: {((df['M'] >= 5) & (df['M'] < 20)).sum()}")
print(f"Werte 20-50 GeV: {((df['M'] >= 20) & (df['M'] < 50)).sum()}")
print(f"Werte 50-100 GeV: {((df['M'] >= 50) & (df['M'] < 100)).sum()}")
print(f"Werte > 100 GeV: {(df['M'] >= 100).sum()}")