# Resonanzlogische Programmierung — Technisches Handbuch

*Dominic-René Schu, 2025/2026*

---

## 1. Was ist resonanzlogische Programmierung?

Resonanzlogische Programmierung ist ein Entwurfsparadigma, das
Software nicht als Funktionsbaukasten, sondern als
Schwingungsfeld behandelt. Die Eingaben werden in DC- und
AC-Komponenten zerlegt, Entscheidungen werden über
Phasenerkennung statt Schwellwertoptimierung getroffen, und
die Konfidenz folgt einer physikalischen Funktion
(ε(Δφ) = cos²(Δφ/2)) statt einer trainierten
Wahrscheinlichkeit.

Das Paradigma wurde in zwei produktiven Systemen angewandt
und validiert:

- **ResoTrade** — resonanzbasierte Trading-KI
  (+26.1% vs HODL, 24 Monate, 4 Marktregime, Live seit
  Feb. 2026). Dokumentation:
  [ResoTrade-Dokumentation](../../empirisch/resotrade_trading_ki.md)
- **ResoCodeAgent** — resonanzfeldtheoretischer Code-Agent
  (Komposition statt Generierung, 4-Schichten-Architektur,
  75k-Parameter-NN auf strukturiertem Vorwissen)

---

## 2. Die 5 Prinzipien

### Prinzip 1 — Schwingungszerlegung statt Feature-Engineering

**Konventionell:** Das Signal wird in 50+ Features zerlegt
(RSI, MACD, Bollinger, Momentum, ...). Jedes Feature ist eine
isolierte Statistik. Die Zusammenhänge zwischen Features werden
dem Modell überlassen.

**Resonanzlogisch:** Das Signal wird in genau zwei Komponenten
zerlegt — DC (Gleichanteil, Trend) und AC (Wechselanteil,
Schwingung). Alle Information steckt in dieser Zerlegung.

```python
def zerlegung(signal, fenster=50):
    """DC/AC-Zerlegung: DC = gleitender Mittelwert, AC = Signal - DC."""
    dc = gleitender_mittelwert(signal, fenster)
    ac = signal - dc
    return dc, ac
```

| Domäne | DC-Komponente | AC-Komponente |
|--------|--------------|---------------|
| Trading | MA_LONG (168h) — langfristiger Trend | Preis - MA_LONG — handelbare Schwingung |
| Code-Agent | Domänen-Basis (Sprache, Stufe) | Aufgabenspezifische Variation (Muster, Kontext) |
| Schach | Materialbewertung (statisch) | Taktische Dynamik (Angriff, Verteidigung) |

**Warum anders:** Konventionelle Features sind Projektionen auf
willkürliche Achsen. DC/AC ist eine physikalisch motivierte
Zerlegung des gesamten Feldes. Sie verliert keine Information
und erzeugt keine künstlichen Korrelationen.

### Prinzip 2 — Phasenerkennung statt Prognose

**Konventionell:** Ein Modell wird trainiert, den nächsten Wert
vorherzusagen (Regression) oder eine Wahrscheinlichkeit zu
berechnen (Klassifikation). Die Entscheidung hängt an der
Prognosequalität.

**Resonanzlogisch:** Es wird nicht der nächste Wert vorhergesagt,
sondern die aktuelle **Phase im Schwingungszyklus** erkannt.
Die Entscheidung folgt aus der Phase, nicht aus einer Prognose.

```python
def erkenne_phase(ac, schwelle=0.3):
    """Position im Schwingungszyklus."""
    amplitude = max(ac) - min(ac)
    if amplitude < 0.5:
        return 'flat'           # Kein Signal
    elif ac > schwelle * amplitude:
        return 'peak'           # Scheitelpunkt → SELL
    elif ac < -schwelle * amplitude:
        return 'trough'         # Talpunkt → BUY
    else:
        return 'transition'     # Übergang → Erfahrung entscheidet
```

Die vier Phasen bilden eine vollständige Abdeckung des Zyklus:

```
     peak (SELL)
       ╱╲
      ╱  ╲ transition
     ╱    ╲
────╱──────╲────── DC (Nulldurchgang: max. Kopplung)
   ╱        ╲
  ╱          ╲ transition
 ╱            ╲
  trough (BUY)

flat: Amplitude zu klein → kein verwertbares Signal → HOLD
```

