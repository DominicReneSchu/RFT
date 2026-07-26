"""
ResoAgent — Minimal example of the 4-layer architecture.

Shows the complete pipeline:
  Task → Classification → Experience → Guard → NN → Decision → Audit

Based on Resonance Field Theory (RFT):
  E = π · ε(Δφ) · ℏ · f
  → Coupling efficiency ε determines how strongly task and source resonate.
"""

import math
from dataclasses import dataclass, field


# ══════════════════════════════════════════════════════════════
# LAYER 1 — Classification
# ══════════════════════════════════════════════════════════════

SECURITY_LEVELS = {
    "critical": ["auth", "crypto", "payment", "medical"],
    "high":     ["database", "api", "session", "admin"],
    "medium":   ["validation", "logging", "config", "cache"],
    "low":      ["formatting", "display", "sorting", "conversion"],
}

SOURCE_HIERARCHY = {
    "critical": ["rfc_standards", "owasp", "official_docs"],
    "high":     ["official_docs", "owasp", "reference_impl"],
    "medium":   ["official_docs", "stackoverflow_top", "github_popular"],
    "low":      ["official_docs", "stackoverflow", "tutorials"],
}


def classify_task(task: str, language: str = "python") -> dict:
    """Layer 1: Rule-based task classification (Axiom A1, A5)."""
    t = task.lower()
    level = "low"
    for lvl, keywords in SECURITY_LEVELS.items():
        if any(kw in t for kw in keywords):
            level = lvl
            break

    pattern = "general"
    for m in ["auth", "crypto", "api", "database", "validation"]:
        if m in t:
            pattern = m
            break

    return {
        "language": language,
        "level": level,
        "pattern": pattern,
        "chain": f"{language}|{level}|{pattern}",
    }


# ══════════════════════════════════════════════════════════════
# LAYER 2 — Experience Store (3-Tier) + Pattern Library
# ══════════════════════════════════════════════════════════════

@dataclass
class ExperienceStore:
    """
    Experience store modeled after ResoTrade (Axiom A4).
    Chain → Result → Count, O(1) lookup.
    """
    fine: dict = field(default_factory=dict)
    coarse: dict = field(default_factory=dict)
    domain: dict = field(default_factory=dict)

    DECAY = 0.995

    def record(self, chain: str, source: str, outcome: str):
        """Record an experience."""
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
        Coupling efficiency ε between task and source (Axiom A4).
        Fallback chain: Fine → Coarse → Domain → 0.5 (neutral).
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
        """Gradual forgetting (Axiom A4: coupling energy decays)."""
        for store in [self.fine, self.coarse, self.domain]:
            for key in store:
                for outcome in store[key]:
                    store[key][outcome] *= self.DECAY


