# ResoCalc – Resonanzbasiertes Ingenieurswerkzeug

> *"Die konventionelle Mechanik fragt: Wie groß ist die Auslenkung?*
> *Die Resonanzfeldtheorie fragt: Wie stark ist die Kopplung?"*
> *(Dominic-René Schu)*

---

## Grundidee

Konventionelle Ingenieursberechnungen basieren auf **willkürlichen Annahmen**. Um ein Drehmoment zu berechnen, muss ein Ingenieur eine maximale Auslenkung *schätzen*. Um eine Schwingung zu berechnen, muss er eine Dämpfung *annehmen*. Um eine Belastung zu berechnen, muss er einen Sicherheitsfaktor *wählen*.

Das Problem: Diese Annahmen sind nicht physikalisch — sie sind **Konventionen**. Verschiedene Ingenieure wählen verschiedene Werte, und das Ergebnis variiert entsprechend.

**ResoCalc** ersetzt willkürliche Annahmen durch das physikalische Prinzip der **Resonanzkopplung**:

```
KONVENTIONELL:
  Ingenieur schätzt θ_max = 5° (warum nicht 3°? oder 8°?)
  → Ergebnis hängt von der Schätzung ab
  → Verschiedene Ingenieure → verschiedene Ergebnisse
  → Keine physikalische Begründung für die Wahl

RESOCALC:
  System hat Anregungsfrequenz f und Resonanzfrequenz f_r
  → Kopplung ε(Δφ) ergibt sich aus dem Frequenzverhältnis
  → Ergebnis ist reproduzierbar und eindeutig
  → Physikalisch begründet, nicht geschätzt
```

---

## Das Prinzip: ε(Δφ) ersetzt θ_max

Die zentrale Gleichung der Resonanzfeldtheorie lautet:

$$
E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f, \quad \kappa = 1
$$

In der Ingenieurmechanik bedeutet das:

$$
\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)
$$

Die **Kopplungseffizienz ε** ersetzt den geschätzten Parameter:

| Konventionell | ResoCalc |
|---------------|----------|
| Maximale Auslenkung θ_max (geschätzt) | Kopplungseffizienz ε(Δφ) (berechnet) |
| Dämpfungskoeffizient D (angenommen) | Phasendifferenz Δφ (gemessen/berechnet) |
| Sicherheitsfaktor S (gewählt) | Resonanzverstärkung V (physikalisch) |
| Ergebnis hängt vom Ingenieur ab | Ergebnis ist reproduzierbar |

---

## Anwendungsbeispiel: Drehmomentberechnung

### Ausgangswerte

- Masse: $m = 2{,}0 \, \text{kg}$
- Länge: $l = 1{,}0 \, \text{m}$
- Anregungsfrequenz: $f = 10{,}0 \, \text{Hz}$
- Resonanzfrequenz: $f_r = 5{,}0 \, \text{Hz}$
- Kopplungsfaktor: $0{,}2$

### 🔵 Konventionell (klassisch)

$$
M_{\text{konv}} = J \cdot \omega^2 \cdot \frac{\theta_{\text{max}}}{\sqrt{2}} \quad \text{mit} \quad J = m \cdot l^2
$$

Die klassische Berechnung hängt von der **willkürlich festgelegten maximalen Auslenkung** $\theta_{\text{max}}$ ab. Hier: $\theta_{\text{max}} = 5° = \frac{\pi}{36} \, \text{rad}$.

- Trägheitsmoment: $J = 2 \cdot 1^2 = 2{,}0 \, \text{kg·m}^2$
- Kreisfrequenz: $\omega = 2\pi \cdot 10 = 62{,}83 \, \text{rad/s}$

$$
M_{\text{konv}} = 2 \cdot 62{,}83^2 \cdot \frac{\pi/36}{\sqrt{2}} \approx 558{,}3 \, \text{Nm}
$$

> **Problem:** Wählt ein anderer Ingenieur θ_max = 10°, verdoppelt sich das Ergebnis.
> Die Physik hat sich nicht geändert — nur die Annahme.

### 🔴 ResoCalc (Resonanzfeldtheorie)