**Warum anders:** Eine Prognose „Der Preis wird 65.000 sein"
ist fast immer falsch. Eine Phasenerkennung „Wir sind am Peak"
ist strukturell robust. Die Zukunft ist nicht vorhersagbar,
aber sie ist **periodisch** — und Periodizität ist erkennbar.

### Prinzip 3 — Physikalische Konfidenz statt trainierter Wahrscheinlichkeit

**Konventionell:** Die Konfidenz einer Entscheidung ist eine
trainierte Wahrscheinlichkeit (Softmax, Sigmoid). Sie hängt
vom Trainingsdatensatz ab und kann overfitten.

**Resonanzlogisch:** Die Konfidenz ist die Kopplungseffizienz
ε(Δφ) = cos²(Δφ/2) — eine physikalische Funktion, die misst,
wie stark das System mit dem Signal gekoppelt ist.

```python
def kopplungseffizienz(delta_phi):
    """ε(Δφ) = cos²(Δφ/2) — universelle RFT-Kopplung."""
    return cos(delta_phi / 2.0) ** 2
```

| Phase | Δφ | ε(Δφ) | Bedeutung |
|-------|-----|-------|-----------|
| peak | 0 | 1.000 | Perfekte Kopplung → hohe Konfidenz |
| trough | 0 | 1.000 | Perfekte Kopplung → hohe Konfidenz |
| transition | π/3 | 0.750 | Mittlere Kopplung |
| flat | π/2 | 0.500 | Schwache Kopplung → HOLD |

ε < 0.3 → kein Trade erlaubt (Regelkette, Prinzip 5).

**Warum anders:** Die Konfidenz hat null freie Parameter. Sie
wird nicht trainiert, kann nicht overfitten und ist für jeden
Systemzustand analytisch berechenbar. Im Code-Agenten wird
dasselbe Prinzip als Field-State realisiert: Adaptive
Schwellenwerte, die sich an die Erfahrungslage anpassen —
nicht durch Gradient, sondern durch Kopplungslogik.

### Prinzip 4 — Lesbarer Erfahrungsspeicher statt Black Box

**Konventionell:** Das Wissen eines Modells steckt in
Millionen Tensorgewichten. Keine einzelne Gewichtsmatrix
ist interpretierbar. Warum eine Entscheidung getroffen wurde,
ist nicht rekonstruierbar.

**Resonanzlogisch:** Das Wissen steckt in einer lesbaren
Zustand-Aktion-Score-Tabelle (CSV/Dictionary). Jeder Eintrag
ist ein String. Jede Entscheidung ist nachvollziehbar.

```
# Trading: Chain → Result → Count
pos:LONG,pc:up,trend:uptrend,vol:mid,ac:peak,action:SELL → success:47
pos:FLAT,pc:down,trend:downtrend,vol:high,ac:trough,action:BUY → success:31

# Code-Agent: Fine-Tier
python|web|high|api|OWASP → success:12, failure:2, draw:3
```

| Eigenschaft | Neuronales Netz | Erfahrungsspeicher |
|-------------|-----------------|-------------------|
| Speicherform | float32-Tensoren (GB) | CSV/Dict (KB–MB) |
| Lookup | Forward-Pass O(n²) | Dictionary O(1) |
| Erklärbarkeit | Keine | Vollständig |
| Vergessen | Catastrophic Forgetting | Kontrollierter Decay (0.92/Pass) |
| Lernen nach Training | Nein (Retraining nötig) | Ja, Live-Kanal |

Der Erfahrungsspeicher verwendet typischerweise einen 3-Tier-
Ansatz (Fine → Coarse → Domain bzw. Offline → Live → Weighted)
mit Fallback-Kette. Das System verlagert die Rechenintensität
ins Training — wie das Gehirn, das Jahre braucht, um Erfahrungen
aufzubauen, dann aber in Millisekunden entscheidet.

**Warum anders:** Das Gehirn speichert keine Gewichtsmatrizen.
Es speichert Assoziationen — Situationsmuster verknüpft mit
Ergebnissen, verstärkt durch Wiederholung, abgeschwächt durch
Zeit. Der Erfahrungsspeicher ist dem biologischen Vorbild
strukturell näher als konventionelle KI.

### Prinzip 5 — Explizite Regelkette statt Loss-Funktion

