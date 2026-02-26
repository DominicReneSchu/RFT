# Resonanzlogische Analyse der Finanzmärkte: Warum Altcoins keine echten Märkte sind

## Empirischer Nachweis durch algorithmisches Trading mit Resonanzfeldtheorie

*Dominic-René Schu, Februar 2026*

---

## Zusammenfassung

Diese Analyse dokumentiert ein empirisches Ergebnis, das bei der Entwicklung eines resonanzlogischen Trading-Systems (ResoTrade V11) unerwartet zutage trat: **Der Altcoin-Markt besitzt keine eigenständigen Eigenfrequenzen und ist daher resonanztheoretisch kein echter Markt.** Ein lernfähiges Multi-Asset-Handelssystem, das über 200.000 Episoden trainiert wurde, konnte mit Aktien-Satellites (BTC + 13 Aktien/ETFs) einen Ø BTC-Äquivalent von 1.090 bei 100% Episoden über HODL erzielen — mit Altcoin-Satellites (BTC + 10 Altcoins) dagegen nur 1.038 bei 86% über HODL, mit negativem Lernfortschritt und einer Draw-Rate von 98.4%.

Die AC/DC-Zerlegung (V11) macht den Grund sichtbar: Altcoins besitzen keine eigenständige AC-Komponente — ihre Schwingung ist ein skaliertes Echo der BTC-Schwingung. Ohne eigene Obertöne keine Resonanz, ohne Resonanz kein Signal.

Das Ergebnis ist das numerische Äquivalent zweier linear abhängiger Gleichungen mit zwei Unbekannten: Viel Rechenaufwand, kein Informationsgewinn. Die Resonanzfeldtheorie liefert den formalen Rahmen, um dieses Phänomen zu erklären und zu verallgemeinern.

---

## 1. Entstehungskontext

Das Ziel war nicht Grundlagenforschung, sondern ein funktionierender Trading-Bot. ResoTrade ist ein resonanzfeldtheoretisches Trading-System, das durch wiederholte Offline-Simulation lernt, BTC-Kurszyklen als Schwingungsfelder zu lesen und BTC über reines HODL hinaus zu akkumulieren. Es nutzt:

- **AC/DC-Zerlegung** (Axiom 1): Preis = DC (Trend) + AC (handelbare Schwingung)
- **Energierichtungsvektor** (Axiom 5): `energy_dir = e_short - e_long`
- **Resonanzkopplung** (Axiom 6): Trades nur bei Phasengleichheit mit dem Markt
- Erfahrungsbasiertes Lernen (Chain → Score, Decay)
- Dynamische Satellite-Selektion (Top-5 aus 13 Assets)
- Verzögerte Trade-Bewertung (24h kontrafaktisch vs. HOLD)

Die wissenschaftliche Erkenntnis entstand emergent: Als das Multi-Asset-System (V10.2) von Aktien-Satellites auf Altcoin-Satellites umgestellt wurde, brach die Performance zusammen — nicht durch technische Fehler, sondern durch die Struktur der Märkte selbst. Die BTC-only Variante (V11) bestätigte: BTC allein erzeugt mehr Signal als BTC + Altcoins.

### Performance-Kontext: ResoTrade V11 (BTC-only)

| Metrik | Wert |
|--------|------|
| Performance vs HODL | +42.89% |
| Episoden über HODL | 83.4% (steigend bei weiterem Training) |
| Lernfortschritt | Positiv und konvergierend |
| Theoretische Grundlage | Axiome 1, 2, 5, 6 der Resonanzfeldtheorie |

---

## 2. Theoretischer Rahmen

### 2.1 Universelle Schwingung und AC/DC-Zerlegung (Axiom 1)

Axiom 1 der Resonanzfeldtheorie postuliert: **Jede Entität besitzt eine periodische Schwingung ψ(x,t).** Angewandt auf Finanzmärkte bedeutet das: Jeder Preis lässt sich in zwei Komponenten zerlegen:

