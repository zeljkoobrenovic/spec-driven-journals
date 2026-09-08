# Review: Security Education

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready. The record makes the strongest possible case for the chapter's
core move — users as an engineered control, baseline before program, behavior
change over completion rates — and all four modalities tell the same story
without contradiction. The checklist is a faithful item-for-item reproduction
of the source PDF (all nine sections, Program Design through Final Review;
nothing invented, nothing dropped). All ten success criteria are met, every
`[[…]]` cross-link resolves to a journal slug, the tab tour names exactly
Checklist / TL;DR / Conversation, the highlight's DRAFT matches the
front-matter `draft:gray`, and the summary lands at 457 words. The only real
wobble is a naming inconsistency between spec and article over what the source
chapter is called.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[spec.md · Sources/External; Intent ¶1]** The spec calls the source "the
  Security Education chapter," but the book's chapter is *User Education* —
  the *checklist* is what is titled Security Education. index.md gets this
  exactly right ("the User Education chapter … whose checklist is titled
  Security Education"), so the spec and the article disagree about the
  chapter's name. *Align the spec's external-source line (and Intent) to "the
  User Education chapter, whose checklist is titled Security Education."*

### Nits

- **[index.md · Scope and Revisiting]** "everyone in my organization —
  employees, and contractors within our systems" — stray comma in a
  two-element list. *Drop the comma.*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~130 words). This is the journal's established house
  pattern, so noted only for awareness.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (ongoing-not-annual, baseline-first, no-blame, behavior-change test) |
| Program design survives | met | index.md · Statement block 1; checklist.md §1; summary bullet 1 |
| Baseline discipline survives | met | index.md · Statement block 2 + Rationale ¶2; checklist.md §2 |
| Rules and reporting survive | met | index.md · Statement block 3; checklist.md §3 |
| Training and reinforcement survive | met | index.md · Statement block 4 + Rationale ¶5; checklist.md §4 |
| Positive reinforcement survives | met | index.md · Statement block 5 + Rationale ¶4; checklist.md §5; dialog "Never Punish the Report" |
| Incident-response coupling survives | met | index.md · Statement block 6 + Rationale ¶6; checklist.md §6; dialog "The Exercise Tests Us Too" |
| Metrics loop survives | met | index.md · Statement block 7; checklist.md §§7–8 (full tracking set + success measures) |
| Final review survives as completion check | met | checklist.md §9 (all five items) |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — [[phishing-response]], [[incident-response]],
[[policies]], and [[security-program]] each appear only as negative space with
the correct pointers; no vendor or platform is named anywhere.

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the two-line board report
  (reporting-rate and click-rate trends against the baseline), the
  "cheapest incident is the one reported in minutes" economics, the
  serial-clicker carve-out (management matter, outside the program), and
  the false-positives-are-the-price stance match across article, summary,
  and dialog.
- **Terminology:** consistent — "controls get engineered, not lectured,"
  "behavior change against the baseline, not course-completion rates,"
  "completion-rate theater" recur verbatim where each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben
  match the journal's dialog cast.
- **Coverage parity:** even. The dialog compresses the rules-and-guidelines
  beat (stakeholder input, policy consistency) to implication, which is
  acceptable — it is the least argumentative section of the source.

## Layer-by-layer notes

### Spec

- Well-formed against the template; success criteria map one-to-one onto the
  source's nine sections plus credit. The chapter-name slip noted under Minor
  is the only blemish.

### index.md

- House record shape fully observed: DRAFT highlight matching front matter,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
  Related Records → Scope → References. No image references, no icon/logo
  front matter — correct for this journal's current stage.
- Rationale is the strongest section: "treating users as the problem produces
  exactly the users you feared," "a program with twelve objectives has none,"
  "fear teaches concealment" all earn their place.
- All six distinct `[[…]]` targets are valid journal slugs.

### checklist.md

- Faithful to the source PDF section by section: Program Design (7 items),
  Establish a Baseline (4), Rules and Guidelines (5), Training and
  Reinforcement (6), Positive Reinforcement (5), Incident Response (4),
  Metrics to Track (10), Measure Overall Success (7), Final Review (5) — all
  present, no invented obligations, wording tracks the source with only
  cosmetic smoothing.

### summary.md

- On target: leads with the decision, 457 words, honest "What it costs"
  (standing work, delayed launch, false-positive noise), correct not-doing
  list with resolving links.

### dialog.md

- Ben presses with the real objections (nobody believes in awareness
  training; the baseline is a delay; where is the accountability; false
  positives) and Ana's answers carry the record's actual arguments. The
  closer — "the module produces certificates; the program produces reports
  in minutes" — is the record's argument in one line.

## Fixes applied (2026-08-22)

- **[minor · spec.md]** External-source line and Intent aligned to the
  article's (correct) naming: the *User Education* chapter, whose checklist
  is titled Security Education.
- **[nit · index.md · Scope and Revisiting]** Stray comma removed
  ("employees and contractors within our systems").
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the
  journal's established house pattern.
