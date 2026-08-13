# Review: Operating Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, internally consistent record. The spec is a clean contract, the article carries all three practices with the chapter's concrete numbers intact, the checklist is a faithful and well-organized runnable companion, and the comic tells the same story on-model. Publish-ready as a draft; the most useful improvement is to surface the 24×7-coverage expectation somewhere in the article itself (it currently lives only in the checklist) and to trim the load-numbers repetition between the Statement and the Rationale.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "On-call, sustainable by design"]** The spec's on-call criterion leads with "24×7 coverage where the business needs it," but the article never states it — it appears only in checklist §2. A reader of the Article tab alone misses the coverage expectation. *Add a half-sentence to the first on-call bullet.*
- **[index.md · Rationale ¶3 vs Statement "Load has numbers"]** The Rationale paragraph re-runs the Statement bullet nearly beat for beat: both state the 1-in-4 / five-pages numbers and both conclude "breach = stability problem, stability outranks features." The Rationale's genuinely new idea (the numbers as *diagnostic*, compensation as symptom-treatment) is diluted by re-stating the numbers a fourth time. *Let the Rationale lean on the diagnostic framing and drop the restated limits.*
- **[comics.md · Panels 2, 3, 5–8 alt text]** Alt texts say "an engineer" / "an ops worker" while the rendered images clearly depict Kai (and, in Panel 5, Vera). The images are on-model; the alt text under-describes the cast, which weakens both accessibility and future regeneration fidelity. *Name Kai/Vera in the alt text where they appear.*

### Nits

- **[index.md · front matter excerpt]** The list "on-call no more than one week in four, fewer than five meaningful pages per engineer per week, and reassessed staffing when operations consume half of capacity" breaks parallelism — two limits, then a past-participle action. *Rephrase the third item ("staffing reassessed when…").*
- **[index.md · excerpt vs highlight]** The excerpt and the highlight blockquote are near-verbatim duplicates (house pattern, but this pair is longer than most — six clauses each); trimming one of them slightly would sharpen both.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The on-call side survives | met (one gap in index) | index.md · Statement/Rationale; 24×7 coverage only in checklist.md §2 |
| The support side survives | met | index.md · Statement "Support, structured and separated"; checklist.md §§3–8 (far-flung time zones §7, support org §8) |
| The feedback side survives | met | index.md · Statement "Operational feedback" + Rationale ¶6; checklist.md §§9–13 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — support-specialist hiring appears only as a scaling move, no incident-runbook or tooling content, planning mechanics deferred to [[planning-and-delivery]].
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — 1 week in 4 (ideally 1 in 6–8), fewer than five meaningful pages, ~50% capacity staffing trigger, and "breach = stability problem" agree across article, checklist, and comic.
- **Terminology:** Consistent — "merged DevOps rotation/model," "critical incident," "business-hours support rotation," "process theater" all travel intact.
- **Voice & tone:** Consistent first-person operating-model register; the comic keeps the same argument arc (hook → problem → wrong way → principle → practice → cost → closer).
- **Coverage parity:** Even for the form. The comic compresses the feedback practice to "review turns signals into priorities" and omits SLOs/synthetic monitoring — acceptable compression for nine panels, noted only for awareness.

## Layer-by-layer notes

### Spec

- Clean template use; the five criteria are genuinely checkable (each names the concrete beats that must survive).
- Non-goals do real fencing work against three sibling records; Decision log records the framing choice explicitly.

### index.md

- Follows the journal's record shape exactly (Statement → How to Read This → Rationale → What This Means in Practice table → Anti-Patterns → Related Records → Scope → References); all five `[[…]]` cross-links resolve to existing posts.
- The Anti-Patterns section is a highlight — eight patterns, each earning its name, all traceable to claims in the body.
- The three figures exist on disk, are captioned Figure 1–3, and match their alt text.
- Main weaknesses are the two minor findings above: the missing 24×7 line and the Statement/Rationale repetition of the load numbers.

### checklist.md

- Faithful, well-grouped reproduction: 13 numbered sections plus a Quick Health Check, terminology consistent with the article throughout.
- Carries several beats the article compresses (far-flung time zones §7, error-budget caution §9, release-engineering proportionality §10) — appropriate for the modality's runnable purpose.

### comics.md

- All nine referenced panel images exist on disk; captions run Panel 1–9 and match their images; spot-checked panels (2, 4, 5) are on-model for the VERA/KAI cast.
- Alt text in the non-named panels is generic ("an engineer") where the images show the cast — see the minor finding.
- The closer (Panel 9) lands the record's quotable line ("unmeasured is unmanaged") — good echo of the highlight.

## Fixes applied (2026-08-13)

- index.md · Statement, "On-call, sustainable by design" — fixed: first on-call bullet now states the rotation provides 24×7 coverage where the business needs it.
- index.md · Rationale ¶3 vs Statement "Load has numbers" — fixed: dropped the restated limits from the Rationale; the paragraph now leads with the diagnostic framing.
- comics.md · Panels 2, 3, 5–8 alt text — fixed: alt text now names Kai (Panels 2, 3, 5, 6, 7, 8) and Vera (Panels 3, 5, 7, 8) where the images depict them.
- index.md · front matter excerpt — fixed: third item rephrased to "staffing reassessed when…" to restore parallelism.
- index.md · excerpt vs highlight — fixed: excerpt's final sentence compressed ("operational signals — SLOs, synthetic monitoring, regular operational reviews — flow back into engineering priorities") to reduce the near-verbatim duplication.