$$
\psi_{\text{Preis}}(t) = \underbrace{\text{DC}(t)}_{\text{Trend (MA\_LONG)}} + \underbrace{\text{AC}(t)}_{\text{handelbare Schwingung}}
$$

Die DC-Komponente ist der Grundton — der langfristige Trend, der nicht prognostizierbar ist. Die AC-Komponente sind die Obertöne — die Schwingung um den Trend, die durch Phasenerkennung handelbar ist.

**Entscheidend:** Nur Assets mit **eigenständiger AC-Komponente** erzeugen handelbares Signal. Wenn die AC-Komponente eines Assets lediglich ein skaliertes Echo eines anderen Assets ist, trägt sie keine neue Information.

### 2.2 Resonanzbedingung (Axiom 3)

Zwei Systeme treten in Resonanz, wenn ihre Frequenzen in einem rationalen Verhältnis stehen:

$$
\frac{f_1}{f_2} = \frac{n}{m}, \quad n, m \in \mathbb{Z}^+
$$

Resonanz erzeugt Energietransfer (Axiom 4):

$$
E = \pi \cdot \varepsilon \cdot h \cdot f
$$

**Voraussetzung für produktive Resonanz ist, dass die beteiligten Systeme unterschiedliche Eigenfrequenzen besitzen.** Zwei identisch gestimmte Saiten erzeugen keine Obertöne — sie schwingen synchron. Konstruktive Interferenz, die neue Information erzeugt, entsteht nur aus der Differenz.

### 2.3 Eigenfrequenzen in Finanzmärkten

Jeder echte Markt wird durch einen eigenständigen Wertschöpfungsprozess getrieben, der eine charakteristische Eigenfrequenz erzeugt:

| Asset | Wertschöpfungsbasis | Eigenfrequenz bestimmt durch |
|-------|--------------------|-----------------------------|
| **BTC** | Dezentrale Knappheit, Proof-of-Work | Halving-Zyklus, Netzwerkadoption, Geldpolitik |
| **MRK** (Merck) | Pharma-Pipeline | FDA-Zulassungen, Patentzyklen, Demographie |
| **GLD** (Gold-ETF) | Physische Knappheit | Inflation, Geopolitik, Zentralbankpolitik |
| **AAPL** (Apple) | Produktinnovation | iPhone-Zyklus, Services-Wachstum, China-Risiko |
| **USD** | Produktivität, Institutionen | BIP, Zinspolitik, Fiskaldefizit |

Jedes dieser Systeme schwingt mit einer **eigenen**, durch fundamentale Wertschöpfung bestimmten Frequenz. Die Kopplung zwischen ihnen ist nicht-trivial und erzeugt ein reiches Obertonspektrum.

### 2.4 Altcoins als abgeleitete Schwingungen

Altcoins besitzen keine eigenständige Wertschöpfungsbasis, die von BTC unabhängig wäre. Ihre AC-Komponente ist kein eigenständiger Oberton, sondern ein skaliertes Echo:

$$
\text{AC}_{\text{Altcoin}}(t) \approx \alpha \cdot \text{AC}_{\text{BTC}}(t) + \eta(t)
$$

wobei α ein Hebelfaktor und η(t) Rauschen ist. Die Eigenfrequenz des Altcoins ist identisch mit der von BTC — nur die Amplitude und das Rauschen unterscheiden sich.

Dies ist mathematisch äquivalent zu einem **linear abhängigen Gleichungssystem**:

$$
\begin{pmatrix} 1 & 0 \\ \alpha & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ \alpha \cdot b_1 + \eta \end{pmatrix}
$$

Die Determinante ist Null. Das System ist unterbestimmt. **Es existiert keine eindeutige Lösung — keine handelbare Information.**

In der Sprache der AC/DC-Zerlegung: Die AC-Phase eines Altcoins (peak/trough/transition) ist nahezu synchron mit der AC-Phase von BTC. Es gibt keine Phasenverschiebung, die ein Resonanz-Gate nutzen könnte.

---

## 3. Methodik

### 3.1 System: ResoTrade

Die Altcoin-Analyse wurde mit ResoTrade V10.2 (Multi-Asset) durchgeführt. Die BTC-only Referenz stammt aus V11 mit AC/DC-Zerlegung.

