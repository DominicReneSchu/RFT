# κ-Parameter in der RFT: Konventionsdeklaration (RT-11)

*Dominic René Schu, August 2026*
*Status: Abgeschlossen (Aug 2026)*

---

## Übersicht

Dieses Dokument bearbeitet RT-11: die Frage, ob der Kopplungsparameter κ in der
FLRW-Friedmann-Gleichung der RFT aus den Axiomen abgeleitet werden kann, oder ob
κ als Konvention gesetzt wird.

**Ergebnis:** κ_RFT = 1 ist eine **explizite Konventionsdeklaration** mit physikalischer
Begründung. Eine formale Ableitung von κ = 8πG aus den RFT-Axiomen A1–A7 ist nicht
möglich, weil G_sync auf dem internen Phasenraum operiert und keinen direkten Zugang
zur Newtonschen Gravitationskonstante G hat. κ_RFT = 1 entspricht der Wahl natürlicher
Einheiten für die Kopplung zwischen Resonanzfeldenergie und Raumzeitgeometrie.

---

## Ausgangslage

### Der κ-Parameter im Code

In `coupled_flrw.py` erscheint κ in der modifizierten Friedmann-Gleichung:

```
H² = (κ/3) · ρ_total / (1 + α·ε²)
```

und in der Beschleunigungsgleichung:

```
ä/a = −(κ/6) · (ρ_total + 3p_total) / (1 + α·ε²)
```

Der Standardwert ist `kappa=1.0`. In der Allgemeinen Relativitätstheorie gilt
κ = 8πG/c⁴ (oder in natürlichen Einheiten mit c = 1: κ = 8πG).

### Das Problem

RT-11 stellt fest: κ = 1 ist im Code ein freier Parameter ohne formale Ableitung
aus den RFT-Axiomen. Die RFT beansprucht axiomatische Vollständigkeit (A7 bewiesen,
A3 als Korollar aus A7) — der ungeklärte Status von κ ist ein Inkonsistenzrisiko.

---

## Analyse: Kann κ aus den RFT-Axiomen abgeleitet werden?

### Die RFT-Axiome und Gravitation

Die Axiome A1–A7 der RFT formulieren:

- **A1** — Alle physikalischen Systeme schwingen.
- **A2** — Resonanzkopplung zwischen Systemen mit gleicher Frequenz.
- **A3** — Resonanzbedingung: fᵢ/fⱼ ∈ ℚ (Korollar aus A7, RT-35).
- **A4** — Kopplungsenergie: E = π · ε(Δφ) · ℏ · f.
- **A5** — Vektorialität: Ê⃗ = E_eff · ê(Δφ, ∇Φ) (irreduzibles Postulat, RT-36).
- **A6** — Resonanzerhaltung.
- **A7** — G_sync-Invarianz (bewiesen, RT-02).

**Beobachtung:** Keines dieser Axiome enthält die Newtonsche Gravitationskonstante G
oder eine direkte Kopplung an die Raumzeitgeometrie. Die RFT beschreibt Resonanzfelder
in einer gegebenen Raumzeitgeometrie (Hintergrundfeld-Näherung in der FLRW-Simulation).
Die Rückreaktion der Resonanzfelder auf die Geometrie — durch κ parametrisiert —
ist nicht aus den axiomatischen Resonanzbedingungen allein ableitbar.

### Warum κ = 8πG nicht aus G_sync folgt

G_sync = ℝ⁺_× × U(1) × Aff⁺(ℝ) operiert auf:
- Frequenzen (ℝ⁺_× — Skalengruppe)
- Phasen (U(1) — Phasenrotation)
- Zeitparametern (Aff⁺(ℝ) — affine Zeittransformationen)

Die Gruppe hat keinen Faktor, der auf Raumzeitkrümmungsgrößen wirkt. G_sync ist
eine **interne Symmetriegruppe** des Resonanzfelds, keine Raumzeitsymmetriegruppe.
Die Einsteinschen Feldgleichungen G_μν = κ T_μν verknüpfen Geometrie (G_μν) mit
Materie (T_μν) über κ — diese Verknüpfung liegt außerhalb des Wirkungsbereichs
von G_sync.

**Formal:** Es gibt keine Darstellung von G_sync, die κ als Eigenwert oder
invariante Größe auszeichnet.

---

## Konventionsdeklaration: κ_RFT = 1

### Begründung

Die RFT-Simulationen (FLRW-Framework) arbeiten in einem **dimensionslosen
Einheitensystem**, in dem die relevanten Skalen durch die Resonanzfeldparameter
(m, λ, α, g) gesetzt werden. In diesem System ist κ kein dimensionsloser Parameter,
sondern ein Einheiten-Konversionsfaktor.

Die Wahl κ_RFT = 1 ist die **kanonische Konvention** für dimensionslose
Feldtheorien:

| System | κ-Wert | Bedeutung |
|--------|--------|-----------|
| SI-Einheiten | 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J | Physikalischer Wert |
| Nat. Einheiten (G=c=1) | 8π ≈ 25.13 | Geometrische Einheiten |
| Planck-Einheiten (ℏ=G=c=1) | 8π | Planck-System |
| **RFT-Konvention** | **1** | Normierte Kopplung (dimensionslos) |

