# Review: OSINT and Purple Teaming

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready, and the strongest dialog of the set — Ben's "why is a
defensive journal teaching people to attack?" opener and the
record-the-prediction beat give the conversation a real spine. The checklist
faithfully reproduces the source chapter checklist (all 17 sections, from
Authorization and Scope through Continuous Improvement, including the Maltego,
Shodan, and Responder-lab walkthroughs — nothing invented, nothing dropped),
all seven spec success criteria are met, every `[[link]]` resolves, the tab
tour names exactly Checklist / TL;DR / Conversation, and the summary is 426
words. One small alignment gap worth closing: the article never mentions the
chapter's Maltego and Shodan walkthroughs, though the spec lists them as kept
worked examples and sibling records name their worked tools in the article.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Investigation is disciplined" block]** The spec's
  investigation-discipline criterion includes "the Maltego and Shodan reviews
  kept as scoped, authorized worked examples," and they are kept — but only in
  the checklist; the article never names them. Sibling records surface their
  chapter's worked tools in the article (vulnerability-management names Nmap,
  Flan Scan, osquery in its Statement), so the omission reads as a gap rather
  than a choice, and a reader of the article alone would not know the
  checklist carries two full tool walkthroughs. *Add one clause pointing at
  the chapter's Maltego and Shodan walkthroughs as scoped, authorized worked
  examples in the Checklist tab.*

### Nits

- **[index.md · Statement, "Purple teaming is planned" block]** The planning
  bullet omits the source's "backups and recovery procedures available where
  needed" item (checklist §12 has it). Acceptable Statement-level compression;
  noted for awareness. *No change.*
- **[dialog.md · Ben's concession]** "Alright" — the journal's other dialogs
  in this batch use "All right" ("All right, I'll concede it crisply" / "All
  right, here's my concession"). *Normalize to "All right."*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim. Journal house pattern; awareness only.

## Spec ↔ post alignment

All seven success criteria met:

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (mirror → drill → owner/deadline/retest test) |
| Authorization and scope survive | met | index.md Statement block 1; checklist.md §1 |
| Full exposure sweep survives | met | index.md Statement block 2 (five channel bullets covering §§2–8); checklist.md §§2–8 |
| Investigation discipline survives | met (with the Maltego/Shodan naming gap above) | index.md Statement block 3; checklist.md §§9–11 |
| Purple-team loop survives | met | index.md Statement blocks 4–5; checklist.md §§12–16 incl. Responder lab and its hardening follow-through |
| Continuous improvement survives | met | index.md Statement block 5 closer; checklist.md §17 |
| Credit is explicit | met | index.md Authoritative References |

Non-goals respected: vulnerability-management, logging-and-monitoring,
incident-response, and user-education appear only as scoped negative space
with correct pointers; the "not an offensive-security charter" non-goal is
carried unusually well — the defensive framing is restated in the highlight,
How to Read This, the practice table, and Ben's opening challenge. Drift:
none; spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the authorization frame (written
  approval, scope, RoE, emergency stop), the record-expected-detections-first
  discipline, the never-reuse-captured-credentials rule, and the
  owner/deadline/retest finish line appear identically in all four files.
- **Terminology:** "the defender's mirror," "turns the mirror into a drill,"
  "indistinguishable from an attack," "the trophy hunt," "the scripted demo,"
  and the closing regression question ("which of the gaps we found last time
  came back?") recur verbatim where needed.
- **Coverage parity:** even — the sweep's seven channels, the discipline
  rules, and the loop all surface in summary bullets and dialog sections.

## Layer-by-layer notes

### Spec

Well-formed; the exposure-sweep and purple-team-loop criteria enumerate their
sub-commitments, all traceable. The offensive-security non-goal is the
record's most important framing decision and is logged clearly.

### index.md

House record shape fully observed: DRAFT highlight matching `draft:gray`,
Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
Related Records → Scope and Revisiting → Authoritative References. All seven
distinct `[[…]]` targets valid. No image references; no icon/logo front
matter. Rationale earns its length — "converts an attacker's free head start
into my own prioritized to-do list" and "a detection that has never been
exercised is a guess" are the record's best lines.

### checklist.md

Faithful to the source section by section, all 17 sections in source order,
near-verbatim bullets, no inventions. The closing loop line lands the spec's
load-bearing test.

### summary.md

426 words; leads with the decision; honest costs (authorization ceremony
accepted deliberately, recurring standing work, remediation competing with
feature work); correct not-doing list.

### dialog.md

The strongest of the batch: Ben's objections escalate naturally (why teach
attacking → bureaucracy → surveillance risk → theater → deck-and-forget), and
Ana's surveillance answer ("the fix for social exposure is education, not
surveillance") handles the record's most delicate ground well.

## Fixes applied (2026-08-22)

- **[minor · index.md Statement]** Added the worked-examples clause to the
  "Investigation is disciplined" block: the chapter's Maltego and Shodan
  walkthroughs are now named as scoped, authorized worked examples living in
  the Checklist tab.
- **[nit · dialog.md]** "Alright" → "All right," matching the journal's other
  dialogs.
- **[nit · index.md Statement, planning bullet]** Skipped — deliberate
  Statement-level compression; checklist §12 carries the backups item.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
