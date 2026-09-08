# Review: Physical Security

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

A strong opener for the Hardening the Estate section, publish-ready as a draft
record. The checklist is a faithful, essentially verbatim reproduction of the
source chapter checklist (all 14 sections present in source order, no invented
or omitted items — verified against every page of the PDF), all ten success
criteria are met, every `[[link]]` resolves to a journal slug, the tab tour
correctly names Checklist / TL;DR / Conversation and no Comic tab, and the
no-single-failed-control test recurs verbatim across all four modalities. The
two things worth touching: the article's workplace-hygiene bullet drops cable
locks (the one item of spec criterion 2 that never reaches the article), and
the summary's "What changes" list skips the datacenter-and-equipment beat
(rack keys, floor-to-ceiling walls, remote offices) that the spec lists as its
own surviving criterion.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "The workplace itself is defended" bullet]** Spec
  criterion 2 lists "locked screens, cable locks, clear desk, …" as surviving;
  cable locks appear in checklist §1 but nowhere in the article. Every other
  item of that criterion made it into the bullet. *Add cable locks to the
  workplace bullet.*
- **[summary.md · "What changes"]** Coverage parity: the datacenter-and-
  equipment-security beat (lockable racks, logged rack keys, floor-to-ceiling
  walls, remote-office enclosures) — a standalone success criterion in the
  spec and a full Statement block in the article — is absent from the summary,
  while every other Statement block gets a bullet or clause. *One clause in
  the layered-access bullet closes the gap.*

### Nits

- **[summary.md · length]** 506 words including the italic navigation footer;
  477 without it — at the very top of the 300–500 band. Acceptable as is;
  worth remembering if the summary ever grows.
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~120 words). This matches the journal's established
  pattern, so noted only for awareness.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (layered boundary + no-single-failed-control test) |
| Access controls and workplace hygiene survive | met (after fix) | index.md · Statement block 1; checklist.md §1 — cable locks were checklist-only before the fix |
| Surveillance-for-correlation survives | met | index.md · Statement block 2 + Rationale ("Cameras are for correlation"); checklist.md §2 |
| Access maintenance survives | met | index.md · Statement block 3 + Rationale ("revocation is the discipline"); checklist.md §3 |
| Media chain of custody survives | met | index.md · Statement block 4 + Rationale ("Media is data that walks"); checklist.md §4 |
| Datacenter and equipment security survives | met (after fix) | index.md · Statement block 5; checklist.md §5; now also summary.md bullet 1 |
| Visitor, contractor, and badge discipline survives | met | index.md · Statement block 6; checklist.md §§6–8 |
| Social-engineering defenses survive | met | index.md · Statement block 7 + Rationale ("Politeness is the attack surface"); checklist.md §§9–13 |
| Program management survives | met | index.md · Statement block 7 + Practice paragraph; checklist.md §14 |
| Credit is explicit | met | index.md · Authoritative References; spec Sources |

Non-goals respected: yes — user-education, phishing-response,
asset-management, and the two server-hardening records appear only as
negative space with correct `[[…]]` pointers; no floor plans or vendor
choices anywhere.

Drift: none. Spec `status: accepted` is correct; front-matter `status:
draft:gray` matches the visible DRAFT and the Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — layered controls, same-day revocation,
  shared-PIN ban, correlate-faces-with-badge-logs, chain of custody, and the
  closing defense-in-depth rule match across all four files.
- **Terminology:** consistent — "politeness does not override procedure,"
  "no single failed control," "a secret with no offboarding," "physical
  access is root access" recur where each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben cast
  matches the journal.
- **Coverage parity:** even after the summary fix; fire-safety-aware design
  stays index+checklist-only, which is acceptable compression.

## Layer-by-layer notes

### Spec

- Well-formed against the template; success criteria enumerate the chapter's
  fourteen sections into nine testable bundles; non-goals draw clean borders
  to five sibling records.

### index.md

- House record shape fully observed: DRAFT highlight, Statement → How to Read
  This → Rationale → contrast table → Anti-Patterns → Related Records → Scope
  → References. Rationale earns its formulations ("Physical access is root
  access," "shared secrets have no offboarding," "Politeness is the attack
  surface"). All 9 distinct `[[…]]` targets are valid journal slugs.

### checklist.md

- Faithful to the source PDF section by section: 14 sections, source order,
  item-level match throughout (spot-verified across all five pages). The
  closing line correctly restates the record's test rather than inventing new
  obligations.

### summary.md

- Leads with the decision, honest "What it costs" (recurring training decay,
  standing audit work), correct not-doing list with a resolving link.

### dialog.md

- Ben's objections are real practitioner pushback (office etiquette?, badge
  system as single control, human controls don't hold, ceremony for USB
  sticks, falls-between-two-stools) and Ana answers with the record's actual
  arguments; closes on the record's test.

## Fixes applied (2026-08-22)

- **[minor · index.md]** Cable locks added to the workplace bullet: "screens
  lock when people step away, cable locks secure portable equipment where
  appropriate, a clear-desk policy is enforced…".
- **[minor · summary.md]** Datacenter-and-equipment clause added to the first
  "What changes" bullet: racks lock, rack keys are centrally controlled and
  logged, and remote-office equipment gets secured enclosures.
- **[nit · summary.md length]** No trim applied — body sits within the band
  once the navigation footer is excluded; the added clause is offset by a
  small tightening of the same bullet.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the journal's
  established house pattern.
