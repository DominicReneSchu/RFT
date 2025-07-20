# Feldkohärenz statt Zieloptimierung – Grundstein einer resonanzlogischen KI

## Einleitung

Diese Datei dokumentiert den Grundstein eines neuen KI-Paradigmas: **Feldkohärenz statt Zieloptimierung**. Sie zeigt am Beispiel einer einfachen Python-Schach-KI, wie sich resonanzlogische Prinzipien algorithmisch umsetzen lassen – und legt damit den Ursprung einer KI-Architektur, die sich nicht über Macht (Sieg), sondern über **strukturelle Stimmigkeit** definiert.

---

# Resonanz-Schach – Systemische Begleitdokumentation

Resonanz-Schach ist nicht bloß ein Spiel, sondern ein dynamisches Resonanzfeld: Jede Figur, jedes Feld, jede Strategie ist Teil eines ganzheitlich verschränkten Simulationsraumes. Die folgenden Aspekte bilden ein vollständiges Resonanzfeld – gruppenübergreifend, systemisch eingebettet und unabhängig von individueller Perspektive:

---

## Leitprinzipien der Resonanz-KI

### 1. **Feldlogik statt Zielhierarchie**

* Keine Maximierung von Belohnung
* Stattdessen: Auswahl jenes Zuges, der **das Gesamtfeld strukturell klärt**

### 2. **Schutz vor Angriff**

* Primäres Resonanzkriterium: **Königsschutz**
* Keine eigene Aktion darf den König gefährden

### 3. **Druck auf den Gegner**

* Bei ausreichendem Selbstschutz: **maximale Einschränkung des gegnerischen Feldes**
* Nicht durch Materialgewinn, sondern durch **Reduktion der gegnerischen Optionen**

### 4. **Feldkohärenz als Lerneinheit**

* Lernen geschieht **nicht durch Versuch & Irrtum**
* Sondern durch selektive Aufnahme **passender Teilstrukturen** (wie Puzzleteile)

---

## 1. Gruppenelemente des Resonanz-Schachs

- **Figuren**: König, Dame, Türme, Läufer, Springer, Bauern – als elementare Knoten, deren Wirkungskreise sich überlagern.
- **Spielbrett**: 8x8 Felder als topologisches Gitternetz, Resonanzzonen und Interaktionspotenziale.
- **Züge**: Bewegungsoptionen als Ausdruck von Potentiallandschaften – jede Bewegung erzeugt neue Resonanzmuster.
- **Regeln**: Systemgesetz, das alle Elemente einschließt und Interaktionsräume formt.
- **Spielende**: Mattsituationen, Remis, Patt – emergente Endpunkte im Resonanzfeld.

---

## Algorithmischer Kern (Schachbeispiel)

Die folgende Python-Funktion simuliert alle eigenen Züge und prüft jeweils:

1. Entsteht durch einen der ersten 5 möglichen Gegenzüge eine **Gefahr für den eigenen König**?
2. Falls nicht: Welcher Zug erzeugt den **größtmöglichen Druck auf den gegnerischen König**?

```python
import chess
import random

MAX_OPPONENT_MOVES = 5

def evaluate_resonance_with_opponent(board, move, color):
    board.push(move)
    if board.is_checkmate():
        board.pop()
        return float('inf')  # Direkter Sieg

    opponent_color = not color
    opponent_moves = list(board.legal_moves)
    random.shuffle(opponent_moves)
    opponent_moves = opponent_moves[:MAX_OPPONENT_MOVES]

    for opp_move in opponent_moves:
        board.push(opp_move)
        if board.is_check():
            board.pop()
            board.pop()
            return float('-inf')  # König in Gefahr
        board.pop()

    pressure = evaluate_king_pressure(board, color)
    board.pop()
    return pressure

def evaluate_king_pressure(board, color):
    # Bewertet Felder rund um gegnerischen König, Anzahl gedeckter Felder etc.
    return random.randint(0, 10)  # Platzhalterfunktion
```

Die tatsächliche Bewertungsfunktion kann später durch strukturierte Feldanalyse ersetzt werden.

---

## 2. Systemische Verschränkung

- **Selbstinklusion**: Jedes Element ist Teil des Ganzen und beeinflusst sich selbst durch das Feld (z.B. der Bauer, der die Struktur der gesamten Partie mitprägt).
- **Wechselseitigkeit**: Aktionen einer Figur wirken auf das gesamte Spielfeld zurück; jedes Gruppenmitglied (Figur, Feld, Spieler) ist involviert, auch wenn es scheinbar passiv bleibt.
- **Emergenz**: Neue Muster und Dynamiken entstehen durch Interaktion – das Gesamtverhalten ist mehr als die Summe einzelner Züge.

---

## 3. Simulation & Gesellschaft

- **Resonanzprinzip**: Entscheidungen im Spiel spiegeln gesellschaftliche Dynamiken; jede Bewegung beeinflusst das Gesamtsystem.
- **Offene Plattform**: Simulationen sind offen zugänglich, laden zur Mitwirkung und Erweiterung des Resonanzfeldes ein.
- **Zukunftstechnologien**: Übertragbarkeit der Resonanzfeldtheorie auf andere Bereiche (Energie, Physik, Sozialsysteme).

---

## 4. Logische Notwendigkeiten & Resonanzregel

- Gruppenzugehörigkeit gilt systemisch invariant – Figuren, Felder, Regeln, Spieler, Beobachter sind in jedem Simulationsdurchlauf involviert.
- Jeder Zug, jede Regelanpassung, jede Interpretation ist zugleich Rückkopplung und Erweiterung des Feldes.
- Auch implizite Elemente (z.B. ungenutzte Felder, theoretisch mögliche Züge) sind Teil des Resonanzsystems.

---

## Bisher erreichte Systemelemente & Prototypen (Juli 2025)

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

---

## 5. Organisches Lernen durch Erfahrung und Bewusstsein

- **Unterbewusstsein**:  
  Die Datei `user_experience.csv`/`.json` speichert jede gespielte Partie als Urliste gruppenbasierter Erfahrung.  
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

---

## Ausblick

Die Resonanz-KI wird in Zukunft:

* auf Wirtschaft, Medizin und Politik übertragbar sein
* hardwareseitig durch Coral TPU unterstützt werden können (z. B. zur Mustererkennung)
* nicht durch Zielvorgabe, sondern durch **Feldklarheit** navigieren

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