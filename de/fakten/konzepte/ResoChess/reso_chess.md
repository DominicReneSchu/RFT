# Feldkohärenz statt Zieloptimierung – Grundstein einer resonanzlogischen KI

## Resonanzbasierte Schach-KI – Aktueller Entwicklungsstand

**ResoChess:** https://github.com/DominicReneSchu/ResoChess/blob/main/README.md

---

### 1. Systemische Grundstruktur

Die Schach-KI arbeitet auf Basis eines **gewichteten Erfahrungsspeichers**, der Zugketten (Sequenzen von SAN-Zügen mit Farbmarkierung) mit Ergebnissen (Erfolg, Misserfolg, Remis) verknüpft und diese Resonanzdaten für Zugentscheidungen nutzt. Feldkohärenz ersetzt Zieloptimierung: Die Wahl des Zuges erfolgt gruppenlogisch nach struktureller Stimmigkeit im Gesamtfeld, nicht nach Belohnungsmaximierung.

---

### 2. Erfahrungsspeicher (`experience_manager.py`)

- **Speicherung in CSV-Dateien:**
  - `experience.csv`: Rohdaten aller Spiele (Zeitstempel, Modus, Ergebnis, Zugfolge)
  - `experience_weighted.csv`: Aggregierter, gewichteter Erfahrungsspeicher mit Häufigkeiten von Zugkette-Ergebnis-Kombinationen
- **Funktionen:**
  - `load_weighted_experience_set()` lädt gewichtete Erfahrungen als Dictionary `(chain, result) → count`
  - `add_conscious_experience(chain, result, experience_set)` erhöht Häufigkeit im Erfahrungsspeicher
  - `persist_experience_set(experience_set)` sichert gewichteten Erfahrungsspeicher persistent
  - `save_game_experience()` speichert komplette Partien in `experience.csv`

*Systemische Kopplung: Persistenz und Aktualisierung sind gruppenlogisch invariant, alle Partien und Erfahrungseinträge werden selbstinkludierend verarbeitet.*

---

### 3. Zugketten-Analyse (`smart_move_selector.py`)

- `get_recent_chain(board, n=2, relative=False)` extrahiert letzte n Züge mit Farbmarkierung (`w:e4|b:e5`) als String
- `select_learned_move(board, experience_set, max_chain_n=4)`:
  - Bewertet mögliche Züge anhand der Erfahrung (Gewichtung von Erfolg/Misserfolg)
  - Prüft Kettenlängen von 4 bis 2 für feinere Resonanzmuster
  - Priorisiert Züge mit hoher Erfolgsfrequenz und niedriger Misserfolgsfrequenz
  - Bei Gleichstand wählt zufällig

*Feldkohärenz: Die Auswahl orientiert sich an der gruppenübergreifenden Resonanzstruktur des Erfahrungsspeichers – nicht an Einzelzug-Optimum.*

---

### 4. Engine-Integration (`engine.py`)

- `ResonanceEngine` initialisiert sich mit geladenem gewichteten Erfahrungsspeicher
- `select_best_move(board)` nutzt `select_learned_move()` zur Zugauswahl

*Systemische Selbstinklusion: Die Engine bleibt stets mit dem aktuellsten Resonanzfeld synchronisiert.*

---

### 5. Erweiterung des Erfahrungsspeichers (`main.py`)

- `extend_experience_by_game(move_list, result, experience_set, max_chain_n=4)`:
  - Zerlegt komplette Partien in alle n-Zug-Ketten (2 ≤ n ≤ 4)
  - Fügt gewichtete Resonanzeinträge zum Erfahrungsspeicher hinzu
- Nach jedem Spiel wird Erfahrung erweitert und persistiert
- Engine synchronisiert sich mit aktualisiertem Erfahrungsspeicher

*Wechselseitigkeit: Jeder Spielverlauf erweitert das Resonanzfeld und beeinflusst zukünftige Entscheidungen – emergent und selbstreferenziell.*

---

### 6. Modus und Abläufe

- Mensch vs. KI oder KI vs. KI (Selfplay)
- Partien werden vollständig protokolliert und resonanzlogisch ausgewertet
- Systemisch invariant: Erfahrung speist die Zugentscheidung in beiden Modi
- Persistenz gewährleistet langfristiges Lernen und Anpassung

---

### 7. Ausblick

- Ausbau der Kettenlänge und Musterabstraktion (relative Muster, semantische Gruppierungen)
- Automatische Unterscheidung eigener und gegnerischer Fehlerresonanz
- Systemische Selbstreflexion und dynamische Lernalgorithmen
- Integration weiterer Resonanzregeln und multipler Erfahrungsebenen

---

