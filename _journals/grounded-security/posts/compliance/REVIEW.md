# Review: Industry Compliance Standards and Frameworks

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready. The hardest problem this chapter poses — turning an
alphabet-soup literacy checklist into an argument — is solved well: the
floor/building frame, the three-layer map, and "category confusion at the top
becomes control failure at the bottom" give the record a spine the source
does not have, without inventing anything the source does not say. The
checklist is a complete, faithful reproduction of the PDF (Core Concepts,
all five regulations with their sub-lists, all seven frameworks, all three
regulated industries with their program sub-blocks, and the first-person
Final Review — nothing invented, nothing dropped). All seven success
criteria are met, every `[[…]]` cross-link resolves, the tab tour names
exactly Checklist / TL;DR / Conversation, the highlight's DRAFT matches
`draft:gray`, and the summary lands at 472 words. Two small wobbles worth
fixing: a "four vocabularies" line in the dialog whose referent is the
seven-framework shelf, and one comma-drowned GLBA bullet in the Statement.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[dialog.md · "Frameworks Are Instruments", Ana's first answer]** "The
  anti-pattern is adopting all of them and operationalizing none — four
  vocabularies, zero controls improved." The "four vocabularies" tag comes
  from the article's framework-collector anti-pattern (which names four:
  ISO, NIST, COBIT, CIS), but here "all of them" refers to the seven
  frameworks Ana has just listed, so the arithmetic reads as a slip.
  *Either name the four (matching the article's anti-pattern verbatim) or
  drop the number.*
- **[index.md · Statement, GLBA bullet]** The bullet is a comma-separated
  super-list whose items themselves contain commas: "an ongoing obligation
  to protect customer privacy, administrative, technical, and physical
  safeguards, a concrete control set (…), third-party providers in scope,
  and enforcement by the FTC, FDIC, Federal Reserve, and OCC." On first
  read "privacy, administrative, technical" parses as one list. Also drops
  the source's "and confidentiality." *Promote the top-level separators to
  semicolons and restore "and confidentiality."*

### Nits

- **[checklist.md · FISMA heading]** "Federal Information Security
  Management Act" — the 2014 statute renamed it the Modernization Act, but
  the source PDF says Management, so the checklist is source-faithful as
  written. Noted only; no change (fidelity to the source wins).
- **[index.md · front matter `excerpt`]** The excerpt reprises the
  highlight nearly verbatim. Journal house pattern; noted only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (floor-not-program, three layers, data-to-regulation map, compliant ≠ secure) |
| Core concepts survive | met | index.md · Statement block 1; checklist.md §1 |
| The regulation map survives | met | index.md · Statement block 2 (all five regulations with enforcement texture); checklist.md §2 complete |
| The framework shelf survives | met | index.md · Statement block 3 + Rationale ¶4; checklist.md §3 (all seven) |
| Regulated-industry context survives | met | index.md · Statement block 4 + Rationale ¶5; checklist.md §4 (finance/government/healthcare incl. CMMC, Impact Levels, FedRAMP, FISMA, HITRUST) |
| Final review survives as completion check | met | index.md · "The posture is literacy, verified"; checklist.md §5 (all seven items, first person preserved) |
| Credit is explicit | met | index.md · Authoritative References (handbook + regulations + frameworks) |

Non-goals respected: yes — [[security-program]], [[policies]],
[[standards-and-procedures]], [[asset-management]], and
[[cloud-infrastructure]] appear only as negative space with correct
pointers; the record explicitly defers statutory interpretation to counsel.

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — floor/building, the five mappings with
  their enforcement realities (card brands switching off processing, HHS,
  banking regulators, auditor-verified SOX controls), frameworks-as-chosen-
  instruments, and regulated-equals-secure-inverted match across article,
  summary, and dialog.
- **Terminology:** consistent — "the floor is mandatory; it is just not the
  building," "category confusion at the top becomes control failure at the
  bottom," "annual evidence factory," and the per-dataset test question
  recur verbatim where needed.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben
  match the journal cast.
- **Coverage parity:** even — every Statement block has a summary bullet and
  a dialog section; the checklist carries the full detail the prose
  compresses.

## Layer-by-layer notes

### Spec

- Well-formed; the success criteria enumerate the chapter's content at
  unusually fine grain (which made verification easy), and the non-goals
  pre-empt the obvious boundary disputes with the four sibling records.

### index.md

- House record shape fully observed: DRAFT highlight matching front matter,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns
  → Related Records → Scope → References. No images, no icon/logo front
  matter.
- Rationale earns its length: "the floor is not the building," "budgets flow
  to attestation instead of defense," "compliance officers coordinate; the
  executive must still comprehend" all carry weight. The seven distinct
  `[[…]]` targets are valid journal slugs.

### checklist.md

- Complete and faithful section by section against the PDF, including every
  nested sub-list (FERPA consent contents and record examples, the twelve
  GLBA controls, HIPAA safeguard categories, PAN/name/expiration/service
  code, COBIT's four domains, ISO 27001–27006, ATT&CK's four coverage
  areas, CSF's three components, the financial risk list, government
  challenges and four programs, healthcare penalties and HITRUST's four
  inputs). Final Review keeps the source's first-person phrasing, which the
  article correctly leans on ("the literacy cannot be delegated").

### summary.md

- On target: leads with the decision, 472 words, honest "What it costs"
  (real study, funding controls no assessor asked for, standing scope
  discipline), correct not-doing list with resolving links.

### dialog.md

- Ben's objections are the real ones (compliance as invoice, taxonomy as
  officer work, framework shelf as consultant fodder, regulated industries
  as a paragraph) and Ana answers from the record. The closer lands on the
  chapter's own closing words. One arithmetic wobble noted under Minor.

## Fixes applied (2026-08-22)

- **[minor · dialog.md]** Framework-collector line aligned with the
  article's anti-pattern: now names ISO, NIST, COBIT, and CIS explicitly
  ("ISO, NIST, COBIT, and CIS all 'adopted,' none operationalized — four
  vocabularies, zero controls improved"), so the count matches its
  referent.
- **[minor · index.md · Statement, GLBA bullet]** Top-level separators
  promoted to semicolons and the source's "and confidentiality" restored:
  "an ongoing obligation to protect customer privacy and confidentiality;
  administrative, technical, and physical safeguards; a concrete control
  set (…); third-party providers in scope; and enforcement by the FTC,
  FDIC, Federal Reserve, and OCC."
- **[nit · checklist.md FISMA heading]** Skipped — source-faithful as
  written; fidelity to the PDF wins over the 2014 rename.
- **[nit · index.md excerpt]** Skipped — journal house pattern.
