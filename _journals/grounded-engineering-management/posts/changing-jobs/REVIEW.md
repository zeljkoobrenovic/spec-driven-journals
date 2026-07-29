# Review: Changing Jobs

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The article covers the full arc the spec demands (explore →
promotion-vs-switch → interviews → leveling → onboarding), the checklist is a
faithful first-person adaptation of the source PDF (verified against
`Checklist_ TSEG _ Changing Jobs (1).pdf`), and the comic lands the
"5–10 year decision, not a compensation event" spine well. The single most
important thing to address is the inconsistent grammatical person across the
Statement bullets; the rest is polish and one deliberate coverage gap worth a
one-line note.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 1

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement bullets 3–4]** The bullets shift person: bullets 1–2
  run "I expect engineers to…", bullet 3 goes imperative ("Ask the recruiter…"),
  and bullet 4 mixes third person with a stray second person ("why they believe
  you're ready"). *Pick one address for all six bullets.*
- **[index.md · throughout]** The "trust, context, influence" triple appears six
  times in the article alone (highlight, Statement bullet 2, Rationale ¶3,
  Figure 2 caption, practice table, anti-pattern 3) plus the comic. It is the
  load-bearing phrase, but two of the six could go without loss. *Cut it from
  the practice table or anti-pattern, where the point is already made.*
- **[checklist.md ↔ index.md · "Leave well"]** The leave-well beat (Statement
  bullet 6, anti-pattern "Leaving badly", comic panel 8 — the closer) has no
  checklist counterpart. That is faithful to the PDF, but a checklist-first
  reader misses the record's closing commitment. *Consider a one-line
  house-addition item or a note in the checklist's intro line.*
- **[comics.md · Panel 7]** The "The cost:" label doesn't fit its content —
  deliberate landing is the follow-through, not a cost; the shared eight-beat
  scaffold is forcing the label here. *Reword the caption lead (e.g. "The
  follow-through:").*

### Nits

- **[index.md · How to Read This]** Figure 1 sits inside "How to Read This",
  while the sibling posts anchor figures in Statement or Rationale — harmless,
  but it breaks the journal's pattern.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Explore stage survives | met | index.md · Statement bullet 1; checklist.md · §1 |
| Promotion vs switching survives | met | index.md · Statement bullet 2, Rationale ¶3; checklist.md · §2 |
| Interview prep and leveling survive | met | index.md · Statement bullets 3–4, Rationale ¶4; checklist.md · §3–5 |
| Onboarding survives | met | index.md · Statement bullet 5, Rationale ¶5; checklist.md · §6 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — promotions, career-paths terrain, and hiring are
handled via cross-links only. All `[[…]]` targets resolve (promotions,
own-your-career, engineering-career-paths, thriving-in-different-environments,
first-three-months — all in this journal; the spec's hiring-well and hiring
targets also resolve).

Drift: none — the "leave well" beat goes beyond the source checklist but is
explicitly grounded in the spec's Intent ("would rather lose someone well than
keep them badly"), so it is spec-compliant, not drift. Spec `accepted` stands.

## Cross-modality alignment

- **Facts & framing:** consistent — the 5–10 year horizon, the reset triple, the
  full comparison axes (compensation, role, growth, team, mission, flexibility,
  upside), the down-/up-level treatment, and the 1/3/6-month landing structure
  are identical across article, checklist, and comic.
- **Terminology:** consistent — "reactive jump", "what the switch resets",
  "work log", "leveling with clear eyes" travel intact; comic panel titles reuse
  the article's anti-pattern names.
- **Voice & tone:** consistent — manager's voice in the article, engineer's
  first person in the checklist, per the spec's Audience section.
- **Coverage parity:** nearly even — the one asymmetry is "leave well" (in
  article and comic, absent from the checklist; finding above). Conversely the
  checklist's resume/take-home interview details are appropriately compressed
  out of the article.

## Layer-by-layer notes

### Spec

- Well-structured; six checkable criteria that partition the arc without
  overlap; Non-goals cleanly separate the internal-promotion and
  terrain-mapping records. No bloat.
- The Intent's "would rather lose someone well than keep them badly" framing is
  the article's spine — good example of the spec actually driving the post.

### index.md

- House shape fully observed; the Rationale's five paragraphs mirror the
  Statement's five stages in order, which makes the article easy to navigate.
- "A manager who can't discuss leaving can't coach a career" is a strong,
  quotable opening rationale — the best paragraph in the piece.
- All three figures exist on disk and are captioned; eight anti-patterns map
  cleanly onto the stages.

### checklist.md

- Verified against the source PDF: all six sections reproduced faithfully,
  converted from the PDF's imperative to the engineer's first person — a
  legitimate adaptation consistent with the spec's "reproduced, adapted".
  Task-list markdown is well formed; section numbering matches the PDF's.

### comics.md

- Eight panels, all image files present under
  `assets/images/changing-jobs/`; alt text and captions agree (panel 7 label
  aside); the offer-letter/crates/fork/bridge metaphors are coherent.
- Panel 8 ("leave well … stays a colleague for decades") is a faithful echo of
  the highlight's closing line — good closer discipline.

## Fixes applied (2026-07-29)

- **Verbatim self-repetition** — "trust, context, influence" trimmed from two of its six article sites as the review suggests: the practice-table row now reads "the switch's reset costs are real" and anti-pattern 3 now reads "not everything rebuilt from zero"; the triple remains in the highlight, Statement bullet 2, Rationale ¶3, and Figure 2 caption.
- **Comic caption fix** — Panel 7 caption lead reworded from "The cost:" to "The follow-through:", matching the panel's deliberate-landing content.
