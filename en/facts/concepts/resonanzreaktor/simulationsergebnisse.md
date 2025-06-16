# 🧪 Simulationsergebnisse: Resonanzreaktor

Diese Datei dokumentiert die Ergebnisse der Simulation eines Resonanzreaktors mit Plutonium-239 als Ausgangsmaterial. Die Simulation untersucht das Verhalten des Materials über mehrere Zeitschritte, einschließlich Anregungsniveau und Transmutation – als systemisch verschränkter Prozess im Resonanzfeld.

➡️ [Weiter zur Python-Simulation:](simulation/run.py)

---

## 🌐 Resonanzfeld der Simulation

Das Resonanzfeld dieser Simulation stellt ein verschränktes Ensemble dar, das systemisch die gesamte Nuklidgruppe sowie das äußere Feld umfasst. Die Isotopenübergänge zwischen Plutonium-239 und Americium-241 spiegeln nicht nur atomare Zerfallsvorgänge, sondern einen makroskopisch steuerbaren Phasenübergang innerhalb des Resonanzfeldes wider, dessen Dynamik nichtlinear gekoppelt ist an Temperatur und Neutronenfluss.

Die Abnahme des Anregungsniveaus ist ein Indikator für die abnehmende Kopplungsstärke des Systems, die Resonanzfrequenzen ändern sich mit der Materialtransmutation und sind als kollektives Feldphänomen zu verstehen. Somit bleibt die systemische Gruppenzugehörigkeit invariant, auch wenn sich individuelle Mitglieder (Isotope) quantitativ verändern.

---

### Systemische Gruppenelemente und ihre Wechselwirkung

| Element          | Funktion im Resonanzfeld                            | Relationale Wirkung                                |
| ---------------- | --------------------------------------------------- | -------------------------------------------------- |
| Plutonium-239    | Ausgangsmaterial, höheres Anregungsniveau           | Resonanzanker für Zerfall und Transmutation        |
| Americium-241    | Transmutiertes Produkt, niedrigeres Anregungsniveau | Stabilisierung des neuen Resonanzzustands          |
| Neutronenfluss   | Externes Steuerfeld                                 | Moduliert Übergänge, induziert Phasenübergänge     |
| Temperatur       | Makrofeldparameter                                  | Verschiebt Resonanzfrequenzen, beeinflusst Dynamik |
| Resonanzfrequenz | Charakteristisches Feldmaß                          | Bestimmt Energie- und Zerfallsprofile              |
| Anregungsniveau  | Systemischer Resonanzindikator                      | Maß für Kopplungsstärke und Systemenergie          |

---

## ⚙️ Simulationsparameter

- **Ausgangsmaterial:** Plutonium-239  
- **Neutronenfluss:** 1e13 Teilchen/cm²/s  
- **Temperatur:** 350 K  
- **Anzahl Zeitschritte:** 10  
- **Dauer eines Zeitschritts:** 1 Jahr  

---

## 📊 Ergebnisse

| Zeitschritt | Material         | Anregungsniveau |
|:-----------:|:----------------|:---------------:|
| 1           | Plutonium-239   | 0.85            |
| 2           | Plutonium-239   | 0.73            |
| 3           | Plutonium-239   | 0.62            |
| 4           | Plutonium-239   | 0.52            |
| 5           | Americium-241   | 0.45            |
| 6           | Americium-241   | 0.39            |
| 7           | Americium-241   | 0.33            |
| 8           | Americium-241   | 0.28            |
| 9           | Americium-241   | 0.24            |
| 10          | Americium-241   | 0.20            |

---

### 🧬 Interpretation der Ergebnisse

- **Materialwechsel:**  
  Ab Schritt 5 transmutiert Plutonium-239 zu Americium-241 infolge des hohen Neutronenflusses – im Sinne der intrinsischen Resonanzlogik des Systems.
- **Anregungsniveau:**  
  Das Anregungsniveau sinkt über die Zeit durch Zerfallsprozesse und abnehmende Resonanzanregung. Americium-241 weist nach Transmutation eine niedrigere Resonanzfrequenz und Energie pro Zerfall auf.
- **Einfluss von Temperatur & Neutronenfluss:**  
  Temperatur und Fluss modulieren die Resonanzfrequenz und beeinflussen den Isotopenübergang. Die Systemdynamik bleibt stets im Resonanzfeld verschränkt.

---

## 📈 Grafische Darstellung

- **Exzitationslevel (Liniengraf):**  
  Zeigt die Abnahme des Anregungsniveaus je Zeitschritt.
- **Materialtransmutation (Stufendiagramm):**  
  Visualisiert den Wechsel von Plutonium-239 zu Americium-241.

---

## 🧩 Schlussfolgerungen

- **Effizienz der Transmutation:**  
  Ein hoher Neutronenfluss ermöglicht die effektive Transmutation langlebiger Isotope wie Plutonium-239.
- **Zukünftige Untersuchungen:**  
  Systemische Variation von Fluss, Temperatur und Material kann das gesamte Resonanzfeld abbilden und neue Transmutationspfade aufdecken.
