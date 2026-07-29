# Review: Promotions

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is tight and every success criterion is
met; the checklist is a faithful, well-formed reproduction of the source PDF
(verified against `Checklist_ TSEG _ Promotions (1).pdf`); the comic carries the
article's beats in the right order with all eight panel images on disk. The
single most important thing to address is a small caption/image mismatch in
comic panel 7; everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 1

### Blockers

- None.

### Major

- None.

### Minor

- **[comics.md · Panel 7]** Caption says "headcount, budget, and approval rates
  are real" but the alt text (and image) show three gates labeled "headcount,
  budget, and need". *Align the caption with the drawn labels, or fold approval
  rates into the alt text.*
- **[index.md · Statement "Produce, organize, publish" + Figure 2 caption]**
  "Producing high-quality work is a third of the job" (Statement bullet 4) is
  repeated nearly verbatim in the Figure 2 caption ("Producing is a third of the
  job"). *Let the caption carry a different angle of the same point.*
- **[index.md · Rationale, "Honesty about the odds" ¶]** The final sentence does
  triple duty (breadth/depth/judgment + self-worth + relationships) and
  pre-states two Anti-Patterns ("Promotion as the only scoreboard", "Burning
  relationships to advance"). *Trim the trailing clause; the Anti-Patterns
  section already owns those beats.*

### Nits

- **[index.md · figures]** Each figure block is followed by a double blank line
  (consistent across the journal's posts; harmless in the rendered page, but
  inconsistent source formatting).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| System-awareness expectation survives | met | index.md · Statement bullet 1; checklist.md · §1 |
| Produce, organize, publish survives | met | index.md · Statement bullet 4, Rationale ¶3; checklist.md · §4 |
| Support structure survives | met | index.md · Statement bullets 5–6, Rationale ¶4; checklist.md · §5–7 |
| Realism survives | met | index.md · Statement bullet 7, Rationale ¶5; checklist.md · §9–10 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — the review cycle, general career ownership, and job
changes are touched only via `[[…]]` cross-links, all of which resolve
(own-your-career, performance-review-cycle, changing-jobs,
engineering-career-paths in this journal; career-conversations in
grounded-people-management-tools).

Drift: none — spec `accepted` is accurate; spec and post agree.

## Cross-modality alignment

- **Facts & framing:** consistent — the decided-before-the-cycle claim, the
  produce/organize/publish split, the broader-than-one-manager support case, and
  the headcount/budget/approval-rate realism appear identically in article,
  checklist, and comic (one caption/alt wording mismatch in panel 7, above).
- **Terminology:** consistent — "cycle-time scramble", "lossy channel",
  "produce, organize, publish", "terminal level" travel intact across all three
  modalities.
- **Voice & tone:** consistent — manager's first person in the article,
  engineer's first person in the checklist (as the spec's Audience section
  prescribes), neutral captions in the comic.
- **Coverage parity:** even — all seven Statement beats land in the checklist's
  ten sections; the comic compresses to the load-bearing five and closes on the
  article's "title catches up with reality" line.

## Layer-by-layer notes

### Spec

- Clean template use; six checkable, non-overlapping success criteria; Non-goals
  crisply fence off the three adjacent records. No bloat — the spec is shorter
  than the post, as it should be.
- Decision log and Changelog agree with what is actually in the folder
  (checklist + comics present, summary/dialog deliberately unchecked).

### index.md

- House record shape fully observed: status highlight, Statement → How to Read
  This → Rationale → What This Means in Practice → Anti-Patterns → Related
  Records → Scope and Revisiting → Authoritative References; headings in Title
  Case; the says/does-not-say table is well used.
- The Rationale's five paragraphs map one-to-one onto the Statement's
  load-bearing bullets — good structure; only the last paragraph over-packs
  (finding above).
- All three inline figures exist on disk and are captioned with numbered,
  italic captions.

### checklist.md

- Verified against the source PDF: all ten sections reproduced faithfully,
  first person preserved, numbering added (the PDF's sections are unnumbered) —
  a legitimate adaptation. Task-list markdown is well formed throughout.
- Terminology matches the article exactly (produce/organize/publish bolded in
  §4; "prepared well before the promotion cycle begins" is the item the article
  cites as "a checklist item, not a nice-to-have").

### comics.md

- Eight panels, all image files present under
  `assets/images/promotions/`; captions are one line each; the shared
  hook → problem → wrong way → principle → how it runs → mechanic → cost →
  closer scaffold reads cleanly.
- VERA/ARLO cast block matches the journal's other comics; the visual metaphor
  (binder, gates, timeline) stays coherent panel to panel.

## Fixes applied (2026-07-29)

- **Verbatim self-repetition** — Figure 2 caption no longer repeats Statement bullet 4's "Producing is a third of the job"; the caption now carries the three-pillars/half-built-publish angle only.
- **Comic caption fix** — Panel 7 caption aligned with the drawn gate labels: "headcount, budget, and business need are real gates" (was "approval rates", which the image does not show).