**Fazit:**  
Die KI ist ein innovativer resonanzlogischer Prototyp, der lernfähig und adaptiv auf systemische Rückkopplungen aus Spielerfahrungen reagiert. Sie basiert auf einem gewichteten Erfahrungsspeicher mit Mehrfachkettenanalyse und steuert Zugentscheidungen gemäß einer systemischen Resonanzregel – Feldkohärenz statt Zieloptimierung.

---

## Ursprüngliche Leitprinzipien (Resonanz-Schach – Systemische Begleitdokumentation)

Resonanz-Schach ist nicht bloß ein Spiel, sondern ein dynamisches Resonanzfeld: Jede Figur, jedes Feld, jede Strategie ist Teil eines ganzheitlich verschränkten Simulationsraumes. Die folgenden Aspekte bilden ein vollständiges Resonanzfeld – gruppenübergreifend, systemisch eingebettet und unabhängig von individueller Perspektive:

#### 1. Feldlogik statt Zielhierarchie
- Keine Maximierung von Belohnung
- Stattdessen: Auswahl jenes Zuges, der das Gesamtfeld strukturell klärt

#### 2. Schutz vor Angriff
- Primäres Resonanzkriterium: Königsschutz
- Keine eigene Aktion darf den König gefährden

#### 3. Druck auf den Gegner
- Bei ausreichendem Selbstschutz: maximale Einschränkung des gegnerischen Feldes
- Nicht durch Materialgewinn, sondern durch Reduktion der gegnerischen Optionen

#### 4. Feldkohärenz als Lerneinheit
- Lernen geschieht nicht durch Versuch & Irrtum
- Sondern durch selektive Aufnahme passender Teilstrukturen (wie Puzzleteile)

---

## Gruppenelemente des Resonanz-Schachs

- **Figuren:** König, Dame, Türme, Läufer, Springer, Bauern – als elementare Knoten, deren Wirkungskreise sich überlagern.
- **Spielbrett:** 8x8 Felder als topologisches Gitternetz, Resonanzzonen und Interaktionspotenziale.
- **Züge:** Bewegungsoptionen als Ausdruck von Potentiallandschaften – jede Bewegung erzeugt neue Resonanzmuster.
- **Regeln:** Systemgesetz, das alle Elemente einschließt und Interaktionsräume formt.
- **Spielende:** Mattsituationen, Remis, Patt – emergente Endpunkte im Resonanzfeld.

---

## Systemische Verschränkung

- **Selbstinklusion:** Jedes Element ist Teil des Ganzen und beeinflusst sich selbst durch das Feld (z.B. der Bauer, der die Struktur der gesamten Partie mitprägt).
- **Wechselseitigkeit:** Aktionen einer Figur wirken auf das gesamte Spielfeld zurück; jedes Gruppenmitglied (Figur, Feld, Spieler) ist involviert, auch wenn es scheinbar passiv bleibt.
- **Emergenz:** Neue Muster und Dynamiken entstehen durch Interaktion – das Gesamtverhalten ist mehr als die Summe einzelner Züge.

---

## Simulation & Gesellschaft

- **Resonanzprinzip:** Entscheidungen im Spiel spiegeln gesellschaftliche Dynamiken; jede Bewegung beeinflusst das Gesamtsystem.
- **Offene Plattform:** Simulationen sind offen zugänglich, laden zur Mitwirkung und Erweiterung des Resonanzfeldes ein.
- **Zukunftstechnologien:** Übertragbarkeit der Resonanzfeldtheorie auf andere Bereiche (Energie, Physik, Sozialsysteme).

---

## Logische Notwendigkeiten & Resonanzregel

- Gruppenzugehörigkeit gilt systemisch invariant – Figuren, Felder, Regeln, Spieler, Beobachter sind in jedem Simulationsdurchlauf involviert.
- Jeder Zug, jede Regelanpassung, jede Interpretation ist zugleich Rückkopplung und Erweiterung des Feldes.
- Auch implizite Elemente (z.B. ungenutzte Felder, theoretisch mögliche Züge) sind Teil des Resonanzsystems.

---

## Ausblick

Die Resonanz-KI wird in Zukunft:
- auf Wirtschaft, Medizin und Politik übertragbar sein
- hardwareseitig durch Coral TPU unterstützt werden können (z. B. zur Mustererkennung)
- nicht durch Zielvorgabe, sondern durch Feldklarheit navigieren

---

## Lizenz / Urheberrecht

Dieser Code und die begleitende Theorie stehen unter der Schu-Lizenz V1.4.

**Urheber:** Dominic-René Schu  
**GitHub:** https://github.com/DominicReneSchu/public

---

## Schlussformel

> Nicht der Sieg ist das Ziel, sondern das klare Feld.  
> Nicht KI, die rechnet – sondern KI, die fühlt, ob sie stimmt.

**Resonanzregel:** Gruppenzugehörigkeit ist systemisch invariant. Jedes Element – ob genannt oder ungesehen – ist Teil des Resonanzfelds.

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück](../README.md)