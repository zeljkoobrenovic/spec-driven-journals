---
status: accepted
revised: 2026-10-21
---

# Spec: Part VI — MONEY: Conversion and Monetization

## Intent

Orient the reader to Part VI: why conversion and monetization should be designed as one pipeline with a built-in conflict between revenue and liquidity, which question each of the five chapters answers, and when to read each one. Frame the part through the Veldmark decisions on the contact path, monetization proposals, advertising rules and the group entitlement service in 2027.

## Audience

Chief architects, monetization and commercial-platform leads, product and engineering directors who decide what a marketplace sells, how it is delivered and how it is billed.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS callout using exact names (Fast Mail for Fraudsters, Multiplier Creep, Billing by Guesswork) linked to [[where-listing-systems-go-wrong]].
- [ ] States the part's argument: marketplaces sell access to attention, and every revenue line must measure and cap what it costs the match rate.
- [ ] A "Chapters in this part" table lists all five chapters in config order with the question each answers and when to read it.
- [ ] Connects back to [[part-5]] and [[part-4]], forward to [[part-7]], and points to RECONCILED's [[payments-fundamentals]] for payments depth.
- [ ] A Veldmark thread, labeled fictional, whose facts match the scenario ledger (conversation service and safety gate May 2027, live Nov 2027 for Tradeyard NL/BE; lead event contract Q1 2028; May 2027 monetization proposals; July 2027 Veldmark Ads rules; Tally designed Oct 2027 after 1,140 dealers were overbilled).
- [ ] Ends with a hand-off to [[messaging-and-leads]].
- [ ] 500–800 words of prose outside the callouts and table.

## Non-goals

Re-teaching any chapter's content; defining lead, VAS, entitlement or ad stack beyond one clause; external factual claims.

## Modalities

Article only for now.

## Open questions

- None open. *(Resolved 2026-10-19: the chapter 29 row and the Veldmark thread were updated from the written [[transactions-and-payments]] chapter.)*

## Decision log

- 2026-10-19: Modeled on [[part-2]] (callout set, chapter table, connections, Veldmark thread, hand-off) so all part intros look alike.
- 2026-10-19: Failure patterns limited to the three strongest for the part; Vanity Liquidity left to the chapters.
- 2026-10-19: The Veldmark thread lists decisions only; figures stay in the chapters, except the €1.31 billion group revenue and the overbilling count that motivate the part.

## Sources

`config.yaml`, `PLAN.md` (contracts 28–32), `_research/scenario-ledger.md`, and the KEY POINTS and lead paragraphs of [[messaging-and-leads]], [[monetization-models]], [[products-and-entitlements]] and [[advertising-platforms]]. No external factual claims.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: chapter 29 row rewritten from the written chapter, Safe Deal transaction-platform decision added to the Veldmark thread, Golf leads labeled raw versus merged. *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 742 → 746 prose words; two sentences tightened (the part argument now says what the chapters design; the Part V threads read as one list); no heading, section or fact changes. *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