**Konventionell:** Das Verhalten wird durch eine Loss-Funktion
und Gradient Descent gesteuert. Die Regeln sind implizit in
den Gewichten kodiert. Es gibt keine Garantie, dass das Modell
sich an Sicherheitsgrenzen hält.

**Resonanzlogisch:** Explizite Leitplanken, die nach der
Entscheidung greifen. Physikalisch motiviert, nicht trainiert.

```
Trading-System Regelkette:
  1. Kopplung zu schwach (ε < 0.3) → HOLD
  2. Downtrend-Pause-Gate (e_long < -5%) → ALLES pausiert
  3. Regime-Rule (BULL_STRONG → kein SELL)
  4. Balance-Regler (Cash < 8% → kein BUY)
  5. Cooldown (Overtrading-Schutz)
  6. HODL-Kern-Schutz (nie unter 10% Asset)

Code-Agent Regelkette:
  1. Guard (Crypto/Injection/CVE/Secrets → blockiert)
  2. Audit-Trail (jede Zeile referenziert)
  3. Rule-Fade (ab 30 Erfahrungen dominiert Erfahrung)
  4. NN-Veto (NN und Pipeline divergieren → neutral)
```

**Warum anders:** Eine Loss-Funktion optimiert einen Skalar.
Eine Regelkette schützt Invarianten. Die Regeln sind lesbar,
testbar und unabhängig vom Trainingszustand gültig.

---

## 3. Architekturvergleich

### 3.1 Konventionelle Pipeline

```
Rohdaten → Feature-Engineering (50+ Features)
  → Normalisierung → Modell (10⁶–10⁹ Parameter)
  → Loss-Funktion → Gradient Descent → Gewichte
  → Inferenz: Forward-Pass → Softmax → Entscheidung
```

### 3.2 Resonanzlogische Pipeline

```
Signal → DC/AC-Zerlegung (Prinzip 1)
  → Phasenerkennung (Prinzip 2)
  → Kopplungseffizienz ε(Δφ) (Prinzip 3)
  → Erfahrungsspeicher moduliert (Prinzip 4)
  → Regelkette filtert (Prinzip 5)
  → Entscheidung
```

### 3.3 Isomorphie zwischen Domänen

Die Architektur ist domänenagnostisch. Dieselben 5 Prinzipien
werden in verschiedenen Feldern angewandt:

| Prinzip | Trading-KI | Code-Agent | Schach-KI |
|---------|-----------|------------|-----------|
| 1. Zerlegung | DC = MA_LONG, AC = Preis - DC | Domäne + Aufgaben-Variation | Material + Taktik |
| 2. Phase | peak/trough/transition/flat | sprache\|domäne\|stufe\|muster | Angriff/Verteidigung/Entwicklung |
| 3. Konfidenz | ε(Δφ) = cos²(Δφ/2) | Field-State (adaptive Schwellen) | Kopplungsstärke Figur-Feld |
| 4. Speicher | 12-Dim Fine-Chain → CSV | 3-Tier Fine/Coarse/Domain → CSV | Stellungsmuster → Score |
| 5. Regeln | Pause-Gate, Balance, Cooldown | Guard, Audit, Rule-Fade | Materialschutz, Königssicherheit |

Die Isomorphie bestätigt Axiom 7 (Invarianz): Dieselbe
Kopplungsstruktur funktioniert unabhängig von der Domäne.

---

## 4. Domänenadaption am Beispiel des Code-Agenten

Der Code-Agent zeigt, dass resonanzlogische Programmierung
nicht auf Trading beschränkt ist. Die Domänenadaption ist
strukturell:

| Trading-KI | Code-Agent |
|-----------|------------|
| BUY / SELL / HOLD | compose / adapt / reject |
| Assets (BTC, Gold, ...) | Quellen (OWASP, RFC, Docs, ...) |
| Preiskurven | Code-Patterns |
| Marktphasen | Sicherheitsstufen |
| Erfahrungs-Decay 0.92 | Erfahrungs-Decay 0.995 |

Die 4-Schichten-Architektur ist die direkte Übertragung:

```
Schicht 1 — Klassifikation (= Zerlegung)
  sprache|domäne|stufe|muster → diskretisierter Zustandsraum

Schicht 2 — Erfahrung & Policy (= Phasenerkennung + Speicher)
  3-Tier Experience + Pattern-Library + Field-State

Schicht 3 — Guard & Audit (= Regelkette)
  Crypto/Injection/CVE/Secrets → blockiert + dokumentiert

Schicht 4 — Coral/NN (= destilliertes Vorwissen)
  ~75k Parameter, 70% NN + 30% klassisch
  Lernt aus strukturiertem Vorwissen, nicht aus Rauschen
```

