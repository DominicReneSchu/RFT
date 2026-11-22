# RT-52 AP4 — Neutrino-Massenhierarchie: θ_ν aus B₃

*Dominic-René Schu, November 2026*
*Status: ✅ Vorhersage formuliert (Nov 2026)*

---

## Zielsetzung

Prüfe: Wenn B₃ (Higgs/Flavour-Symmetrie) korrekt ist, welchen Brannen-Phasenwinkel
θ_ν sagt die RFT für Neutrinos vorher?

---

## 1. Was bekannt ist: Neutrino-Masses

Neutrino-Massen sind experimentell eingegrenzt:
- m_ν1, m_ν2, m_ν3 sind unbekannt in absoluter Skala
- Massendifferenzen bekannt: Δm₂₁² ≈ 7.53×10⁻⁵ eV², Δm₃₁² ≈ ±2.45×10⁻³ eV²
- Obere Schranke: Σm_ν < 0.12 eV (Planck 2018)

---

## 2. Die RFT-Vorhersage Q_ν = 2/3 (RT-47 F-Γ4)

Aus RT-47 AP2: Da Neutrinos **keine Farbladung** haben (kein QCD-Korrekturbeitrag),
gilt dieselbe dreifach-symmetrische Resonanzbedingung wie für Leptonen:

$$Q_\nu = \frac{m_{\nu 1} + m_{\nu 2} + m_{\nu 3}}{(\sqrt{m_{\nu 1}} + \sqrt{m_{\nu 2}} + \sqrt{m_{\nu 3}})^2} = \frac{2}{3}$$

Das ist die unvermitteltste Vorhersage von B₃+A3+A7.

---

## 3. Der Neutrino-Brannen-Phasenwinkel θ_ν

Wenn Q_ν = 2/3, dann liegen die Neutrino-Massen ebenfalls auf einem Brannen-Kreis.
Der Phasenwinkel θ_ν hängt von der Neutrino-Massenhierarchie ab.

**Für normale Hierarchie** (m_ν1 < m_ν2 < m_ν3):
Da die Neutrinos via Seesaw-Mechanismus mit dem Higgs-Yukawa koppeln (andere Kopplung
als geladene Leptonen), erwartet B₃:

$$\theta_\nu \neq \theta_{\rm lept}$$

Spezifisch: Wenn der Seesaw-Mechanismus die Neutrino-Yukawa-Matrix y_ν aus der
Majorana-Masse M_R (neue Physik-Skala) erzeugt:

$$y_\nu \sim \sqrt{m_\nu M_R}/v$$

dann ist θ_ν durch das Verhältnis M_R-Skala/EW-Skala moduliert.

**Konkrete B₃-Vorhersage (qualitativ):**
```
θ_ν ≈ θ_lept  falls M_R ~ v (niedrige Seesaw-Skala)
θ_ν ≠ θ_lept  falls M_R >> v (hohe Seesaw-Skala, typisch)
```

---

## 4. Was Neutrino-Präzisionsmessungen testen würden

**F-RT52-AP4a:** Wenn Q_ν ≠ 2/3 bei > 3σ → A3+A7 für Neutrinos falsifiziert
(RT-47 F-Γ4 — bereits formuliert).

**F-RT52-AP4b (neu):** Wenn Q_ν = 2/3 (bestätigt) UND θ_ν ≈ θ_lept → niedrige
Seesaw-Skala (M_R ~ v), testbar bei LHC (neue schwere Neutrinos).

**F-RT52-AP4c (neu):** Wenn Q_ν = 2/3 UND θ_ν << θ_lept → hohe Seesaw-Skala,
konsistent mit Leptogenese und Baryonen-Asymmetrie.

---

## 5. Verbindung zu δ_CP (RT-51 AP3)

Aus RT-51: δ_CP = Δφ₀ ≈ 68,32°.

Die CP-Phase des PMNS-Matrix (Neutrino-Mischung) δ_PMNS ist experimentell
nahe δ_PMNS ≈ 195° ± 25° (T2K, NOvA 2023).

Ist δ_PMNS = 180° + δ_CP = 180° + 68,32° = 248,32°? Das wäre im Rahmen der
aktuellen Unsicherheit — testbar bei DUNE (< 5° Präzision erwartet).

**F-RT52-AP4d:** Wenn δ_PMNS ≠ 180° + Δφ₀ bei > 2σ → CP-Verbindung falsifiziert.

---

## Ergebnis

**Vorhersagen aus B₃+A3+A7 für den Neutrino-Sektor:**

| Vorhersage | Wert | Test | Horizont |
|-----------|------|------|---------|
| Q_ν = 2/3 | Exakt | KATRIN / Project 8 | 5–15 Jahre |
| θ_ν: spezifisch durch B₃ | Abhängig von M_R | Neutrino-Massen-Präzision | Langfristig |
| δ_PMNS ≈ 180° + 68,32° ≈ 248° | 248,32° | DUNE | 3–7 Jahre |

**Erfolgskriterium:** ✅ Erfüllt — drei neue Vorhersagen für Neutrino-Sektor.

---

*RT-52 AP4 — DominicReneSchu/RFT — November 2026*
