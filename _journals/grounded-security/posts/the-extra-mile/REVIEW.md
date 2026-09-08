# Review: The Extra Mile

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as the journal's closer, and no content changes were required —
the cleanest post of the five reviewed. The checklist reproduces the source
chapter checklist exactly (Email Server Security with its two subsections,
DNS Server Security with all six, Security Through Obscurity with its
supplements and five do-nots, Ongoing Security Learning with all four
resource groups, and the 11-item Final Review — nothing invented, nothing
dropped), all seven spec success criteria are met, every `[[link]]` resolves,
the tab tour names exactly Checklist / TL;DR / Conversation, the summary is
444 words, and the dialog's framing ("explain the anticlimax") turns the
chapter's grab-bag nature into the record's argument instead of apologizing
for it. Only awareness-level nits below.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Statement, closing block]** "**The final review is run.**" is
  a bold-lead paragraph, while the five preceding Statement blocks use a
  standalone bold sentence followed by bullets. Reads as a deliberate compact
  coda summarizing the 11-item Final Review; noted only because it breaks the
  block pattern. *No change — intentional structure.*
- **[index.md · Statement, "Recursion is a privilege" bullet]** The source's
  "allow external-facing DNS queries only where required" item is folded into
  the recursion bullet rather than surfaced separately. Acceptable
  Statement-level compression; checklist.md carries it verbatim. *No change.*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~140 words). Journal house pattern; awareness only.

## Spec ↔ post alignment

All seven success criteria met:

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (provable mail → continuity → DNS as control → obscurity as layer → learning → obscurity test) |
| Email server security survives | met | index.md Statement block 1; checklist.md §1 Configuration |
| Email administration survives | met | index.md Statement block 2 incl. the make-or-buy review; checklist.md §1 Email Administration |
| DNS server security survives | met | index.md Statement block 3 (five bullets covering recursion, split DNS, zone transfers, passive monitoring/sinkhole, DNSSEC); checklist.md §2 |
| Obscurity-as-a-layer survives | met | index.md Statement block 4 (all five do-nots present); checklist.md §3 |
| Ongoing learning survives | met | index.md Statement block 5; checklist.md §4 (books, sources, podcasts, CISA/NVD, CTFs, pruning) |
| Final Review survives | met | checklist.md closing section (11 items, matching the source); index.md Statement coda |
| Credit is explicit | met | index.md Authoritative References (handbook, CISA, NIST NVD) |

Non-goals respected: network-security, phishing-response,
logging-and-monitoring, vulnerability-management, and user-education each
appear only as boundary references with correct `[[…]]` pointers (the
user-education boundary is carried implicitly by the team-vs-workforce
framing of the learning section). Drift: none; spec `status: accepted` is
correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the obscurity test is verbatim-identical
  in highlight, Statement, checklist closer, summary, and dialog; the
  DNSSEC trade-off (complexity, operational risk, amplification) and the
  sinkhole-as-self-reporting-list image match across all four files; the
  dialog's "eleven lines" claim for the Final Review is checklist-accurate.
- **Terminology:** "the worst ratio of importance to attention,"
  "deliverability is a security property wearing an operations costume,"
  "a single point of failure with a notice period," "close the leak, wire
  the sensor," "obscurity buys minutes; controls buy safety" recur where
  each modality needs them.
- **Coverage parity:** even — all five Statement blocks map to summary
  bullets and dialog sections; the make-or-buy honesty beat appears in all
  four files.

## Layer-by-layer notes

### Spec

Well-formed; the DNS criterion enumerates every sub-commitment and all are
traceable. The Final-Review-as-completion-check criterion is a good catch —
it forces the checklist to keep the source's closing section, and it did.

### index.md

House record shape fully observed: DRAFT highlight matching `draft:gray`,
Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
Related Records → Scope and Revisiting → Authoritative References. All six
distinct `[[…]]` targets valid. No image references; no icon/logo front
matter. The Rationale's meal/seasoning hierarchy and "DNSSEC is a trade-off,
not a virtue" carry the chapter's two most contrarian points faithfully.

### checklist.md

Faithful to the source section by section; the added §1–4 numbering is a
lossless navigation aid, and Final Review is left unnumbered outside the
sequence, matching the source's placement.

### summary.md

444 words; leads with the decision; the costs section is the best in the
batch ("continuity plumbing that nobody thanks you for until the renewal
that did not get missed"; "explaining why less looks like more"); correct
not-doing list.

### dialog.md

The anticlimax framing works: Ben's objections (nineties BIND manual; more
crypto is automatically good; a homework assignment in an operating record)
are the ones this chapter actually gets, and Ana's DNSSEC answer refuses the
checkbox exactly as the record does. Ben's closer ("the systems that never
page you are the ones that fail loudest in the end") earns the journal's
final word.

## Fixes applied (2026-08-22)

- None required — no blockers, majors, or minors found. All three nits
  skipped deliberately: the Statement coda is intentional structure, the
  recursion-bullet folding is checklist-covered compression, and the
  excerpt-mirrors-highlight pattern is the journal's house convention. No
  modality files were changed, so no spec Changelog entry was added.
