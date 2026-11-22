# RT-54 — Kerr-Metrik als anisotrope ε-Modulation: Rotierende Schwarze Löcher

*Dominic-René Schu, November 2026*
*Status: ✅ Analytisch abgeschlossen (Nov 2026)*
*Vorgänger: RT-40 (ε=1/γ²), RT-53 (Schwarzschild als isotropes ε), RT-52 (Brannen-Phase θ, Brücke B₃)*

---

## Zielsetzung

RT-53 zeigt, dass die Schwarzschild-Zeitdilatation ein ε-Effekt ist:
ε_Schwarz(r) = 1 − r_S/r (kugelsymmetrisch).

RT-54 erweitert das auf rotierende Schwarze Löcher (Kerr-Metrik):

$$\boxed{\varepsilon_{\rm Kerr}(r,\vartheta) = 1 - \frac{r_S \cdot r}{r^2 + a^2\cos^2\vartheta} = 1 - \frac{r_S r}{\Sigma}}$$

mit Σ = r² + a²cos²ϑ und Spin-Parameter a = J/(Mc).

**Das ist eine anisotrope ε-Modulation in der Energiekugel** — der erste physikalische Fall
einer richtungsabhängigen ε-Struktur in der RFT.

---

## 1. Die Kerr-ε-Struktur

### 1.1 Parametrisierung

| Symbol | Bedeutung |
|--------|-----------|
| r_S = 2GM/c² | Schwarzschild-Radius |
| a = J/(Mc) | Spin-Parameter (0 ≤ a ≤ r_S/2) |
| Σ = r² + a²cos²ϑ | Kerr-Strukturfunktion |
| Δ = r² − r_S·r + a² | Horizont-Funktion |
| ϑ | Polarer Winkel (Breitengrad) |

### 1.2 Grenzfälle

| Grenzfall | Bedingung | ε-Form |
|-----------|-----------|--------|
| Schwarzschild | a = 0 | ε = 1 − r_S/r (isotrop) |
| Equatorial Kerr | ϑ = π/2 | ε = 1 − r_S/r (wie Schwarzschild!) |
| Polar Kerr | ϑ = 0 | ε = 1 − r_S·r/(r²+a²) |
| Extremal (a=r_S/2) | a→max | r_H = r_S/4 |

**Bemerkenswertes Ergebnis:** An der Ergosphäre (ε=0) am Äquator gilt immer r_ergo = r_S/2
— unabhängig von a! Die Ergosphäre am Äquator ist für alle Kerr-BH gleich groß.

---

## 2. Ereignishorizont und Ergosphäre als ε=0-Flächen

### 2.1 Ereignishorizont (Δ = 0)

```
r_H = r_S/2 ± √((r_S/2)² − a²)
```

| a/a_max | r_H (äußerer) | r_H (innerer) |
|---------|---------------|---------------|
| a = 0 (Schwarzschild) | r_S/2 | r_S/2 (entartet) |
| a = 0,5·a_max | 0,933·r_S/2 | 0,067·r_S/2 |
| a = a_max (extremal) | 0,5·r_S/2 | 0,5·r_S/2 (entartet) |

### 2.2 Ergosphäre (ε = 0, aber Δ > 0)

```
r_ergo(ϑ) = r_S/2 + √((r_S/2)² − a²cos²ϑ)
```

Die Ergosphäre ist der Bereich, in dem **ε = 0, aber kein Ereignishorizont existiert**.
Ein Objekt kann die Ergosphäre verlassen — aber es kann dabei keine statische Position
einnehmen (Frame-Dragging erzwingt Mitrotation).

**RFT-Deutung:** In der Ergosphäre ist ε = 0 (vollständige Entkopplung), aber die
Phasendynamik Δφ → π wird durch den Drehimpuls **lokal wieder von π wegbewegt**.
Ein Resonator in der Ergosphäre hat ε = 0 im r-Sektor, aber ε > 0 im φ-Sektor (Rotation).

---

## 3. Frame-Dragging als Rotation von ê (Energierichtung A5)

### 3.1 Lense-Thirring-Effekt

Ein rotierendes Schwarzes Loch "schleppt" den Raumzeit-Rahmen mit sich. Die
Winkelgeschwindigkeit des Frame-Draggings (bei r >> r_S):

```
Ω_LT = 2GJ/(c²r³) = a·r_S·c/(2r³)
```

