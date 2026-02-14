# Resonanzlogische Analyse der Finanzmärkte: Warum Altcoins keine echten Märkte sind

## Empirischer Nachweis durch algorithmisches Trading mit Resonanzfeldtheorie

*Dominic Schu, Februar 2026*

---

## Zusammenfassung

Diese Analyse dokumentiert ein empirisches Ergebnis, das bei der Entwicklung eines resonanzlogischen Trading-Systems (ResoTrade V10.2) unerwartet zutage trat: **Der Altcoin-Markt besitzt keine eigenständigen Eigenfrequenzen und ist daher resonanztheoretisch kein echter Markt.** Ein lernfähiges Multi-Asset-Handelssystem, das über 200.000 Episoden trainiert wurde, konnte mit Aktien-Satellites (BTC + 13 Aktien/ETFs) einen Ø BTC-Äquivalent von 1.090 bei 100% Episoden über HODL erzielen — mit Altcoin-Satellites (BTC + 10 Altcoins) dagegen nur 1.038 bei 86% über HODL, mit negativem Lernfortschritt und einer Draw-Rate von 98.4%.

Das Ergebnis ist das numerische Äquivalent zweier linear abhängiger Gleichungen mit zwei Unbekannten: Viel Rechenaufwand, kein Informationsgewinn. Die Resonanzfeldtheorie liefert den formalen Rahmen, um dieses Phänomen zu erklären und zu verallgemeinern.

---

## 1. Entstehungskontext

Das Ziel war nicht Grundlagenforschung, sondern ein funktionierender Trading-Bot. ResoTrade V10.2 ist ein Multi-Asset-Handelssystem, das BTC-Akkumulation über reines HODL hinaus optimiert. Es nutzt:

- Resonanzanalyse (FFT, Amplituden, MA-Crossover)
- Erfahrungsbasiertes Lernen (Chain → Score, Decay)
- Dynamische Satellite-Selektion (Top-5 aus 13 Assets)
- Verzögerte Trade-Bewertung (24h kontrafaktisch vs. HOLD)
- Cluster-System (Asset-Gruppen mit unterschiedlicher BTC-Korrelation)

Die wissenschaftliche Erkenntnis entstand emergent: Als das System von Aktien-Satellites auf Altcoin-Satellites umgestellt wurde, brach die Performance zusammen — nicht durch technische Fehler, sondern durch die Struktur der Märkte selbst.

---

## 2. Theoretischer Rahmen

### 2.1 Resonanzbedingung (Axiom 3)

Zwei Systeme treten in Resonanz, wenn ihre Frequenzen in einem rationalen Verhältnis stehen:

$$
\frac{f_1}{f_2} = \frac{n}{m}, \quad n, m \in \mathbb{Z}^+
$$

Resonanz erzeugt Energietransfer (Axiom 4):

$$
E = \pi \cdot \varepsilon \cdot h \cdot f
$$

**Voraussetzung für produktive Resonanz ist, dass die beteiligten Systeme unterschiedliche Eigenfrequenzen besitzen.** Zwei identisch gestimmte Saiten erzeugen keine Obertöne — sie schwingen synchron. Konstruktive Interferenz, die neue Information erzeugt, entsteht nur aus der Differenz.

### 2.2 Eigenfrequenzen in Finanzmärkten

Jeder echte Markt wird durch einen eigenständigen Wertschöpfungsprozess getrieben, der eine charakteristische Eigenfrequenz erzeugt:

| Asset | Wertschöpfungsbasis | Eigenfrequenz bestimmt durch |
|-------|--------------------|-----------------------------|
| **BTC** | Dezentrale Knappheit, Proof-of-Work | Halving-Zyklus, Netzwerkadoption, Geldpolitik |
| **MRK** (Merck) | Pharma-Pipeline | FDA-Zulassungen, Patentzyklen, Demographie |
| **GLD** (Gold-ETF) | Physische Knappheit | Inflation, Geopolitik, Zentralbankpolitik |
| **AAPL** (Apple) | Produktinnovation | iPhone-Zyklus, Services-Wachstum, China-Risiko |
| **USD** | Produktivität, Institutionen | BIP, Zinspolitik, Fiskaldefizit |

