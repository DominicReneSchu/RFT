"""
ResoAgent — Minimales Beispiel der 4-Schichten-Architektur.

Zeigt den vollständigen Durchlauf:
  Aufgabe → Klassifikation → Erfahrung → Guard → NN → Entscheidung → Audit

Basiert auf der Resonanzfeldtheorie (RFT):
  E = π · ε(Δφ) · ℏ · f
  → Kopplungseffizienz ε bestimmt, wie stark Aufgabe und Quelle resonieren.
"""

import math
from dataclasses import dataclass, field


# ══════════════════════════════════════════════════════════════
# SCHICHT 1 — Klassifikation
# ══════════════════════════════════════════════════════════════

SICHERHEITSSTUFEN = {
    "critical": ["auth", "crypto", "payment", "medical"],
    "high":     ["database", "api", "session", "admin"],
    "medium":   ["validation", "logging", "config", "cache"],
    "low":      ["formatting", "display", "sorting", "conversion"],
}

QUELLEN_HIERARCHIE = {
    "critical": ["rfc_standards", "owasp", "official_docs"],
    "high":     ["official_docs", "owasp", "reference_impl"],
    "medium":   ["official_docs", "stackoverflow_top", "github_popular"],
    "low":      ["official_docs", "stackoverflow", "tutorials"],
}


def classify_task(task: str, language: str = "python") -> dict:
    """Schicht 1: Regelbasierte Aufgaben-Klassifikation (Axiom A1, A5)."""
    t = task.lower()
    stufe = "low"
    for level, keywords in SICHERHEITSSTUFEN.items():
        if any(kw in t for kw in keywords):
            stufe = level
            break

    muster = "general"
    for m in ["auth", "crypto", "api", "database", "validation"]:
        if m in t:
            muster = m
            break

    return {
        "sprache": language,
        "stufe": stufe,
        "muster": muster,
        "chain": f"{language}|{stufe}|{muster}",
    }


# ══════════════════════════════════════════════════════════════
# SCHICHT 2 — Erfahrungsspeicher (3-Tier) + Pattern-Library
# ══════════════════════════════════════════════════════════════

@dataclass
class ExperienceStore:
    """
    Erfahrungsspeicher nach ResoTrade-Vorbild (Axiom A4).
    Chain → Result → Count, O(1)-Lookup.
    """
    fine: dict = field(default_factory=dict)
    coarse: dict = field(default_factory=dict)
    domain: dict = field(default_factory=dict)

    DECAY = 0.995

    def record(self, chain: str, source: str, outcome: str):
        """Erfahrung aufzeichnen."""
        fine_key = f"{chain}|{source}"
        coarse_key = f"{chain.split('|', 1)[1]}|{source}"
        domain_key = f"{chain.split('|')[1]}|{source}"

        for store, key in [
            (self.fine, fine_key),
            (self.coarse, coarse_key),
            (self.domain, domain_key),
        ]:
            if key not in store:
                store[key] = {"success": 0, "failure": 0, "draw": 0}
            store[key][outcome] += 1

    def confidence(self, chain: str, source: str) -> float:
        """
        Kopplungseffizienz ε zwischen Aufgabe und Quelle (Axiom A4).
        Fallback-Kette: Fine → Coarse → Domain → 0.5 (neutral).
        """
        fine_key = f"{chain}|{source}"
        if fine_key in self.fine:
            return self._score(self.fine[fine_key])

        parts = chain.split("|", 1)
        coarse_key = f"{parts[1]}|{source}" if len(parts) > 1 else fine_key
        if coarse_key in self.coarse:
            return self._score(self.coarse[coarse_key])

        domain_key = f"{chain.split('|')[1]}|{source}" if "|" in chain else fine_key
        if domain_key in self.domain:
            return self._score(self.domain[domain_key])

        return 0.5

    @staticmethod
    def _score(counts: dict) -> float:
        total = counts["success"] + counts["failure"] + counts["draw"]
        if total == 0:
            return 0.5
        return counts["success"] / total

    def apply_decay(self):
        """Graduelles Vergessen (Axiom A4: Kopplungsenergie zerfällt)."""
        for store in [self.fine, self.coarse, self.domain]:
            for key in store:
                for outcome in store[key]:
                    store[key][outcome] *= self.DECAY


