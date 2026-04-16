# 🤖 ResoAgent — Resonanzlogische Agenten-KI

*Dominic-René Schu, 2025/2026*

Der **ResoAgent** ist eine Agenten-KI, die auf den Axiomen der
Resonanzfeldtheorie (RFT) operiert. Statt Code zu generieren,
**komponiert** der ResoAgent Code aus verifizierten Quellen —
jede Zeile ist rückverfolgbar. Vier aufeinander aufbauende Schichten
destillieren Sicherheitsregeln, Erfahrung und Pattern-Wissen in ein
neuronales Entscheidungs-Herzstück.

**Beispielcode:** [reso_agent_example.py](reso_agent_example.py)

---

## Grundidee

Das Halluzinations-Problem großer Sprachmodelle (LLMs) wird
systemisch gelöst: Der Agent generiert keinen Code, sondern
**sucht, bewertet und komponiert** Code aus geprüften Quellen
(RFC-Standards, OWASP, offizielle Dokumentation, bekannte
Bibliotheken). Jede Code-Zeile hat eine nachweisbare Herkunft.

**Domänen-Adaption aus ResoTrade:**

| ResoTrade | ResoAgent |
|-----------|-----------|
| BUY / SELL / HOLD | compose / adapt / reject |
| Assets (BTC, Gold, …) | Quellen (OWASP, RFC, Docs, …) |
| Preiskurven | Code-Patterns (strukturelle Ähnlichkeit) |
| Erfahrungsspeicher | 3-Tier Experience (Fine/Coarse/Domain) |
| Coral Edge TPU | NN-Herzstück (~75k Parameter) |

---

## 4-Schichten-Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                SCHICHT 4 — Coral/NN (~75k Parameter)        │
│     Destilliert Schichten 1–3 → optimale Quellen-Strategie  │
│           Gewicht: 70% NN + 30% klassische Pipeline         │
└───────────────────────┬─────────────────────────────────────┘
                        │ NN-Konfidenz fließt in Policy
┌───────────────────────┴─────────────────────────────────────┐
│                SCHICHT 3 — Guard & Audit                    │
│   Schutzregeln (Crypto/Injection/CVE/Secrets/Lizenz)        │
│   Vollständiger Audit-Trail (ISO 27001 / SOC2 ready)        │
└───────────────────────┬─────────────────────────────────────┘
                        │ Guard-Features → NN Input
┌───────────────────────┴─────────────────────────────────────┐
│             SCHICHT 2 — Erfahrung & Policy                  │
│   3-Tier Experience (Fine/Coarse/Domain) + Pattern-Library  │
│   Adaptive Schwellenwerte + Rule-Fade (ab 30 Erfahrungen)   │
└───────────────────────┬─────────────────────────────────────┘
                        │ Experience-Konfidenz → NN Input
┌───────────────────────┴─────────────────────────────────────┐
│              SCHICHT 1 — Klassifikation                     │
│   sprache | domäne | stufe | muster → Aufgaben-Vektor       │
└─────────────────────────────────────────────────────────────┘
```

### Vollständige Pipeline

```
Aufgabe → Klassifikation → Pattern-Match → Quellen-Ranking (NN + Erfahrung)
  → Retrieval → Guard-Check → Komposition → Audit-Trail → Experience-Update
