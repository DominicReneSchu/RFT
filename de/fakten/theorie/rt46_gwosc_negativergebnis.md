# RT-46 Zusatz — LIGO/GWOSC Versuch: Negativergebnis und Diagnose

*Dominic-René Schu, November 2026*

---

## Versuch: GWTC-3 SNR-Korrelation

Idee: Für 20 GW-Events aus GWTC-3 — testet ε_exp(Δφ) ≈ cos²(Δφ/2)?

**ε_exp** = 2ρ_H·ρ_L/(ρ_H²+ρ_L²) — SNR-Balance H1/L1
**Δφ** = 2πf_peak·Δt_HL — Phasendifferenz bei Peak-Frequenz

**Ergebnis:**

| Metrik | Wert |
|--------|------|
| χ²_red H1 (RFT) | 0,222 |
| χ²_red H0 (const) | 0,035 |
| H0 besser | ❌ H0 klar besser |
| Pearson r(ε_exp, cos²) | 0,276 (p=0,24, nicht signifikant) |

---

## Warum der Ansatz nicht funktioniert

**1. Selektionsbias:** Nur Events im Katalog, die BEIDE Detektoren triggern.
ε_exp ≈ 0,85 ± 0,19 für alle Events — kein dynamischer Bereich für cos²-Test.
12/20 Events haben ε_exp > 0,9.

**2. Definitions-Mismatch:**
ε_exp = 2ρ_Hρ_L/(ρ_H²+ρ_L²) misst SNR-Balance (wie symmetrisch das Event detektiert wird)
— **nicht** die physikalische Kopplung zwischen zwei Resonatoren im RFT-Sinn.

**3. Phasen-Mismatch:**
Δφ = 2πf·Δt ist die Signal-Propagationsphase (Laufzeitphase).
Die RFT Δφ ist die **Schwingungsphasendifferenz** der Resonatoren — anderes Konzept.

---

## Was tatsächlich funktionieren würde

**Stochastischer GW-Hintergrund — Overlap Reduction Function Γ(f):**

```
Γ(f) ∝ ∫ dΩ [F+_H(Ω)·F+_L(Ω) + F×_H(Ω)·F×_L(Ω)] · e^{2πif·Δt(Ω)}
```

Diese Funktion beschreibt, wie gut H1 und L1 als Paar korrelieren:
- f → 0: Γ(0) = 1 (volle Kopplung)
- f → ∞: Γ → 0 (ε → 0 bei vielen Phasenzyklen)
- Erster Nulldurchgang: f ≈ c/(2d) ≈ 50 Hz (H1-L1-Basislinie)

Die Hüllkurve von Γ(f) hat strukturell cos²-Charakter — das ist
die korrekte LIGO-Realisierung der RFT-Kopplungseffizienz.

**Benötigt:** Download der LIGO-Strain-Daten (~4 GB) von gwosc.org

---

## Ehrlicher Abschluss

> Das LIGO-Experiment ist **konzeptionell richtig**, aber der Versuch mit
> GWTC-3-Katalogdaten scheitert an Selektionsbias und Definitions-Mismatches.
>
> Ein echter Test erfordert die rohen Strain-Daten und die Berechnung von Γ(f).
> Das ist **RT-58** (neue Aufgabe): Stochastische GW-Hintergrund-Suche als RFT-Test.

---

*RT-46 Zusatz — DominicReneSchu/RFT — November 2026*
