---
status: accepted
revised: 2026-10-21
---

# Spec: Part VII — TRUST: Making Strangers Safe to Stay With

## Intent

Orient the reader to Part VII: why trust in a stays marketplace should be built as one platform of records (shared decisions, enforcement, identity, review history and market rules) with detection and thresholds kept per marketplace, where hotels and homes differ in what they need from it, and which question each of the six chapters answers. Frame the part through Corvane's 2027 sequence of incidents and the four group platforms they produced: Ordinance, Vouch, Corvane ID and Warden.

Productscape domains: framing for the trust, identity, reviews, protection and compliance domains (the part intro covers no bricks of its own; chapters 31–36 cover them).

## Audience

Chief architects, trust-and-safety and fraud engineering leads, identity architects, and regulatory or privacy leads of accommodation and hosted-stays marketplaces deciding which Part VII chapter to read for the decision in front of them.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS THIS PART ADDRESSES callout using exact pattern names, linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument: trust is a platform of records, not a collection of tools.
- [ ] A short paragraph names where hotels and homes differ (supply-side account takeover vs two strangers in one home; who carries identity, insurance and short-term-rental law) and notes that the OTA inherits the homes problem.
- [ ] One mermaid diagram with a Figure caption: brand detectors, Corvane ID, Ordinance and Vouch feeding Warden's decisions, enforcement out, receipts back, reasons to statements and reports.
- [ ] Corvane (labeled fictional) uses only figures from chapters 31–36: €48,540 Turia loss, €31,640 avoided in the replay, 16-day cross-brand gap, €212,000 reimbursed to 310 guests, 9.4 million stored images, 3,610 ring reviews, 6,900 Spanish removals reclassified in under an hour vs nine analysts over seven weeks; platform dates Ordinance (17 March 2027), Vouch (18 May 2027), Corvane ID (June 2027), Warden (17 August 2027).
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, each with what it decides, its Corvane case and when to read it.
- [ ] Names [[part-8]] and hands off to [[stays-trust-and-safety]].
- [ ] 500–900 words of body.

## Non-goals

Teaching any chapter's content: the trust decision and enforcement ([[stays-trust-and-safety]]), fraud typology and the booking risk score ([[travel-fraud]]), identity levels and the partner role model ([[identity-accounts-and-access]]), review law and integrity ([[reviews-and-reputation]]), screening and claims ([[protection-and-incidents]]) and the regulatory map ([[stays-regulation]]). No external company facts or regulations are cited; the chapters carry the sources.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-21: Modeled on LISTED's Part V intro and this book's Part II intro: one paragraph per chapter instead of a table, and the Corvane thread compressed to one paragraph naming the four group platforms in the order they were approved.
- 2026-10-21: Failure patterns chosen: Trust After the Incident (named by all six chapters), The Unwatched Model (chapters 31, 32, 34 and 35) and City-by-City Firefighting (chapter 36). The Hotel-Shaped Home was left out because the hotels-and-homes paragraph already carries it.
- 2026-10-21: The diagram shows Warden as the decision hub with the other three platforms as inputs, because that is the dependency chapters 32–36 describe; Fathom and Harbor are left to the chapters to keep the figure at seven nodes.
- 2026-10-21: No regulation fine figures in the callouts; the business case uses Corvane's own losses so the intro needs no external citation.

## Sources

Internal: [[stays-trust-and-safety]], [[travel-fraud]], [[identity-accounts-and-access]], [[reviews-and-reputation]], [[protection-and-incidents]], [[stays-regulation]] (callouts, leads, Corvane worked examples and Chief Architect's views), [[where-stay-platforms-go-wrong]], [[meet-corvane]]; `_research/scenario-ledger.md`; `_research/style-guide.md`.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
