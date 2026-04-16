
### Schrödinger-Referenz (1D)

Dieses Repo enthält eine numerische Referenz-Implementierung der 1D Schrödinger-Gleichung, um spätere Resonanz-/Phasen-Gittermodelle dagegen zu testen.

Ausführen:

```bash
python python/schrodinger_1d_reference.py --plot
```

Parameterbeispiel:

```bash
python python/schrodinger_1d_reference.py --V harmonic --Vstrength 0.01 --steps 3000 --dt 0.01 --plot
```

Smoke-Kriterium: Normabweichung bleibt klein (unitäre Split-Operator-Evolution).