Jedes dieser Systeme schwingt mit einer **eigenen**, durch fundamentale Wertschöpfung bestimmten Frequenz. Die Kopplung zwischen ihnen ist nicht-trivial und erzeugt ein reiches Obertonspektrum.

### 2.3 Altcoins als abgeleitete Schwingungen

Altcoins besitzen keine eigenständige Wertschöpfungsbasis, die von BTC unabhängig wäre:

$$
\psi_{\text{Altcoin}}(t) \approx \alpha \cdot \psi_{\text{BTC}}(t) + \eta(t)
$$

wobei $\alpha$ ein Hebelfaktor und $\eta(t)$ Rauschen ist. Die Eigenfrequenz des Altcoins ist identisch mit der von BTC — nur die Amplitude und das Rauschen unterscheiden sich.

Dies ist mathematisch äquivalent zu einem **linear abhängigen Gleichungssystem**:

$$
\begin{pmatrix} 1 & 0 \\ \alpha & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ \alpha \cdot b_1 + \eta \end{pmatrix}
$$

Die Determinante ist Null. Das System ist unterbestimmt. **Es existiert keine eindeutige Lösung — keine handelbare Information.**

---

## 3. Methodik

### 3.1 System: ResoTrade V10.2

- Multi-Asset Trading mit hybridem Lernansatz (30% Regel + 70% Erfahrung × Konfidenz)
- State-Repräsentation: 12 Dimensionen (Position, Trend, MA, Volatilität, Cash, Allokation, Relative Strength, Cluster)
- Trade-Bewertung: Verzögert (24h), kontrafaktisch gegen HOLD
- HODL-Kern: 60% des BTC-Bestands unverkäuflich
- Schutzregeln: ATH, Trend, MA, Allokationslimits

### 3.2 Experimentaufbau

Drei identische Konfigurationen, nur die Satellite-Assets unterscheiden sich:

| Konfiguration | Core | Satellites | Cluster |
|---------------|------|-----------|---------|
| **A: BTC + Aktien** | BTC | NVDA, AAPL, TSLA, MSFT, AMZN, META, MCD, MRK, AZN, COIN, SPY, QQQ, GLD | Tech, Value, ETF |
| **B: BTC + Altcoins** | BTC | ETH, XRP, ADA, AVAX, LINK, AAVE, CRV, BONK, LTC, BCH | L1, DeFi, Sentiment, Store |
| **C: BTC only** | BTC | — | — |

### 3.3 Trainingsparameter

| Parameter | Wert |
|-----------|------|
| Episoden (Konfiguration A) | 20.000 |
| Episoden (Konfiguration B) | 200.000+ |
| Startkapital | 0.8 BTC + 23.305 USD (≈ 1.0 BTC-Äquivalent) |
| Window Length | 90 Schritte (Stundendaten) |
| Trade-Bewertungshorizont | 24 Schritte |
| Max. aktive Satellites | 5 pro Episode |
| Decay-Faktor | 0.9995 |
| Datenquelle | yfinance (180 Tage, 1h OHLC) |

---

## 4. Ergebnisse

### 4.1 Vergleichstabelle

| Metrik | BTC + Aktien | BTC + Altcoins | BTC only (V9) |
|--------|-------------|---------------|---------------|
| **Ø BTC-Äquivalent** | **1.090** | 1.038 | 1.144 |
| **Median** | **1.077** | 1.033 | — |
| **Min / Max** | **1.020 / 1.282** | 0.927 / 1.173 | — |
| **Episoden über HODL** | **100%** | 86% | 100% |
| **Draw-Rate** | 84% | **98.4%** | ~80% |
| **Success-Rate** | 14% | **0.9%** | ~18% |
| **Failure-Rate** | 2% | 0.7% | ~2% |
| **Lernfortschritt** | **+0.001 (↑)** | -0.002 (↓) | +0.003 (↑) |
| **BTC_BUY S:F** | **5.2:1** | ∞:1 (7:0) | 4.2:1 |
| **BTC_SELL S:F** | 2.2:1 | **0.0:1** (0:21) | — |

### 4.2 Trade-Chain-Analyse

**Konfiguration A (BTC + Aktien):**

