# Experimenteller Vorschlag — Falsifizierbare RFT-Vorhersage

> **Kritikpunkt 3.1 (SI-Einheiten / Kalibrierung):** Dimensionslose
> Simulationsparameter (λ, V_strength) auf SI-Einheiten abbilden und
> eine konkrete, falsifizierbare Vorhersage formulieren.

---

## 1. Ausgangslage: Störungstheorie-Ergebnis

Die Störungsanalyse (`schrodinger_1d_rft_perturbation.py`) hat für
die dynamische RFT mit dem density-Rückkopplungsmodell
$\dot{\Delta\varphi} = \lambda \int |\psi|^4\,\mathrm{d}x$
folgende Skalierungsgesetze numerisch und analytisch verifiziert:

| Observable | Exponent (numerisch) | Exponent (Theorie) | Abweichung |
|------------|---------------------:|-------------------:|-----------:|
| $1 - F$ (Fidelity) | 2.001 | 2 | 0.05 % |
| $|\Delta\langle x\rangle|$ | 1.001 | 1 | 0.1 % |
| $|\Delta\langle p\rangle|$ | 1.001 | 1 | 0.1 % |
| $\max|\Delta\psi|$ | 0.999 | 1 | 0.1 % |

Die analytische Vorhersage 1. Ordnung stimmt mit der Numerik bis auf
einen relativen Fehler von $1.3 \times 10^{-4}$ überein.

**Zentrale numerische Ergebnisse (Präfaktoren):**

$$
|\Delta\langle x\rangle| \approx 4.9 \cdot \lambda, \quad
|\Delta\langle p\rangle| \approx 3.2 \cdot \lambda, \quad
1 - F \approx 138 \cdot \lambda^2
$$

Dass $1 - F \sim \lambda^2$ folgt direkt daraus, dass die Fidelity

$$
|\langle\psi_0|\psi_0 + \lambda\psi_1\rangle|^2
= 1 - \lambda^2\,\|\psi_1\|^2 + \mathcal{O}(\lambda^3)
$$

ist. Die Numerik bestätigt die Störungstheorie auf 4 Dezimalen.

---

## 2. SI-Kalibrierung

### 2.1 Physikalisches System

**Ultrakalte ⁸⁷Rb-Atome in einer harmonischen Falle** — das
experimentelle Standardsystem für Präzisions-QM weltweit:

| Parameter | Symbol | Wert |
|-----------|--------|-----:|
| Atommasse | $m$ | 86.909 u = $1.443 \times 10^{-25}$ kg |
| Fallenfrequenz | $\omega$ | $2\pi \times 100\;\mathrm{Hz}$ (einstellbar) |
| Planck-Konstante | $\hbar$ | $1.055 \times 10^{-34}\;\mathrm{J\cdot s}$ |

### 2.2 Skalenabbildung

Die dimensionslose Simulation ($\hbar = m = 1$) wird über drei
Konversionsgrößen auf SI abgebildet:

| Größe | Formel | Wert ($\omega = 2\pi \times 100\;\mathrm{Hz}$) |
|-------|--------|-------:|
| Oszillatorlänge | $a_\mathrm{ho} = \sqrt{\hbar/(m\omega)}$ | $1.08\;\mu\mathrm{m}$ |
| Längeneinheit | $\ell = V_\mathrm{strength}^{1/4} \cdot a_\mathrm{ho}$ | $0.41\;\mu\mathrm{m}$ |
| Zeiteinheit | $\tau = \sqrt{V_\mathrm{strength}} / \omega$ | $0.225\;\mathrm{ms}$ |
| Energieeinheit | $E = \hbar / \tau$ | $2.92 \times 10^{-12}\;\mathrm{eV}$ |
| Impulseinheit | $p = \hbar / \ell$ | $2.60 \times 10^{-28}\;\mathrm{kg\cdot m/s}$ |
| Simulationszeit | $T = 20\,\tau$ | $4.5\;\mathrm{ms}$ |

Die Konsistenz wird durch 6 unabhängige Relationen verifiziert
(z. B. $\hbar = m\,\ell^2/\tau$, $E\cdot\tau = \hbar$).

