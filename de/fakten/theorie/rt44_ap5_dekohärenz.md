# RT-44 AP5 — Messprozess und Dekohärenz als ε-Übergang

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Quantenmessung als ε-Übergang formal beschreiben;
Dekohärenzzeit aus RFT-Parametern abschätzen.

**Ergebnis:** Messprozess = Übergang ε: (0,1) → 1 durch Kopplung an makroskopisches
Umfeld. Dekohärenzzeit τ_D ~ 1/β aus der RFT-Kopplungsdynamik.

---

## 2. Messprozess als ε-Übergang

### 2.1 Zustände

| Phase | Phasendifferenz | ε | Physikalischer Zustand |
|-------|-----------------|---|------------------------|
| Vor Messung | Δφ ∈ (0, π) | ε ∈ (0,1) | Superposition (Wellenregime) |
| Während Messung | Δφ → 0 | ε → 1 | Kopplung an Apparat (Lokalisierung) |
| Nach Messung | Δφ ≈ 0 | ε ≈ 1 | Lokalisierter Zustand (Projektion) |

### 2.2 Mechanismus

**Vor Messung:** Das Quantensystem S befindet sich in Superposition.
Die Phasendifferenz Δφ_SA zwischen S und dem Messapparat A ist nicht fixiert:
ε(Δφ_SA) < 1.

**Messung:** Durch physikalischen Kontakt (Photon, elektrisches Feld, etc.) wird
S an A gekoppelt. Die RFT-Kopplungsdynamik:

```
dK/dt = αG cos(Δφ_SA) − β K
```

treibt das System in Richtung K → K_stat = (αG/β) cos(Δφ_SA).
Bei vollständiger Kopplung: Δφ_SA → 0, ε → 1.

**Physikalische Interpretation:** Die Phasendifferenz Δφ_SA kollabiert zur dominanten
Eigenphase des Messapparats. Das ist der ε-Übergang des Messprozesses.

---

## 3. Dekohärenzzeit aus RFT-Parametern

### 3.1 Charakteristische Zeitskala

Die Relaxationsgleichung für die Kopplungseffizienz (aus RT-42 AP2):

```
ε̇ = −β(1 − ε)
→  ε(t) = 1 − (1 − ε₀) e^{−βt}
```

**Dekohärenzzeit:** τ_D = 1/β

Bei Erreichen von ε(τ_D) = 1 − (1−ε₀)/e ≈ 1 − 0,37(1−ε₀): ~63% des Weges von
ε₀ nach 1.

### 3.2 Skalierung mit Systemgröße

Der Dissipationsparameter β hängt von der Stärke der Umgebungskopplung ab:

```
β ∝ (Anzahl der Umgebungsfreiheitsgrade) × (Kopplungsstärke)²
```

| System | β (Schätzung) | τ_D = 1/β |
|--------|---------------|-----------|
| Makroskopischer Körper (10²³ Atome) | ~10²³ Hz | ~10⁻²³ s |
| Einzelnes Molekül (Luft, 300K) | ~10¹² Hz | ~10⁻¹² s = 1 ps |
| ⁸⁷Rb-Atom in BEC (10⁻⁷ K) | ~10⁻³ Hz | ~10³ s |
| Einzelnes Spin im Vakuum | ~10⁻⁶ Hz | ~10⁶ s |

**Konsistenz:** Makroskopische Objekte dekohärieren extrem schnell (τ_D ~ 10⁻²³ s)
→ klassisches Verhalten. Quantensysteme bei tiefen Temperaturen haben lange τ_D →
beobachtbare Quanteneffekte. Konsistent mit experimentellen Befunden.

---

## 4. Zeigerbasisbestimmung

Die bevorzugten Dekohärenz-Basiszustände (Zeigerbasis) sind diejenigen, die
unter der Kopplung an die Umgebung stabil sind:

```
ε(Δφ_S−E) = 1   für Zeigerbasis-Zustände |a⟩
```

d.h. die Zustände, die mit dem Messapparat E resonant koppeln (Δφ_SE → 0).

Das erklärt, warum in einem Positionsmessgerät Ortseigenzustände die Zeigerbasis
bilden: Lokalisierte Zustände koppeln effizienter (ε → 1) an makroskopische
Objekte als Impulseigenzustände.

---

## 5. Gisin-Konsistenz

Aus der Gisin-Analyse (Schrödinger-Simulation): Die Kopplung ist lokal —
kein nichtlokaler Kollaps.

Die ε-Übergang-Beschreibung des Messprozesses ist lokal: Δφ_SA ändert sich
lokal am Ort der Messung. Fernkorrelationen (Verschränkung) werden in AP7 behandelt.
Kein Widerspruch zu A6 (Information propagiert nur entlang kohärenter Resonanzpfade).

---

## 6. Ergebnis

```
τ_D = 1/β   (Dekohärenzzeit aus RFT-Kopplungsdynamik)
Messprozess: ε: (0,1) → 1  (ε-Übergang durch Kopplung)
Zeigerbasis: Zustände mit ε(Δφ_S−E) → 1
```

**Erfolgskriterium:** ✅ Erfüllt — Dekohärenzzeit aus RFT-Parametern abschätzbar;
Messprozess als quantitativer ε-Übergang beschrieben.

---

*RT-44 AP5 — DominicReneSchu/RFT — November 2026*
