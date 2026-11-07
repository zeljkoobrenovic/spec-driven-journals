---
status: accepted
revised: 2026-11-07
---

# Spec: Case: Amazon, From Monolith to Services to the Everything Store

## Intent

Test the book's argument against the most quoted company in commerce architecture, using only Amazon's dated public record: the 2006 interview digest and the 2007 Dynamo paper for the move from a monolith to services and the always-writeable cart; the 2012 and 2022 DynamoDB sources for the operability lesson; the 2006 FBA launch, the 2018 shareholder letter series and the FY2025 10-K for the retailer-to-platform story; the 2024–2026 letters and releases for the delivery promise; and the 2024–2026 pages on Rufus/Alexa for Shopping, Buy for Me, Shop Direct and the Perplexity statement for agents. After reading, a newcomer can say which four rules transfer to a merchant (the contract as the only door; the cart as an availability problem; operability decides adoption; the promise as the product), which do not (the network, the robots, the database lineage), and where the public evidence stops.

## Audience

Readers new to commerce architecture. The engineer or architect who hears "Amazon did microservices" in a design review and needs to know what the sources actually say benefits most; the product manager or leader who sells on Amazon and sends stock to its fulfillment program benefits from the seller-of-record and external-location framing. Every term (monolith, SOA, tail latency, always writeable, eventual consistency, managed service, 1P/3P, seller of record, FBA, regionalization, placement, delivery promise, agentic commerce, product feed) is explained in one plain clause on first use.

## Success criteria

- [x] Every company fact carries its year in the sentence and a source in Sources and Evidence; facts the brief tagged as widely reported or unfetched (the 2005 Prime release, the 2004 two-pizza dating, the monolith's name, the February 2026 delivery record, the API mandate) are presented as such, not as Amazon documents.
- [x] Every statement about how Amazon's systems work beyond the published papers is inside a `> **INFERENCE, NOT DOCUMENTED:**` block.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The chapter contains the lessons table (lesson, evidence, transfers or not), a "What the Dynamo paper documents / does not say" table, the third-party share series 1999–2018, the promise requirements table, and three mermaid diagrams with captions.
- [x] The Prime Video 2023 post is presented as a narrow cost-and-coupling case, not as "Amazon abandoned microservices".
- [x] A "Where the evidence stops" section precedes "What to Take Away"; the three take-away tiers are present and honest; 6–10 questions to ask; the closing hands off to [[case-zalando]].
- [x] One short paragraph says what Kestrel & Pine takes from the case, tied to Waypoint W1, W5 and W8 and to ledger facts (40% of German marketplace units in Amazon's program, the static 22:00 promise, the four-hour WMS queue, 34 integrations, 14 in technology).
- [x] No "Across Scale Stages" section (Part XI); length 4,500–6,000 words.

## Non-goals

- The architecture styles as a general comparison, and when a split is justified — [[commerce-architecture-styles]].
- API governance as a discipline, versioning and deprecation — [[api-contracts-and-versioning]]; Zalando's written guidelines — [[case-zalando]].
- Marketplace selling mechanics, listings, SP-API, channel allocation — [[marketplaces-and-channel-integration]].
- The delivery promise engine and carrier integration — [[shipping-and-delivery]]; peak-day capacity — [[peak-load-and-reliability]] and [[journey-peak-day]].
- Agentic commerce protocols, EU constraints and the merchant's readiness list — [[ai-and-agentic-commerce]].
- Any description of Amazon's current order, pricing, promise or inventory systems; the chapter says the evidence stops there.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ACM Queue text of the 2006 Vogels interview and Fast Company's 2004 profile were blocked on 7 November 2026; if a reviewer can fetch them, the "widely reported" labels on the 2001 wall quotation and the two-pizza dating can be upgraded.
- The Amazon v. Perplexity case status, Buy for Me's commission terms and the Alexa for Shopping feature set are volatile; re-check before any print edition.
- Whether to add the Prime Day 2021 DynamoDB figure to the peak chapter's evidence rather than keeping it only here.

## Decision log

- **2026-11-07** — Organized the chapter by Amazon's own documents in date order (2006–2007 architecture, 2012–2022 database, 2005–2026 business, 2024–2026 promise, 2022–2026 agents) rather than by the book's capability map, because a case study's value is the provenance of each claim, and a reader should see which decade each one comes from.
- **2026-11-07** — Kept the "API mandate" but labeled it as Yegge's 2011 recollection throughout, rejecting both omitting it (it is the rule readers will ask about) and presenting it as an Amazon document (no Amazon page confirms it).
- **2026-11-07** — Gave the Prime Video 2023 post its own short section rather than a footnote, because it is the one source readers cite as a reversal and its actual scope needs stating.
- **2026-11-07** — Limited the Kestrel & Pine content to one paragraph of take-aways plus references in the inference blocks, per the Part XI brief; no scene, no scale-stages table.

## Sources

- **Internal**
  - `_research/brief-cases-amazon-zalando.md` (Part A, Part C, key numbers, open questions) — every Amazon fact and its tag.
  - `_research/scenario-ledger.md` — the Amazon.de channel, the 40% program-fulfilled share, W1/W5/W8, the static promise, the Black Friday figures.
  - [[commerce-architecture-styles]], [[api-contracts-and-versioning]], [[marketplaces-and-channel-integration]], [[shipping-and-delivery]], [[ai-and-agentic-commerce]] — owning chapters linked rather than re-taught.
  - [[case-zalando]] — the companion case the chapter hands off to.
- **External**
  - DeCandia et al., *Dynamo: Amazon's Highly Available Key-value Store* (SOSP 2007) — the cart's availability rule and the SOA statement.
  - High Scalability, *Amazon Architecture* (2007) — the 2001 scaling wall and services per page.
  - Vogels, *Amazon DynamoDB* (2012); Elhemali et al., USENIX ATC (2022) — the operability lesson and Prime Day scale.
  - Amazon shareholder letters 2018, 2024, 2025; Form 10-K FY2025; Small Business Empowerment Reports 2022 and 2024 — the business model, the third-party share and the delivery network.
  - Amazon pages on Rufus/Alexa for Shopping, Buy for Me, Shop Direct, Buy with Prime and the Perplexity statement; Retail Dive (2025); InfoQ (2023) — agents and the Prime Video nuance.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: marketplace-program share restored to the ledger's scope. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