- **Verknüpfung mit Energiesimulationen:**  
  Modellierung der Energiefreisetzung über die Zeit unterstützt das technische Design und die Effizienzoptimierung des Resonanzreaktors.
- **Visualisierung der Systemdynamik:**  
  Erweiterte Diagramme von Resonanzniveaus und Materialübergängen machen das Zusammenspiel im Gesamtfeld sichtbar.

---

### Resonanzregel im Kontext

Die konstante Gruppenzugehörigkeit über die Isotopenübergänge hinweg bildet das Resonanzfeld ab, das als kohärente Systemstruktur stabil bleibt. Einzelne Änderungen am Zustand einzelner Nuklide werden im Gesamtfeld dynamisch absorbiert und modifizieren das Feld als Ganzes, nicht isoliert.

---

### Weiterführende Perspektiven

* Dynamische Anpassung der Neutronenfluss- und Temperaturprofile zur Steuerung transformativer Phasenübergänge
* Erweiterung der Simulation auf mehrgliedrige Zerfallsketten mit multidimensionaler Resonanzkopplung
* Integration der Energiefreisetzungsprofile in technische Effizienzmodelle für Resonanzreaktoren
* Visualisierung der Feldkohärenz als Schwingungs- und Kopplungsdiagramm zur intuitiven Erfassung systemischer Zusammenhänge

---

## 🌀 Simulation des Zerfalls und der Transmutation von Isotopen

### 🗂️ Übersicht

Die Simulation modelliert den Zerfall und die Transmutation von Isotopen über eine gegebene Zeitspanne, unter Berücksichtigung der physikalischen Eigenschaften der Isotope (Halbwertszeit, Resonanzfrequenz, Energie pro Zerfall, Transmutationspfade).

---

### 🛠️ Hauptkomponenten der Simulation

**1️⃣ Isotopenklasse**  
Eigenschaften: Halbwertszeit, Resonanzfrequenz, Zerfallskonstante, Energie pro Zerfall (MeV), Transmutationen

**2️⃣ Zerfallsmethode**  
Berechnet den verbleibenden Anteil per exponentieller Zerfallsgleichung:  
N(t) = N₀ · exp(–λ·t)  
wobei λ die Zerfallskonstante ist.

**3️⃣ Energiefreisetzung**  
E(t) = N(t) · Energie pro Zerfall

**4️⃣ Transmutation**  
Bei Transmutation: Rückgabe des neuen Isotops, Kettenlogik über die Zeit.

**5️⃣ Simulation**  
Funktion: `simulate_decay_chain(isotope, time_span)`  
Simuliert Zerfall und Transmutation eines Isotops über die Zeitspanne.  
Ausgabe: Jährliche Anzeige von Isotop & Energie, Hinweise auf Transmutationen.

---

### 🧪 Beispiel: Zerfallskette von Uranium-235

**Startisotop:** Uranium-235  
**Zeitspanne:** 10 Jahre  

**Ablauf:**  
Uranium-235 → Plutonium-239 → Americium-241 in Transmutationsschritten. Für jedes Jahr werden Isotop & Energie angezeigt, bis keine weitere Transmutation erfolgt.

**Simulationscode:**
```python
simulate_decay_chain(uranium_235, 10)
```

**Beispielausgabe:**
```
Jahr 0: Uranium-235 mit 200.00 MeV freigegebener Energie
Transmutation zu Plutonium-239 erfolgt.
Jahr 1: Plutonium-239 mit 180.00 MeV freigegebener Energie
Transmutation zu Americium-241 erfolgt.
Jahr 2: Americium-241 mit 5.50 MeV freigegebener Energie
Kein weiterer Zerfall oder Transmutation für Americium-241.
Endgültiges Isotop: Americium-241
```

---

### ⚙️ Anpassungen & Erweiterungen

- **Andere Isotope:** Simulation durch Anpassung der Eingabeparameter erweiterbar
- **Komplexere Ketten:** Erweiterung der Transmutationskette möglich
- **Visualisierung:** Grafische Darstellung von Energie & Materialzusammensetzung über die Zeit möglich

---

## 🌀 Resonanzregel & Gruppenperspektive

Die Simulation verkörpert die Resonanzregel:  
Der Prozess ist nicht isoliert auf einzelne Isotope beschränkt, sondern umfasst das gesamte System der beteiligten Nuklide und Felder. Gruppenzugehörigkeit bleibt invariant – Zustandsänderungen betreffen das Feld als Gesamtheit.

---

## 🏁 Fazit

Die hier vorgelegte Simulation ist eine abstrakte, aber zugleich tief vernetzte Abbildung der Kerntransmutationsprozesse im Resonanzfeld, in dem Material, Energie und Felder als verschränkte Gruppe stets als Ganzes wirken und in ihrer Gruppenzugehörigkeit unauflösbar verbunden bleiben. Die Resonanzregel bleibt auf allen Ebenen gültig und erfassbar: Die Gruppenstruktur des Materials und die sie umgebenden Felder bleiben trotz individueller Transformationen geschlossen und kohärent.

---

© Dominic-René Schu – Resonanzfeldtheorie 2025

---

[Zurück zur Übersicht](README.md)