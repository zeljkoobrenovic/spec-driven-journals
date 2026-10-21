---
status: accepted
revised: 2026-10-21
---

# Spec: Part I — MARKETPLACE: The Business Behind the Listings

## Intent

Orient the reader to Part I: why a listing-systems book starts with the business rather than the systems, what the six chapters argue (marketplace model, liquidity, industry history, capabilities, bounded contexts, vertical physics), and how that vocabulary becomes the justification for every later boundary, shared platform and non-functional requirement. Frame the part through Ingrid Halvorsen's first months at Veldmark, testing the board-approved Common Ground program against the business.

## Audience

Chief and enterprise architects, principal engineers and engineering or product leaders of listing marketplaces who want to know what Part I covers and which chapter to read for the decision in front of them.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a failure-pattern callout using exact names linked to [[where-listing-systems-go-wrong]].
- [ ] States the part's argument in a short lead (model decides architecture; liquidity is the product; describe the business in terms that outlive systems).
- [ ] A "Chapters in this part" table lists all six chapters in config order as `[[permalink]]` | question | read it when.
- [ ] Explains the connection to the Preface and to [[part-2]].
- [ ] Veldmark thread (labeled fictional) uses only ledger facts: 20 marketplace profiles, Poland overlap, 38% vs 11% liquid cells, capability map of 31 March 2027 with five overlaps, 19 bounded contexts approved May 2027, share table ratified April 2027.
- [ ] Hands off to [[marketplace-taxonomy]].
- [ ] 500–800 words.

## Non-goals

Teaching any chapter's content (each chapter owns its terms), company facts (no sources needed), or the listing domain model ([[part-2]]).

## Modalities

Article only.

## Open questions

- ~~[[industry-evolution]] row written from the PLAN contract~~ — resolved 2026-10-19: the table row and Veldmark bullet now follow the written chapter (five waves; sediment; March 2027 separability decision).

## Decision log

- 2026-10-19: Structure follows the sibling [[part-2]] intro (callouts, chapter table, connections, Veldmark thread) for consistency across part intros; no learning-path diagram, to stay within 800 words.
- 2026-10-19: Failure patterns chosen: Vanity Liquidity, The Forced Fit, Deal-Shaped Architecture, the three most often named by the part's chapters.

## Sources

Internal: [[marketplace-taxonomy]], [[liquidity-and-network-effects]], [[industry-evolution]], [[business-capabilities]], [[bounded-contexts]], [[vertical-requirements]], [[meet-veldmark]]; `_research/scenario-ledger.md`.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: ch. 03 table row and Veldmark bullet rewritten from the written chapter (five waves, sediment, March 2027 separability decision). *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 678 → 680 prose words (already within budget; light pass); headings unchanged (fixed part-intro shape); lead's three steps made explicit; "How this part connects" now opens with its point (the vocabulary); one Veldmark bullet reworded. *(AI-mediated session)*
- **2026-10-20** — Second sharpening pass: 680 → 689 prose words; headings unchanged; the lead's second paragraph now opens with a claim ("Sharing decisions need three pieces of business knowledge") instead of "The part argues in three steps". *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
