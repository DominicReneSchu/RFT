# Journal Selection — Resonance Field Theory Submission

*Dominic-René Schu — August 2026*
*Manuscript: "Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"*

---

## Primary Choice: Journal of Physics Communications (JPhysComm)

**Publisher:** IOP Publishing
**ISSN:** 2399-6528
**URL:** https://iopscience.iop.org/journal/2399-6528
**Submission portal:** https://mc.manuscriptcentral.com/jphyscomm

### Rationale

**1. Scope alignment.**
JPhysComm's stated scope is "the communication of significant new results across all areas of physics." The journal explicitly does not apply a novelty filter that excludes unorthodox approaches — the criterion is significance and rigor, not alignment with a specific subdiscipline. RFT is an axiomatic framework with cross-domain empirical validation. It is not primarily a contribution to particle physics, cosmology, or quantum mechanics individually — it spans all three. JPhysComm is the IOP journal best suited to such interdisciplinary scope.

**2. Open Access.**
JPhysComm is fully Open Access (Gold OA). This ensures the manuscript is immediately and freely accessible worldwide without a paywall. Given that the associated code and data are already on a public GitHub repository, a closed-access journal would create an inconsistency in the overall open science posture of the work.

**3. IOP LaTeX class already implemented.**
The manuscript `rft_manuscript_en_iop.tex` uses `\documentclass[12pt]{iopart}`, which is the IOP house style. No reformatting is required for submission.

**4. Article character.**
JPhysComm publishes "communications" in the sense of significant original results that are complete and clearly argued — not letters (brief, no full derivation) and not review articles. The manuscript is complete: it includes the full axiomatic derivation, all four validation domains with quantitative results, comparison with established theories, and two experimental proposals. This fits the JPhysComm article category exactly.

**5. Expected review timeline.**
Typical review time at JPhysComm: 4–8 weeks from submission to first decision. This is consistent with the scope of the manuscript and the need for timely feedback.

**6. Article Processing Charge (APC).**
As of 2025, the APC for JPhysComm is approximately £1,600 GBP / €1,900 EUR for corresponding authors without institutional affiliation. For independent researchers, IOP Publishing offers a waiver or discount application process. Waiver eligibility is assessed on a case-by-case basis for authors without institutional access to transformative agreements. Authors affiliated with institutions covered by IOP Publishing Read and Publish agreements pay no APC directly.
**Action required:** Apply for APC waiver as independent researcher at the time of submission via the ScholarOne portal.

---

## Alternative: New Journal of Physics (NJP)

**Publisher:** IOP Publishing / Deutsche Physikalische Gesellschaft
**ISSN:** 1367-2630
**URL:** https://iopscience.iop.org/journal/1367-2630

### Rationale

NJP has a higher impact factor than JPhysComm and an explicitly interdisciplinary remit: "open access to significant, novel, and broad-impact physics results." The "broad-impact" criterion and the IOP/DPG co-sponsorship make it well-suited for a manuscript that claims cross-domain universality.

**Advantages over JPhysComm:**
- Higher visibility and citation impact
- Explicitly welcomes interdisciplinary submissions
- Strong community in mathematical physics and quantum foundations

**Disadvantages:**
- Longer typical review time (~3 months first decision)
- Stricter scope filtering: NJP editors may flag an axiomatic framework without a peer-reviewed community in an established NJP subdiscipline
- Higher risk of desk rejection on scope grounds

**Recommendation:** Submit to NJP as a second attempt if JPhysComm rejects on scope grounds (not on scientific grounds). If JPhysComm accepts, NJP is not needed.

---

## Not Recommended

**Physical Review Letters (PRL)**
- Maximum length: 4 pages — insufficient for the full axiomatic derivation, 4 validation domains, and 2 experimental proposals
- Scope is tightly defined around high-energy physics, condensed matter, and precision measurements; axiomatic frameworks spanning multiple domains have a high desk-rejection rate
- Would require severe condensation that would obscure the central theoretical arguments

**Foundations of Physics**
- Well-suited for the philosophical and foundational aspects of RFT (A5 as irreducible postulate, π as fundamental constant)
- However, the primary empirical community for particle physics and cosmology does not read Foundations of Physics regularly; the impact on practitioners would be lower
- If the manuscript is eventually split (theory paper + applications paper), Foundations of Physics would be appropriate for the purely axiomatic part

**arXiv (preprint server, not a journal)**
- arXiv is not a peer-reviewed journal and does not constitute a publication
- However, simultaneous arXiv posting is strongly recommended (see below)

---

## Parallel arXiv Submission — Strongly Recommended

**Action: Submit to arXiv simultaneously with or immediately before journal submission.**

### Category Selection

**Primary:** `quant-ph` (Quantum Physics)
- Justification: The Schrödinger derivation (§4.4), the ⁸⁷Rb BEC prediction (§6.2), and the coupling operator formalism are directly relevant to the quantum physics community. The quant-ph readership is also familiar with BEC experiments, decoherence, and precision measurements — the audience most likely to evaluate Experiment II.

**Alternative if quant-ph moderators desk-reject:** `physics.gen-ph` (General Physics)
- physics.gen-ph accepts frameworks that do not fit cleanly into a standard subdiscipline. There is a lower bar for cross-domain or foundational work.
- Note: physics.gen-ph has lower readership than quant-ph. Use as fallback only.

### Why arXiv Matters

1. **Priority date:** arXiv establishes a timestamped public record before journal review begins. Given that the repository is already public on GitHub, arXiv adds a citable, indexed, DOI-linked preprint.

2. **Visibility during review:** The 4–8 week JPhysComm review window is a period during which the manuscript cannot be cited or found on Google Scholar. An arXiv preprint eliminates this gap.

3. **Community feedback:** arXiv submission may generate early reader comments (via email or arXiv comments) that can be used to strengthen the manuscript before or during revision.

4. **IOP policy:** IOP Publishing explicitly allows authors to post preprints on arXiv before, during, and after journal review. There are no embargo restrictions for JPhysComm or NJP.

5. **Journal of Physics Communications is arXiv-friendly:** JPhysComm frequently references arXiv preprints in reviewer correspondence and does not penalize prior arXiv posting.

### arXiv Submission Checklist

- [ ] Account at arXiv.org (create or log in)
- [ ] Upload `rft_manuscript_en_iop.tex` + all class files + figures
- [ ] Select primary category: `quant-ph`; secondary: `physics.gen-ph` and/or `math-ph`
- [ ] Add abstract (same as manuscript; arXiv allows up to 1920 characters)
- [ ] Set "Journal-ref" field to blank until journal acceptance; update after acceptance
- [ ] After submission, add arXiv ID (e.g., arXiv:2026.XXXXX) to manuscript footnote before final journal proof

---

## Timeline Overview

| Step | Target Date | Notes |
|------|-------------|-------|
| Abstract word count reduction | Within 1 week | Mandatory — IOP limit 200 words |
| Figure resolution check/conversion | Within 1 week | Convert to PDF/EPS where needed |
| RT-08, RT-10 limitation statements added | Within 1 week | One sentence each in §4.3 and §4.5 |
| RT-38 protocol URL added to §6 | Within 1 week | One sentence |
| A5 clarification added to §2.5 | Within 1 week | One sentence |
| Compile final PDF | Day before submission | Verify no LaTeX errors |
| arXiv submission | Day of journal submission | quant-ph or physics.gen-ph |
| ScholarOne portal submission | Target: within 2 weeks | Apply for APC waiver if needed |
| Expected first decision | 4–8 weeks after submission | JPhysComm typical timeline |

---

*Journal selection version: RT-39, August 2026 — Dominic-René Schu*
