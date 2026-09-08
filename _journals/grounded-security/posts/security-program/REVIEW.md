# Review: Creating a Security Program: Risk Before Tools

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

A strong, publish-ready opener for The Security Program section. The
checklist is a faithful, essentially verbatim reproduction of the source
chapter checklist — all 14 sections, every subsection (executive/risk/
security/audit/coordination, the nine baseline sweeps, the four treatments,
the seven kill-chain stages, the four tabletop phases, the full completion
review) — with nothing invented and nothing omitted. All eight success
criteria are met, every `[[link]]` resolves, the tab tour names Checklist,
TL;DR, and Conversation only, and the four modalities tell one story with no
factual wobbles. The Rationale is the best section — "Authority is a
control," "likelihood times impact converts anxiety into a queue," and
"accepted risk is a decision with a name and an expiry date" all earn their
place. Only one grammar slip found in a load-bearing Statement bullet.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Executive leadership with teeth"]** Zeugma:
  "sufficient authority to make organization-wide decisions, long-term
  goals, funding, and approval of major milestones" — "make" does not
  distribute over "goals/funding/approval" (the source gives each its own
  verb: establish goals, allocate funding, approve milestones). *Give each
  object its verb: "make organization-wide decisions, set long-term goals,
  allocate funding, and approve major milestones."*

### Nits

- **[index.md · highlight + Statement "Fit over fashion" + practice table
  row 1 + Rationale ¶1]** The blind-application warning appears four times.
  Within the house what/not-what/why layering, but the fourth pass (table)
  adds no new angle. Noted only.
- **[index.md · Statement, "A security team for daily operations"]** The
  security team's source duty list (asset management, threat and
  vulnerability assessment, monitoring, risk-management activities,
  training) is compressed to four items, dropping "risk-management
  activities" — retained verbatim in checklist.md §2, so lossless overall.
  Noted only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (program shape + risk-register test) | met | index.md · highlight |
| Groundwork and framework survive | met | index.md · Statement block 1; checklist.md §1 |
| Team structure survives (incl. RMF/OCTAVE, combine-then-separate) | met | index.md · Statement block 2; checklist.md §2 |
| Baseline posture survives (full nine-part sweep) | met | index.md · Statement block 3; checklist.md §3 |
| Risk assessment and treatment survive (1–5 ratings, four treatments, acceptance bar) | met | index.md · Statement blocks 4–6; checklist.md §§4–6 |
| Governance and prioritization survive | met | index.md · Statement blocks 7–8; checklist.md §§7–8 |
| Rehearsal survives (≈3 use cases, kill chain, tabletops, drills, skills, completion review) | met | index.md · Statement block 9; checklist.md §§10–14 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — asset management, policies, compliance, incident
response, and vulnerability management appear only as explicit hand-offs
with correct `[[…]]` pointers, and the record contains no product choices.
Drift: none; spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — Risk = Likelihood × Impact on 1–5,
  acceptance as "the most heavily documented treatment" with annual
  reassessment, business-context-before-vendor, four milestone tiers, the
  two-clean-tabletops revisit trigger, and the closing register test appear
  identically everywhere they recur.
- **Terminology:** consistent — "a backup that has never been restored is a
  hope, not a control," "suggestion box with a title," "risk register
  graveyard" recur verbatim where each modality needs them.
- **Coverage parity:** even; the dialog compresses kill-chain mapping and
  team skill development to mentions, which is proportionate for the form.

## Layer-by-layer notes

### Spec

- Well-formed; success criteria are compound (house pattern, noted not
  counted). The load-bearing test in Intent matches the article, checklist
  closing, summary, and dialog word for word.

### index.md

- House record shape fully observed: DRAFT highlight matching
  `status: draft:gray`, Statement → How to Read This → Rationale → contrast
  table → Anti-Patterns → Related Records → Scope and Revisiting →
  References. No icon/logo front matter, no images, date 2026-08-22.
- All 8 distinct `[[…]]` targets are valid journal slugs.

### checklist.md

- Verbatim-faithful to `Checklist_ DSH _ 01`: 14 numbered sections matching
  the source's numbering, all sub-bullets present (RMF/OCTAVE, the seven
  common threats, the nine tabletop departments); no invented obligations.
  Closing paragraph hands off to [[asset-management]] and restates the
  register test — consistent with the article.

### summary.md

- 459 words, in band; leads with the decision; costs are real costs
  (standing governance, cross-department tabletop time, deferred ambitions);
  not-doing list matches the spec's non-goals with resolving links.

### dialog.md

- Ben presses with genuine objections (numerology-with-a-spreadsheet,
  org-chart cosplay, register-goes-to-sleep, cyber-insurance itch); Ana's
  answers carry the record's actual arguments and the revisit triggers.
  Closes on the audit test — same wording as the article.

## Fixes applied (2026-08-22)

- **[minor · index.md Statement]** Executive-leadership bullet rewritten to
  distribute verbs: "…sufficient authority to make organization-wide
  decisions, set long-term goals, allocate funding, and approve major
  milestones." Matches the source's verb-per-duty structure; no scope
  change.
- **[nit · index.md repetition]** Skipped — within the house
  what/not-what/why layering; removing the table row would break the
  contrast-table rhythm.
- **[nit · index.md security-team compression]** Skipped — deliberate
  compression, lossless via checklist.md §2.