Die RFT-Konvention κ_RFT = 1 entspricht der Normierung der Gravitationskopplung
auf Einheit. Sie ist physikalisch äquivalent zur Wahl eines Einheitensystems, in dem
die Planck-Energiedichte auf 1 normiert ist.

### Formale Deklaration

> **Konvention RT-11:**
> In allen RFT-Simulationen gilt κ_RFT = 1. Dieser Wert ist kein aus den
> Axiomen A1–A7 ableitbarer Parameter, sondern eine Normierungskonvention
> für das dimensionslose Simulationseinheitensystem. Für den Vergleich mit
> kosmologischen Beobachtungsdaten (z.B. H₀ in km/s/Mpc) ist κ durch den
> physikalischen Wert 8πG/c⁴ zu ersetzen und die Felder entsprechend zu skalieren.

### Konsistenzprüfung

Die Konvention κ_RFT = 1 ist intern konsistent, wenn die Simulation qualitativ
korrekte Aussagen liefert, die unabhängig vom absoluten κ-Wert sind:

1. **η(Δφ) = cos²(Δφ/2)** — Diese Relation hängt nicht von κ ab (rein kinematisch).
2. **d_η wächst mit H₀** — Die Hubble-Reibung ist unabhängig von κ (geometrischer Effekt).
3. **Δd_η(SH0ES − Planck) = 0.0114** — Diese Differenz ist κ-unabhängig (Verhältnis).

Die zentralen Ergebnisse des FLRW-Frameworks sind κ-invariant. κ = 1 ist daher
eine konservative, nicht-falschifizierende Konventionswahl.

---

## Verknüpfung mit dem Axiomensystem

### Auswirkung auf A4

Axiom A4 lautet: E = π · ε(Δφ) · ℏ · f. Die Verbindung zwischen dieser
Resonanzenergie und der Raumzeitgeometrie (κ-Kopplung) ist eine **Erweiterungsannahme**,
die nicht in A4 enthalten ist. Sie entspricht dem physikalischen Bild:

```
T_μν[Resonanzfeld] = (π · ε · ℏ · f) · u_μ u_ν / c²
```

Die Ankopplung an die Friedmann-Gleichung über κ = 1 ist eine Modellierungswahl,
nicht eine axiomatische Konsequenz.

### Status im Axiomensystem

| Größe | Axiomatischer Status | Begründung |
|-------|---------------------|------------|
| ε(Δφ) = cos²(Δφ/2) | Abgeleitet aus A7 (RT-02) | k=1-Darstellung von U(1) |
| fᵢ/fⱼ ∈ ℚ (A3) | Korollar aus A7 (RT-35) | Darstellungsstruktur ℝ⁺_× |
| ê = ∇Φ/|∇Φ| (A5) | Irreduzibles Postulat (RT-36) | G_sync nicht zuständig |
| **κ_RFT = 1** | **Konvention (RT-11)** | **Normierungsfreiheit im Einheitensystem** |

---

## Konsequenz für das Manuskript (RT-37)

§7 des IOP-Manuskripts (Erweiterungen) soll folgende Klarstellung enthalten:

> „Der Parameter κ in der modifizierten Friedmann-Gleichung ist in den
> RFT-Simulationen auf κ = 1 gesetzt (dimensionsloses Einheitensystem).
> Für den quantitativen Vergleich mit kosmologischen Beobachtungsgrößen
> ist κ durch den physikalischen Wert 8πG/c⁴ zu ersetzen. Die qualitativen
> Ergebnisse (η-Korrektur, d_η-Skalierung mit H₀) sind κ-invariant."

---

## Verbindung zu anderen Tasks

| Task | Verbindung |
|------|------------|
| RT-02 | G_sync-Gruppenstruktur — zeigt, warum κ nicht aus G_sync folgt |
| RT-36 | A5 ebenfalls irreduzibel — strukturelle Parallele |
| RT-04 | FLRW-Solver SI-Einheiten — dort κ = 8πG explizit setzen |
| RT-37 | Manuskript §7: κ-Konvention explizit dokumentieren |
| RT-32 | lambda_eps4-Erweiterung — κ bleibt 1, lambda_eps4 neu |

---

## Verweise

- [gsync_gruppenstruktur.md](gsync_gruppenstruktur.md) §4 — G_sync-Wirkungsraum
- [a5_vektorialitaet_herleitung.md](a5_vektorialitaet_herleitung.md) — strukturelle Parallele (A5 irreduzibel)
- [../docs/definitionen/axiomatische_grundlegung.md](../docs/definitionen/axiomatische_grundlegung.md) §A4, §A7
- [../simulationen/FLRW-Simulationen/core/coupled_flrw.py](../simulationen/FLRW-Simulationen/core/coupled_flrw.py) — κ als Parameter `kappa`
- [../../../../RESEARCH_TASKS.md](../../../../RESEARCH_TASKS.md) — RT-11 Gesamtstatus