```
BTC_BUY_SMALL      S:F = 5.2:1    ← Profitabel
TSLA_SELL_SMALL    S:F = ∞:1      ← Informativ
MRK_SELL_SMALL     S:F = 2.8:1    ← Diversifikationsgewinn
AMZN_SELL_SMALL    S:F = 8.0:1    ← Unabhängiges Signal
```

**Konfiguration B (BTC + Altcoins):**

```
AVAX_SELL_SMALL    S:F = 0.9:1    ← Neutral (kein Signal)
BTC_SELL_SMALL     S:F = 0.0:1    ← Katastrophal
BCH_SELL_SMALL     S:F = ∞:1     ← Nur weil BCH chronisch fällt
CRV_SELL_SMALL     S:F = ∞:1     ← Draw-dominiert, kein Signal
```

### 4.3 Cluster-Bilanz

**Konfiguration A:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| crypto (BTC) | 6.0:1 | Starke Eigenmode |
| tech | 1.8:1 | Unabhängige Information |
| value | 8.0:1 | Höchste Diversifikation |
| etf | 0.8:1 | Geringste Eigenständigkeit |

**Konfiguration B:**

| Cluster | S:F | Interpretation |
|---------|-----|----------------|
| core (BTC) | 0.3:1 | **Durch Altcoins gestört** |
| l1 | 0.9:1 | Keine verwertbare Information |
| defi | ∞:1 | Draw-dominiert |
| store | ∞:1 | Draw-dominiert |
| sentiment | 0.0:1 | Reines Rauschen |

### 4.4 Kernbeobachtung: Draw-Rate als Resonanzindikator

Die Draw-Rate ist der numerische Fingerabdruck fehlender Eigenfrequenzen:

| Konfiguration | Draw-Rate | Bedeutung |
|---------------|-----------|-----------|
| BTC + Aktien | 84% | System findet handelbare Differenzen |
| BTC + Altcoins | **98.4%** | Fast jede Aktion ist äquivalent zu HOLD |
| BTC only | ~80% | BTC allein hat mehr Signal als BTC + Altcoins |

**98.4% Draw bedeutet: Das System kann die Altcoin-Bewegungen nicht von Rauschen unterscheiden.** Jeder Kauf und Verkauf eines Altcoins ist nahezu identisch mit Nichtstun, weil der Altcoin sich synchron zu BTC bewegt. Die 1.6% Nicht-Draw sind statistisches Rauschen, kein Signal.

---

## 5. Resonanztheoretische Interpretation

### 5.1 Eigenfrequenz-Analyse

```
Aktienmarkt:
  BTC  ────── f₁ (Krypto-Adoption, Halving)
  MRK  ────── f₂ (Pharma-Pipeline, FDA)
  GLD  ────── f₃ (Inflation, Geopolitik)
  AAPL ────── f₄ (iPhone-Zyklus, China)
  
  → 4 unabhängige Gleichungen, 4 Unbekannte → lösbar
  → Reiches Obertonspektrum → Handelbares Signal

Altcoin-Markt:
  BTC  ────── f₁
  ETH  ────── α₁·f₁ + η₁
  ADA  ────── α₂·f₁ + η₂
  AVAX ────── α₃·f₁ + η₃
  
  → 1 unabhängige Gleichung, n Unbekannte → unterbestimmt
  → Kein Obertonspektrum → Kein Signal, nur Echo
```

### 5.2 Resonanzbedingung und Informationsgehalt

Axiom 6 der Resonanzfeldtheorie besagt: **Information ist strukturierte Resonanz.** Informationsaustausch findet ausschließlich über kohärente Resonanzpfade statt — durch Synchronisation von Phase und Frequenz.

Zwischen BTC und Aktien existieren solche Pfade: Wenn BTC fällt und MRK steigt, ist das ein kohärentes Signal (Kapital fließt von Risk-on zu Defensiv). Das System kann diese Phasenverschiebung lernen und handeln.

Zwischen BTC und Altcoins existieren diese Pfade nicht: Wenn BTC fällt, fallen Altcoins auch. Wenn BTC steigt, steigen Altcoins auch. Es gibt keine Phasenverschiebung, keine kohärente Differenz, keinen Informationsgehalt. Das System lernt nichts, weil es nichts zu lernen gibt.

### 5.3 BTC-Dominanz-Zyklus: Scheinbare Unabhängigkeit