### 2.3 Herleitung

Die dimensionslose Schrödinger-Gleichung mit $\hbar = m = 1$:

$$
i\,\partial_{\tilde{t}}\,\psi = -\tfrac{1}{2}\,\partial_{\tilde{x}}^2\,\psi
+ V(\tilde{x})\,\psi
$$

wird über $x = \ell\,\tilde{x}$, $t = \tau\,\tilde{t}$ auf SI abgebildet.
Das harmonische Kopplungspotential
$V(\tilde{x}) = \tfrac{1}{2}\,V_\mathrm{strength}\,\tilde{x}^2$
wird identifiziert mit $V_\mathrm{phys}(x) = \tfrac{1}{2}\,m\,\omega^2\,x^2$:

$$
V_\mathrm{strength} = \frac{m^2\,\omega^2\,\ell^4}{\hbar^2}
\quad\Longrightarrow\quad
\ell = V_\mathrm{strength}^{1/4} \cdot \sqrt{\frac{\hbar}{m\,\omega}}
$$

---

## 3. Falsifizierbare Vorhersage

### 3.1 Positionsverschiebung

$$
\boxed{|\Delta\langle x\rangle|_\mathrm{SI}
= C_x \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}}
$$

wobei $C_x \approx 4.9$ der numerisch bestimmte Präfaktor ist
und $\ell \approx 0.41\;\mu\mathrm{m}$ für $\omega = 2\pi \times 100\;\mathrm{Hz}$.

### 3.2 Vorhersagetabelle

| $\lambda$ | $|\Delta\langle x\rangle|$ [µm] | $1 - F$ | Detektierbar? |
|----------:|------:|-------:|:---:|
| 0.001 | 0.002 | $1.4 \times 10^{-4}$ | Nein (Einzelschuss) |
| 0.01 | 0.020 | 0.014 | Ja (10 000 Schuss) |
| 0.05 | 0.099 | 0.345 | Ja (100 Schuss) |
| 0.1 | 0.199 | 1.38 | Ja (100 Schuss) |
| 0.5 | 0.994 | 34.5 | Ja (Einzelschuss) |
| 1.0 | 1.987 | 138 | Ja (Einzelschuss) |

### 3.3 Frequenzabhängigkeit

Niedrigere Fallenfrequenz = größeres $a_\mathrm{ho}$ = bessere Sensitivität:

| $\omega / 2\pi$ [Hz] | $a_\mathrm{ho}$ [µm] | $\ell$ [µm] | $\lambda_\mathrm{min}$ (100 Schuss) |
|------:|------:|------:|------:|
| 10 | 3.41 | 1.28 | 0.016 |
| 50 | 1.53 | 0.57 | 0.036 |
| 100 | 1.08 | 0.41 | 0.050 |
| 500 | 0.48 | 0.18 | 0.113 |
| 1000 | 0.34 | 0.13 | 0.159 |

**Optimaler Bereich:** $\omega \lesssim 2\pi \times 50\;\mathrm{Hz}$
(aber längere Präparationszeit).

---

## 4. Experimentelles Protokoll

### 4.1 Vorbereitung

1. **BEC-Präparation:** ⁸⁷Rb-Kondensat in magnetischer oder optischer Falle,
   $T < 200\;\mathrm{nK}$, $N \sim 10^5$ Atome.

2. **Harmonische Falle:** Einstellbar auf $\omega = 2\pi \times (10{-}500)\;\mathrm{Hz}$.
   Axiale Frequenz bestimmt $a_\mathrm{ho}$ und damit die Sensitivität.

3. **Wellenpaket-Initialisierung:** Impuls-Kick über Bragg-Puls
   oder Raman-Übergang: $\hbar k_0 = \hbar / \ell$.

### 4.2 Messung

4. **Propagation:** Wellenpaket in der Falle propagieren lassen
   für $t \approx 4.5\;\mathrm{ms}$ (bei $\omega = 2\pi \times 100\;\mathrm{Hz}$).

5. **Absorptionsbildgebung:** Falle abschalten, Time-of-Flight,
   Absorptionsbild aufnehmen. Räumliche Auflösung: $\sim 1\;\mu\mathrm{m}$.

