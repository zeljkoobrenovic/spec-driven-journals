---
status: accepted
revised: 2026-11-07
---

# Spec: Introduction: Why Commerce Architecture Matters

> Working doc for the introduction in this folder. The spec drives the page; the page is the artifact.

## Intent

Open ORDERED for a reader new to commerce architecture. State the book's argument (a commerce platform is a promise-keeping machine; most failures are a promise one system made and another could not keep; architecture decides who may make which promise, how the others learn of it and what happens when they disagree), show how the order's journey (Eva's jacket) and the four scale stages organize the book, route a reader with a decision already on the desk to the right chapter, and teach how to read the book's evidence labels and take-away tiers. The page describes what the written parts actually say, not what the plan hoped.

## Audience

Newcomers by role: engineers, product managers, analysts, consultants and leaders who have just joined a retailer, brand, wholesaler, commerce software vendor or agency. The reader with a pending decision (replatform, OMS, PIM, overselling, marketplaces) benefits most from the routing table; the first-time reader from the argument and the part table.

## Success criteria

- [ ] Openers in order: IN THIS SECTION (one sentence), KEY POINTS (exactly three, the book's argument), `<br>`, a lead built on Eva's order and its five promises. No WHY IT MATTERS callout (dropped book-wide).
- [ ] Says what the reader needs to know already and what not, and defines every term it uses (SKU, ATP, OMS, WMS, PSP, EDI, ERP, PIM, system of record, idempotency, eventual consistency).
- [ ] One mermaid diagram of the order's journey across the parts, with a numbered caption.
- [ ] The four scale stages match the ledger; explains why every chapter in Parts II–VIII has "Across Scale Stages".
- [ ] One part table (section, question, chapters) with `[[part-N]]` links, and a routing table of about twelve rows using only valid permalinks.
- [ ] The six kinds of statement and the three take-away tiers are explained; dated claims carry their dates and sources.
- [ ] Draws-on section: public dated sources, research briefs, Productscape models as maps only via [[domain-coverage]]; vendor-neutral; never mentions the private source journal or its brief.
- [ ] Hand-offs to RECONCILED, LISTED and Architecting Agentic Systems via the allowed sibling permalinks; 3,000–4,500 words of prose.

## Non-goals

- The sixteen failure patterns in depth ([[where-commerce-platforms-go-wrong]]).
- Kestrel & Pine's full profile, systems and incidents ([[meet-kestrel-and-pine]]).
- Any chapter's argument beyond one line; the templates ([[toolkit]]) and definitions ([[glossary]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Replace the mermaid journey diagram with a generated book-map illustration in the visual pass?
- Revisit the routing table once reviewers report which decisions readers actually bring.

## Decision log

- **2026-11-07** — Lead built on Eva's order as five promises, so the argument is concrete before it is stated.
- **2026-11-07** — Part table phrased as one question per part, taken from the written part intros rather than the plan.
- **2026-11-07** — "Why claims carry dates" uses public, dated interface changes (Zalando 2025, bol 2026, Shopify versioning) and the Omnibus 30-day rule, all already cited in chapters.
- **2026-11-07** — WHY IT MATTERS callout omitted, following the book-wide change.

## Sources

- Internal: [[where-commerce-platforms-go-wrong]], [[meet-kestrel-and-pine]], [[part-1]] … [[part-11]], [[domain-coverage]], [[toolkit]], `_research/style-guide.md`, `_research/scenario-ledger.md`, `PLAN.md`.
- External: Zalando Engineering (2025), bol partner platform (2026), Shopify API versioning documentation, Directive (EU) 2019/2161.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: "a ledger story" now reads as a Kestrel & Pine story. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 1 mermaid diagram as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