Der einzige Moment, in dem Altcoins scheinbar unabhängig von BTC agieren, ist der BTC-Dominanz-Zyklus: BTC steigt zuerst, dann rotiert Kapital in Altcoins. Aber diese Rotation ist:

1. **Zeitlich begrenzt** (wenige Wochen pro Zyklus)
2. **Prädiktiv nicht nutzbar** (der Übergang ist nicht stationär)
3. **Amplitudenabhängig** (funktioniert nur in Bullenmärkten)

Das System hat über 200.000 Episoden versucht, diesen Zyklus zu lernen. Ergebnis: negativer Lernfortschritt (-0.002). Der Zyklus ist zu instabil und zu kurz, um als eigenständige Frequenz zu fungieren.

---

## 6. Implikation für Geldsysteme

Diese Analyse ergänzt das [duale Resonanz-Geldsystem](../docs/gesellschaft/duales_resonanz_geldsystem.md) um eine empirische Dimension:

### 6.1 Bitcoin als einzige Kryptowährung mit innerem Wert

BTC hat eine eigenständige Eigenfrequenz, weil sein Wert durch einen nicht-replizierbaren Prozess entsteht:

- **Proof-of-Work**: Energiebindung als physikalische Wertbasis
- **Algorithmische Knappheit**: 21 Millionen, Halving als Taktgeber
- **Netzwerkeffekt**: Metcalfesches Gesetz, selbstverstärkend
- **Dezentralität**: Kein einzelner Impulsgeber

Altcoins replizieren diese Eigenschaften nicht — sie setzen auf den BTC-Resonanzboden auf und absorbieren einen Teil der Preisamplitude, ohne eigene Information zu liefern.

### 6.2 Aktien und Fiat-Währungen als echte Resonanzpartner

Aktien repräsentieren reale Wertschöpfung: Produkte, Patente, Mitarbeiter, Cashflows. Jedes Unternehmen ist ein eigenständiger Resonator mit eigener Frequenz. Fiat-Währungen spiegeln die Produktivität und institutionelle Stabilität eines Staates — ihr Wert ist durch das BIP gedeckt.

Diese Assets können mit BTC in echte Resonanz treten, weil sie unabhängige Eigenfrequenzen besitzen. Die Kopplung ist nicht-trivial und erzeugt handelbares Signal.

### 6.3 Konsequenz für das duale Geldsystem

Das duale Resonanz-Geldsystem (BTC extern, nationale Resonanzmünze intern) erhält durch diese Analyse eine empirische Stütze:

- **BTC als externe Resonanzwährung funktioniert**, weil BTC eine eigenständige Eigenfrequenz hat
- **Altcoins sind als Reservewährung ungeeignet**, weil sie keine eigenständige Information tragen
- **Nationale Währungen (gedeckt durch BIP) ergänzen BTC**, weil sie unabhängige Eigenfrequenzen besitzen

---

## 7. Warum Scam funktioniert — und warum er sich selbst entlarvt

### 7.1 Das Geschäftsmodell

Altcoins erzeugen die **Illusion** unabhängiger Märkte. Sie haben eigene Ticker, eigene Charts, eigene Narrativen. Die Preisbewegung suggeriert Unabhängigkeit — besonders in den kurzen Phasen der Altcoin-Season, wenn Kapital von BTC in Altcoins rotiert.

Diese Illusion reicht aus, um:
- Handelsgebühren zu generieren (Exchanges profitieren unabhängig von der Richtung)
- Spekulation zu befeuern (Hebel auf einen Hebel)
- Narrative zu verkaufen ("die nächste Ethereum-Killer-Chain")

### 7.2 Warum das System es entlarvt

Ein resonanzlogisches Handelssystem ist immun gegen Narrativen. Es bewertet nur: **Hat dieser Trade nach 24h besser performt als Nichtstun?** Wenn die Antwort über 200.000 Episoden in 98.4% der Fälle "identisch" lautet, ist die Schlussfolgerung zwingend: **Es gibt kein Signal.**

Was Menschen intuitiv erkennen ("Altcoins fühlen sich wie Scam an"), aber schwer formalisieren können, macht die Resonanzfeldtheorie mathematisch greifbar:

> **Ein System ohne eigene Eigenfrequenz kann keine eigenständige Resonanz erzeugen. Ohne Resonanz kein Informationsaustausch. Ohne Information kein Handelswert.**

### 7.3 Die Zeitdimension

Scam entlarvt sich über die Zeit, weil Rauschen nicht akkumuliert. In 100 Episoden kann eine zufällige Altcoin-Rotation profitabel erscheinen. In 200.000 Episoden konvergiert der Erwartungswert gegen Null (bzw. gegen die Fee-Kosten). Die Draw-Rate steigt asymptotisch gegen 100%.

Echte Märkte dagegen stabilisieren sich: Die Aktien-Konfiguration zeigte über 20.000 Episoden einen stabilen Ø von 1.090 mit positivem Lernfortschritt. Das Signal verschwindet nicht — es verstärkt sich.

---

## 8. Methodik-Transparenz

### 8.1 Einschränkungen

- Datenumfang: 4.159 Stundendaten (≈ 173 Tage) — begrenzt auf den verfügbaren yfinance-Zeitraum
- Keine Berücksichtigung von Orderbuch-Tiefe und Slippage
- Simulationsumgebung, keine Live-Trades
- Altcoin-Auswahl auf Top-10 nach Kraken-Liquidität beschränkt
- SUI, UNI, PEPE hatten 0 Datenpunkte und wurden ausgeschlossen (11 statt 14 Assets)

### 8.2 Reproduzierbarkeit

Die Ergebnisse sind reproduzierbar mit dem ResoTrade V10.2 System. Die Konfiguration unterscheidet sich nur in `asset_registry.py`:

- Konfiguration A: xStocks-Registry (13 Aktien/ETFs)
- Konfiguration B: Crypto-Registry (10 Altcoins)

Alle anderen Parameter (Policy, Bewertung, Schutzregeln, Decay) sind identisch.

### 8.3 Stärke der Evidenz

| Kriterium | Bewertung |
|-----------|-----------|
| Stichprobengröße | 200.000+ Episoden (stark) |
| Kontrollgruppe | Ja (BTC+Aktien, BTC-only) |
| Lernfortschritt | Negativ bei Altcoins, positiv bei Aktien (stark) |
| Draw-Rate-Differenz | 98.4% vs. 84% (14pp, stark) |
| S:F Core-Cluster | 0.3:1 vs. 6.0:1 (stark) |
| Min-Wert | 0.927 vs. 1.020 (stark) |

---

## 9. Fazit

### 9.1 Kernaussage

**Der Altcoin-Markt ist resonanztheoretisch kein eigenständiger Markt.** Altcoins sind linear abhängige Ableitungen von Bitcoin, die keine eigenständigen Eigenfrequenzen besitzen und daher keinen handelbaren Informationsgehalt erzeugen. Ein lernfähiges Handelssystem kann über 200.000 Episoden keinen stabilen Vorteil aus der BTC-Altcoin-Rotation ziehen.

### 9.2 Verallgemeinerung

Dieses Ergebnis ist nicht auf Altcoins beschränkt. Es gilt für jede Asset-Klasse, deren Preisbewegung vollständig durch ein anderes Asset erklärt werden kann:

> **Resonanz entsteht nur zwischen Systemen mit verschiedenen Eigenfrequenzen. Ohne Eigenfrequenz keine Resonanz, ohne Resonanz kein Informationsaustausch, ohne Information kein Markt.**

### 9.3 Resonanzregel

Gruppenzugehörigkeit ist systemisch invariant. Ein Altcoin gehört zur Gruppe "BTC-Derivat" — unabhängig davon, wie er sich nennt, welches Narrativ er trägt, oder welche technologische Innovation er verspricht. Die Resonanzfeldtheorie macht diese Zugehörigkeit sichtbar, wo klassische Finanzanalyse versagt.

---

## Referenzen

- Schu, D. (2025). *Resonanzfeldtheorie: Axiomatische Grundlage, Kopplungsoperator und mathematische Konsequenzen.*
- Schu, D. (2025). *Duales Resonanz-Geldsystem.*
- Schu, D. (2026). *ResoTrade V10.2 — Multi-Asset Resonanz-KI mit Kraken-Live-Trading.* (Systemdokumentation)

---

*© Dominic Schu, 2026 — Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../../README.md)