**RFT-Deutung (Axiom A5):** Der Vakuumvektor ê im Resonanzfeld rotiert mit Ω_LT.
Das ist die direkte physikalische Realisierung der Energierichtung A5 — die Richtung
der Resonanzkopplung dreht sich mit dem Kerr-Drehimpuls.

### 3.2 Gyromagnetisches Verhältnis g = 2

Das Kerr-Schwarze-Loch hat (falls geladen) ein gyromagnetisches Verhältnis g = 2 —
identisch mit dem Elektron! Dies ist kein Zufall, sondern eine Konsequenz der Spinor-
Struktur des Kerr-Raumzeit-Tensors.

**RFT-Verbindung:** A9_Spin (RT-44 AP6) → Zweimoden-Spinor → g = 2 aus SU(2).
Das Kerr-Schwarze Loch realisiert dieselbe SU(2)-Struktur wie das Elektron —
in makroskopischem Maßstab.

---

## 4. Penrose-Prozess als RFT-Resonanzübertragung

### 4.1 Penrose-Prozess

In der Ergosphäre kann ein Teilchen in zwei zerfallen:
- Teilchen 1 fällt ins Schwarze Loch
- Teilchen 2 verlässt die Ergosphäre mit mehr Energie als das ursprüngliche Teilchen

Das Schwarze Loch verliert dabei Drehimpuls (und Rotationsenergie).

### 4.2 RFT-Deutung

In der RFT: In der Ergosphäre ist ε_r = 0, aber ε_φ > 0.
Ein Resonator zerfällt so, dass ein Anteil in den ε_φ-Sektor übertragen wird —
Rotationsenergie des BH wird in Strahlungsenergie umgewandelt.

Das ist eine **negative Kopplungseffizienz** im r-Sektor: ε_r < 0 möglich,
wenn Δφ_r > π (Übersteigen der Halbkopplung in Rotationsrichtung).

**Falsifikationskriterium F-RT54-1:** Wenn Penrose-Prozess nicht die vorhergesagte
ε_φ-Struktur zeigt → RFT-Deutung der Ergosphäre widerlegt.

---

## 5. Verbindung zu RT-52: Kerr als Beispiel für B₃

**Zentrales neues Ergebnis:**

Schwarzschild: ε(r) — kugelsymmetrisch — **kein bevorzugter ê-Vektor** in der Energiekugel.
Kerr: ε(r,ϑ) — achsensymmetrisch — **ê_J (Rotationsachse) definiert eine ausgezeichnete Richtung**.

**Das Kerr-Schwarze Loch ist das erste RFT-Beispiel einer physikalisch realisierten
asymmetrischen Richtung ê in der Energiekugel!**

Das ist direkt relevant für RT-52 (Brücke B₃): Die Brannen-Phase θ benötigt eine
asymmetrische Referenzrichtung ê. Das Kerr-BH zeigt, dass solche Richtungen in der RFT
physikalisch durch Drehimpuls realisiert werden.

**Hypothese RT-54 → RT-52:** Wenn die elektroschwache Symmetriebrechung analog zum
Kerr-Drehimpuls eine ausgezeichnete Richtung ê_EW im Phasenraum definiert, dann
liefert der B₃-Mechanismus θ durch denselben geometrischen Prozess wie die
Kerr-Metrik die Ergosphären-Achse ê_J liefert.

---

## 6. Vollständige ε-Hierarchie der RFT-Raumzeitgeometrie

```
Minkowski (flach):        ε = 1                    [RT-40, Grundzustand]
         ↓
Schwarzschild (Masse):    ε(r) = 1 − r_S/r         [RT-53, kugelsymmetrisch]
         ↓
Kerr (Masse + Spin):      ε(r,ϑ) = 1 − r_Sr/Σ      [RT-54, achsensymmetrisch]
         ↓
Kerr-Newman (M+J+Q):      ε(r,ϑ) = 1 − (r_Sr−r_Q²)/Σ [RT-55, offen]
         ↓
Allgemeine Raumzeit:      ε(x^μ) aus Einst.-Gl.      [RT-56, offen]
```

---

## Falsifikationskriterien

| Kriterium | Bedingung | Test |
|-----------|-----------|------|
| **F-RT54-1** | Penrose-Prozess zeigt nicht ε_φ-Struktur | Akkretionsscheiben-Modellierung |
| **F-RT54-2** | Frame-Dragging ≠ ê-Rotation (A5) | LIGO/LISA Messungen |
| **F-RT54-3** | g ≠ 2 für Kerr (elektromagnetisch) | Theoretische Konsistenz |

---

*RT-54 — DominicReneSchu/RFT — November 2026*
