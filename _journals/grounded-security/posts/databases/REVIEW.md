# Review: Databases

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record once one factual slip is corrected. The
record closes the Hardening the Estate sequence well: the five-question
governance test is adopted verbatim and lands identically in all four
modalities, the injection-inherits-the-app's-privileges multiplier and the
keys-taped-to-the-padlock image give the chapter's largest checklist a real
argument, and the checklist itself is a faithful reproduction of the source
(all 20 sections plus the Priority Reminder and its verdict sentence, in
source order, item-for-item with nested sub-items intact — verified against
every page of the PDF). The slip: the chapter's "Questions You Should Be
Able to Answer" section contains **seventeen** questions, but spec, article,
summary, and dialog all call them "twenty" — the section number (20)
mistaken for the count. All eight success criteria are otherwise met, every
`[[link]]` resolves, and the tab tour names Checklist / TL;DR / Conversation
with no Comic tab.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[spec.md · criterion 7; index.md · "How to Read This"; summary.md ·
  footer; dialog.md · closing exchange]** The question set is called "the
  chapter's twenty questions" in all four files, but the source section
  (numbered 20) contains seventeen questions — the checklist reproduces all
  seventeen correctly, so the modalities contradict the record's own
  Checklist tab. *Say "seventeen" (or drop the count).*

### Nits

- **[index.md · front matter `tags`]** "security" and "defensive security"
  are generic where sibling records use only specific tags (same slip as
  `endpoints` pre-review). *Drop the two generic tags.*
- **[index.md · Scope and Revisiting]** Faulty parallel: "It applies to
  every database … — and as the audit bar for the existing estate and for
  anything acquired" — "applies to X and as Y" doesn't parse (same
  construction as `endpoints` pre-review). *"…and serves as the audit
  bar…"*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim — the journal's established pattern, noted for awareness
  only. (summary.md is the journal's longest at 522 words including the
  navigation footer; the body sits inside the 300–500 band.)

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (full bar + five-questions test) |
| Architecture and classification survive | met | index.md · Statement block 1 + Rationale ("defending a sample"); checklist.md §§1–2 |
| Access control and PAM survive | met | index.md · Statement block 2; checklist.md §§3–4 |
| Encryption and secrets survive | met | index.md · Statement blocks 3–4 + Rationale ("key separation"); checklist.md §§5–6 |
| Attack modes survive | met | index.md · Statement block 5 + Rationale (injection, insiders); checklist.md §§7–10 |
| Operations survive | met | index.md · Statement blocks 6–7 + Rationale ("untested backups are a hope"); checklist.md §§11–15 |
| Cloud, governance, IR, and third parties survive | met | index.md · Statement block 8 + Rationale ("inherit convenience, not security"; governance); checklist.md §§16–19 |
| The question sets survive | met (count fixed) | checklist.md §20 (all seventeen) + Priority Reminder with the chapter's verdict sentence |
| Credit is explicit | met | index.md · Authoritative References (handbook + CIS Benchmarks + DISA STIGs) |

Non-goals respected: yes — authentication, secure-software-development,
disaster-recovery, and cloud-infrastructure appear only as negative space
with correct `[[…]]` pointers; MySQL/PostgreSQL/SQL Server/MongoDB are
consistently framed as the worked example.

Drift: none beyond the count slip (now fixed in the spec as well). Spec
`status: accepted` is correct; front-matter `status: draft:gray` matches the
visible DRAFT and the Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — protect-data-where-it-lives, the
  injection multiplier, key separation, attacker-resistant backups with the
  last-successful-restore probe, cloud parity, and the five-question verdict
  match across all four files. The only factual wobble was the
  seventeen-vs-twenty count, fixed.
- **Terminology:** consistent — "where a security failure becomes the
  headline," "defending a sample of them," "a padlock with the key taped to
  it," "the backup strategy is a belief," "inherited systems are never
  assumed to meet the standard" recur where each modality needs them.
- **Voice & tone:** consistent; Ana/Ben cast matches the journal; Ben's
  "before some of our engineers could vote" and "whiff of paranoia" keep the
  dialog audible.
- **Coverage parity:** even — all eight Statement blocks reach the summary's
  six bullets and the dialog; availability/resilience is the thinnest thread
  outside index/checklist (one clause in the summary's operations bullet),
  acceptable compression.

## Layer-by-layer notes

### Spec

- Well-formed; the eight criteria bundle the chapter's twenty sections
  without losing the question sets or the priority reminder; the
  load-bearing test is quoted in the intent and adopted verbatim everywhere.

### index.md

- House record shape fully observed: DRAFT highlight, Statement → How to
  Read This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope → References. Rationale earns its formulations ("hoping the breach
  lands in the sample," "Cloud databases inherit convenience, not
  security"). The restore-date audit probe recurs at exactly the right
  moments. All 8 distinct `[[…]]` targets are valid.

### checklist.md

- Faithful to the source PDF: 20 sections + Priority Reminder, source
  order, item-level match throughout including all nested sub-lists (data
  classes, attack types, CIS/DISA, the eight governance minimums, the five
  IR determinations) and the source's closing verdict sentence, reproduced
  with a one-line handoff that invents no obligations.

### summary.md

- Leads with the decision, six "What changes" bullets covering the
  Statement, honest "What it costs" (rework of admin-connected apps named
  as paid-down debt), correct not-doing list with resolving links.

### dialog.md

- Strong arc (why-the-data-layer → privilege → keys/copies/backups → cloud
  parity and the five questions); Ben's objections are the right ones
  (inventory-isn't-security, OWASP fatigue, compliance-form encryption,
  provider-absorbs-it), and the closing exchange lands the verdict
  verbatim.

## Fixes applied (2026-08-22)

- **[minor · spec.md, index.md, summary.md, dialog.md]** "twenty questions"
  corrected to "seventeen" in all four places: spec criterion 7, the
  article's How to Read This, the summary's navigation footer, and Ben's
  closing-exchange line in the dialog. The checklist already reproduced all
  seventeen and needed no change.
- **[nit · index.md]** Generic tags "security" and "defensive security"
  removed; specific tags retained, matching sibling records.
- **[nit · index.md]** Scope sentence repaired: "…and serves as the audit
  bar for the existing estate and for anything acquired."
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the
  journal's established house pattern.
