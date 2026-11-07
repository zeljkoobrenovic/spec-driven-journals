---
status: accepted
revised: 2026-11-07
---

# Spec: Part XI — PRACTICE: How Others Built It

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part XI for a reader new to commerce architecture: say that the four cases (Shopify, Amazon, Zalando, the composable movement) test the book's argument against whole companies, explain how they are read (public evidence only, every claim dated, inferences labeled, each case ending where the evidence stops), remind the reader that each company's answers depend on its scale and business model (The Giant's Boots), and give one paragraph per case naming the question it decides and what Kestrel & Pine takes from it.

## Audience

Newcomers to commerce architecture; the engineer, architect or leader who hears "Amazon did microservices" or "go composable" in a design review benefits most. They should leave knowing how to read a company case and which kind of lesson transfers to a merchant of their size.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] The lead states the reading rules: public evidence only, year in the sentence, old sources flagged, inferences labeled, each case ending with "Where the Evidence Stops".
- [ ] The lead names The Giant's Boots and says the companies' answers depend on scale and business model; names Kestrel & Pine as fictional once; says the cases sit beside the order's journey.
- [ ] One or two mermaid diagrams of 5–9 nodes, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per case in config order, `[[permalink]]` first, the question in bold, the Kestrel & Pine take-away named, ending "Begin with [[case-shopify]]."
- [ ] Every figure matches the chapters (2.8 million lines; 2001; 3% in 1999 to over 60%; 85-plus teams; 30 minutes at Cyber Week; 37%; 62 million customers; February 2027 pitch) and Waypoint decisions match the ledger (W1, W4, W5, W8).
- [ ] No "Across Scale Stages" section, no take-away tiers; a one-line `## Sources and Evidence`.

## Non-goals

- Re-telling any case; the chapters own the evidence and its sources.
- The architecture-style and build-or-buy arguments ([[commerce-architecture-styles]], [[build-buy-or-assemble]]).
- Failure-pattern definitions ([[where-commerce-platforms-go-wrong]]).

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 draws the reading method (dated claim → documented or inference → transfers, giant-only, evidence stops) because the method is what the four cases share.
- **2026-11-07** — Figure 2 maps each case to the Waypoint decision it confirms (W1, W4, W5, W8), because every case's Kestrel & Pine section ends that way and none changes the architecture.
- **2026-11-07** — Three failure patterns: The Giant's Boots (all four cases), The Pulled Rug (Shopify, Zalando), The Spaghetti Junction (Amazon, composable); The Secret Agent and The Message in a Bottle stay in the chapters.

## Sources

- **Internal**
  - [[case-shopify]], [[case-amazon]], [[case-zalando]], [[case-composable-movement]] — the chapters summarized, in their words and numbers.
  - `_research/scenario-ledger.md` (Waypoint W1–W8) and `PLAN.md` (Part XI contracts); `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: composable pitch attributed to the consultancy (item 13a). *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
