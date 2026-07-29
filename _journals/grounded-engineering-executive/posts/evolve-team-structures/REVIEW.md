# Review: Evolve Team Structures

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong appendix record: the "living design / teams as sensors / triggered evolution" framing is clear, the argument in Rationale is tight, and the checklist reproduces all ten PDF sections faithfully. Two things need fixing before this is publish-clean: every comic caption is duplicated (each `**Panel N:**` line appears twice), and the third evolution trigger is stated inconsistently — the highlight, excerpt, Figure 3 caption, and comic Panel 5 say "work waiting/queuing behind one team," while the spec, Statement, Rationale, and checklist say "many business services rely on many lower-level services."

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 2 · nit 2

### Blockers
- None.

### Major
- **[comics.md · all eight panels]** Every panel caption line is duplicated — each `**Panel N:** …` line appears twice in a row (lines 11–12, 15–16, 19–20, 23–24, 27–28, 31–32, 35–36, 39–40). Neighboring posts (`introduction`, `organizational-design`) carry one caption per panel; this will render doubled captions on the Comic tab. *Delete the duplicate line under each panel.*
- **[index.md · highlight (line 17), excerpt (line 9), Figure 3 caption (line 48); comics.md · Panel 5]** The third trigger is misstated as "too much work waiting on one team" / "too many teams waiting on one" / "queues behind one team." Per the spec, Statement bullet 3, Rationale, and the checklist, the third trigger is "many business services rely on many lower-level services"; teams-waiting-on-one-team is a *symptom of the first* trigger (software too large for one team). The quotable summary and its echoes contradict the body. *Reconcile the highlight, excerpt, Figure 3 caption, and comic Panel 5 with the canonical trigger list.*

### Minor
- **[comics.md · alt texts]** Alt texts omit the `Comic panel:` prefix used consistently by sibling posts' comics (e.g. `introduction`, `organizational-design`), a small house-convention drift.
- **[index.md · Rationale, "Defined triggers" paragraph (line 45)]** One long paragraph carries all three triggers plus their symptom lists — dense to parse in one pass. *Consider a short list or splitting into three sentences-per-trigger with clearer seams.*

### Nits
- **[index.md · Scope and Revisiting]** The final sentence restates the entire Final Health Check list from the Checklist tab — a mild redundancy; a shorter pointer would do.
- **[comics.md · Panel 8 caption]** "Never done — current." reads slightly telegraphic even for a comic caption; fine if intentional, but it leans on the article's phrasing ("I declare it *current*") that a comic-only reader won't have.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | partial | index.md · highlight — present and quotable, but the third trigger in it is misstated (see Major finding) |
| Triggers explicit with symptoms | met | index.md · Rationale ("Defined triggers…"); checklist.md · "Watch for Triggers" |
| Collaboration → XaaS lifecycle argued | met | index.md · Rationale ("Collaboration is a mode of discovery…") + Figure 2 |
| Sensing framed as executive duty | met | index.md · Rationale ("Sensing is the organ…"); checklist.md · "Build Organizational Sensing" |
| Review rhythm survives | met | index.md · Statement bullet 5, Practice table; checklist.md · "Review and Evolve Regularly" |
| Checklist survives intact (ten sections) | met | checklist.md — all ten sections with sub-groupings preserved |
| Credit explicit | met | index.md · Authoritative References (Skelton & Pais, teamtopologies.com) |

Non-goals respected: yes — no taxonomy lecture (defers to [[static-team-topologies]] / [[team-interaction-modes]]), no reorg playbook, permanent flux explicitly disclaimed.
Drift: none structural; the trigger-wording inconsistency is an internal defect, not spec drift. Spec `status: accepted` remains right once fixed.

## Cross-modality alignment

- **Facts & framing:** One discrepancy — the third trigger (see Major finding) differs between highlight/excerpt/Figure 3/comic Panel 5 and Statement/Rationale/checklist. Everything else (timeboxed collaboration, XaaS maturation, few-months review rhythm, sensing) is consistent.
- **Terminology:** Consistent — "living design," "sensors," "triggers," "X-as-a-Service" are used identically across article, checklist, and comic.
- **Voice & tone:** Consistent first-person declarative in the article; comic uses the shared VERA/LEO cast in the house style.
- **Coverage parity:** Good — the comic covers hook → problem → principle → sensing → triggers → lifecycle → rhythm → closer, matching the article's beats. The checklist adds no beats the article lacks. Platformization appears in article and checklist but not the comic — acceptable compression for the form.

## Layer-by-layer notes

### Spec
- Well-formed contract: seven checkable criteria, clear non-goals fencing off the sibling taxonomy records, decision log explains the appendix-record status.
- No bloat; Open questions empty and closed; changelog current.

### index.md
- House record shape is complete and correctly ordered (Statement → How to Read This → Rationale → Practice table → Anti-Patterns → Related Records → Scope → References); headings in Title Case; all five `[[…]]` cross-links resolve to existing permalinks.
- All three figure images exist under `assets/images/evolve-team-structures/`; captions numbered and italicized per house style.
- The Rationale is the strongest section — each paragraph opens with a bolded claim and argues it. The Anti-Patterns list is vivid and non-redundant.
- The only argument-level weakness is the trigger-wording inconsistency at the top of the post (highlight/excerpt), which is exactly the part executives will quote.

### checklist.md
- Faithful reproduction: ten sections, sub-groupings (collaboration purposes, trigger symptom groups, reassessment options, sensing questions) preserved; framing note pointing at the Article tab is present.
- Trigger section matches the spec's canonical three triggers, symptoms and all — this is the reference version the article's highlight should match.

### comics.md
- All eight panel images exist on disk; cast/style block matches the journal's shared VERA/LEO convention.
- Every caption line is duplicated — the file's one real defect.
- Panel arc is coherent (laminated chart → strangled delivery → living design → sensors → triggers → lifecycle → review → adaptive org) and maps cleanly onto the article.
