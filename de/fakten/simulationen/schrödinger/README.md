
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

---

## FFT-Normierungskonventionen und k-Gitter

### Warum ist Skalierung nötig?

`numpy.fft.fft` liefert *unskalierte* diskrete Fourier-Koeffizienten:

```
FFT(ψ)[k] = Σ_{n=0}^{N-1}  ψ[n] · exp(-2πi·k·n/N)
```

Für physikalische Erwartungswerte im Impulsraum brauchen wir eine *kontinuierlich normierte* Wellenfunktion ψ̃(k), die Parseval's Gleichung im diskreten Sinne erfüllt:

```
Σ |ψ̃(k)|² · dk  ≈  Σ |ψ(x)|² · dx  =  1
```

Die nötige Skalierung ergibt sich aus den numpy-Konventionen (Gitterpunkte N, Gitterabstand dx, Gitterlänge L = N·dx):

```
ψ̃(k) = (dx / √(2π)) · FFT(ψ)
```

Diese Skalierung stellt sicher, dass `Σ |ψ̃(k)|² · dk = 1`, wenn `Σ |ψ(x)|² · dx = 1`.
**Ohne diese Skalierung** wäre `<p>` um einen Faktor `~N·dx/√(2π)` verfälscht
(z. B. `~658` statt `~1` für k0=1 bei typischen Gitterparametern).

### Das k-Gitter (dk und k-Gitterpunkte)

Das k-Gitter wird durch die FFT-Konvention festgelegt:

```python
dk = 2π / L          # Abstand zwischen k-Punkten im Fourierraum
k  = 2π · np.fft.fftfreq(N, d=dx)   # k-Werte in physikalischen Einheiten
```

- `dk = 2π/L` ist die **Frequenzauflösung** im k-Raum; sie bestimmt die Genauigkeit der Impulserwartungswerte.
- `k` enthält positive und negative k-Werte (gemäß FFT-Reihenfolge: positive zuerst, dann negative).
- `np.fft.fftshift` kann benutzt werden, um die Reihenfolge zu zentrieren (für Plots).

### Zweifache Kontrolle von `<p>`

Das Skript berechnet `<p>` auf zwei unabhängigen Wegen:

1. **k-Raum** (`expectation_p_from_k`):
   ```
   <p> = Σ ħk · |ψ̃(k)|² · dk
   ```

2. **x-Raum via Ableitungsoperator** (`expectation_p_from_x`):
   ```
   <p> = Re( Σ ψ*(x) · (-iħ ∂_x ψ(x)) · dx )
   ```
   Die Ableitung wird spektral exakt über FFT berechnet: `∂_x ψ = IFFT(ik · FFT(ψ))`.
   Dies setzt periodische Randbedingungen voraus (korrekt für FFT). Für ein gut lokalisiertes Wellenpaket, das den Rand nicht erreicht, stimmen beide Methoden überein.

Beide Methoden sollten für das freie Gauß-Wellenpaket exakt `<p> ≈ ħ·k0` liefern und über die gesamte Simulation konstant bleiben.
