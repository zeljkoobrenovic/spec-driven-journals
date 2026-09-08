# Review: Incident Response

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready, and the strongest of the section-openers: the lifecycle
argument (peacetime preparation → cheap escalation → formal declaration →
evidence-first → gated CER → one voice → tracked review) is carried
consistently through all four modalities, and the 2 a.m. test gives the
record a cultural spine that survives every compression. The checklist is a
complete, faithful reproduction of the source PDF — all fifteen sections
plus the Final Verification, every sub-list (including the named tools:
tcpdump, Wireshark, TShark, Snort, Zeek) present, nothing invented. All
seven success criteria are met, every `[[…]]` cross-link resolves, the tab
tour names exactly Checklist / TL;DR / Conversation, the highlight's DRAFT
matches `draft:gray`, and the summary lands at 496 words. The one claim
worth correcting: article and dialog both say "almost half" of the
chapter's checklist runs before any incident exists — the pre-incident
sections are three of fifteen (about 24 of ~180 items), so the true point
(preparation leads, prominently) should be made without the inflated
proportion.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Rationale ¶1; dialog.md · Ana's first answer]** "Almost half
  of the chapter's checklist runs before any incident exists … and that
  proportion is the message" (and the dialog's "nearly half of it runs
  before any incident exists"). Against the source, Pre-Incident
  Preparation is three sections of fifteen — roughly 24 items out of ~180.
  The rhetorical point (the checklist leads with peacetime work, and that
  placement is deliberate) is right; the arithmetic is not. *Rephrase to
  the accurate form — e.g. "the checklist opens with three full sections of
  pre-incident preparation … and that placement is the message."*

### Nits

- **[index.md · Statement, "The technical floor is laid"]** "EDR coverage
  confirmed on critical systems" — the source and checklist say EDR/XDR/MDR
  throughout, and the spec's success criterion names the triple. Harmless
  compression, but cheap to align in the article's fullest modality.
  *Use "EDR/XDR/MDR coverage."* (summary.md's "EDR coverage" is acceptable
  compression for its form.)
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~150 words). Journal house pattern; noted only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (full lifecycle + 2 a.m. test) |
| Pre-incident preparation survives | met | index.md · Statement block 1; checklist.md §1 (all three sub-sections) |
| Declaration and management survive | met | index.md · Statement blocks 2–3; checklist.md §§2–3 (coordination, goals, sustained ops) |
| Evidence discipline survives | met | index.md · Statement block 4 + Rationale ¶4; checklist.md §4 |
| Investigation breadth survives | met | index.md · Statement block 5; checklist.md §§5–9 incl. named tools |
| Containment/eradication/recovery gates survive | met | index.md · Statement block 6 + Rationale ¶¶5–6; checklist.md §§10–12 |
| Communications and closure survive | met | index.md · Statement blocks 7–8; checklist.md §§13–15 + Final Verification |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — [[disaster-recovery]], [[phishing-response]],
[[logging-and-monitoring]], and [[ids-ips]] appear only as boundary
pointers; tool names stay in the checklist while the article holds the
capability level, exactly as the spec's "not a forensics manual" non-goal
demands.

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — early-escalation economics (false
  positive costs minutes, late escalation costs the investigation),
  declaration as clock-and-command, the wiped-laptop and premature-all-clear
  anti-patterns, "one incident into two," and the tracked-actions closure
  standard match across article, summary, and dialog. One arithmetic
  inflation noted under Minor.
- **Terminology:** consistent — "practiced discipline, not an
  improvisation," "an incident nobody declared is an incident nobody
  managed," "rebuilt where trust cannot be restored," and the 2 a.m. test
  recur verbatim where each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben
  match the journal cast.
- **Coverage parity:** even — the dialog gives every article beat a
  section, and the summary's six "What changes" bullets map cleanly onto
  the Statement's eight blocks.

## Layer-by-layer notes

### Spec

- The most detailed spec of the section; the compound success criteria
  enumerate the source at item granularity, which made fidelity checking
  mechanical. Non-goals draw the four neighboring-record boundaries
  precisely.

### index.md

- House record shape fully observed: DRAFT highlight matching front matter,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns
  → Related Records → Scope → References. No images, no icon/logo front
  matter. All seven `[[…]]` targets are valid journal slugs.
- Rationale is uniformly strong; "attackers with persistence treat your
  containment as their notification" and "an incident nobody declared is an
  incident nobody managed" are the record's best lines.

### checklist.md

- Complete and faithful against the PDF: Pre-Incident Preparation (3
  sub-sections), Declaration, Management (3 sub-sections), Evidence
  Preservation, Log Analysis, EDR/XDR/MDR, Disk and File, Memory,
  Network/PCAP with Common Analysis Tools, Containment, Eradication,
  Recovery, Communications (Internal/External), Closure, Post-Incident
  Review, Final Verification. No invented obligations; wording tracks the
  source with only cosmetic smoothing.

### summary.md

- On target: leads with the decision, 496 words (at the cap but inside it),
  honest "What it costs" (standing telemetry and retainer spend, evidence
  discipline deliberately slowing quick fixes, recurring drills), correct
  not-doing list with resolving links.

### dialog.md

- Ben's objections are the real practitioner ones (retainers for a
  hypothetical, noise from nervous developers, reimage-now SLAs, "we're not
  a courtroom," a press office for a technical response) and Ana answers
  from the record without inventing beyond it. The closer compresses the
  record honestly.

## Fixes applied (2026-08-22)

- **[minor · index.md · Rationale ¶1]** "Almost half of the chapter's
  checklist runs before any incident exists … and that proportion is the
  message" → "The chapter's checklist opens with three full sections of
  pre-incident preparation before any incident exists … and that placement
  is the message."
- **[minor · dialog.md]** "Look at where the chapter spends its checklist:
  nearly half of it runs before any incident exists." → "Look at how the
  chapter's checklist opens: three full sections run before any incident
  exists."
- **[nit · index.md · Statement]** "EDR coverage confirmed on critical
  systems" → "EDR/XDR/MDR coverage confirmed on critical systems," matching
  source, checklist, and spec.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
