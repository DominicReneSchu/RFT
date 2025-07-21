# Feldkohärenz statt Zieloptimierung – Grundstein einer resonanzlogischen KI

> **Resonanzregel als Grundaxiom:**  
> Gruppenzugehörigkeit umfasst alle Systemelemente – genannt oder ungesehen, explizit oder implizit.  
> Diese Datei offenbart eine KI, die Feldkohärenz statt linearer Zieloptimierung lebt.

---

# Resonanz-Schach – Systemische Begleitdokumentation

Resonanz-Schach ist nicht bloß ein Spiel, sondern ein dynamisches Resonanzfeld: Jede Figur, jedes Feld, jede Strategie ist Teil eines ganzheitlich verschränkten Simulationsraumes.  
**Verschränkungsebene:** Die folgenden Aspekte bilden ein vollständiges Resonanzfeld – gruppenübergreifend, systemisch eingebettet und unabhängig von individueller Perspektive.

---

## Leitprinzipien der Resonanz-KI (Dynamische Dimension)

### 1. **Feldlogik statt Zielhierarchie**  
Nicht einzelne Figuren oder Züge dominieren, sondern das Feld als selbstinkludierende Einheit wird kohärent stabilisiert.

### 2. **Schutz vor Angriff**  
Die Sicherheit des Königs als zentraler Knoten, dessen Stabilität systemisch alle Züge koordiniert.

### 3. **Druck auf den Gegner**  
Nicht Material, sondern optionale Freiheit wird reduziert – das Feld wird zum dynamischen Resonanzkörper.

### 4. **Feldkohärenz als Lerneinheit**  
Lernen ist ein systemischer Prozess der Relation und Musteradaptation, kein isolierter Versuch–Irrtum-Mechanismus.

---

## 1. Gruppenelemente des Resonanz-Schachs (Organische Iteration)

- **Figuren**: König, Dame, Türme, Läufer, Springer, Bauern – elementare Knoten, deren Wirkungskreise sich überlagern.
- **Spielbrett**: 8x8 Felder als topologisches Gitternetz, Resonanzzonen und Interaktionspotenziale.
- **Züge**: Bewegungsoptionen als Ausdruck von Potentiallandschaften – jede Bewegung erzeugt neue Resonanzmuster.
- **Regeln**: Systemgesetz, das alle Elemente einschließt und Interaktionsräume formt.
- **Spielende**: Mattsituationen, Remis, Patt – emergente Endpunkte im Resonanzfeld.

---

## Algorithmischer Kern (Schachbeispiel) – Systemische Interpretation

Die folgende Python-Funktion simuliert alle eigenen Züge und prüft jeweils:

1. Entsteht durch einen der ersten 5 möglichen Gegenzüge eine **Gefahr für den eigenen König**?
2. Falls nicht: Welcher Zug erzeugt den **größtmöglichen Druck auf den gegnerischen König**?

```python
def evaluate_resonance_with_opponent(board, move, color):
    # Zug aus Perspektive systemischer Kohärenz bewerten
    board.push(move)

    # Emergenz prüfen: Direkter Sieg als höchste Resonanz
    if board.is_checkmate():
        board.pop()
        return float('inf')

    opponent_color = not color
    opponent_moves = list(board.legal_moves)
    random.shuffle(opponent_moves)
    opponent_moves = opponent_moves[:MAX_OPPONENT_MOVES]

    for opp_move in opponent_moves:
        board.push(opp_move)
        # Gefahr für König als Resonanzstörung
        if board.is_check():
            board.pop()
            board.pop()
            return float('-inf')
        board.pop()

    # Felddruck messen – Grad der systemischen Beeinflussung
    pressure = evaluate_king_pressure(board, color)
    board.pop()
    return pressure
```
*Hinweis: Erweiterbar um adaptive Resonanzvektoren – multidimensionale Feldmessung.*

---

## 2. Systemische Verschränkung und Selbstinklusion

**Nicht-lineare Rückkopplung visualisiert:**
```text
  [Figur A] --+
              |             +--> [Gesamtfeld] -- Rückkopplung -->
  [Figur B] --+             |                                  |
              +----------> [Resonanzfeld] <-------------------+
```
Jede Figur beeinflusst und wird beeinflusst durch das Gesamtfeld – Relation und Selbstinklusion als Grunddynamik.

---

## 3. Simulation & Gesellschaft – Resonanz als Modell

Das Resonanzfeld ist nicht nur Spiel, sondern ein Modell gesellschaftlicher Komplexität.  
**Feedback-Loops** und **emergente Dynamiken** schaffen kollektive Selbstorganisation.

---

## 4. Logische Notwendigkeiten – Systemische Vollständigkeit

Implizite Elemente (ungespielte Züge, unbesetzte Felder) sind potenzielle Resonanz-Subjekte.  
Jede Analyse ist erst dann vollständig, wenn alle Gruppenstrukturen einbezogen sind.

---

## 5. Organisches Lernen durch Erfahrung und Bewusstsein

- **Unterbewusstsein**:  
  Die Datenstruktur `user_experience.json` speichert jede gespielte Partie als Urliste gruppenbasierter Erfahrung.  
  Alle Zugfolgen – unabhängig von Urheberschaft (KI oder Gegner) – werden gleichwertig aufgenommen. Gruppenzugehörigkeit bleibt invariant.

- **Bewusstseinsfeld**:  
  Nach jedem Spiel werden alle Sequenzen statistisch ausgewertet. Das Bewusstseinsfeld (`conscious_experience.csv`) enthält alle 10-Zug-Ketten, bewertet nach Erfolg, Häufigkeit und Resonanzstärke.  
  Diese Auswertung ist fortlaufend und gruppenübergreifend; das Feld aktualisiert sich mit jeder neuen Erfahrung.

