# Review: Policies: What Must Be Achieved, in Writing

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready. The checklist reproduces the source chapter checklist
verbatim — all six sections (Foundation, Language, Required Document
Contents, the 26-item Coverage list, Management, Review and Maintenance)
with nothing invented and nothing omitted. All eight success criteria are
met, every `[[link]]` resolves, the findability test is stated identically
in all four modalities, and the dialog's "twenty-six items" claim checks
out against the source. The Rationale carries the record: "'Should' is a
loophole spelled politely," "an unowned policy is a rumor," and "coverage
gaps are silent permissions" are exactly the quotable formulations the spec
asks for. The one fidelity slip: the article's coverage sweep merged the
source's "Workstation security" and "Server security and auditing" into
"workstation and server security," silently dropping the auditing scope —
now restored.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Statement, "Coverage is deliberate, not accidental"]** The
  coverage sweep renders the source's separate "Workstation security" and
  "Server security and auditing" entries as "workstation and server
  security," dropping "auditing" — the only lossy compression in an
  otherwise item-complete sweep (all 26 source entries otherwise
  accounted for; checklist.md keeps them verbatim). *Restore "server
  security and auditing."*
- **[index.md · same bullet]** The coverage paragraph is a single ~100-word
  sentence. It deliberately mirrors the source's flat list and ends on the
  record's own line ("a gap in coverage is a silent permission"), so the
  length reads as a rhetorical sweep rather than a defect; noted only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (what-not-how, language rule, governed document, lifecycle, findability test) | met | index.md · highlight |
| Policy foundation survives | met | index.md · Statement block 1; checklist.md · Policy Foundation |
| Language discipline survives (must/will/shall/do; exceptions documented) | met | index.md · Statement block 2; checklist.md · Policy Language |
| Required document contents survive | met | index.md · Statement block 3; checklist.md · Required Document Contents |
| Coverage list survives (full 26-item list in the checklist) | met | checklist.md · Policy Coverage (verbatim); index.md coverage sweep (fidelity fix applied) |
| Policy management survives (separate docs, framework, central storage, backup + physical copies) | met | index.md · Statement block 5; checklist.md · Policy Management |
| Living-document lifecycle survives | met | index.md · Statement block 6; checklist.md · Review and Maintenance |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — the how is consistently deferred to
[[standards-and-procedures]], policy substance to the named records, and
the compliance frame to [[compliance]]; nothing in any modality writes a
policy's content. Drift: none; spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the what/how split, the banned-words
  list, documented exceptions, backup and physical copies, annual +
  triggered review, and the two-directional findability test appear
  identically across article, checklist, summary, and dialog.
- **Terminology:** consistent — "an unowned policy is a rumor," "a written
  exception is a decision and an unwritten one is erosion" / "quiet
  amendment," "a policy nobody can find binds nobody," and the
  archaeology/sediment imagery recur without contradiction.
- **Coverage parity:** even — each of the six checklist sections gets an
  article Statement block, a summary bullet, and a dialog exchange; the
  eight anti-patterns are distributed across the dialog rather than listed,
  which suits the form.

## Layer-by-layer notes

### Spec

- Well-formed; the non-goals section is unusually sharp (the "not the
  content of each named policy" boundary pre-empts the obvious scope
  creep), and the load-bearing test appears word-identical in all four
  modalities.

### index.md

- House record shape fully observed: DRAFT highlight matching
  `status: draft:gray`, MADR-ish order, contrast table, eight anti-patterns,
  six related records, revisit triggers tied to the record's own test. No
  icon/logo front matter, no images, date 2026-08-22. Tab tour names
  Checklist, TL;DR, and Conversation only.
- All 6 distinct `[[…]]` targets are valid journal slugs.

### checklist.md

- Verbatim-faithful to `Checklist_ DSH _ 03`: six sections, unnumbered as in
  the source, every item present including the full 26-entry coverage list.
  No invented obligations. Closing paragraph hands off to
  [[standards-and-procedures]] and restates the two-directional test.

### summary.md

- 446 words, in band; costs are honest (per-document governance overhead,
  leadership attention in "still true, re-dated" years, two document
  layers); not-doing list matches the spec's non-goals with resolving links.

### dialog.md

- Ben's objections are the right ones (binders vs. protection, vagueness,
  grammar-as-control, exceptions driven underground, paper in 2026); Ana's
  answers stay inside the record and the closing "condition" exchange is a
  genuinely good landing. "Twenty-six items" verified against the source.

## Fixes applied (2026-08-22)

- **[nit · index.md coverage sweep]** "workstation and server security" →
  "workstation security, server security and auditing" — restores the
  auditing scope the source's separate entries carry; the sweep is now
  item-complete against all 26 source entries.
- **[nit · index.md coverage sentence length]** Skipped — the single-sweep
  sentence is a deliberate rhetorical mirror of the source list; splitting
  it would dilute the "silent permission" landing.