def pattern_match(chain: str, library: list, threshold: float = 0.7) -> dict | None:
    """
    Layer 2: Pattern matching via cosine similarity (Axiom A3).
    Resonance condition: similarity ≥ threshold → coupling.
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
# LAYER 3 — Guard & Audit
# ══════════════════════════════════════════════════════════════

GUARD_RULES = [
    {
        "name": "crypto_rule",
        "patterns": ["md5", "sha1", "des", "ecb", "random.random"],
        "severity": "BLOCK",
        "fix": "Use bcrypt/argon2 (password) or AES-256-GCM",
    },
    {
        "name": "injection_rule",
        "patterns": ["f\"select", "f'select", "format(\"select"],
        "severity": "BLOCK",
        "fix": "Use parameterized queries",
    },
]


def guard_check(code: str, classification: dict) -> list:
    """Layer 3: Check protection rules (Axiom A6: information integrity)."""
    issues = []
    code_lower = code.lower()

    for rule in GUARD_RULES:
        for pattern in rule["patterns"]:
            if pattern in code_lower:
                issues.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": f"Pattern '{pattern}' detected",
                    "fix": rule["fix"],
                })

    if classification["level"] in ("critical", "high"):
        issues.append({
            "rule": "audit_note",
            "severity": "INFO",
            "message": f"Level '{classification['level']}' — verified sources only",
        })

    return issues


def generate_audit_trail(classification: dict, source: str,
                         guard_results: list, confidence: float) -> dict:
    """Audit trail: every decision is traceable (Axiom A6)."""
    return {
        "chain": classification["chain"],
        "level": classification["level"],
        "source": source,
        "confidence": round(confidence, 3),
        "guard_checks": len(guard_results),
        "blocks": sum(1 for g in guard_results if g["severity"] == "BLOCK"),
        "passed": all(g["severity"] != "BLOCK" for g in guard_results),
    }


# ══════════════════════════════════════════════════════════════
# LAYER 4 — NN Decision (simplified)
# ══════════════════════════════════════════════════════════════

def nn_decision(classification: dict, experience_conf: float,
                guard_blocks: int) -> tuple:
    """
    Layer 4: Neural decision core (simplified).

    Real system: ~75k parameters
      Input(60) → Dense(256,ReLU) → Dense(128,ReLU) → Dense(64,ReLU) → Softmax(3)

    Here: Rule-based approximation with ε(Δφ) = cos²(Δφ/2).
    """
    # Coupling efficiency ε(Δφ) = cos²(Δφ/2) from the RFT base formula
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
# PIPELINE — Complete pipeline
# ══════════════════════════════════════════════════════════════

def process_task(task: str, experience: ExperienceStore,
                 pattern_library: list) -> dict:
    """
    Complete ResoAgent pipeline.

    Task → Classification → Experience → Pattern → Guard → NN → Decision
    """
    # Layer 1
    cls = classify_task(task)
    sources = SOURCE_HIERARCHY[cls["level"]]

    # Layer 2: Best source based on experience
    best_source, best_conf = sources[0], 0.5
    for src in sources:
        conf = experience.confidence(cls["chain"], src)
        if conf > best_conf:
            best_source, best_conf = src, conf

    # Layer 2: Pattern check (Axiom A3)
    matched_pattern = pattern_match(cls["chain"], pattern_library)

    # Layer 3: Guard check
    sample_code = f"# Code from {best_source} for: {task}"
    guard_results = guard_check(sample_code, cls)
    blocks = sum(1 for g in guard_results if g["severity"] == "BLOCK")

    # Layer 4: NN decision
    action, nn_confidence = nn_decision(cls, best_conf, blocks)

    # Audit trail
    audit = generate_audit_trail(cls, best_source, guard_results, nn_confidence)

    # Experience update
    outcome = "success" if action == "compose" else "draw"
    experience.record(cls["chain"], best_source, outcome)

    return {
        "task": task,
        "classification": cls,
        "source": best_source,
        "experience_confidence": round(best_conf, 3),
        "pattern_match": matched_pattern is not None,
        "decision": action,
        "nn_confidence": round(nn_confidence, 3),
        "audit": audit,
    }


# ══════════════════════════════════════════════════════════════
# DEMO
# ══════════════════════════════════════════════════════════════

def demo():
    print("=" * 70)
    print("  ResoAgent — Resonance-Logical Agent AI (Example)")
    print("  Base formula: E = pi * epsilon(Delta_phi) * hbar * f")
    print("=" * 70)

    # Experience store with prior experience
    exp = ExperienceStore()
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|critical|auth", "owasp", "success")
    exp.record("python|low|general", "tutorials", "success")
    exp.record("python|medium|validation", "official_docs", "success")

    # Pattern library (learned patterns)
    patterns = [
        {"chain": "python|critical|auth", "source": "owasp",
         "success_rate": 0.92},
        {"chain": "python|high|api", "source": "official_docs",
         "success_rate": 0.85},
        {"chain": "python|low|sorting", "source": "stackoverflow",
         "success_rate": 0.78},
    ]

    # Run tasks through the pipeline
    tasks = [
        "Implement user authentication with bcrypt",
        "Sort a list of integers efficiently",
        "Create a REST api endpoint with input validation",
        "Implement AES-256 crypto encryption for payment data",
    ]

    for task in tasks:
        result = process_task(task, exp, patterns)

        print(f"\n{'─' * 70}")
        print(f"  Task:          {result['task']}")
        print(f"  Chain:         {result['classification']['chain']}")
        print(f"  Level:         {result['classification']['level']}")
        print(f"  Source:        {result['source']}")
        print(f"  epsilon:       {result['experience_confidence']}")
        print(f"  Decision:      {result['decision'].upper()}")
        print(f"  NN confidence: {result['nn_confidence']}")
        print(f"  Pattern:       {'Match' if result['pattern_match'] else 'No match'}")
        print(f"  Audit:         {'Passed' if result['audit']['passed'] else 'Blocked'}")

    print(f"\n{'=' * 70}")
    print(f"  Experience store after {len(tasks)} tasks:")
    print(f"  Fine entries:   {len(exp.fine)}")
    print(f"  Coarse entries: {len(exp.coarse)}")
    print(f"  Domain entries: {len(exp.domain)}")
    print("=" * 70)


if __name__ == "__main__":
    demo()
