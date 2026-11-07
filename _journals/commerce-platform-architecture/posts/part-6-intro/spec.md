---
status: accepted
revised: 2026-11-07
---

# Spec: Part VI — INTEGRATION: Making Separate Systems Behave Like One

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part VI for a reader new to commerce architecture: state the part's argument (integration is decided per flow and every flow needs an owner; separate systems are built to disagree and must be designed to recover and to prove it; moving the data is half the work and meaning the same customer, product and order by it is the other half), say that the part sits underneath every step of the order's journey, give Kestrel & Pine's integration facts in one paragraph, and give one paragraph per chapter that names the question it decides and its Kestrel & Pine case.

## Audience

Newcomers to commerce architecture; the engineer, product manager or integration lead in their first weeks at a merchant that runs a dozen systems benefits most. They should leave knowing the five questions Part VI answers (talk, recover, promise, mean, count), in order, and why the part ends in the data warehouse.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits relative to Eva's jacket, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[integration-styles]]."
- [ ] Every number and date matches the chapters and the scenario ledger (13 systems, 34 integrations, 13 unowned, 3 reconciled, €96,000, €19,400 and 212 returns, €8,200, 2.3% and about 390 variants, 8 February 2027, 410,000/38,000/165,000/61,000, 21,000 and 96,000 linked, 21,050/22,710/24,140 and 23,150, 23 dropped orders).
- [ ] No "Across Scale Stages" section, no take-away tiers; 500–900 words.
- [ ] A one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's mechanisms (idempotency keys, the outbox, versioning strategies, matching rules, the metrics layer); the intro summarizes, it does not re-argue.
- The Waypoint decisions in detail ([[meet-kestrel-and-pine]] and the chapters own them).
- Which system owns each fact ([[boundaries-and-systems-of-record]] and [[part-5]] own it) and how the platforms themselves are built ([[part-7]]).

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 shows the joins Eva's order crosses (eight systems, the stock sync chain, the refund path, the warehouse extract) rather than the four integration styles, because the chapters draw the styles and the intro's job is the shape of the landscape the part works on.
- **2026-11-07** — Figure 2 maps the five questions (talk, recover, promise, mean, count) to one answer each, taken from the closing line of [[commerce-data-and-analytics]], instead of a reading-order diagram; the five chapters share the questions more than a sequence.
- **2026-11-07** — Four failure patterns: The Spaghetti Junction (chapters 24 and 27), The Message in a Bottle (24, 25, 26 and 28), The Pulled Rug (26) and The Familiar Stranger (27 and 28); Schrödinger's Order, The Boomerang, The Phantom Stock and The Lynchpin were left to the chapters that address them directly.

## Sources

- **Internal**
  - [[integration-styles]], [[events-consistency-and-reconciliation]], [[api-contracts-and-versioning]], [[identity-and-master-data]], [[commerce-data-and-analytics]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the fictional facts.
  - `PLAN.md` (Part VI contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS tightened; iPaaS and PSP expanded. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass (follow-up): 13 unowned integrations dated to January 2027, per consistency item 16. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass (follow-up): trimmed from 1,555 to about 1,500 words to meet the new part-intro target, by cutting sentences that repeat the failure patterns and the lead. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