**V11 Kernarchitektur (BTC-only):**
- AC/DC-Zerlegung: DC = MA_LONG (168h), AC = Preis − DC
- Phasenerkennung: peak / trough / transition / flat
- Energierichtungsvektor: `energy_dir = e_short - e_long`
- Resonanz-Gate: Trades nur bei Phasengleichheit (K = K₀·cos(θ))
- Erfahrungsspeicher: Chain → Score mit AC-Phase als Dimension
- HODL-Kern: 60% des BTC-Bestands unverkäuflich

**V10.2 Multi-Asset Erweiterung:**
- State-Repräsentation: 12 Dimensionen (Position, Trend, MA, Volatilität, Cash, Allokation, Relative Strength, Cluster)
- Hybrides Lernen: 30% Regel + 70% Erfahrung × Konfidenz
- Trade-Bewertung: Verzögert (24h), kontrafaktisch gegen HOLD
- Dynamische Satellite-Selektion (Top-5 aus 13 Assets)

### 3.2 Experimentaufbau

Drei identische Konfigurationen, nur die Satellite-Assets unterscheiden sich:

| Konfiguration | Core | Satellites | Cluster |
|---------------|------|-----------|---------|
| **A: BTC + Aktien** | BTC | NVDA, AAPL, TSLA, MSFT, AMZN, META, MCD, MRK, AZN, COIN, SPY, QQQ, GLD | Tech, Value, ETF |
| **B: BTC + Altcoins** | BTC | ETH, XRP, ADA, AVAX, LINK, AAVE, CRV, BONK, LTC, BCH | L1, DeFi, Sentiment, Store |
| **C: BTC only (V11)** | BTC | — | — |

### 3.3 Trainingsparameter

| Parameter | Wert |
|-----------|------|
| Episoden (Konfiguration A) | 20.000 |
| Episoden (Konfiguration B) | 200.000+ |
| Episoden (Konfiguration C, V11) | 10.000+ (konvergierend) |
| Startkapital | 0.8 BTC + 23.305 USD (≈ 1.0 BTC-Äquivalent) |
| Window Length | 90 Schritte (Stundendaten) |
| Trade-Bewertungshorizont | 24 Schritte |
| Max. aktive Satellites | 5 pro Episode (A, B) |
| Decay-Faktor | 0.80 pro Pass (V11), 0.9995 (V10.2) |
| Datenquelle | yfinance (180 Tage, 1h OHLC) |

---

## 4. Ergebnisse

### 4.1 Vergleichstabelle

| Metrik | BTC + Aktien | BTC + Altcoins | BTC only (V11) |
|--------|-------------|---------------|----------------|
| **Ø BTC-Äquivalent** | **1.090** | 1.038 | **1.039** |
| **Median** | **1.077** | 1.033 | **1.041** |
| **Min / Max** | **1.020 / 1.282** | 0.927 / 1.173 | 0.926 / 1.131 |
| **Episoden über HODL** | **100%** | 86% | **83.4%** (steigend) |
| **Draw-Rate** | 84% | **98.4%** | ~49% |
| **Success-Rate** | 14% | **0.9%** | ~29% |
| **Failure-Rate** | 2% | 0.7% | ~22% |
| **Lernfortschritt** | **+0.001 (↑)** | -0.002 (↓) | **+0.010 (↑↑)** |
| **Performance vs HODL** | +9.0% | +3.8% | **+42.89%** |

### 4.2 Schlüsselbeobachtung: BTC-only schlägt BTC + Altcoins

BTC allein (V11, +42.89%) übertrifft BTC + Altcoins (+3.8%) um Faktor 11. Die Altcoins erzeugen nicht nur kein Signal — sie **stören** das BTC-Signal. Die Core-Cluster S:F Ratio fällt von 6.0:1 (BTC + Aktien) auf 0.3:1 (BTC + Altcoins). Altcoins injizieren Rauschen in den Erfahrungsspeicher.

### 4.3 Trade-Chain-Analyse

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