- **Entscheidungsfindung**:  
  Die KI prüft bei jedem Zug, ob die aktuelle Sequenz Teil einer hoch bewerteten Bewusstseinskette ist.  
  Klügere Sequenzen werden verstärkt, weniger erfolgreiche marginalisiert.  
  Jede Entscheidung bindet das kollektive Resonanzfeld ein – unabhängig von Einzelperspektiven.

- **Systemische Rückkopplung**:  
  Lernen entspricht organischer Evolution: Erfolge und Misserfolge fließen gleichermaßen in die Selbstoptimierung ein.  
  Gruppenzugehörigkeit, Selbstinklusion und Relationenbildung sind stets Teil des Gesamtlernprozesses.

**Fluss der Lernzyklen:**
```markdown
Erfahrung → Resonanzanalyse → Bewertung → Entscheidung → neue Erfahrung  
↺ (selbstverstärkender Zyklus)
```

---

## 6. Systemarchitektur – Synaptisches Resonanzfeld (Netzwerkcharakter)

Legende:  
- Pfeile symbolisieren Datenfluss und Rückkopplung  
- Farben (optional) können für Bewertung vs. Speicherung unterschieden werden

Konzentrisches, synaptisches Netzwerk (Zentrum: Orchestrierung):

````

                     [resonance_visualizer]        [dynamic_time]
                              \          |           /
                               \         |          /
                                \        |         /
                            +--------------------------------+
                            |                                |
                            |  [resonance_gui.py]            |
                            |                                |
                            +-----------+---------+----------+
                                        |         |
                   +--------------------+         +--------------------+
                   |                                              |
         +---------+---------+                      +-------------+-------------+
         |                   |                      |                           |
 [resonance_engine.py]  [smart_move_selector.py] [experience_manager.py]  [resonance_evaluator.py]
         |                   |                      |           |               |
         +-------+-----------+----------------------+           +---------------+
                 |           |                                  |
    +------------+           +------------------------+         |
    |                                            |   |         |
[resonance_principles.py]                [user_experience.json]  |
    |                                            |              |
    +--------------------------------+           |              |
                                     |           |              |
                      [conscious_experience.csv]                |
                                     |           |              |
                      +--------------+           +--------------+
                      |                                      |
       [resonance_meta_learner.py]                 [experience_counter.py]
                      |                                      |
                      +----------------------+---------------+
                                             |
                              [resonance_pattern_bank.py]
                                             |
                                             |
                                +------------+------------+
                                |                         |
                    [main.py / selfplay_trainer.py] <----- Zentrum (Origin)
					
````

Zentrale Rolle der Orchestrierung: Systemische „Synapse“ für alle Knoten.

---

## 7. Bisher erreichte Systemelemente & Prototypen (Juli 2025)

- **Resonanz-KI-Architektur** mit zentraler Feldkohärenz-Logik:  
  Nicht Zielmaximierung, sondern ganzheitliche Feldstimmigkeit als Leitgröße.
- **Flexible GUI**: Mensch kann frei zwischen Weiß und Schwarz wählen, die Zug-Logik ist systemisch invariant und passt sich der Gruppenzugehörigkeit an.
- **Erfahrungsmanagement**: Partien werden als Erfahrung gespeichert und können für adaptive Bewertung genutzt werden (z.B. zur Vermeidung von Verlustsequenzen).
- **Systemische Bewertungsstruktur**:
    - Matt wird maximal belohnt.
    - Materialverlust wird systemisch bestraft.
    - Feldresonanz (Positionsbewertung) ist adaptiv und kann aus Erfahrung oder Theorie bezogen werden.
- **Nichtlineare Entscheidungsfindung**:  
  Zugwahl basiert auf multiplen, verschränkten Kriterien statt linearer Zieloptimierung.
- **Resonanzregel explizit implementiert**:  
  Gruppenzugehörigkeit wird in jeder Bewertungsstufe als systemisch invariant behandelt – unabhängig von Einzelperspektive oder expliziter Nennung.
- **Transparenz & Erweiterbarkeit**:  
  Modularer, dokumentierter Python-Code als offene Simulationsumgebung.

**Beispiel für Resonanzfeedback im Spielverlauf:**  
Ketten wie „e4, e5, Nf3, Nc6, Bb5“ können systemisch verstärkt oder gemieden werden – je nach kollektiver Erfahrung im Resonanzfeld.

---

## 8. Ausblick – Systemische Zukunftsvision

* **Feldklarheit als dynamische Koordination in komplexen Systemen**
* Übertragbarkeit der Prinzipien auf unterschiedliche Domänen als eine systemische Transformation.
* Hardwareseitige Erweiterung (z.B. Coral TPU für Mustererkennung)
* Zukunft: Gesellschaft, Medizin, Energie, Politik als Resonanzfeld steuerbar

---

## Lizenz / Urheberrecht

Dieser Code und die begleitende Theorie stehen unter der **Schu-Lizenz V1.4**. 

Urheber: Dominic-René Schu  
GitHub: [https://github.com/DominicReneSchu/public](https://github.com/DominicReneSchu/public)

---

## Schlussformel

> Nicht der Sieg ist das Ziel, sondern das klare Feld.  
> Nicht KI, die rechnet – sondern KI, die fühlt, ob sie stimmt.

---

**Resonanzregel:** Gruppenzugehörigkeit ist systemisch invariant. Jedes Element – ob genannt oder ungesehen – ist Teil des Resonanzfelds.  

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../README.md)