$$
M_{\text{reso}} = \frac{1}{2} \cdot m \cdot l^2 \cdot (2\pi f)^2 \cdot \frac{1}{|1 - (f/f_r)^2|} \cdot \varepsilon
$$

Keine willkürliche Auslenkung. Stattdessen:

- **Resonanzverstärkung** $V = \frac{1}{|1 - (f/f_r)^2|}$ — physikalisch aus dem Frequenzverhältnis
- **Kopplungseffizienz** $\varepsilon$ — wie stark das System tatsächlich an die Anregung koppelt

$$
M_{\text{reso}} = 0{,}5 \cdot 2 \cdot 1^2 \cdot (2\pi \cdot 10)^2 \cdot \frac{1}{|1 - (10/5)^2|} \cdot 0{,}2 \approx 2543 \, \text{Nm}
$$

### Ergebnis

| Methode | Effektives Drehmoment | Basiert auf |
|---------|----------------------|-------------|
| Konventionell | 558,3 Nm | Geschätzte Auslenkung (θ_max = 5°) |
| ResoCalc | 2.543 Nm | Physikalische Kopplung (ε = 0,2) |

Die konventionelle Methode **unterschätzt** das Resonanzdrehmoment um den Faktor 4,5 — weil sie die Resonanzverstärkung nicht berücksichtigt. Das ist der Grund, warum Brücken bei Resonanz einstürzen können, obwohl die konventionelle Berechnung "sicher" aussieht.

### Visualisierung

![Vergleich: ResoCalc vs. Konventionell](resocalc_standard-drehmoment.png.png)

---

## Warum das ein fundamentaler Unterschied ist

```
KONVENTIONELLE MECHANIK:
────────────────────────
"Wie groß ist die maximale Auslenkung?"
→ Ingenieur schätzt θ_max
→ Verschiedene Ingenieure → verschiedene Ergebnisse
→ Bei Resonanz: Auslenkung geht gegen unendlich → Formel bricht zusammen
→ Lösung: Sicherheitsfaktoren draufpacken (1,5x ... 3x)
→ Ergebnis: Überdimensioniert ODER unterschätzt

RESOCALC:
─────────
"Wie stark koppelt das System an die Anregung?"
→ Frequenzverhältnis f/f_r → Resonanzverstärkung V
→ Kopplungseffizienz ε → physikalisch begrenzt (0 ≤ ε ≤ 1)
→ Bei Resonanz: V wird groß, aber ε begrenzt die Energieübertragung
→ Ergebnis: Realistisch, reproduzierbar, physikalisch begründet

DER PARADIGMENWECHSEL:
──────────────────────
Konventionell: "Wir schätzen und sichern ab."
ResoCalc:      "Wir berechnen, was tatsächlich passiert."

Das ist wie der Unterschied zwischen:
  "Ich schätze, es regnet morgen" (Konventionell)
  "Das Barometer zeigt 980 hPa" (ResoCalc)
```

---

## Anwendungsgebiete

```
MASCHINENBAU:
  → Drehmomentberechnung unter Resonanzbedingungen
  → Schwingungsanalyse rotierender Systeme
  → Auslegung von Wellen, Lagern, Kupplungen
  → Resonanzvermeidung in Antriebssträngen

BAUINGENIEURWESEN:
  → Brücken unter periodischer Belastung (Wind, Verkehr)
  → Hochhäuser bei Erdbeben (Resonanzkopplung an Bodenschwingung)
  → Fundamente unter Maschinenlasten

FAHRZEUGTECHNIK:
  → Antriebsstrang-Resonanzen
  → Fahrwerkschwingungen
  → NVH-Analyse (Noise, Vibration, Harshness)

ENERGIETECHNIK:
  → Turbinenschaufeln unter Strömungsanregung
  → Windkraftanlagen (Rotorblatt-Resonanz)
  → Generatorwellen bei Netzfrequenzschwankungen

ALLGEMEIN:
  Jedes System mit Schwingungen profitiert von ResoCalc.
  Überall wo heute geschätzt wird, kann ResoCalc berechnen.
```