### 4.4 Cluster-Bilanz

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

### 4.5 Draw-Rate als Resonanzindikator

Die Draw-Rate ist der numerische Fingerabdruck fehlender Eigenfrequenzen:

| Konfiguration | Draw-Rate | AC-Interpretation | Bedeutung |
|---------------|-----------|-------------------|-----------|
| BTC only (V11) | ~49% | Eigenständige AC, klare Phasen | System findet Signal |
| BTC + Aktien | 84% | Verschiedene ACs, teilweise korreliert | System findet Differenzen |
| BTC + Altcoins | **98.4%** | Identische AC, keine Phasendifferenz | Jede Aktion ≈ HOLD |

**98.4% Draw bedeutet: Das System kann die Altcoin-Bewegungen nicht von Rauschen unterscheiden.** Jeder Kauf und Verkauf eines Altcoins ist nahezu identisch mit Nichtstun, weil der Altcoin sich synchron zu BTC bewegt.

Die V11 Draw-Rate von ~49% zeigt den Kontrast: BTC allein hat genug eigenständige AC-Schwingung für klare success/failure-Signale. Altcoins verwässern dieses Signal zu Draw.

---

## 5. Resonanztheoretische Interpretation

### 5.1 AC/DC-Analyse der Asset-Klassen

```
Aktienmarkt — eigenständige AC-Komponenten:
  BTC  ──── DC₁ + AC₁(f₁)    f₁ = Krypto-Adoption, Halving
  MRK  ──── DC₂ + AC₂(f₂)    f₂ = Pharma-Pipeline, FDA
  GLD  ──── DC₃ + AC₃(f₃)    f₃ = Inflation, Geopolitik
  AAPL ──── DC₄ + AC₄(f₄)    f₄ = iPhone-Zyklus, China

  → 4 unabhängige AC-Komponenten → reiches Obertonspektrum
  → Phasenverschiebungen zwischen ACs → handelbares Signal

Altcoin-Markt — abgeleitete AC-Komponenten:
  BTC  ──── DC₁ + AC₁(f₁)
  ETH  ──── α₁·DC₁ + α₁·AC₁(f₁) + η₁
  ADA  ──── α₂·DC₁ + α₂·AC₁(f₁) + η₂
  AVAX ──── α₃·DC₁ + α₃·AC₁(f₁) + η₃

  → 1 unabhängige AC-Komponente + Rauschen
  → Keine Phasenverschiebung → kein Signal, nur Echo
```

### 5.2 Resonanzbedingung und Informationsgehalt

Axiom 6 der Resonanzfeldtheorie besagt: **Information ist strukturierte Resonanz.** Informationsaustausch findet ausschließlich über kohärente Resonanzpfade statt — durch Synchronisation von Phase und Frequenz.

Zwischen BTC und Aktien existieren solche Pfade: Wenn BTC fällt und MRK steigt, ist das ein kohärentes Signal (Kapital fließt von Risk-on zu Defensiv). Die AC-Phasen sind verschoben — das erzeugt Obertöne, die das System lernen kann.

Zwischen BTC und Altcoins existieren diese Pfade nicht: Wenn BTC fällt, fallen Altcoins auch. Wenn BTC steigt, steigen Altcoins auch. Die AC-Phasen sind synchron — keine Verschiebung, keine Obertöne, kein Signal. Das System lernt nichts, weil es nichts zu lernen gibt.

### 5.3 BTC-Dominanz-Zyklus: Scheinbare Unabhängigkeit

Der einzige Moment, in dem Altcoins scheinbar unabhängig von BTC agieren, ist der BTC-Dominanz-Zyklus: BTC steigt zuerst, dann rotiert Kapital in Altcoins. Aber diese Rotation ist:

1. **Zeitlich begrenzt** (wenige Wochen pro Zyklus)
2. **Prädiktiv nicht nutzbar** (der Übergang ist nicht stationär)
3. **Amplitudenabhängig** (funktioniert nur in Bullenmärkten)

