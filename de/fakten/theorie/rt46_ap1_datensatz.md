# RT-46 AP1 — Datensatz-Identifikation und Beschaffung

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zieldatensatz

**MultiArm-Pendulum Dataset (Zenodo):**
- DOI: `10.5281/zenodo.6633719`
- URL: `https://zenodo.org/records/6633719`
- Inhalt: Hochaufgelöste Encoder-Daten eines Doppelpendels (θ₁(t), θ₂(t))
- Sampling-Rate: typisch 100–500 Hz
- Format: CSV-Dateien pro Experiment

**Download-Befehl:**
```bash
curl -L "https://zenodo.org/records/6633719/files/double_pendulum_data.zip" -o data.zip
unzip data.zip -d RT46_data/
```

---

## 2. Relevante Observablen für RFT-Test

Aus den Rohdaten (θ₁(t), θ₂(t)) werden abgeleitet:

| Observable | Formel | RFT-Relevanz |
|-----------|--------|--------------|
| Phasendifferenz | Δφ(t) = θ₁(t) − θ₂(t) | Einganggröße von ε |
| RFT-Vorhersage | ε_RFT(Δφ) = cos²(Δφ/2) | Zu testende Hypothese H1 |
| Empirische Kopplung | ε_exp(t) = E_koppl(t)/E_total(t) | Zu messende Größe |
| PCI | PCI(t) = |⟨e^{iΔφ}⟩| ∈ [0,1] | Kohärenzmaß |

---

## 3. Pre-Registrierung der Hypothesen

**H0 (Null):** Das Doppelpendel folgt reiner Lagrange-Dynamik (A=0).
Keine ε(Δφ)-Abhängigkeit der Kopplungsenergie.

**H1 (RFT):** ε_exp(Δφ) = cos²(Δφ/2) — die Kopplungseffizienz folgt dem RFT-Muster.

**Falsifikationskriterium:**
Wenn Likelihood-Ratio-Test H1 vs H0: p_korr < 0,05 → H1 abgelehnt.
Wenn χ²_red(H1) < χ²_red(H0) → H1 besser angepasst → konsistent mit RFT.

---

*RT-46 AP1 — DominicReneSchu/RFT — November 2026*
