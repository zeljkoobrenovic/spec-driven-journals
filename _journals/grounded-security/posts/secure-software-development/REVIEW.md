# Review: Secure Software Development

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready. The checklist is a verbatim-faithful reproduction of the source
chapter checklist (all four sections with their subsections — seven
language-specific considerations, the three testing methods, all six SDLC
stages — and the Final Review; nothing invented, nothing dropped), all six
spec success criteria are met, every `[[link]]` resolves, the tab tour names
exactly Checklist / TL;DR / Conversation, the summary is 491 words, and the
four modalities carry one consistent argument. The Rationale is the strongest
in the batch so far — "poured concrete," "risk allocation, whether we admit it
or not," and the "formally addressed is the honest release valve" paragraph
all earn their place. Findings are cosmetic.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Statement, Go bullet]** The article's Go line lists "garbage
  collection, strong typing, and bounds checking" but drops "limited pointer
  arithmetic," which the source (and checklist.md) include as a fourth
  advantage. Harmless compression, but the list reads as complete when it is
  not. *Add "limited pointer arithmetic."*
- **[dialog.md · "The Stage Everyone Forgets" heading]** The section covers
  three stages (training, requirements, release), so the singular heading
  undersells its own content — the same heading-coverage nit the journal's
  exemplar review flagged. *Pluralize to "The Stages Everyone Forgets."*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~150 words). Journal house pattern; awareness only.

## Spec ↔ post alignment

All six success criteria met:

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (built-in over bolted-on → final review as gate) |
| Language selection survives | met | index.md Statement block 1 (all seven language considerations); checklist.md §1 |
| Secure coding guidelines survive | met | index.md Statement block 2 (broad input definition, four validation checks, approved libraries, eight standard areas, sessions, client–server); checklist.md §2 |
| Testing trio survives | met | index.md Statement block 3 (static incl. secret detection and named limit, dynamic, peer review); checklist.md §3 |
| Six-stage SDLC survives | met | index.md Statement block 4 (all six stages with their commitments); checklist.md §4 |
| Final review survives as the gate | met | index.md Statement block 5 + highlight closer; checklist.md Final Review |
| Credit is explicit | met | index.md Authoritative References |

Non-goals respected: vulnerability-management, standards-and-procedures,
user-education, authentication, and databases each appear only as scoped
negative space with correct `[[…]]` pointers; tools framed as capabilities,
not mandates. Drift: none; spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — six stages named identically everywhere;
  the final-review clauses match across highlight, Statement, checklist, and
  Ana's first answer; "formally addressed" is glossed the same way in index
  and dialog (documented, owned decision — with the dialog adding the apt
  cross-reference to risk-acceptance discipline in [[vulnerability-management]]).
- **Terminology:** "built in, not bolted on," "poured concrete," "the
  suppressed finding," "artisanal crypto," "the orphaned release," "a release
  is not done when the code ships; it is done when someone can operate it
  under attack" recur verbatim where needed.
- **Coverage parity:** even — all five Statement blocks surface in summary
  bullets and dialog sections; the summary compresses the trio and lifecycle
  into single bullets without losing commitments.

## Layer-by-layer notes

### Spec

Well-formed; the success criteria are unusually detailed (the language and
SDLC criteria enumerate every sub-commitment), which made verification easy —
every enumerated item is traceable in index.md and checklist.md.

### index.md

House record shape fully observed: DRAFT highlight matching `draft:gray`,
Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
Related Records → Scope and Revisiting → Authoritative References. All six
distinct `[[…]]` targets valid. No image references; no icon/logo front
matter. The Scope section's AI-assisted-code clause ("changes the volume and
character of code the gate must judge, not the gate itself") is a nice
future-proofing touch beyond the source.

### checklist.md

Faithful to the source PDF section by section, including nested sub-bullets
(input channels, standards areas, secret types) and the unnumbered Final
Review kept outside the four-section sequence, matching the source's
placement.

### summary.md

491 words — at the top of the 300–500 band but inside it; leads with the
decision; honest costs (schedule time, tooling investment, standards
maintenance as owned living documents); correct not-doing list.

### dialog.md

Ben's objections are the real ones (the conference-slide objection, the
escape-hatch objection, the rewrite-in-Rust objection, the
three-thousand-findings war story) and Ana answers from the record rather
than around it. The closer ("turn 'we care about security' into evidence")
is earned.

## Fixes applied (2026-08-22)

- **[nit · index.md Statement, Go bullet]** Added "limited pointer
  arithmetic" to Go's listed protections, completing the source's list.
- **[nit · dialog.md]** Section heading pluralized to "The Stages Everyone
  Forgets" to cover training, requirements, and release.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
