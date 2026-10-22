---
status: accepted
revised: 2026-10-22
---

# Spec: Part I — MARKETPLACE: The Business of a Night's Stay

## Intent

Orient the reader to Part I: why a book about stays-marketplace architecture starts with the business, how the two marketplace types (the OTA-style accommodation marketplace and the hosted-stays marketplace) differ in where their truth lives, and what the four chapters argue: the type, the economics, the capability map and the bounded contexts. The part's conclusion, "share the promise, not the supply", is stated up front so later parts can point back to it.

Productscape domains: framing for all (the part intro covers no bricks of its own; chapters 03 and 04 cover the whole map).

## Audience

Chief and enterprise architects, principal engineers and engineering or product leaders of accommodation and hosted-stays marketplaces who want to know what Part I covers and which chapter to read for the decision in front of them.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names, linked to where-stay-platforms-go-wrong.html.
- [ ] A short lead frames the two marketplace types by source of truth (supply integration vs one-unit integrity and trust) and acknowledges convergence.
- [ ] One diagram (illustrated) with a Figure caption that states the part's conclusion.
- [ ] `## Chapters in this part` has one paragraph per chapter, in config order, each with the question it answers and when to read it, consistent with the written chapters' callouts and Chief Architect's views.
- [ ] Corvane (labeled fictional) uses only facts from the chapters and ledger: 8 February 2027 CEO question, €195 million at 1,400:1, 48-capability map on 23 March 2027, €145 million One Stay program approved April 2027, 23 bounded contexts adopted 5 May 2027.
- [ ] Hands off to [[two-stay-marketplaces]] and names [[part-2]].
- [ ] 500–900 words.

## Non-goals

Teaching any chapter's content (each chapter owns its terms), company facts or sources (the chapters carry them), the supply model ([[part-2]]) and the full one-platform-or-two decision ([[converging-two-marketplaces]]).

## Modalities

Article only.

## Open questions

- None.

## Decision log

- 2026-10-21: Modeled on LISTED's Part I intro, but with one paragraph per chapter instead of a table, as requested, and the Corvane thread folded into one closing paragraph to stay within budget.
- 2026-10-21: Failure patterns chosen: The Hotel-Shaped Home (named by three of four chapters), Price Drift (chapters 03 and 04) and Phantom Availability (chapter 02's look-to-book argument).
- 2026-10-21: The diagram shows the part's conclusion (two supply engines, one offer and reservation contract, shared foundations) rather than a reading path, because the conclusion is what later parts refer back to.

## Sources

Internal: [[two-stay-marketplaces]], [[stays-marketplace-economics]], [[stays-capability-map]], [[stays-bounded-contexts]], [[meet-corvane]], [[where-stay-platforms-go-wrong]]; `_research/scenario-ledger.md`.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: "shopping requests" wording for the 1,400 figure; capability map and context map flagged as v1 with a pointer to the December 2027 revisions; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 857 → 858 words; Hotel-Shaped Home callout corrected to "three of the four chapters" (economics chapter does not name it); two long Corvane sentences split; no sections changed. *(AI-mediated session)*