6. **Wiederholung:** $N = 100{-}10\,000$ identische Durchläufe.

### 4.3 Auswertung

7. **Statistik:** Mittlere Position $\langle x\rangle_\mathrm{exp}$
   aus $N$ Messungen. Standardfehler:
   $\sigma_{\Delta x} = \sigma_\mathrm{single} / \sqrt{N}$.

8. **Vergleich mit Theorie:**
   - **Nullhypothese** $H_0$: $\Delta\langle x\rangle = 0$ (Standard-QM, $\lambda = 0$)
   - **Alternativhypothese** $H_1$: $|\Delta\langle x\rangle| = C_x \cdot \lambda \cdot \ell > 0$ (RFT)

9. **Ergebnis:**
   - $|\Delta\langle x\rangle| > 2\sigma$: RFT-Effekt nachgewiesen → $\lambda$ bestimmt
   - $|\Delta\langle x\rangle| \leq 2\sigma$: Obere Schranke $\lambda_\mathrm{max}$

---

## 5. Messmethode: Absorptionsbildgebung

### Prinzip

Ein resonanter Laserstrahl wird durch die Atomwolke geschickt.
Die Absorption ist proportional zur Säulendichte
$n_\mathrm{col}(x, y) = \int |\psi(x, y, z)|^2\,\mathrm{d}z$.

Aus dem Absorptionsprofil wird $\langle x\rangle$ bestimmt.

### Auflösung

| Methode | Räumliche Auflösung |
|---------|-------------------:|
| Standard-Absorption | ~ 1 µm |
| Hochauflösendes Objektiv | ~ 0.3 µm |
| Fluoreszenz-Detektion | ~ 0.5 µm |
| Quantengasenmikroskop | ~ 0.5 µm (Einzelatom) |

Für $N = 100$ Wiederholungen: $\sigma_\mathrm{eff} = 1\;\mu\mathrm{m} / \sqrt{100} = 0.1\;\mu\mathrm{m}$.

---

## 6. Bilanz gegenüber der Peer-Review

| Gutachter-Kritikpunkt | Status |
|-----------------------|--------|
| 1.2 Spezifikation $\varepsilon(\Delta\varphi)$ | ✅ $\cos^2(\Delta\varphi/2)$, analytisch, invertierbar |
| Schrödinger aus Axiom 4 ableiten | ✅ Vier Stufen, numerisch verifiziert |
| QM eines einzelnen Teilchens | ✅ Vollständig |
| Korrespondenzprinzip | ✅ Statisch + dynamisch ($\lambda \to 0$) |
| Störungstheorie | ✅ Skalierung exakt, analytisch verifiziert |
| **3.1 SI-Einheiten / Kalibrierung** | ✅ **Hier adressiert** |
| 1.1 Lagrange-Dichte / Wirkungsprinzip | ⚠️ Motiviert, nicht abgeleitet |
| 2.1 ART-Grenzwert | ❌ Offen (bewusst abgegrenzt) |
| 2.2 Eichinvarianz / U(1) | ❌ Offen |
| Gisin-Theorem / No-Signaling | ⚠️ 1-Teilchen adressiert, Mehrteilchen offen |

---

## 7. Empfohlener nächster Schritt

Das Simulationspaket ist mit diesem experimentellen Vorschlag für den
1-Teilchen-Sektor **abgeschlossen und falsifizierbar**. Der logische
nächste Punkt wäre:

1. **Kontakt zu Experimentalgruppe:** Die Vorhersage
   $|\Delta\langle x\rangle| = 2.0 \cdot \lambda\;\mu\mathrm{m}$
   ist mit bestehender BEC-Technologie testbar. Gruppen wie Bloch (MPQ),
   Ketterle (MIT), oder Cornells BEC-Gruppe haben die nötige Infrastruktur.

2. **2-Teilchen-Erweiterung:** Für das Gisin-Theorem und No-Signaling
   muss die Simulation auf verschränkte 2-Teilchen-Zustände erweitert
   werden (nächste theoretische Hürde).

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück zur Schrödinger-Übersicht](../README.md)
