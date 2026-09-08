# Review: Microsoft Windows Infrastructure

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record, and one of the strongest arguments in the
section: the "one system, not a fleet" framing, the privilege-as-attribution
reading, and the four-artifact practice test give the chapter's 130-odd items
a genuine executive shape. The checklist is a faithful reproduction of the
source (all 17 numbered sections plus the Final Review, in source order,
item-for-item — verified against every page of the PDF, including the SIDWalk
mention and the 16-item Final Review), all ten success criteria are met,
every `[[link]]` resolves, and the tab tour names Checklist / TL;DR /
Conversation with no Comic tab. The one parity gap: the SMB-share discipline
(a standalone spec criterion and Statement block) never reaches the summary,
whose "What changes" list covers the other six Statement beats.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[summary.md · "What changes"]** Coverage parity: the share-discipline
  beat (SMB shares inventoried, scanned, pruned; share and NTFS permissions
  restricted; periodic re-audit — spec criterion 4, Statement block 3,
  checklist §3) is absent from the summary except for a passing "unusual SMB
  access" in the detection bullet. Every other Statement block has its own
  bullet. *Add a short shares bullet.*

### Nits

- **[index.md · Statement, "New systems land managed"]** Agreement slip:
  "their placement and policy application is verified" — compound subject
  wants "are verified".
- **[dialog.md · closing exchange]** Ben's takeaway compresses the article's
  four-artifact practice test (unsupported-systems list, Domain Admins
  membership, trust map, last AD restore date) to "two questions". Not a
  contradiction — deliberate compression that keeps the two most quotable —
  but a reader moving between tabs may notice the count differs.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (one-system shape + attribution-and-recovery test) |
| Legacy hygiene survives | met | index.md · Statement block 1 + Rationale ("Legacy is a risk decision"); checklist.md §1 |
| Patch and software management survives | met | index.md · Statement block 2; checklist.md §2 |
| Share discipline survives | met (after fix) | index.md · Statement block 3; checklist.md §3; now also summary.md |
| Forest-boundary and trust discipline survives | met | index.md · Statement block 4 + Rationale ("The forest is the boundary"); checklist.md §§4–5 |
| Domain-controller discipline survives | met | index.md · Statement block 5 + Rationale ("crown-jewel treatment"); checklist.md §6 |
| Directory structure survives | met | index.md · Statement block 6; checklist.md §§7–9 |
| Privilege and attribution survive | met | index.md · Statement block 7 + Rationale ("attribution guarantee"); checklist.md §§10–13 |
| Group Policy enforcement survives | met | index.md · Statement block 8 + Rationale ("A baseline that is not enforced is a preference"); checklist.md §§14–15 |
| Monitoring and recovery survive | met | index.md · Statement block 9 + Rationale ("Recovery must assume the credentials are gone"); checklist.md §§16–17 + Final Review |
| Credit is explicit | met | index.md · Authoritative References (handbook + NIST/Microsoft baselines) |

Non-goals respected: yes — authentication, endpoints, unix-servers,
logging-and-monitoring, and disaster-recovery appear only as negative space
with correct `[[…]]` pointers; WSUS/Configuration Manager/LAPS are
consistently framed as the worked example, not a mandate, in all modalities.

Drift: none. Spec `status: accepted` is correct; front-matter `status:
draft:gray` matches the visible DRAFT and the Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — forest-not-domain boundary, crown-jewel
  DCs up to forest rebuild, LAPS-unique local passwords, tested restores
  protected from admin compromise, NIST/Microsoft baselines as starting
  point all match across the four files.
- **Terminology:** consistent — "one system, not a fleet," "every
  administrative act has exactly one author," "a backup the attacker can
  reach is not a backup," and the attribution-and-recovery test recur where
  each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben cast
  matches the journal.
- **Coverage parity:** even after the summary fix; the dialog's light touch
  on shares and FSMO detail is acceptable compression (FSMO seizure appears
  in the DC-recovery exchange).

## Layer-by-layer notes

### Spec

- Well-formed; the ten success criteria map the chapter's 17 sections into
  testable bundles without losing the Final Review (explicitly required and
  delivered). Non-goals include the tool-mandate disclaimer the article
  honors.

### index.md

- House record shape fully observed: DRAFT highlight, Statement → How to
  Read This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope → References. Rationale is the strongest section — "the estate's
  real attack surface is the graph," "a GPO wins arguments automatically,"
  "recovery must assume the credentials are gone." The concrete
  four-artifact test in Practice is exactly the executive hook the spec's
  audience section asks for. All 8 distinct `[[…]]` targets are valid.

### checklist.md

- Faithful to the source PDF: 17 sections + Final Review, source order,
  item-level match throughout, including §9's deliberate AGDLP/AGUDLP
  double-chain and the SIDWalk pointer. Closing line restates the record's
  test without inventing obligations.

### summary.md

- Leads with the decision, honest "What it costs" (administration friction,
  standing cadence work, uncomfortable legacy conversations), correct
  not-doing list with resolving links. 492 words including footer — in band.

### dialog.md

- Ben's objections are the right ones (least-novel-advice, AD trivia,
  rich-company absolutism, plans-for-failure, Domain-Admins-always-grows)
  and Ana's answers carry the record's actual arguments; the
  phishing-target rationale for separate admin accounts is a good addition
  that stays within the record's claims.

## Fixes applied (2026-08-22)

- **[minor · summary.md]** Added a shares bullet to "What changes": "File
  shares stop leaking. SMB shares are inventoried, scanned for exposure,
  reviewed for sensitive data, and pruned; share and NTFS permissions are
  both restricted and periodically re-audited." Body stays within the
  300–500-word band.
- **[nit · index.md]** "their placement and policy application is verified"
  → "are verified".
- **[nit · dialog.md]** Skipped — the two-of-four compression in Ben's
  closing line is deliberate dialog economy, not an inconsistency of fact;
  rewording would flatten the exchange.
