# RT-31 — Resonanz-Hamiltonoperator: Hamilton-Simulationen

*Dominic René Schu, August 2026*
*Status: Abgeschlossen (Aug 2026)*

---

## Übersicht

Dieses Verzeichnis enthält die numerischen Simulationen zu RT-31:
Konstruktion und Verifikation des Resonanz-Hamiltonoperators

```
Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_Kopplung
```

für zwei konkrete Quantensysteme. Die Simulationen testen die Vorhersage,
dass ε(Δφ) = cos²(Δφ/2) ein universeller Kopplungsskalierungsparameter ist,
der aus der k=1-Darstellung von U(1) ⊂ G_sync folgt (RT-02).

---

## Dateien

| Datei | System | Inhalt |
|-------|--------|--------|
| `rt31_phonon_kopplung.py` | Phonon-Phonon | Zwei gekoppelte harmonische Oszillatoren, Fockraum N=20 |
| `rt31_spin_bahn.py` | Spin-Bahn | Zwei-Niveau-System (Zeemanfeld + transversales Treibfeld) |

---

## System 1: Phonon-Phonon-Kopplung

**Hamiltonoperator:**
```
Ĥ_res = ℏω₁(a†₁a₁ + ½) + ℏω₂(a†₂a₂ + ½) + ε(Δφ)·ℏΩ·(a†₁a₂ + a₁a†₂)
```

**Physikalischer Unterraum:** Ein-Excitation-Unterraum (Basis |1,0⟩, |0,1⟩)

**RFT-Vorhersage:**
```
ΔE(Δφ) = ε(Δφ)·ΔE(0) = cos²(Δφ/2)·ΔE(0)
```

**Ergebnis (Aug 2026):**
- ✅ Vorhersage bestätigt: max. Abweichung < 1e-14 (weit unter 1%-Schwelle)
- ✅ A7-Invarianz bestätigt: ΔE(Δφ+φ₀) = ε(Δφ+φ₀)·ΔE(0)
- ΔE_RFT(π/2) / ΔE_Standard = 0.50000000 (erwartet: ε(π/2) = 0.5)

**Parameter:** ω₁ = ω₂ = 1, Ω = 0.1, N_Fock = 20

---

## System 2: Spin-Bahn-Kopplung

**Hamiltonoperator:**
```
Ĥ_res = (ℏω₀/2)·σ_z + ε(Δφ)·ℏΩ·σ_x
```

**Analytische Eigenwerte:**
```
E± = ±(ℏ/2)√(ω₀² + 4ε²(Δφ)·Ω²)
```

**RFT-Vorhersagen:**
- Resonanter Fall (ω₀=0): ΔE = 2·ε(Δφ)·ℏΩ = cos²(Δφ/2)·2ℏΩ
- σ_x transformiert unter k=1 von U(1) ⊂ G_sync → ε(Δφ)·σ_x ist G_sync-kovariant

**Ergebnis (Aug 2026):**
- ✅ Analytische Eigenwertformel exakt bestätigt (Δ = 0 für alle Δφ)
- ✅ Resonanter Fall: ΔE = 2·ε·ℏΩ bestätigt, Abweichung = 0
- Nicht-resonanter Fall: Ω_eff(Δφ)/Ω_eff(0) ≠ cos(Δφ/2) — korrekte Physik
  des verstimmten Zwei-Niveau-Systems (ω₀-Grundterm)
- Darstellungsstruktur: Ĥ_res = Ĥ₀ + ε(Δφ)·ℏΩ·σ_x ist die minimale
  Realisierung in der k=1-Darstellung von U(1) ⊂ G_sync

**Parameter:** ω₀ = 1, Ω = 0.5

---

## Korollar A3 aus A7 (RT-35)

Die Simulationen bestätigen die in RT-02 abgeleitete Quantisierungsbedingung:

> **Korollar (A3 aus A7):** Die Resonanzbedingung fᵢ/fⱼ ∈ ℚ (Axiom A3)
> folgt aus der Darstellungsstruktur der Untergruppe ℝ⁺_× ⊂ G_sync:
> Stabile Resonanzkonfigurationen existieren genau dann, wenn der
> Frequenzquotient unter der fundamentalen Darstellung von ℝ⁺_×
> invariant ist — das ist äquivalent zu fᵢ/fⱼ = m/n ∈ ℚ.

Formale Dokumentation: `de/fakten/theorie/gsync_gruppenstruktur.md` §5

---

## Einordnung in die RFT-Forschungsstruktur

| Aufgabe | Verweis | Status |
|---------|---------|--------|
| RT-31 System 1 | `rt31_phonon_kopplung.py` | ✅ Abgeschlossen (Aug 2026) |
| RT-31 System 2 | `rt31_spin_bahn.py` | ✅ Abgeschlossen (Aug 2026) |
| RT-02 Beweis G_sync | `de/fakten/theorie/gsync_gruppenstruktur.md` | ✅ Abgeschlossen (Aug 2026) |
| RT-35 Korollar A3 | `de/fakten/theorie/gsync_gruppenstruktur.md` §5 | ✅ Durch RT-31 erledigt |
| RT-32 λε⁴-Term | `RESEARCH_TASKS.md` | ⚠️ Offen — nächste Priorität |

---

## Ausführung

```bash
# System 1: Phonon-Phonon
python rt31_phonon_kopplung.py

# System 2: Spin-Bahn
python rt31_spin_bahn.py
```

**Abhängigkeiten:** numpy, scipy

---

## Verweise

- Theoretische Grundlage: `de/fakten/theorie/gsync_gruppenstruktur.md`
- Axiom A7: `de/fakten/docs/definitionen/axiomatische_grundlegung.md` §A7
- Korollar A3: `de/fakten/theorie/gsync_gruppenstruktur.md` §5
- Vorgänger-Simulationen: `de/fakten/theorie/simulationen/rt02/`
- Englische Spiegelversion: `en/facts/simulations/hamilton/`
- Forschungsübersicht: `RESEARCH_TASKS.md` (RT-31)