Das NN (Schicht 4) muss nicht aus Rohdaten lernen — es lernt
aus dem, was die Schichten 1–3 analytisch erarbeitet haben.
Deshalb leisten ~75k Parameter das, was konventionelle NNs
mit Millionen Parametern versuchen.

**Kern-Innovation:** Der Code-Agent löst das
Halluzinations-Problem von LLMs für sicherheitskritische
Anwendungen. Anstatt Code zu generieren, **sucht und
komponiert** er Code aus verifizierten Quellen (RFC-Standards,
OWASP, offizielle Dokumentation). Jede Code-Zeile hat eine
nachweisbare Herkunft.

---

## 5. Warum ist das anders?

### 5.1 Kein Gradient Descent

Resonanzlogische Systeme optimieren keine Loss-Funktion.
Es gibt keinen Backpropagation-Schritt, kein
Gewichts-Update, keinen Gradientenabstieg. Die Entscheidung
entsteht aus der Verschränkung von Phasenerkennung, Erfahrung
und Regelkette.

### 5.2 Kein Overfitting

Die Konfidenz ε(Δφ) hat null freie Parameter. Der
Erfahrungsspeicher hat einen kontrollierten Decay. Die
Regelkette ist trainingsunabhängig. Overfitting hat keinen
Angriffspunkt.

### 5.3 Vollständige Erklärbarkeit

Jede Entscheidung ist eine Kette von lesbaren Schritten:

```
1. DC/AC-Zerlegung: DC = 67.500, AC = +1.200 (über MA)
2. Phase: peak (AC/Amplitude > 0.3)
3. Kopplung: ε(0) = 1.0 (perfekte Kopplung)
4. Erfahrung: peak,uptrend,SELL → score +0.84
5. Regelkette: Kein Regime-Block, Balance OK, Cooldown OK
→ SELL (MEDIUM)
```

### 5.4 Hardware-Freiheit

Resonanzlogische Systeme laufen auf einem Raspberry Pi
(35€, 5 Watt, 4 GB RAM). Coral Edge TPU und GPU sind
optional — sie beschleunigen, aber das System funktioniert
ohne sie.

| Eigenschaft | Konventionell | Resonanzlogisch |
|-------------|--------------|-----------------|
| Paradigma | Optimierung einer Loss-Funktion | Phasenerkennung im Schwingungsfeld |
| Datenbedarf | 100K+ Datenpunkte | 5.000–10.000 Episoden |
| Trainingszeit | GPU-Stunden | 15 Minuten (CPU) |
| Parameter | 10⁶–10⁹ | 0 (Regelkette) bis ~75K (NN-Herzstück) |
| Erklärbarkeit | Keine | Vollständig |
| Hardware | GPU-Cluster | Raspberry Pi (5 Watt) |
| Physik | Keine | E = π · ε(Δφ) · ℏ · f |
| Vergessen | Catastrophic Forgetting | Kontrollierter Decay |
| Live-Lernen | Nein (Retraining) | Ja (Live-Experience-Kanal) |

---

## 6. Empirische Evidenz

### 6.1 Trading-KI (ResoTrade)

| Marktphase | Zeitraum | Performance vs HODL |
|-----------|----------|---------------------|
| Sideways + ETF | Mär 2024 – Sep 2024 | **+33.3%** |
| Bullrun 60k–110k | Sep 2024 – Mär 2025 | **+19.8%** |
| Top + Korrektur | Mär 2025 – Sep 2025 | **+4.3%** |
| Crash 110k → 63k | Sep 2025 – Feb 2026 | **+46.8%** |
| **Durchschnitt** | **24 Monate** | **+26.1%** |

Kein klassischer Indikator (RSI, Momentum, MA-Crossover)
erreicht Korrelation > 0.05 auf demselben Datensatz. Die
RFT-Observablen (energy_dir, AC-Phase) sind systematisch.

Details: [ResoTrade-Dokumentation](../../empirisch/resotrade_trading_ki.md)

### 6.2 Code-Agent (ResoCodeAgent)