def pattern_match(chain: str, library: list, threshold: float = 0.7) -> dict | None:
    """
    Schicht 2: Pattern-Matching via Cosinus-Ähnlichkeit (Axiom A3).
    Resonanzbedingung: Ähnlichkeit ≥ Schwelle → Kopplung.
    """
    chain_set = set(chain.split("|"))
    best, best_score = None, 0.0

    for pattern in library:
        p_set = set(pattern["chain"].split("|"))
        intersection = len(chain_set & p_set)
        union = len(chain_set | p_set)
        score = intersection / union if union > 0 else 0.0

        if score >= threshold and score > best_score:
            best, best_score = pattern, score

    return best


# ══════════════════════════════════════════════════════════════
# SCHICHT 3 — Guard & Audit
# ══════════════════════════════════════════════════════════════

GUARD_RULES = [
    {
        "name": "crypto_rule",
        "patterns": ["md5", "sha1", "des", "ecb", "random.random"],
        "severity": "BLOCK",
        "fix": "Verwende bcrypt/argon2 (Passwort) oder AES-256-GCM",
    },
    {
        "name": "injection_rule",
        "patterns": ["f\"select", "f'select", "format(\"select"],
        "severity": "BLOCK",
        "fix": "Parameterisierte Queries verwenden",
    },
]


def guard_check(code: str, classification: dict) -> list:
    """Schicht 3: Schutzregeln prüfen (Axiom A6: Informationsintegrität)."""
    issues = []
    code_lower = code.lower()

    for rule in GUARD_RULES:
        for pattern in rule["patterns"]:
            if pattern in code_lower:
                issues.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": f"Pattern '{pattern}' erkannt",
                    "fix": rule["fix"],
                })

    if classification["stufe"] in ("critical", "high"):
        issues.append({
            "rule": "audit_note",
            "severity": "INFO",
            "message": f"Stufe '{classification['stufe']}' — nur geprüfte Quellen",
        })

    return issues


def generate_audit_trail(classification: dict, source: str,
                         guard_results: list, confidence: float) -> dict:
    """Audit-Trail: Jede Entscheidung nachvollziehbar (Axiom A6)."""
    return {
        "chain": classification["chain"],
        "stufe": classification["stufe"],
        "quelle": source,
        "konfidenz": round(confidence, 3),
        "guard_checks": len(guard_results),
        "blockaden": sum(1 for g in guard_results if g["severity"] == "BLOCK"),
        "bestanden": all(g["severity"] != "BLOCK" for g in guard_results),
    }


# ══════════════════════════════════════════════════════════════
# SCHICHT 4 — NN-Entscheidung (vereinfacht)
# ══════════════════════════════════════════════════════════════

def nn_decision(classification: dict, experience_conf: float,
                guard_blocks: int) -> tuple:
    """
    Schicht 4: Neuronales Entscheidungs-Herzstück (vereinfacht).

    Echtes System: ~75k Parameter
      Input(60) → Dense(256,ReLU) → Dense(128,ReLU) → Dense(64,ReLU) → Softmax(3)

    Hier: Regelbasierte Approximation mit ε(Δφ) = cos²(Δφ/2).
    """
    # Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) aus RFT-Grundformel
    delta_phi = math.pi * (1.0 - experience_conf)
    epsilon = math.cos(delta_phi / 2) ** 2

    if guard_blocks > 0:
        return "reject", 0.95
    elif epsilon >= 0.7:
        return "compose", epsilon
    elif epsilon >= 0.4:
        return "adapt", epsilon
    else:
        return "reject", 1.0 - epsilon


# ══════════════════════════════════════════════════════════════
# PIPELINE — Vollständiger Durchlauf
# ══════════════════════════════════════════════════════════════

