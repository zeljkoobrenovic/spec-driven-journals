# Review: Disaster Recovery

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready and internally the tightest of the assigned batch. The
business-first spine (signed, priced RPO/RTO → per-system strategy →
dependency honesty → rehearsed failover/failback → tests without a safety
net → controls held through the disaster) is carried through all four
modalities without a single factual contradiction, and the anti-pattern
list is the journal's best so far ("the plan on the dead wiki," "the
security holiday," "the one-way failover"). The checklist is a complete,
faithful reproduction of the source PDF — all fifteen numbered sections,
item for item, nothing invented, nothing dropped. All nine success criteria
are met, every `[[…]]` cross-link resolves, the tab tour names exactly
Checklist / TL;DR / Conversation, and the highlight's DRAFT matches
`draft:gray`. The only rule breach found: the summary ran 515 words against
the journal's 300–500 band.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[summary.md · whole file]** 515 words — over the journal's 300–500 band
  for the TL;DR modality. The overflow is padding, not content: strategy
  bullet parentheticals and doubled qualifiers that the Article carries
  anyway. *Trim ~20 words without dropping any commitment.*

### Nits

- **[dialog.md · "Security During the Worst Week"]** "ransomware operators
  in particular count on recovery-mode sloppiness" — a reasonable
  inference, but it is the one sentence in the post arguing slightly beyond
  what the source or article states. Acceptable within the dialog's voice;
  noted for awareness only.
- **[index.md · front matter `excerpt`]** The excerpt reprises the
  highlight nearly verbatim (~160 words). Journal house pattern; noted
  only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (business-driven targets → restore-proven test) |
| Business-owned objectives survive | met | index.md · Statement block 1 + Rationale ¶1; checklist.md §1 |
| The strategy ladder survives | met | index.md · Statement block 2 + Rationale ¶2; checklist.md §2 (all five rungs with their honesty clauses) |
| Cloud-native DR survives | met | index.md · Statement block 3 + Rationale ¶3; checklist.md §3 (all twelve items incl. cost review) |
| Dependency discipline survives | met | index.md · Statement block 4 + Rationale ¶4; checklist.md §4 |
| Scenarios and procedures survive | met | index.md · Statement blocks 5–6 + Rationale ¶¶5, 8; checklist.md §§5–7 (six scenarios, failover, failback) |
| Honest testing survives | met | index.md · Statement block 7 + Rationale ¶6; checklist.md §8 |
| Security-through-disaster survives | met | index.md · Statement blocks 8–9 + Rationale ¶7; checklist.md §§9–15 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — [[incident-response]], [[cloud-infrastructure]],
[[physical-security]], and [[asset-management]] appear only as boundary
pointers; no backup product is named anywhere, honoring the
capability-level non-goal.

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the signed-and-priced targets, the
  slowest-dependency RTO rule, the transport-time honesty clause, the
  convenient-test and security-holiday anti-patterns, and the
  restore-proven test match across article, summary, and dialog.
- **Terminology:** consistent — "a backup that has never been restored is a
  hope, not a plan," "a recovery that reopens the breach is not a
  recovery," "silence during small outages is how organizations rehearse
  silence for the big one," and "cheaper to have and easier to fake" recur
  verbatim where each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben
  match the journal cast.
- **Coverage parity:** even — every Statement block has a summary bullet
  and a dialog beat; the dialog's closing "hope with a table of contents"
  is a worthy extension of the record's own test rather than a departure
  from it.

## Layer-by-layer notes

### Spec

- Well-formed; the success criteria enumerate the source at item
  granularity, and the Intent's one-sentence ladder summary matches the
  checklist's §2 exactly. "All fifteen sections" in Sources is accurate.

### index.md

- House record shape fully observed: DRAFT highlight matching front matter,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns
  → Related Records → Scope → References. No images, no icon/logo front
  matter. All six `[[…]]` targets are valid journal slugs.
- Rationale is uniformly strong; "RPO and RTO are business decisions
  wearing technical clothes" and "the cloud makes recovery cheaper to have
  and easier to fake" are the record's best formulations, and "failback is
  the forgotten half" earns its own paragraph.

### checklist.md

- Complete and faithful against the PDF: §§1–15 present with every item,
  including the §2 strategy sub-items (nested under their "Consider …"
  parents — a lossless structural improvement), the six §5 scenarios, and
  §15's business-continuity alignment closer. No invented obligations.

### summary.md

- Correct shape and content (decision first, honest costs, correct
  not-doing list with resolving links); length was the one issue, fixed
  below.

### dialog.md

- Ben's objections are the practitioner's real ones (green dashboard as
  solved problem, business owners dragged into infrastructure choices, the
  brutal-test pushback, 3 a.m. control-dropping as pragmatic triage) and
  Ana answers from the record. The closer is the record's test restated
  with a memorable tag.

## Fixes applied (2026-08-22)

- **[minor · summary.md]** Trimmed from 515 to 497 words: strategy bullet
  parentheticals compressed ("with transport and restore time" → "transport
  and restore time"; "(synchronized, geographically separated)" dropped —
  carried by article and checklist), "Critical systems are identified,
  each gets" → "Each critical system gets," failover bullet qualifiers
  tightened ("disaster-declaration" → "declaration," "exact documented
  steps" → "exact steps"), testing bullet verbs elided, and "tested against
  real scenarios" → "tested" in the lead (the scenarios remain in the
  bullets). No commitment dropped.
- **[nit · dialog.md]** Skipped — the ransomware-sloppiness inference is
  within the dialog's allowed voice.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
