---
status: accepted
revised: 2026-11-07
---

# Spec: Part IV — FULFILLMENT: From Warehouse to Doorstep and Back

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part IV for a reader new to commerce architecture: state the part's argument (the physical world has its own systems of record; every promise about it must be computed from their facts; the customer must be shown one status built from their events), say where the part sits on Eva's jacket, give Kestrel & Pine's fulfillment facts in one paragraph, and give one paragraph per chapter that names the question it decides and its Kestrel & Pine case.

## Audience

Newcomers to commerce architecture; the engineer, product manager or operations lead in their first weeks at a merchant with a warehouse, carriers, stores or a returns flow benefits most. They should leave knowing the five questions Part IV answers, in order, and why the part ends with the customer's view.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits on Eva's jacket, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[warehouse-and-fulfillment]]."
- [ ] Every number and date matches the chapters and the scenario ledger (336,000 parcels, 9,400 wholesale shipments, 8,500 m², 72,000 returns, 24%, six stores, 37 items, 212 returns and €19,400, #1052877 and 11 tickets, roughly 8,000 orders, 13–22 April 2027).
- [ ] No "Across Scale Stages" section, no take-away tiers; 500–900 words.
- [ ] A one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's content; the intro summarizes, it does not re-argue.
- The Waypoint decisions in detail ([[meet-kestrel-and-pine]] and the chapters own them).
- The availability calculation ([[inventory-and-availability]]) and the order state machines ([[order-management]]), which Parts II and III own.

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 shows the systems the five chapters cover around the order record (warehouse, carriers, stores, returns portal, service views) rather than the order's step-by-step path, because the chapters each draw their own flows and the intro's job is the shape of the part.
- **2026-11-07** — Figure 2 states the part's common rule (each promise computed from the fact of the system that keeps it) and maps the four incidents onto it, instead of a reading-order diagram.
- **2026-11-07** — Four failure patterns: The Phantom Stock (chapters 17 and 18), Schrödinger's Order (chapters 15, 17, 18 and 19), The Boomerang (chapter 18), The First Snowfall (chapters 15 and 16); The Pulled Rug, The Message in a Bottle and The Familiar Stranger were left to the chapters that address them directly.

## Sources

- **Internal**
  - [[warehouse-and-fulfillment]], [[shipping-and-delivery]], [[stores-and-omnichannel]], [[returns-and-exchanges]], [[customer-service-and-notifications]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the fictional facts.
  - `PLAN.md` (Part IV contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: acronyms expanded (WMS, POS, disposition), wave timing and Store Stock Mirage wording aligned with the ledger, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