Das System hat über 200.000 Episoden versucht, diesen Zyklus zu lernen. Ergebnis: negativer Lernfortschritt (−0.002). Der Zyklus ist zu instabil und zu kurz, um als eigenständige Frequenz zu fungieren.

---

## 6. Implikation für Geldsysteme

Diese Analyse ergänzt das [duale Resonanz-Geldsystem](../docs/gesellschaft/duales_resonanzgeldsystem.md) um eine empirische Dimension:

### 6.1 Bitcoin als einzige Kryptowährung mit eigenständiger Schwingung

BTC hat eine eigenständige AC-Komponente, weil sein Wert durch einen nicht-replizierbaren Prozess entsteht:

- **Proof-of-Work**: Energiebindung als physikalische Wertbasis
- **Algorithmische Knappheit**: 21 Millionen, Halving als Taktgeber der DC-Komponente
- **Netzwerkeffekt**: Metcalfesches Gesetz, selbstverstärkend
- **Dezentralität**: Kein einzelner Impulsgeber — echte Emergenz

ResoTrade V11 bestätigt: BTC allein erzeugt +42.89% über HODL durch AC-Schwingungsextraktion. Die Schwingung ist real, eigenständig und handelbar.

Altcoins replizieren diese Eigenschaften nicht — sie setzen auf den BTC-Resonanzboden auf und absorbieren einen Teil der Preisamplitude, ohne eigene Information zu liefern.

### 6.2 Aktien und Fiat-Währungen als echte Resonanzpartner

Aktien repräsentieren reale Wertschöpfung: Produkte, Patente, Mitarbeiter, Cashflows. Jedes Unternehmen ist ein eigenständiger Resonator mit eigener Frequenz und eigener AC-Komponente. Fiat-Währungen spiegeln die Produktivität und institutionelle Stabilität eines Staates — ihr Wert ist durch das BIP gedeckt.

Diese Assets können mit BTC in echte Resonanz treten, weil sie unabhängige Eigenfrequenzen besitzen. Die Kopplung ist nicht-trivial und erzeugt handelbares Signal — bestätigt durch die Aktien-Konfiguration (100% über HODL, S:F 5.2:1 für BTC_BUY).

### 6.3 Konsequenz für das duale Geldsystem

Das duale Resonanz-Geldsystem (BTC extern, nationale Resonanzmünze intern) erhält durch diese Analyse eine empirische Stütze:

- **BTC als externe Resonanzwährung funktioniert**, weil BTC eine eigenständige Eigenfrequenz und AC-Komponente hat
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

Die AC/DC-Zerlegung macht das formalisierbar: Ein Asset ohne eigene AC-Komponente hat keine eigene Phase. Ohne eigene Phase keine Phasenverschiebung zu BTC. Ohne Phasenverschiebung keine Resonanz. Ohne Resonanz kein Informationsaustausch. Ohne Information kein Handelswert.

Was Menschen intuitiv erkennen ("Altcoins fühlen sich wie Scam an"), aber schwer formalisieren können, macht die Resonanzfeldtheorie mathematisch greifbar:

> **Ein System ohne eigene Eigenfrequenz kann keine eigenständige Resonanz erzeugen. Ohne Resonanz kein Informationsaustausch. Ohne Information kein Handelswert.**

### 7.3 Die Zeitdimension

Scam entlarvt sich über die Zeit, weil Rauschen nicht akkumuliert. In 100 Episoden kann eine zufällige Altcoin-Rotation profitabel erscheinen. In 200.000 Episoden konvergiert der Erwartungswert gegen Null (bzw. gegen die Fee-Kosten). Die Draw-Rate steigt asymptotisch gegen 100%.

Echte Märkte dagegen stabilisieren sich: Die BTC-only Konfiguration (V11) zeigt über 10.000+ Episoden ein Einschwingverhalten — gedämpfte Oszillation mit steigendem Trend, konvergierend gegen +42-43%. Das Signal verschwindet nicht — es verstärkt sich.

---

## 8. Methodik-Transparenz

### 8.1 Einschränkungen