```

---

## Axiom-Zuordnung

| Axiom | Anwendung im ResoAgent |
|-------|------------------------|
| A1 (Universelle Schwingung) | Aufgaben als Schwingungssignal — Zerlegung in Klassifikationsdimensionen |
| A2 (Superposition) | Überlagerung mehrerer Quellen-Signale zur Gesamtempfehlung |
| A3 (Resonanzbedingung) | Pattern-Match: Cosinus-Ähnlichkeit ≥ Schwelle → Resonanz erkannt |
| A4 (Kopplungsenergie) | Experience-Konfidenz als Kopplungsstärke zwischen Aufgabe und Quelle |
| A5 (Energierichtung) | compose / adapt / reject als gerichtete Entscheidung |
| A6 (Informationsfluss) | Guard-Regeln und Audit-Trail sichern Informationsintegrität |
| A7 (Invarianz) | Sprach- und domänenunabhängige Architektur (Python, JS, Rust, …) |

---

## Erfahrungssystem (3-Tier)

```
Fine:   sprache|domäne|stufe|muster|quelle → success/failure/draw
Coarse: stufe|muster|quelle               → generalisiert über Sprachen/Domänen
Domain: domäne|stufe|quelle               → aggregiert pro Domäne
```

**Fallback-Kette:** Fine → Coarse → Domain → 0.5 (neutral)

**Rule-Fade:** Ab 30 Erfahrungen dominiert Erfahrung über Regeln —
das System entwickelt sich von regelbasiert zu erfahrungsgetrieben.

---

## Quellen-Hierarchie

| Sicherheitsstufe | Quellen (Priorität absteigend) |
|------------------|-------------------------------|
| **critical** | RFC/NIST/ISO → OWASP → offizielle Docs → Referenzimpl. → intern geprüft |
| **high** | Offizielle Docs → OWASP → Referenzimpl. → SO (Score >50) → intern |
| **medium** | Offizielle Docs → SO (Score >50) → GitHub (>1000★) → intern |
| **low** | Offizielle Docs → SO → GitHub (>1000★) → Tutorials |

---

## Schutzregeln (Guard)

| Regel | Prüfung | Severity |
|-------|---------|----------|
| Crypto-Regel | Keine unsichere Kryptographie (MD5, SHA1, DES, ECB, rand()) | BLOCK |
| Injection-Regel | Keine String-Formatierung in SQL-Queries | BLOCK |
| Audit-Regel | Quelle muss zur Sicherheitsstufe passen | WARN |
| CVE-Regel | Keine bekannten Schwachstellen im Code | BLOCK |
| Lizenz-Regel | Keine inkompatiblen Lizenzen | WARN |

---

## Erweiterungen (V15.x)

| Version | Feature |
|---------|---------|
| V15.0 | Resonanz-Lernen — web-gestütztes Dimensions-Lernen |
| V15.1 | ManualTrainer — Kindheitsphase + CompletionStore |
| V15.2 | Dezentrales ResoAgent-Netz (mDNS, Port 7433, Erfahrungs-Sync) |
| V15.3 | Chat-Sessions + VocabularyCrawler |
| V15.4 | Kettenbasiertes Training (Vervollständigung) |
| V15.6 | Wartungs-Daemon + Parameter-Tuning im Dashboard |

---

## NN-Herzstück (Schicht 4)

```
Architektur: Input(60) → Dense(256, ReLU) → Dense(128, ReLU) → Dense(64, ReLU) → Dense(3, Softmax)
Parameter:   ~75.000
Output:      compose / adapt / reject
Backend:     NumPy (Fallback, immer verfügbar) | TensorFlow GPU | Coral TPU
Gewicht:     70% NN + 30% klassische Pipeline (nach Training)
```

**Input-Features (60 Dimensionen):**
- Klassifikations-Vektor (Sprache, Domäne, Stufe, Muster — one-hot, 30 dims)
- Experience-Konfidenz pro Quelle (Top-10, 10 dims)
- Pattern-Match-Scores (Top-5, 5 dims)
- Guard-Features (Blocks, Warnings, Severity, 5 dims)
- Quellen-Reputation (Top-10, 10 dims)

**Veto-Regeln:**
1. NN und klassische Pipeline divergieren (compose vs. reject) → adapt (neutral)
2. NN-Konfidenz < 0.4 → klassischer Fallback

Das NN destilliert, was die Schichten 1–3 analytisch erarbeitet haben —
dadurch genügen ~75k Parameter für das, was konventionelle NNs mit
Millionen Parametern versuchen.

---

## Design-Prinzipien

- **Komposition statt Generierung** — verifizierte Bausteine mit Herkunftsnachweis
- **3-Tier Erfahrung** — Fine → Coarse → Domain Fallback-Kette
- **Rule-Fade** — Ab 30 Erfahrungen dominiert Erfahrung über Regeln
- **NN als Herzstück** — destilliert Schichten 1–3, dominiert mit 70% Gewicht
- **Hardware-Kaskade** — Coral TPU → GPU → CPU → NumPy-Fallback
- **Atomic Writes** — alle Persistenz-Operationen sind atomar (tmp → rename)
- **Adaptive Schwellenwerte** — passen sich der Erfahrungslage an
- **Vollständiger Audit-Trail** — ISO 27001 / SOC2 / HIPAA / PCI-DSS ready

---

> „Komposition statt Generierung — jede Zeile hat eine Herkunft."

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)