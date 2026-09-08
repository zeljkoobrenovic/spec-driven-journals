# Review: Logging and Monitoring

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready. This is the largest source checklist in the batch and the
reproduction is faithful throughout: all 17 source sections in source order
(SIEM Planning and Design through Ongoing SIEM Maintenance), the Sysmon
event-ID subsection, the three cloud-provider subsections, and the closing
analysts-can-investigate bar — nothing invented, nothing dropped (the
checklist adds section numbering the source lacks, which aids navigation and
loses nothing). All six spec success criteria are met, every `[[link]]`
resolves, the tab tour names exactly Checklist / TL;DR / Conversation, the
summary is 457 words, and the article's Rationale ("Collecting everything is
a decision to find nothing," "An alert nobody can investigate is noise with a
severity label," "A SIEM tuned once at installation is a museum") is the
record at its best. Findings are cosmetic.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[dialog.md · Ben's concession]** "Alright" — the journal's other dialogs
  use "All right." *Normalize.*
- **[summary.md · "What changes" bullets 3 and 5]** Two of five bullets open
  with the same lead ("Coverage becomes estate-wide." / "Coverage becomes
  inspectable."). Reads as a deliberate echo and both claims are accurate;
  noted for awareness. *No change — author-voice call.*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~140 words). Journal house pattern; awareness only.

## Spec ↔ post alignment

All six success criteria met:

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (risk-first design → centralize → coverage → tested-not-trusted → investigable-alert test) |
| SIEM planning survives | met | index.md Statement block 1 (scope, compliance, high-value systems, use cases, frameworks, prioritization, PoC + red-team validation, ROA, central storage, cost-aware collection, high-value-first); checklist.md §1 |
| Analysis and alerting survive | met | index.md Statement block 2; checklist.md §2 |
| Estate-wide coverage survives | met | index.md Statement block 3 (six coverage bullets spanning §§3–14); checklist.md §§3–14 incl. Sysmon event IDs and all three cloud providers |
| Detection testing survives | met | index.md Statement block 4; checklist.md §15 |
| Frameworks and maintenance survive | met | index.md Statement block 5; checklist.md §§16–17 incl. the closing analysts-know bar |
| Credit is explicit | met | index.md Authoritative References (handbook, MITRE ATT&CK, Sigma) |

Non-goals respected: ids-ips, incident-response, osint-purple-teaming, and
the hardening records appear only as consuming/negative-space references with
correct `[[…]]` pointers; Sysmon/Sigma/CloudTrail are framed as worked
examples in How to Read This, exactly as the spec's tool non-goal requires.
Drift: none; spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the Record of Authority, the
  central-storage rule and its attackers-delete-local-logs justification, the
  collect-all-vs-collect-needed cost framing, and the double-barreled closing
  test appear identically in all four files.
- **Terminology:** "designed from risk backwards," "the worst hour," "noise
  with a severity label," "tested, not trusted," "a museum of the environment
  as it existed that quarter," and "log warehouse" recur verbatim where each
  modality needs them.
- **Coverage parity:** even — the five Statement blocks map cleanly to the
  five summary bullets and the dialog's five sections; the dialog gives DNS
  and cloud their own beats, matching the Rationale's emphasis.

## Layer-by-layer notes

### Spec

Well-formed; the estate-coverage criterion enumerates all twelve coverage
domains and every one is traceable in the article's Statement and the
checklist. Success criteria wording matches what shipped.

### index.md

House record shape fully observed: DRAFT highlight matching `draft:gray`,
Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
Related Records → Scope and Revisiting → Authoritative References. All seven
distinct `[[…]]` targets valid. No image references; no icon/logo front
matter. The "incident-response … investigation rather than an archaeology
dig" line in How to Read This earns its place.

### checklist.md

Faithful to the source section by section; the added 1–17 numbering and the
nested restructuring of the Sysmon event bullets are lossless improvements;
all sub-bullets (Sysmon event details, cloud provider items) present.

### summary.md

457 words; leads with the decision; honest costs (real money scaling with
volume, standing analyst time, discipline to delete comforting noise);
correct not-doing list with resolving links.

### dialog.md

Strong: opens on the CFO's question, and Ben's objections are the real ones
(collect-less means answer-less later; everyone says "actionable"; is the
coverage list log-everything through the side door; why re-test respected
rulesets). Ana's "CI for the SOC" and Ben's closing "the dashboards were
never the point; the answers at three a.m. are" both land.

## Fixes applied (2026-08-22)

- **[nit · dialog.md]** "Alright." → "All right." in Ben's concession,
  matching the journal's other dialogs.
- **[nit · summary.md bullets 3/5]** Skipped — deliberate parallel echo;
  author-voice call.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
