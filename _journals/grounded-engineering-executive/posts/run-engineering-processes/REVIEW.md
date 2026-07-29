# Review: Running Engineering Processes

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The "default to baseline, fix execution before structure" stance is stated quotably, argued with the incentive mechanics the spec demands (specialists improve processes rather than eliminate them), and carried consistently through checklist and comic; all eight checklist sections and all eight panel images are present. The most important thing to address is in the checklist: two sections use checkboxes for content that is not checkable — the pros/cons inventory and the either/or questions of the Final Decision Filter — which muddies an otherwise runnable tab.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 1

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · Evaluate Pros & Cons of Your Pattern]** Pros and risks are rendered as task-list checkboxes ("- [ ] Low cost.", "- [ ] Risk: Important processes don't happen.") but they are reference statements, not actions or verifications — ticking "Risk of ossifying processes" has no meaning. *Render this section as plain bullets; keep checkboxes for the actionable sections.*
- **[checklist.md · Final Decision Filter]** The filter's paired either/or questions are split into separate checkboxes ("Is the current model truly failing?" / "Or are we under-executing within it?") — checking both is contradictory, checking neither is the likely outcome. *Merge each pair into one item or render as plain diagnostic questions.*
- **[checklist.md · stray lead-in bullets]** Five plain bullets sit inside task-list sections ("- Determine which pattern best matches…", "- Before moving 'up' the pattern curve:", "- Rule of thumb:", "- Before changing patterns, ask:", "- If forced to choose without context:"), breaking the checkbox pattern each time — the same formatting issue as in sibling checklists, but most frequent here. *Convert lead-ins to prose lines outside the lists.*

### Nits
- **[index.md · after Figures 1–3]** Double blank lines after figure captions, inconsistent with single-line spacing elsewhere. Also **[index.md · Principle highlight]** the highlight runs six sentences — within house norms but the longest of the reviewed set; the last sentence ("I leave baseline only when scale clearly demands it") duplicates the "default is baseline" beat already stated two sentences earlier.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (default to baseline, improve execution before structure) | met | index.md · Principle highlight |
| Rationale argued (early specialists ossify; under-execution the real problem; hold 3–4 years) | met | index.md · Rationale, paragraphs 1, 2, 4 |
| Checklist survives intact — all eight PDF sections | met | checklist.md (Philosophy, Identify Pattern, Pros & Cons, If in Baseline, Budget Reality, Trend Discipline, Decision Filter, Default Recommendation) |
| Anti-patterns concrete, at least three | met | index.md · Anti-Patterns (six, including the three the spec names) |
| Credit explicit (Primer + lethain.com/who-runs-eng-process) | met | index.md · Authoritative References |

Non-goals respected: yes — the meeting portfolio stays in [[meetings]] (explicitly delineated in Related Records), standards in [[calibrating-your-standards]], and no org-chart prescription appears.
Drift: none. Spec `accepted` status is warranted. The decision log's title rationale (active title over question form) is honored by the front matter.

## Cross-modality alignment

- **Facts & framing:** Consistent — the five patterns (named identically in article, checklist, and Figure 1), the ~100-engineer threshold, 6-month rotations, 3–4-year commitment, quality-vs-overhead trade, and the under-execution-first diagnosis all match across files.
- **Terminology:** Consistent — "baseline", "cost curve", "under-executing within it", "cargo-culting", "ossify", "process fads" carry through; comic Panel 6's caption quotes the baseline definition in the article's exact words.
- **Voice & tone:** Consistent — first-person declarative article; imperative checklist; comic in the shared VERA/LEO register, opening with the same "who should run this? — we should" move as How to Read This.
- **Coverage parity:** Even. The comic compresses the budget reality check out (Panel 8 carries trend discipline instead) — acceptable for eight panels; article and checklist both carry it. No modality introduces a beat the others lack.

## Layer-by-layer notes

### Spec
- Five success criteria, all checkable; the checklist criterion enumerates the eight expected sections.
- The decision log entry on the title choice ("question-form title rejected as reading like a quiz") is a good example of recording a small but real editorial decision.
- Intent, Non-goals, and Audience are internally consistent; no bloat; changelog current.

### index.md
- House shape complete, Title Case headings, four [[cross-links]] all resolving to existing posts, three figures captioned with files on disk.
- Rationale paragraph 1 is the argumentative core and does real work: the incentive mechanism (a role that depends on the process existing) explains *why* ossification happens rather than asserting it.
- "Valued work gets done well; invisible work decays" (Rationale para 3) is the record's best aphorism and is properly echoed by comic Panel 7.
- The says/does-not-say table is disciplined; the "Never hire a TPM" disclaimer usefully preempts the obvious misreading.

### checklist.md
- Serves its purpose overall: the eight sections run in decision order (philosophy → identify → evaluate → baseline playbook → budget → trend → filter → default), and the baseline playbook's three sub-groups (Keep It Working / Sustainable / Valued) are genuinely actionable with numbers preserved (<100, 6-month, 3–4 years).
- The pattern-identification section works well as diagnostic checkboxes; the pros/cons and decision-filter sections do not (see Minor) — the checkbox form fits actions and verifications, not reference lists.
- Most stray lead-in bullets of any checklist in the reviewed set (five).

### comics.md
- Eight panels: hire-a-TPM hook → quality/overhead scale → name the pattern → cargo-cult wrong-way → magnifying-glass diagnosis → baseline principle → valued ownership → hold-the-model closer. The arc matches the article's Rationale order almost exactly.
- All eight referenced panel images exist under assets/images/run-engineering-processes/.
- Panel 5's visual (tags for "no owner, no rotation, no recognition") is a precise compression of the article's "ownerless, unrotated, unrecognized" — the tightest article-to-panel mapping in this journal's reviewed set.
- Captions one line each, matching their alt text; props (clipboard, scale, flag) stay consistent.
