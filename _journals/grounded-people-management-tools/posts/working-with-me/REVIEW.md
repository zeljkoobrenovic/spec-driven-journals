# Review: Working with Me

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Strong, publish-ready post. The article is well-grounded in the workbook's
"Working with Claire" essay and the "Working with Me Template," the checklist
faithfully operationalizes the same five-field template plus the cadence and
communication mechanics, and the comic hits the same beats in the house
VERA/NOA style. The single thing worth fixing before calling this done: the
article's Rationale tells the 2010 anecdote but never names the "good craic"
detail that the spec and checklist both use as the load-bearing term for "the
personal, non-work detail" — a reader who only reads the article won't
recognize the phrase the checklist asks them to reproduce.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Major
- **[index.md · Rationale, "A management style nobody wrote down…" paragraph]**
  The anecdote is retold ("her executive assistant read the draft and told her
  it was missing 'the most important thing' — that she likes to have a good
  laugh at work") but drops the source's own term, "good craic," and the
  assistant's name (Maeve), both of which the spec's Decision log calls out as
  the anchor and which `checklist.md` item 2 uses verbatim ("the 'good craic'
  note"). A reader who hits the checklist without having internalized that
  phrase from the article will not connect the two. *Either name "good craic"
  in the article's retelling, or drop the term from the checklist so neither
  modality depends on the other for the phrase to land.*

### Minor
- **[index.md · Rationale, "Declaring my decision style is a kindness…"]** The
  paragraph covers collaborative-but-slow and hands-off/hands-on well but never
  states the source's "I expect you to do the same" / "make sure I know it"
  framing as a two-way ask as crisply as `checklist.md` §4 does; a reader gets
  the norm but not that it's explicitly reciprocal in the source text. Small
  gap, not a contradiction.
- **[spec.md · Success criteria]** The sixth criterion ("the checklist
  operationalizes the actual template") bundles two different claims — template
  fidelity and reproduction of cadence/communication mechanics — under one
  checkbox. Both are true and both are met, but as written the criterion isn't
  independently falsifiable from its neighbors; consider splitting if the spec
  is revised.

### Nits
- **[index.md · Related Records]** Six cross-links, all resolving to existing
  posts in the journal (verified against `config.yaml`) — no issue, noted only
  because it's worth confirming stays true if any target post is renamed.
- **[checklist.md · §1 "My role"]** Item 3 ("Note anything about scope that's
  likely to be unclear from the title alone") is a reasonable elaboration of
  the source's one-line "Describe your role and goals," but it's the checklist's
  only invented item with no direct anchor in the workbook text or the article
  — harmless, just flag it as an addition rather than a distillation if the
  spec is ever audited line-by-line against the source.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (self-awareness framing) | met | index.md highlight + Statement intro |
| Cadence survives with numbers | met | index.md Rationale ¶2; checklist.md §3 |
| Decision style stated honestly | met | index.md Rationale ¶3; checklist.md §4–5 |
| Communication contract explicit | met | index.md Rationale ¶5; checklist.md §9–10 |
| Feedback redirect rule named | met | index.md Rationale ¶6; checklist.md §11 |
| Checklist operationalizes the template | met | checklist.md §1–2 (My role/About me), §3–11 (cadence/style/comms/feedback) |

Non-goals respected: yes — no drift into `management-prerequisites` baseline-cadence
territory, `self-awareness` inventory mechanics, `new-leader-onboarding` sequence,
or formal performance-review process; the feedback commitment stays a personal
norm, not review mechanics.

Drift: none. Spec `status: accepted` against post `draft:gray` is the journal's
standard convention (spec is a settled contract; the record itself is `draft`
pending real-world testing) — not a finding.

## Cross-modality alignment

- **Facts & framing:** consistent — 18-hour email window, FYI rule, collaborative-but-slow
  with the escape hatch, hands-off/hands-on exception, quarterly 3–5 personal
  goals, and the venting-redirect rule all appear the same way across index,
  checklist, and comics.
- **Terminology:** mostly consistent, with the one gap above — "good craic" is
  used in spec.md and checklist.md but the article paraphrases it away.
  Otherwise load-bearing phrases ("FYI = no response required," "what do you
  want to do?," "measure, measure, measure") are reused verbatim across
  index.md, checklist.md, and comics.md panel 6/8 captions.
- **Voice & tone:** consistent first-person declarative register across index
  and checklist; comics captions compress the same voice appropriately for the
  form (terser, present-tense, no loss of the core claims).
- **Coverage parity:** even. Every load-bearing beat in index.md (undocumented
  style costs, cadence-as-numbers, collaborative-but-slow, hands-off exception,
  data-vs-intuition, communication contract, feedback redirect, "quote it back"
  test) is echoed in checklist.md as an actionable item and in comics.md as a
  panel (1–8). No modality introduces a major beat the others lack.

## Layer-by-layer notes

### Spec
- Follows the template sections exactly; each Success criterion is checked and
  traceable to specific text in index.md/checklist.md.
- Decision log usefully records *why* the 2010 anecdote anchors the framing —
  but that framing choice (name "good craic" explicitly) didn't fully survive
  into the article's prose (see Major finding).
- Non-goals are precise and correctly fenced against four neighboring records.
- No stale Open questions; none listed, correctly.

### index.md
- House record shape is intact: Status/Principle highlight, Statement →
  How to Read This → Rationale → What This Means in Practice → Anti-Patterns →
  Related Records → Scope and Revisiting → Authoritative References, in the
  conventional order.
- Section headings are correct Title Case throughout.
- Three figures (five-layers, hands-off/hands-on, communication-contract-flow)
  all have matching image files in `assets/images/working-with-me/` and
  numbered captions.
- The "What This Means in Practice" contrast table is well-formed and each row
  pairs a clean claim with its plausible misreading — a strong instance of the
  journal's contrast-table convention.
- Six `[[...]]` cross-links all resolve to real posts in the same journal
  (`self-awareness`, `management-prerequisites`, `new-leader-onboarding`,
  `manager-transitions`, `career-conversations`) plus one to
  `grounded-engineering-executive`'s `leadership-styles` — all present.

### checklist.md
- Faithfully reproduces the five-field "Working with Me Template" (My role,
  About me, Operating approach, Management style, Supporting you and your
  team) as sections 1–2, 3, 4–8, and 9–11, plus a "Keep it current" closer
  (§12) that isn't in the source template but is a reasonable operational
  addition consistent with the spec's "keep it current" framing.
- The cadence table (§3), the loop-me-in item, and the personal-goals cadence
  item all match the workbook's "Working with Claire" numbers exactly
  (biweekly/weekly, 3–5 goals, 3–6 months, 18-hour read window).
- Sentence-case headings are the journal's own convention here, not a finding.
- No orphaned or unchecked-but-irrelevant items; every checkbox maps to a
  concrete, workbook-grounded commitment.

### comics.md
- 8 panels, cast block matches the journal-standard VERA/NOA character sheet
  used in `self-awareness/comics.md` and other posts in this journal —
  consistent shared cast.
- All 8 panel image files exist in `assets/images/working-with-me/` with
  matching filenames.
- Captions track the article's main beats in order (undocumented style →
  guessing tax → "door is open" strawman → the document as tool → first-week
  handoff → 18-hour rule → collaborative-but-slow escape hatch → "quote it
  back" close) — a clean narrative arc that mirrors the article's Rationale
  paragraph order.
- Visual metaphor (document as artifact, clock/inbox for the 18-hour rule,
  escape-hatch lever for urgency) stays consistent panel to panel.

## Fixes applied (2026-07-29)

- [Major, index.md Rationale] Fixed — named "good craic" and the executive
  assistant Maeve explicitly in the 2010 anecdote retelling, anchoring the
  term the checklist references ("the 'good craic' note").
- [Minor, index.md Rationale, decision-style paragraph] Fixed — added an
  explicit reciprocity sentence ("I expect you to do the same and to make
  sure I know it... just as I commit to telling you when I'm about to get
  hands-on") so the two-way ask reads as crisply as checklist.md §4–5.
- [Minor, spec.md Success criteria] Fixed — split the sixth criterion into
  two independently falsifiable checkboxes: template reproduction, and
  cadence/communication operationalization. Bumped `revised:` to 2026-07-29
  and added a Changelog line.
- [Nit, index.md Related Records — cross-link stability] Skipped — not a
  fix, just a standing observation to reverify if a target post is renamed;
  no action needed now.
- [Nit, checklist.md §1 item 3 — invented item] Skipped — flagged only as a
  documentation note for a future line-by-line spec audit; the item itself
  is accurate and harmless, no change needed.
- Comic-panel count verified: comics.md has exactly 8 panels with 8 matching
  image files in `assets/images/working-with-me/`, consistent with the
  journal's 8-panel convention. The review (REVIEW.md, "comics.md" section)
  already states "8 panels" correctly — there is no "9" miscount in this
  review to correct.