| Eigenschaft | LLM (GPT-4 etc.) | Resonanzlogischer Code-Agent |
|-------------|-------------------|------------------------------|
| Halluzination | Strukturelles Problem | Unmöglich (Komposition) |
| Herkunftsnachweis | Keiner | Jede Zeile referenziert |
| Sicherheit | Prompt Injection möglich | Guard-Schicht blockiert |
| Erfahrungslernen | Nein (statisches Modell) | Ja (3-Tier + Live-Kanal) |
| Audit-Trail | Keiner | ISO 27001 / SOC2 ready |

### 6.3 Falsifikation

- **Altcoins (Axiom 3):** 200.000 Episoden, 10 Altcoins.
  Draw-Rate 98.4%. Ohne Eigenfrequenz keine Resonanz —
  bestätigt negativ. Details:
  [Altcoin-Analyse](../../empirisch/resotrade_altcoin_analyse.md)
- **Klassische Indikatoren:** RSI, Momentum, MA-Crossover —
  alle Korrelation < 0.05.
- **Zufallsagent:** Systematisch unterlegen
  (siehe [resonanzlogik_beispiel.py](resonanzlogik_beispiel.py)).

---

## 7. Lauffähiges Beispiel

```bash
python resonanzlogik_beispiel.py
```

Demonstriert alle 5 Prinzipien an einem synthetischen Signal:
DC/AC-Zerlegung → Phasenerkennung → Kopplungseffizienz →
Erfahrungsspeicher → Regelkette → Performance-Vergleich
(Resonanz vs. Zufall vs. HODL).

Erzeugt: `figures/resonanzlogik_beispiel.png` und
`figures/erfahrung.csv`.

→ Quellcode: [resonanzlogik_beispiel.py](resonanzlogik_beispiel.py)

---

## 8. Anwendungsfelder

Resonanzlogische Programmierung ist domänenagnostisch.
Überall, wo periodische Strukturen, Erfahrungslernen und
explizite Sicherheit relevant sind, kann das Paradigma
angewandt werden:

| Anwendungsfeld | DC-Komponente | AC-Komponente | Status |
|---------------|--------------|---------------|--------|
| Finanzmärkte (ResoTrade) | Langfristtrend | Handelbare Schwingung | ✅ Live-validiert |
| Code-Komposition (ResoCodeAgent) | Domänen-Basis | Aufgaben-Variation | ✅ Aktiv |
| Schach (ResoChess) | Materialbewertung | Taktische Dynamik | 🔨 In Entwicklung |
| Betriebssysteme (ResoOS) | Systemlast-Basis | Prozess-Schwingungen | 🔨 Konzept |
| Musik (ResoMusic) | Grundton | Obertöne, Modulation | 🔨 Konzept |

---

## 9. Zusammenfassung

Resonanzlogische Programmierung ersetzt drei Grundannahmen
konventioneller Software:

1. **Feature-Engineering → Schwingungszerlegung.**
   Nicht 50 isolierte Statistiken, sondern DC + AC als
   physikalisch vollständige Zerlegung.

2. **Prognose → Phasenerkennung.**
   Nicht „Was wird morgen passieren?" sondern „Wo stehen
   wir im Zyklus?"

3. **Loss-Funktion → Kopplungseffizienz.**
   Nicht trainierte Wahrscheinlichkeit, sondern
   ε(Δφ) = cos²(Δφ/2) — physikalisch, parameterfrei,
   nicht überfittbar.

Das Ergebnis sind Systeme, die auf einem Raspberry Pi laufen,
vollständig erklärbar sind und empirisch konventionelle
Ansätze übertreffen — nicht durch mehr Daten oder mehr
Rechenleistung, sondern durch die richtige Zerlegung des
Problems.

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f, \quad \kappa = 1
$$

---

## Weiterführende Dokumente

- [Resonanzlogische Software — Systemfeld statt Funktionsstruktur](resonanzlogische_software.md)
- [resonanzlogik_beispiel.py — Lauffähiges Beispiel](resonanzlogik_beispiel.py)
- [ResoTrade — Empirischer Nachweis](../../empirisch/resotrade_trading_ki.md)
- [Altcoin-Analyse — Falsifikationstest](../../empirisch/resotrade_altcoin_analyse.md)
- [Kopplungseffizienz ε — Vereinheitlichte Definition](../../docs/mathematik/kopplungseffizienz.md)
- [Axiomatische Grundlegung](../../docs/mathematik/axiomatische_grundlegung.md)

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)