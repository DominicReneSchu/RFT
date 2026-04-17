# 🤖 ResoAgent — Resonance-Logic Agent AI

*Dominic-René Schu, 2025/2026*

The **ResoAgent** is an agent AI that operates on the axioms of
Resonance Field Theory (RFT). Instead of generating code,
the ResoAgent **composes** code from verified sources —
every line is traceable. Four mutually building layers
distil safety rules, experience and pattern knowledge into a
neural decision core.

**Example code:** [reso_agent_example.py](reso_agent_example.py)

---

## Core Idea

The hallucination problem of large language models (LLMs) is
solved systemically: The agent generates no code, but
**searches, evaluates and composes** code from vetted sources
(RFC standards, OWASP, official documentation, known
libraries). Every line of code has a provable origin.

**Domain adaptation from ResoTrade:**

| ResoTrade | ResoAgent |
|-----------|-----------|
| BUY / SELL / HOLD | compose / adapt / reject |
| Assets (BTC, Gold, …) | Sources (OWASP, RFC, Docs, …) |
| Price curves | Code patterns (structural similarity) |
| Experience store | 3-tier experience (Fine/Coarse/Domain) |
| Coral Edge TPU | NN core (~75k parameters) |

---

## 4-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                LAYER 4 — Coral/NN (~75k parameters)         │
│     Distils layers 1–3 → optimal source strategy            │
│           Weight: 70% NN + 30% classical pipeline           │
└───────────────────────┬─────────────────────────────────────┘
                        │ NN confidence flows into policy
┌───────────────────────┴─────────────────────────────────────┐
│                LAYER 3 — Guard & Audit                      │
│   Protection rules (Crypto/Injection/CVE/Secrets/Licence)   │
│   Full audit trail (ISO 27001 / SOC2 ready)                 │
└───────────────────────┬─────────────────────────────────────┘
                        │ Guard features → NN input
┌───────────────────────┴─────────────────────────────────────┐
│             LAYER 2 — Experience & Policy                   │
│   3-tier experience (Fine/Coarse/Domain) + pattern library  │
│   Adaptive thresholds + rule fade (from 30 experiences)     │
└───────────────────────┬─────────────────────────────────────┘
                        │ Experience confidence → NN input
┌───────────────────────┴─────────────────────────────────────┐
│              LAYER 1 — Classification                       │
│   language | domain | level | pattern → task vector         │
└─────────────────────────────────────────────────────────────┘
```

### Complete Pipeline

```
Task → Classification → Pattern match → Source ranking (NN + experience)
  → Retrieval → Guard check → Composition → Audit trail → Experience update
```

---

## Axiom Mapping

| Axiom | Application in ResoAgent |
|-------|--------------------------|
| A1 (Universal oscillation) | Tasks as oscillation signal — decomposition into classification dimensions |
| A2 (Superposition) | Superimposition of multiple source signals for overall recommendation |
| A3 (Resonance condition) | Pattern match: cosine similarity ≥ threshold → resonance detected |
| A4 (Coupling energy) | Experience confidence as coupling strength between task and source |
| A5 (Energy direction) | compose / adapt / reject as directed decision |
| A6 (Information flow) | Guard rules and audit trail secure information integrity |
| A7 (Invariance) | Language- and domain-independent architecture (Python, JS, Rust, …) |

---

## Experience System (3-Tier)

```
Fine:   language|domain|level|pattern|source → success/failure/draw
Coarse: level|pattern|source              → generalised across languages/domains
Domain: domain|level|source               → aggregated per domain
```

**Fallback chain:** Fine → Coarse → Domain → 0.5 (neutral)

**Rule fade:** From 30 experiences, experience dominates over rules —
the system evolves from rule-based to experience-driven.

---

## Source Hierarchy

| Security level | Sources (priority descending) |
|----------------|-------------------------------|
| **critical** | RFC/NIST/ISO → OWASP → official docs → reference impl. → internally vetted |
| **high** | Official docs → OWASP → reference impl. → SO (score >50) → internal |
| **medium** | Official docs → SO (score >50) → GitHub (>1000★) → internal |
| **low** | Official docs → SO → GitHub (>1000★) → tutorials |

---

## Protection Rules (Guard)

| Rule | Check | Severity |
|------|-------|----------|
| Crypto rule | No insecure cryptography (MD5, SHA1, DES, ECB, rand()) | BLOCK |
| Injection rule | No string formatting in SQL queries | BLOCK |
| Audit rule | Source must match security level | WARN |
| CVE rule | No known vulnerabilities in code | BLOCK |
| Licence rule | No incompatible licences | WARN |

---

## Extensions (V15.x)

| Version | Feature |
|---------|---------|
| V15.0 | Resonance learning — web-based dimension learning |
| V15.1 | ManualTrainer — childhood phase + CompletionStore |
| V15.2 | Decentralised ResoAgent network (mDNS, port 7433, experience sync) |
| V15.3 | Chat sessions + VocabularyCrawler |
| V15.4 | Chain-based training (completion) |
| V15.6 | Maintenance daemon + parameter tuning in dashboard |

---

## NN Core (Layer 4)

```
Architecture: Input(60) → Dense(256, ReLU) → Dense(128, ReLU) → Dense(64, ReLU) → Dense(3, Softmax)
Parameters:   ~75,000
Output:       compose / adapt / reject
Backend:      NumPy (fallback, always available) | TensorFlow GPU | Coral TPU
Weight:       70% NN + 30% classical pipeline (after training)
```

**Input features (60 dimensions):**
- Classification vector (language, domain, level, pattern — one-hot, 30 dims)
- Experience confidence per source (top-10, 10 dims)
- Pattern match scores (top-5, 5 dims)
- Guard features (blocks, warnings, severity, 5 dims)
- Source reputation (top-10, 10 dims)

**Veto rules:**
1. NN and classical pipeline diverge (compose vs. reject) → adapt (neutral)
2. NN confidence < 0.4 → classical fallback

The NN distils what layers 1–3 have worked out analytically —
this is why ~75k parameters suffice for what conventional NNs
attempt with millions of parameters.

---

## Design Principles

- **Composition instead of generation** — verified building blocks with provenance
- **3-tier experience** — Fine → Coarse → Domain fallback chain
- **Rule fade** — From 30 experiences, experience dominates over rules
- **NN as core** — distils layers 1–3, dominates with 70% weight
- **Hardware cascade** — Coral TPU → GPU → CPU → NumPy fallback
- **Atomic writes** — all persistence operations are atomic (tmp → rename)
- **Adaptive thresholds** — adapt to the current state of experience
- **Full audit trail** — ISO 27001 / SOC2 / HIPAA / PCI-DSS ready

---

> "Composition instead of generation — every line has a provenance."

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[Back to overview](../../../README.md)
