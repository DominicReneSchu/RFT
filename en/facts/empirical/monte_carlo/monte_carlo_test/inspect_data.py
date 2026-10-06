"""Quick inspection of the dielectron dataset."""

from __future__ import annotations

import pandas as pd
import numpy as np

df = pd.read_csv("dielectron.csv")
print(f"Columns: {list(df.columns)}")
print(f"\nNumber of rows: {len(df)}")
print(f"\nStatistics for column 'M':")
print(df["M"].describe())
print(f"\nPercentiles:")
for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
    print(f"  {p}%: {df['M'].quantile(p/100):.2f} GeV")
print(f"\nNaN values: {df['M'].isna().sum()}")
print(f"Values < 2 GeV: {(df['M'] < 2).sum()}")
print(f"Values 2-5 GeV: {((df['M'] >= 2) & (df['M'] < 5)).sum()}")
print(f"Values 5-20 GeV: {((df['M'] >= 5) & (df['M'] < 20)).sum()}")
print(f"Values 20-50 GeV: {((df['M'] >= 20) & (df['M'] < 50)).sum()}")
print(f"Values 50-100 GeV: {((df['M'] >= 50) & (df['M'] < 100)).sum()}")
print(f"Values > 100 GeV: {(df['M'] >= 100).sum()}")
