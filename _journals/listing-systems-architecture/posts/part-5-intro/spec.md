---
status: accepted
revised: 2026-10-20
---

# Spec: Part V — TRUST: Keeping the Marketplace Safe

## Intent

Orient the reader to Part V: why trust and safety, fraud prevention, identity and regulation should be built as one shared trust platform (shared machinery, local policy), which question each of the four chapters answers, and when to read each one. Frame the part through Veldmark's two 2027 fraud incidents and the decisions they drive.

## Audience

Chief architects, trust-and-safety and fraud engineering leads, identity architects and regulatory or data-protection leads of listing marketplaces.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS callout using exact names linked to [[where-listing-systems-go-wrong]].
- [ ] States the argument: trust is a platform capability, not a team with a queue.
- [ ] A "Chapters in this part" table covers all four chapters in config order, drawn from their KEY POINTS and leads.
- [ ] Connects back to [[part-2]], [[part-3]] and [[part-4]] and forward to [[part-6]] (messaging, payments and DAC7, trader records).
- [ ] A Veldmark thread, labeled fictional, matching the ledger: the 7 Mar 2027 phishing link (20:11, sixteen minutes after the 19:55 first contact), the July 2027 Barcelona ring (26 accounts, 180 listings, 63 victims, about €71,000), Veldmark ID (Jun 2027), the obligation register, the shared T&S platform for Tradeyard NL/BE (Nov 2027) with the hashed block list, first-contact friction (Dec 2027).
- [ ] The one external fact (DSA fines up to 6% of worldwide turnover) links to the regulation.
- [ ] Ends with a hand-off to [[trust-and-safety-architecture]].
- [ ] 500–800 words of body.

## Non-goals

Legal detail, fraud typology or identity methods (the chapters own them); Safe Deal volume figures.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-19: Modeled on RECONCILED's part introductions with this book's callout set and a chapter table.
- 2026-10-19: Failure patterns: Moderation as an Afterthought, The Scam Inbox, The Acquisition Archipelago.
- 2026-10-19: Safe Deal and DAC7 numbers deliberately left out of the part intro; [[marketplace-regulation]] owns them (its superseded 4.1M / €310M figures were corrected in the editorial review).

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, the KEY POINTS and lead paragraphs of [[trust-and-safety-architecture]], [[fraud-prevention]], [[identity-and-verification]] and [[marketplace-regulation]], and [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), Art. 52, for the fine ceiling.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: format, ledger facts and links checked; no article changes needed (Safe Deal figures in marketplace-regulation are now corrected to 11.6M / ~€1.02B). *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 666 → 666 words; headings unchanged (house shape); two sentences reworded (the argument sentence and the Veldmark thread's incident link); spec unchanged. *(AI-mediated session)*