def process_task(task: str, experience: ExperienceStore,
                 pattern_library: list) -> dict:
    """
    Vollständige ResoAgent-Pipeline.

    Aufgabe → Klassifikation → Erfahrung → Pattern → Guard → NN → Entscheidung
    """
    # Schicht 1
    cls = classify_task(task)
    sources = QUELLEN_HIERARCHIE[cls["stufe"]]

    # Schicht 2: Beste Quelle nach Erfahrung
    best_source, best_conf = sources[0], 0.5
    for src in sources:
        conf = experience.confidence(cls["chain"], src)
        if conf > best_conf:
            best_source, best_conf = src, conf

    # Schicht 2: Pattern-Check (Axiom A3)
    matched_pattern = pattern_match(cls["chain"], pattern_library)

    # Schicht 3: Guard-Check
    sample_code = f"# Code aus {best_source} fuer: {task}"
    guard_results = guard_check(sample_code, cls)
    blocks = sum(1 for g in guard_results if g["severity"] == "BLOCK")

    # Schicht 4: NN-Entscheidung
    action, nn_confidence = nn_decision(cls, best_conf, blocks)

    # Audit-Trail
    audit = generate_audit_trail(cls, best_source, guard_results, nn_confidence)

    # Experience-Update
    outcome = "success" if action == "compose" else "draw"
    experience.record(cls["chain"], best_source, outcome)

    return {
        "aufgabe": task,
        "klassifikation": cls,
        "quelle": best_source,
        "erfahrungs_konfidenz": round(best_conf, 3),
        "pattern_match": matched_pattern is not None,
        "entscheidung": action,
        "nn_konfidenz": round(nn_confidence, 3),
        "audit": audit,
    }


# ══════════════════════════════════════════════════════════════
# DEMO
# ══════════════════════════════════════════════════════════════

def demo():
    print("=" * 70)
    print("  ResoAgent — Resonanzlogische Agenten-KI (Beispiel)")
    print("  Grundformel: E = pi * epsilon(Delta_phi) * hbar * f")
    print("=" * 70)

    # Erfahrungsspeicher mit Vorerfahrung
    exp = ExperienceStore()
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|low|general", "tutorials", "success")
    exp.record("python|medium|validation", "official_docs", "success")

    # Pattern-Library (gelernte Muster)
    patterns = [
        {"chain": "python|critical|auth", "source": "owasp",
         "success_rate": 0.92},
        {"chain": "python|high|api", "source": "official_docs",
         "success_rate": 0.85},
        {"chain": "python|low|sorting", "source": "stackoverflow",
         "success_rate": 0.78},
    ]

    # Aufgaben durchlaufen
    tasks = [
        "Implement user authentication with bcrypt",
        "Sort a list of integers efficiently",
        "Create a REST api endpoint with input validation",
        "Implement AES-256 crypto encryption for payment data",
    ]

    for task in tasks:
        result = process_task(task, exp, patterns)

        print(f"\n{'─' * 70}")
        print(f"  Aufgabe:       {result['aufgabe']}")
        print(f"  Chain:         {result['klassifikation']['chain']}")
        print(f"  Stufe:         {result['klassifikation']['stufe']}")
        print(f"  Quelle:        {result['quelle']}")
        print(f"  epsilon:       {result['erfahrungs_konfidenz']}")
        print(f"  Entscheidung:  {result['entscheidung'].upper()}")
        print(f"  NN-Konfidenz:  {result['nn_konfidenz']}")
        print(f"  Pattern:       {'Match' if result['pattern_match'] else 'Kein Match'}")
        print(f"  Audit:         {'Bestanden' if result['audit']['bestanden'] else 'Blockade'}")

    print(f"\n{'=' * 70}")
    print(f"  Erfahrungsspeicher nach {len(tasks)} Aufgaben:")
    print(f"  Fine-Eintraege:   {len(exp.fine)}")
    print(f"  Coarse-Eintraege: {len(exp.coarse)}")
    print(f"  Domain-Eintraege: {len(exp.domain)}")
    print("=" * 70)


if __name__ == "__main__":
    demo()