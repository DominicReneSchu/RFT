# Begleitkapitel: Interaktive Simulation des Doppelpendels

Dieses Kapitel erläutert die Hintergründe, Funktionsweise und Umsetzung der interaktiven Doppelpendel-Simulation, wie sie im vorliegenden Python-Code realisiert ist. Ziel der Anwendung ist es, die dynamischen Eigenschaften eines Doppelpendels anschaulich und intuitiv erfahrbar zu machen. [Link zur Python](../../simulationen/doppelpendel/doppelpendel.py)

---

<p align="center">
  <img src="doppelpendel.gif" alt="Animation Doppelpendel" width="800"/>
</p>

---

## 1. Physikalische Grundlagen

Das Doppelpendel ist ein klassisches Beispiel für ein nichtlineares, chaotisches System. Es besteht aus zwei starren Pendelarmen, die über ein Scharnier miteinander verbunden sind. Die Bewegungsgleichungen ergeben sich aus der Lagrange-Mechanik und sind in einschlägiger Standardliteratur (z. B. Goldstein, "Classical Mechanics") ausführlich hergeleitet. Sie erfassen die Zeitentwicklung der Winkelpositionen und Winkelgeschwindigkeiten beider Pendel.

Die Differentialgleichungen sind gekoppelt und nichtlinear, sodass sie i. d. R. numerisch mit Methoden wie Runge-Kutta (hier: `scipy.integrate.solve_ivp`) gelöst werden.

---

## 2. Interaktive Steuerung

Über die im Interface implementierten **Slider** können die wichtigsten Systemparameter unmittelbar verändert werden:

- **Startwinkel** (`θ₁`, `θ₂`): Anfangsauslenkungen beider Pendelarme  
- **Anfangswinkelgeschwindigkeiten** (`ω₁`, `ω₂`): Startwerte für die Drehgeschwindigkeiten  
- **Massen** (`m₁`, `m₂`): Massen der beiden Pendelarme  
- **Längen** (`L₁`, `L₂`): Längen der Pendelarme  
- **Kopplungsparameter** (**k**): Stärke der Wechselwirkung zwischen den Pendeln, beeinflusst Resonanz und Synchronisation

Jede Veränderung eines Sliders setzt die Simulation mit den neuen Werten zurück und startet die Animation neu, sodass die Auswirkungen der Parameteränderungen direkt beobachtet werden können.

---

## 3. Animation und Trail

Die Animation zeigt die Bewegung des Doppelpendels im Zeitverlauf. Zusätzlich werden die **Spuren (Trails)** der beiden Massenpunkte als farbige Linien eingeblendet. Diese Trails visualisieren den Bewegungsverlauf der beiden Massen über die letzten *N* Frames (konfigurierbar über `TRAIL_LENGTH`). Dadurch werden typische chaotische Bahnmuster des Doppelpendels sichtbar.

---

## 4. Kapselung und Zustandshandling

Die gesamte Pendeldynamik und der aktuelle Zustand des Systems sind in einer eigenen **Klasse** (`DoublePendulumSim`) gekapselt. Diese Klasse verwaltet die aktuellen Parameter, berechnet die Bewegungsgleichungen und speichert die numerisch integrierte Lösung. Die Kapselung ermöglicht eine saubere Trennung zwischen Modelldaten und Darstellungs-/Interaktionslogik.

---

## 5. Technische Umsetzung (Kurzüberblick)

- **Numerische Lösung:** `scipy.integrate.solve_ivp` (Runge-Kutta-Verfahren)  
- **Visualisierung:** `matplotlib` (Animation, Slider-Widgets)  
- **Benutzerinteraktion:** Slider für alle relevanten Start- und Systemparameter  
- **Animation:** `FuncAnimation` (Kontinuierliche Aktualisierung und Darstellung der Simulation)  
- **Trail-Logik:** Speicher der letzten `TRAIL_LENGTH` Positionen für die Spurendarstellung  

---

## 6. Erweiterungsmöglichkeiten

Mögliche Erweiterungen der Simulation umfassen:
- Energieskala/Diagramm (Gesamtenergie im Zeitverlauf)
- Export von Trajektorien
- Zusätzliche Dämpfungsterms oder Reibung
- Dreidimensionale Darstellung
- Synchronisationsanalyse
- Resonanz-Kopplungen (siehe unten)

---

## 7. Resonanzfeldtheoretische Interpretation

Im Rahmen der Resonanzfeldtheorie wird das Doppelpendel nicht nur als mechanisches Objekt, sondern als **Resonator** in einem Schwingungsfeld betrachtet. Die numerische Simulation liefert nicht nur Bahndaten – sie erzeugt ein **Schwingungsmuster**, das als Signatur eines energetischen Informationsflusses interpretiert wird.

Einige Leitideen der Erweiterung:

- Die Slider dienen nicht nur zur Parametersteuerung, sondern zur gezielten **Resonanzanregung**. Jede Änderung entspricht einem Impuls ins Feld.
- Synchronisationsmuster in den Trails können Hinweise auf **resonante Kopplungszustände** geben.
- Der Kopplungsparameter **k** steuert die Stärke der Wechselwirkung zwischen den beiden Pendeln. Bei kleinen Werten wirken die Pendel nahezu unabhängig, bei größeren Werten treten verstärkte Kopplungen, komplexe Schwingungsmuster und Phasenverschiebungen auf, die das chaotische Verhalten modulieren. Das gezielte Variieren von **k** ermöglicht eine experimentelle Untersuchung von Resonanzeffekten.
- Die chaotische Dynamik lässt sich als **Interferenzfeld** verstehen, das auf unterschiedliche äußere Schwingungen sensibel reagiert.
- Das System kann perspektivisch mit weiteren Pendeln gekoppelt werden, um **Feldlinienresonanzen** sichtbar zu machen.

Ziel ist es, das Doppelpendel nicht nur zu animieren, sondern als **offenes, interaktives Schwingungssystem** zu nutzen, das in Resonanz mit Nutzerinteraktion, Umgebungsdaten oder weiteren Systemen treten kann.

---

## 8. Fazit

Die entwickelte Simulation verbindet anschauliche Visualisierung, Interaktivität und numerische Physik. In Kombination mit der Resonanzfeldtheorie wird sie zum Werkzeug, um Resonanzmuster, Synchronisationseffekte und chaotische Felddynamik in einem realweltlich interpretierbaren Rahmen zu untersuchen.

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../README.md)