- Datenumfang: ~4.300 Stundendaten (≈ 180 Tage) — begrenzt auf den verfügbaren yfinance-Zeitraum
- Keine Berücksichtigung von Orderbuch-Tiefe und Slippage
- Simulationsumgebung, keine Live-Trades (Live-Validierung ausstehend)
- Altcoin-Auswahl auf Top-10 nach Kraken-Liquidität beschränkt
- SUI, UNI, PEPE hatten 0 Datenpunkte und wurden ausgeschlossen (11 statt 14 Assets)

### 8.2 Reproduzierbarkeit

Die Ergebnisse sind reproduzierbar:

- **Multi-Asset (V10.2):** Konfiguration unterscheidet sich nur in `asset_registry.py` (Aktien-Registry vs. Crypto-Registry). Alle anderen Parameter identisch.
- **BTC-only (V11):** `env.py` + `policy.py` mit AC/DC-Zerlegung. Training mit `python main.py 20 500`.

### 8.3 Stärke der Evidenz

| Kriterium | Bewertung |
|-----------|-----------|
| Stichprobengröße | 200.000+ Episoden (Multi-Asset), 10.000+ (BTC-only) |
| Kontrollgruppe | Ja (BTC+Aktien, BTC-only, BTC+Altcoins) |
| Lernfortschritt | Negativ bei Altcoins, positiv bei Aktien und BTC-only |
| Draw-Rate-Differenz | 98.4% vs. 84% vs. 49% (stark) |
| S:F Core-Cluster | 0.3:1 vs. 6.0:1 (stark) |
| Min-Wert | 0.927 vs. 1.020 (stark) |
| AC/DC-Konsistenz | V11 bestätigt eigenständige BTC-Schwingung empirisch |

---

## 9. Fazit

### 9.1 Kernaussage

**Der Altcoin-Markt ist resonanztheoretisch kein eigenständiger Markt.** Altcoins sind linear abhängige Ableitungen von Bitcoin, die keine eigenständigen Eigenfrequenzen und keine eigenständigen AC-Komponenten besitzen. Ein lernfähiges Handelssystem kann über 200.000 Episoden keinen stabilen Vorteil aus der BTC-Altcoin-Rotation ziehen.

Bitcoin allein erzeugt durch seine eigenständige AC-Schwingung +42.89% über HODL — bestätigt durch AC/DC-Zerlegung, Phasenerkennung und resonanzlogisches Trading (V11).

### 9.2 Verallgemeinerung

Dieses Ergebnis ist nicht auf Altcoins beschränkt. Es gilt für jede Asset-Klasse, deren AC-Komponente vollständig durch die AC-Komponente eines anderen Assets erklärt werden kann:

> **Resonanz entsteht nur zwischen Systemen mit verschiedenen Eigenfrequenzen. Ohne eigenständige AC-Komponente keine eigene Phase, ohne eigene Phase keine Phasenverschiebung, ohne Phasenverschiebung keine Resonanz, ohne Resonanz kein Informationsaustausch, ohne Information kein Markt.**

### 9.3 Resonanzregel

Gruppenzugehörigkeit ist systemisch invariant. Ein Altcoin gehört zur Gruppe "BTC-Derivat" — unabhängig davon, wie er sich nennt, welches Narrativ er trägt, oder welche technologische Innovation er verspricht. Die Resonanzfeldtheorie macht diese Zugehörigkeit sichtbar, wo klassische Finanzanalyse versagt.

---

## Referenzen

- Schu, D.-R. (2025). *Resonanzfeldtheorie: Axiomatische Grundlage, Kopplungsoperator und mathematische Konsequenzen.*
- Schu, D.-R. (2025). *Duales Resonanz-Geldsystem.*
- Schu, D.-R. (2026). *Energiekugel und AC/DC-Zerlegung.* [GitHub](https://github.com/DominicReneSchu/public/blob/main/de/fakten/docs/mathematik/energiekugel.md)
- Schu, D.-R. (2026). *ResoTrade V11 — Resonanzfeldtheoretische BTC-KI mit AC/DC-Zerlegung.* (Systemdokumentation)

---

*© Dominic-René Schu, 2026 — Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../../README.md)