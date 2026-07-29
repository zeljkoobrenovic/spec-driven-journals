# Review: Operational Excellence

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A tight, publish-ready record. The "done means runnable" framing is quotable, the seven areas map cleanly across article, checklist, and comic, the checklist reproduces the Matsudaira source PDF essentially verbatim, all cross-links resolve, and all figure and panel images exist. The most useful fix: the "five keys are one loop" argument only ever places four keys in the loop — quality assurance is named but never given a role — in both the Rationale paragraph and Figure 1's caption.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Rationale ¶2 + Figure 1]** "The five keys are one loop, not five projects" is cashed out with only four keys: "measurement exposes the pain, automation removes it, standardization keeps it removed, and the improvement culture reruns the loop" — quality assurance is listed and then dropped. The Figure 1 alt also reorders and renames the stations ("measure, automate, standardize, quality, improve"), and its caption repeats the four-key walk. *Give QA its place in the loop (e.g., what standardization protects) or soften the "one loop" claim.*
- **[index.md · Statement + Rationale, on-call]** The spec's humane-on-call criterion names three clauses — pain measured, **rotations fair**, feature-work expectations explicit — but rotation fairness never reaches the article; it lives only in checklist §3 ("Rotation selection is fair and well-structured", straight from the source PDF). *One word ("a fair, defined schedule…") in the Statement's on-call bullet closes it.*
- **[index.md · Statement "Recovery" bullet vs. checklist §6/§7]** The article groups "rollback or failover to a known good instance is always possible" under the recovery bullet, but the checklist — faithful to the PDF — lists it under §7 CI/CD, leaving §6 Failover & Recovery with no rollback item. Someone running the checklist area-by-area will look for the article's flagship recovery guarantee in the wrong section. *A parenthetical cross-reference in §6, or noting the grouping in the article, would reconcile them.*

### Nits

- **[index.md · Rationale ¶4]** "a personnel perk" is an odd collocation for the point being made ("not a hardship to be endured" is closer to the meaning).
- **[spec.md · throughout]** The Matsudaira attribution is restated in four places (Intent, criterion 6, Decision log, Sources) — mild accretion for a spec this size.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (done = runnable; management responsibility) | met | index.md · highlight |
| The five keys survive | met | index.md · highlight, Rationale ¶2; checklist preamble |
| All seven areas survive and map to checklist sections | met | index.md · Statement (7 bullets) ↔ checklist §1–7 |
| Humane on-call stance survives | partial | pain + expectations: index.md · Statement, Rationale ¶4; fairness: checklist §3 only |
| Recovery stance survives | met | index.md · Statement, Rationale ¶5; checklist §6 (+ rollback in §7) |
| Credit is explicit | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes — no drift into senior-leadership's True North territory, team-health territory, or SRE how-to (tooling stays with the teams throughout).
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — seven areas, five keys, launch-review-as-cheapest-meeting, measured pain, tested recovery, reversible deploys carry identically across article, checklist, and comic. Checklist verified against the source PDF: faithful, including the rollback item's placement under CI/CD.
- **Terminology:** consistent — "known good instance," "launch readiness," "on-call pain" recur verbatim across modalities. The only mapping wrinkle is the rollback item's home section (Minor above).
- **Voice & tone:** consistent — first-person bar-setting in article, imperative conditions in checklist, comic in the journal's usual terser register.
- **Coverage parity:** the comic's eight panels track the article's arc (ship-time "done" → 3 a.m. archaeology → deferral → the bar → launch review → measured pain → tested plans → calm deploy) with no invented beats. The checklist adds nothing beyond the PDF, as intended.

## Layer-by-layer notes

### Spec

- Well-structured; the Decision log's note that this is the journal's one non-Fournier record in the section is a useful orientation and matches the article's How to Read This.
- Success criteria are checkable and each maps to a concrete location in the post.

### index.md

- MADR-shaped, Title Case headings, status highlight matches front matter. All three figures exist and are captioned; the "What it does **not** say" table is one of the sharper ones in the journal (especially the recovery-ability and quality-trade-off rows).
- Anti-Patterns are concrete and non-overlapping; "An untested plan is a hypothesis, not a plan" earns its place.
- The QA-missing-from-the-loop paragraph is the only argument gap.

### checklist.md

- Seven numbered sections plus the five-keys preamble; item-for-item faithful to the source PDF (verified), well-formed task-list markdown.
- Good call keeping the attribution line at the top, mirroring the PDF.

### comics.md

- All eight panel images exist; cast/style block consistent with the journal (VERA/ARLO).
- Captions match their alt text; the pager/archaeology metaphor holds panel to panel. Panel 4's caption compresses the principle plus manager-ownership cleanly.

## Fixes applied (2026-07-29)

- **Checklist-only spec beat (humane on-call criterion)** — Statement's on-call bullet now reads "A fair, defined schedule and rotation length", bringing rotation fairness into the article as the review suggested.
