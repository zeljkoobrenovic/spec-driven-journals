---
status: accepted
revised: 2026-10-22
---

# Spec: Part X — PRACTICE: How Others Built It

## Intent

Orient the reader to Part X: four case studies (Booking.com, Airbnb, Expedia Group and Vrbo, Agoda and Trip.com) that test the book's patterns against the public record. State the evidence rules the cases follow (documented fact with a date, the author's interpretation, labeled inference, and where the evidence stops), keep fictional Corvane separate from the real companies, compare the four cases side by side, and say which question each case answers and when to read it.

Productscape domains: none of its own; the part intro frames the cases, which test bricks owned by chapters in Parts II–IX.

## Audience

Chief architects, principal engineers and engineering leaders of accommodation and hosted-stays marketplaces who want to know which public case bears on the decision in front of them, and how far its evidence can be trusted.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and FAILURE PATTERNS THIS PART ADDRESSES with exact pattern names, linked to where-stay-platforms-go-wrong.html.
- [ ] "How to read the cases" defines documented fact (with date), the author's interpretation and reference-architecture inference, names the Where the Public Evidence Stops tables, and states that Corvane is fictional, appears only in each final comparison and is not a disguised real company.
- [ ] A comparison table of the four cases: marketplace type, payment model, documented architecture themes, evidence strength.
- [ ] Two illustrations with numbered Figure captions: the lit and dark public record, and the cases testing the book's claims before Corvane enters.
- [ ] Every company fact is taken from chapters 48–51, with its year; no new external claims.
- [ ] `## Chapters in this part` has one paragraph per case in config order, with what it shows and when to read it.
- [ ] Links back to [[evolving-the-platform]], forward to the Reference pages, and hands off to [[case-booking-com]]; 600–1,000 words of body.

## Non-goals

Re-teaching any case: the Booking.com connectivity contract and experimentation ([[case-booking-com]]), Airbnb's migration, payments and search ([[case-airbnb]]), Expedia's consolidation and Rapid rules ([[case-expedia-vrbo]]), Agoda's price cache and Trip.com's filing ([[case-agoda-trip-com]]). No new Corvane facts and no Corvane worked example beyond one reference to chapter 50's migration guardrail.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-21: Modeled on LISTED's Part IX intro (evidence-kinds table, cases side by side, fiction kept separate) and this book's Part VIII intro (one paragraph per chapter, mermaid diagram with caption).
- 2026-10-21: Agoda and Trip.com share one row of the comparison table, because they share one case, with each cell split by company; their evidence strength differs most of any pair.
- 2026-10-21: Key points chosen from what all four cases share: the record is silent on availability, calendar and reservation state machines; hotels and homes stay distinct beneath convergence; contracts and money models outlive technology eras.
- 2026-10-21: Failure patterns chosen by how many cases name them: The Hotel-Shaped Home (48, 49, 50), Phantom Availability (50, 51), Pay-to-Rank Creep (48, 51). Connectivity Roulette and Ledgerless Money are each carried by one case only.

## Sources

Internal: [[case-booking-com]], [[case-airbnb]], [[case-expedia-vrbo]], [[case-agoda-trip-com]] (callouts, timelines, Where the Public Evidence Stops tables, comparisons with Corvane), [[evolving-the-platform]], [[where-stay-platforms-go-wrong]], [[meet-corvane]]; `_research/style-guide.md`; LISTED's Part IX intro as the structural model.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: guidance-cut wording aligned with the Q1 2024 release ("citing", not "because"); figures checked against chapters 48–51. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 689 → 669 prose words; outline unchanged; one recap sentence cut from the hand-off, one vague phrase made plain; success criterion on the diagram updated to the two illustrations the post now has. *(AI-mediated session)*
