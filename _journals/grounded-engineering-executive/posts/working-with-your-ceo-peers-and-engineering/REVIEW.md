# Review: Working with Your CEO, Peers, and Engineering

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All five spec criteria are met, the supported/tolerated/resented diagnostic works well as the organizing frame the Decision log chose, and "Tolerated is not good enough" is the strongest Rationale opening in the set of records reviewed this round. The most important thing to address is a structural completeness gap: the Statement presents seven commitments as the record's skeleton, but two of the source's ten practices — surviving peer panic and the three-year question — appear only in the Rationale, so a reader scanning the Statement gets a list that looks complete and isn't.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement]** The seven commitment bullets cover practices 1–8 of the source but omit peer panic (practice 9) and the long-term three-year perspective (practice 10); both surface only later (Rationale ¶¶4–5, and the three-year question in the highlight). The Statement reads as the complete list when it is not. *Add one bullet each, or a closing line noting the Rationale carries two more.*
- **[index.md · Rationale ¶4]** "I focus on improving execution over replacing them where feasible" — inherited from the source PDF's compressed phrasing, but ambiguous in prose: improving *whose* execution, and who is doing the replacing? *Unpack to something like "help the peer's function execute rather than push to replace them."* (The same compression is fine inside checklist.md §9, where the telegraphic register is expected.)

### Nits
- **[checklist.md · headings]** Sections use `###` (h3) while the sibling checklists in this journal (systems-and-tools, team-first-*) use `##` (h2) — the rendered Checklist tab gets a visibly smaller heading hierarchy than its neighbors.
- **[spec.md · title]** "Spec: Operating Principle: Working with Your CEO…" — double-colon stacking; sibling specs use the plain "Spec: <title>" form.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (company-first balancing stance in one paragraph) |
| Rationale is argued, not asserted | met | index.md · Rationale ¶1 (tolerated), ¶2 (CEO narrative pre-filtered), ¶3 (disagreement ≠ dysfunction) |
| Checklist survives intact | met | checklist.md — all ten practices, source order, sub-groups preserved (5-day escalation, three questions) |
| Anti-patterns are concrete | met | index.md · Anti-Patterns — six, including all four the spec suggests |
| Credit is explicit | met | index.md · Authoritative References (Primer chapter + lethain.com companion essay) |

Non-goals respected: yes — the leadership team below is explicitly deferred to [[gelling-your-engineering-leadership-team]] (both in How to Read This and Related Records), peer onboarding to [[onboarding-peer-executives]], and communication mechanics to [[internal-communication]].
Drift: none. Spec `status: accepted` is accurate; this spec's changelog is current (comics images correctly recorded as generated).

## Cross-modality alignment

- **Facts & framing:** consistent — supported/tolerated/resented, the 5-day escalation clock, stress-before-malice, and the three-year question match across article, checklist, and comic.
- **Terminology:** consistent — "company-first", "toleration", "structured escalation", "peer panic" used identically everywhere.
- **Voice & tone:** consistent first-person declarative; VERA/LEO comic in the house register (Leo carries the mistakes, Vera the corrections — same casting as siblings).
- **Coverage parity:** good — the comic carries seven of the ten practices in eight panels; bridge-narratives, the alignment habit, and limit-concurrent-changes are article/checklist-only, a reasonable compression for the form.

## Layer-by-layer notes

### Spec
- Clean template compliance; the Decision log usefully records *why* the post is organized by the support diagnostic instead of per-relationship sections — and the article honors it.
- Success criteria are checkable, including an enumerated list of all ten checklist sections to verify against.
- Changelog is accurate and current — the only spec in this review batch without a stale image note.

### index.md
- House record shape followed; headings Title Case; all six `[[...]]` cross-links resolve ([[mergers-and-acquisitions]] in Scope included); all three figures exist and are captioned.
- Rationale ¶1's supported/tolerated/resented argument ("resentment is at least visible") is genuinely argued, not asserted — exactly what the spec demanded.
- The [[inspected-trust]] tie-in ("the same discipline applied sideways and upward") is a strong piece of journal-internal wiring.
- Statement completeness gap and one ambiguous inherited sentence (see minors).

### checklist.md
- Faithful ten-practice reproduction in source order with the numbered structure, the five-day escalation steps, and the three closing questions intact.
- The intro line explaining the ordering ("starts with the honest support diagnosis everything else flows from") is a nice touch matching the spec's Decision log.
- Heading level inconsistency with sibling checklists (see nit).

### comics.md
- Eight panels, all image files present under `assets/images/working-with-your-ceo-peers-and-engineering/`; alt text matches captions.
- Clear arc: three-rope hook → toleration problem → old-playbook wrong-way → company-first principle → gather-perspectives discipline → peer-panic move → escalation mechanism → three-year closer.
- Panel 2 ("nod politely and walk away doing nothing") is an unusually good visual for toleration — the record's central and hardest-to-draw idea.
