---
status: accepted
revised: 2026-10-21
---

# Spec: After the Deal: Consolidating Platforms After Acquisitions

## Intent

Give a Chief Architect a defensible way to decide what to consolidate after a marketplace acquisition, in what order and under which conditions. The chapter must present the integration options (hold separate, federate, share services beneath, replatform onto a sibling, merge brands, divest), a consolidation sequence with measured gates that puts invisible and pooled capabilities first and the core product last, a synergy case that counts dis-synergies and separation cost, and the architecture of a brand migration. It owns the terms consolidation sequence, synergy case and brand migration. After reading, the reader can challenge a deal model's technology lines, write an integration decision record and plan a rebrand that does not damage organic traffic, accounts or partner feeds.

## Audience

Chief and enterprise architects, CTOs and integration leads of marketplace groups that buy and sometimes sell marketplaces, and the finance and corporate-development partners who write synergy cases with them.

## Success criteria

- [ ] Integration options are compared in a table with dated public examples (eBay/Marktplaats 2004, iBazar to Vivanuncios 2015, OLX 2014 rebrands, CMA remedies 2021, Immowelt/immonet 2015–2024, Ultimmo 2022).
- [ ] A consolidation sequence with stages and measured gates, explaining why payments consolidate first as contracts and identity sits with trust.
- [ ] Synergy case defined in four parts, with Adevinta's eCG figures summarized and linked to [[case-adevinta]] rather than retold.
- [ ] Brand migration workstreams with Google's site-move guidance (2026), the Kleinanzeigen rebrand (2023) and separate platform migration (published 2025), mobile.de's token-based app rebrand (2025) and the P2B notice period.
- [ ] Veldmark worked example: the Casavista synergy review (deal case, rebrand on 9 March 2026, inverted sequence, Barcelona ring, revised plan matching identity, T&S and catalog dates in other chapters), the Keybridge synergy line withdrawn, the Polish overlap.
- [ ] Trade-off tables (options; speed against safety), vertical differences, failure modes, Chief Architect's view and 6–10 questions; at least three mermaid diagrams.

## Non-goals

- The tenancy model and configuration design ([[multi-country-platforms]]).
- Migration techniques such as strangler fig, parallel run and relevance parity ([[modernization-and-migration]]).
- Team design and acquired organizations ([[organizing-marketplace-engineering]]).
- Full company histories ([[case-adevinta]], [[case-ebay-classifieds]], [[case-aviv]], [[case-olx]]).
- Deal valuation and accounting for acquisitions.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Adevinta's €130–165 million eCG synergy target was achieved is not public.
- Account continuity in the Kleinanzeigen rebrand rests on press reporting; replace with a primary source if one is found.
- Whether OLX will move La Centrale onto its motors platform is not public; revisit when OLX reports on it.
- Otodom and other OLX vertical brand histories could not be verified from primary sources and are not used.

## Decision log

- **2026-10-19** — Set the Veldmark scene in the October–November 2027 synergy review, because the ledger already places Hearthly.es partly on Casavista's code and the Barcelona ring on an unverified login, which makes the inverted sequence concrete.
- **2026-10-19** — Added canonical Casavista synergy figures and the rebrand date to the ledger so later chapters (modernization, case studies) can reuse them.
- **2026-10-19** — Treated Keybridge as a permanent "federate under controls" case and made the withdrawn cross-selling line the chapter's example of a revenue synergy that should never be written.
- **2026-10-19** — Placed payments in stage 1 as a contract consolidation, citing the shared payment provider of Marktplaats and Kleinanzeigen, rather than as a code merger.

## Sources

Internal: [[case-adevinta]], [[multi-country-platforms]], [[business-capabilities]], [[identity-and-verification]], [[fraud-prevention]], [[products-and-entitlements]], [[professional-seller-tooling]], [[marketplace-taxonomy]], [[web-and-seo-architecture]], [[organizing-marketplace-engineering]].

External: eBay 8-K 2004; eBay Vivanuncios 2015; Immowelt 2015; Adevinta 2021, 2023 (annual report and rebrand release) and Strategic Report 2025; Berlin Tech Blog 2025 (two posts); Worldline 2022; Online Marketplaces 2024 and 2025; MySweetImmo 2022; OLX Tech 2026; OLX Group 2025; CMA 2021; Bundeskartellamt 2026; Regulation (EU) 2019/1150; Google Search Central (updated 2026); Wikipedia (OLX).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: AVIV "fully integrated platform" attributed to the interviewer (consistency item 18); American spelling; timetoread corrected to 27 min; Bundeskartellamt 8 Oct 2026 and Adevinta synergy figures re-verified. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 4,969 → 4,982 prose words; no headings renamed; lead now places the chapter as the opener of Part VIII and names what later chapters take from it; decoupling rule moved to the top of the brand-migration section; four paragraphs restructured to lead with their point; one announcing sentence cut. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