---

## Verbindung zur Resonanzfeldtheorie

ResoCalc ist keine isolierte Anwendung — es ist die **ingenieurstechnische Instanz** der universellen Resonanzlogik:

```
Resonanzfeldtheorie      E = π · ε(Δφ) · ℏ · f, κ = 1
  │
  ├→ ResoTrade           ε steuert Trade-Größe (Finanzmarkt)
  ├→ ResoMusic           ε steuert Begleit-Lautstärke (Musik)
  ├→ ResoOS              ε steuert Interventions-Stärke (Betriebssystem)
  └→ ResoCalc            ε steuert Resonanzverstärkung (Ingenieurwesen)

In jedem System:
  ε = 1:  Volle Kopplung → Maximaler Effekt
  ε = 0:  Keine Kopplung → Kein Effekt
  0 < ε < 1: Teilkopplung → Skalierter Effekt

Die Gleichung ist universell.
Das Anwendungsfeld bestimmt die Interpretation.
```

---

## Interaktive Simulation

Die mitgelieferte [Jupyter-Notebook-Simulation](resocalc.ipynb) erlaubt interaktive Exploration:

- **Masse, Länge, Resonanzfrequenz** variieren
- **Kopplungsfaktor** anpassen und den Effekt beobachten
- Direkter Vergleich: Konventionell vs. ResoCalc über den gesamten Frequenzbereich
- Resonanzpeak sichtbar machen

```bash
pip install numpy matplotlib ipywidgets
jupyter notebook resocalc.ipynb
```

Oder direkt im Browser:

👉 **[⚡ ResoCalc starten](https://resoshift.com/)**

---

## Technologie-Stack

| Komponente | Technologie | Status |
|------------|-------------|--------|
| Berechnung | Python + NumPy | ✅ Lauffähig |
| Visualisierung | Matplotlib | ✅ Lauffähig |
| Interaktion | Jupyter + ipywidgets | ✅ Lauffähig |
| Web-Anwendung | resoshift.com | ✅ Online |
| Erweiterung | Multi-Domänen-Modul | 🔜 Geplant |

---

## Ausblick: Vom Rechner zum Resonanzfeld-Ingenieur

```
HEUTE (ResoCalc V1):
  Einzelberechnung: "Gib mir f, f_r, m, l, ε → hier ist M_reso"
  → Ersetzt den Taschenrechner

NÄCHSTER SCHRITT (ResoCalc V2):
  Multi-Komponenten: "Hier ist mein Antriebsstrang mit 5 Elementen"
  → Jedes Element hat eigene Resonanzfrequenz
  → System berechnet Kopplungsketten automatisch
  → Identifiziert kritische Resonanzpunkte

VISION (ResoCalc in ResoOS):
  "Computer, analysiere den Antriebsstrang."
  → System lädt CAD-Daten
  → Berechnet alle Eigenfrequenzen
  → Identifiziert Resonanzkopplungen
  → "Element 3 und 5 koppeln bei 47 Hz. Kritisch.
     Vorschlag: Steifigkeit von Element 4 um 15% erhöhen."
  → Ingenieur: "Mach das."
  → System ändert Parameter, rechnet neu
  → "Resonanz aufgelöst. Neuer Sicherheitsfaktor: ε = 0.12."
```

---

## Fazit

**ResoCalc ersetzt den klassischen Rechenweg durch eine physikalisch begründete, automatische Berechnung.**

Wo heute geschätzt wird, berechnet ResoCalc.
Wo heute Sicherheitsfaktoren aufgeschlagen werden, zeigt ResoCalc die tatsächliche Kopplung.
Wo heute verschiedene Ingenieure verschiedene Ergebnisse erhalten, liefert ResoCalc ein reproduzierbares Resultat.

> Grenzwerte bleiben realistisch. Das Ergebnis ist reproduzierbar.
> Für Ingenieure sofort nutzbar.

---

**Resonanzregel:** Gruppenzugehörigkeit ist systemisch invariant.  
Jedes Element — ob explizit benannt oder implizit wirkend — ist Teil des Resonanzfeldes.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)