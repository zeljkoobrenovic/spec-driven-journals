---
status: accepted
revised: 2026-11-07
---

# Spec: Suites, SaaS, Open Source and Composable: The Platform Landscape in 2026

## Intent

Give a reader who has just joined a merchant, a vendor or an agency a map of the commerce platform market at the book's research cut-off (7 November 2026): the seven categories of platform, how each is priced, what changed between 2023 and 2026, and how to read a vendor's claims. The argument: the category decides where the integration work and the cost land; platforms are priced on the merchant's sales rather than on software; and the 2024–2026 market converged on selling layers beside an existing stack. After reading it, the reader can place any platform in a category, ask for the unit, date and definition behind any vendor number, and see why Kestrel & Pine's W4 (stay and surround) is the shape most Omnichannel-stage merchants end up with.

## Audience

Readers new to commerce architecture. The engineer or product manager who has inherited a platform and is about to sit through a replatforming pitch benefits most; the chapter is written at Noor Visser's altitude in February 2027, before she had the vocabulary to answer "what kind of platform are we on?". Analysts and leaders who must read vendor decks and analyst charts get the reading guide in the second half.

## Success criteria

- [x] The seven categories are defined in one table (what you buy, who runs it, where the integration work lands, examples) and each has a paragraph with at least one dated, sourced vendor example.
- [x] Every vendor fact carries a year or an "accessed 2026-11" date in the sentence; every inference about a real company (Lightspeed's regional risk, Salesforce's GMV pricing, Katapull's unknowns) is labeled as inference or industry belief, and nothing is stated about any vendor's proprietary internals.
- [x] The pricing section has a table of pricing models with dated examples, defines GMV, transaction fee and interchange, and includes a Kestrel & Pine illustration (labeled as an assumption) showing that the subscription line is the smallest line.
- [x] The "What changed, 2023 to 2026" table is dated row by row and supports the chapter's reading that vendors now sell layers beside existing stacks.
- [x] The "How to read a vendor's claims" table teaches unit, date and definition with examples used earlier in the chapter, and the W3Techs versus EHI contrast and the Eurostat EDI statistic are present with their caveats.
- [x] A table says which platform categories fit which scale stage (Starting, Growing, Omnichannel, Group), with what becomes necessary and the warning signs of outgrowing an approach, followed by a judgement.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] Kestrel & Pine figures (platform €2,300 a month, €2.6 million technology spend, 41 apps, 34 integrations, the 2026 incidents, W1–W5) match the ledger; the two February 2027 pitches follow consistency ruling 13 (an outside consultancy's composable rebuild at about €3.2 million; the agency's headless storefront rebuild at about €240,000).
- [x] Two mermaid diagrams with captions; a trade-off table; the three take-away tiers; six to ten questions; grouped Sources and Evidence; the article stays within the 6,500-word cap including tables.

## Non-goals

- The decision method for choosing or changing a platform and the full cost model — [[build-buy-or-assemble]]; migration mechanics — [[replatforming-and-migration]].
- Architecture styles as engineering (monolith, modular monolith, microservices, composable as a style) — [[commerce-architecture-styles]].
- Tenancy, pods and rate limits — [[multi-tenancy-and-isolation]]; apps, plugins and the Forked Platform mechanics — [[extensibility-and-app-ecosystems]]; storefront delivery — [[storefront-architecture]].
- The composable movement's history, commercetools and Shopware in depth, and the MACH survey data — [[case-composable-movement]]; Shopify in depth — [[case-shopify]].
- Agentic commerce protocols and their regional status — [[ai-and-agentic-commerce]]; ERP as hub versus commerce as hub — [[erp-and-back-office-integration]].
- The capability map itself — [[commerce-capability-map]]; the scale stages as a model — [[commerce-scaling-stages]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Salesforce Commerce Cloud's pricing model is stated only as an industry belief; if a Salesforce document confirms or denies GMV-based pricing, the pricing table should be updated.
- SAP Commerce Cloud is described from Spartacus and one analyst note because sap.com refused automated fetching; a reviewer with access to SAP's product pages should check the "cloud ERP edition" wording.
- The commercetools CEO sequence (founder to Andrew Burton in July 2024; Doug McNary signing results by April 2026) is documented at both ends but the handover itself was not found in a release.
- Prices and plan names on every vendor page are volatile; the chapter should be re-dated at the next edition.

## Decision log

- **2026-11-07** — Chose seven categories (adding specialist layers and specialist groups to the usual five) because the ledger's merchant lives in the joins between a platform and its layers, and because the Dutch group model (Katapull) is a real third shape beside suite and composable.
- **2026-11-07** — Put pricing before the timeline and the reading guide, because the price is the clearest public evidence of what a vendor's product really is, and the Kestrel & Pine fees-versus-subscription illustration is the chapter's most transferable lesson.
- **2026-11-07** — Framed the Kestrel & Pine scene as two replatforming pitches (composable and ERP-centered) so the chapter shows the Giant's Boots and the Burned Bridge without naming a vendor; recorded the pitches in the ledger.
- **2026-11-07** — Cut the draft from about 8,700 to under 6,500 words by removing a systems table that duplicated [[meet-kestrel-and-pine]] and shortening every vendor paragraph to its dated facts.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the systems landscape, the 41 apps, the 34 integrations and the Waypoint decisions.
  - [[commerce-capability-map]], [[boundaries-and-systems-of-record]] — the capabilities and the ownership rules the categories map onto.
  - [[build-buy-or-assemble]], [[commerce-architecture-styles]], [[extensibility-and-app-ecosystems]], [[case-shopify]], [[case-composable-movement]] — the chapters that own what this one only names.
  - `_research/brief-platform-landscape.md` and `_research/brief-shopify.md` — the verified vendor facts, pricing, timeline and the claims-reading table; `_research/scenario-ledger.md` and `_research/style-guide.md` — figures and rules.
- **External**
  - Shopify FY2025 Form 10-K (2026) and pricing pages (accessed 2026-11); Commerce.com Q2 2026 SEC exhibit; Lightspeed strategic review (2025) and FY2026 results — the pricing and revenue-mix evidence.
  - Adobe Experience League (2026), Shopware releases and pricing (2025–2026), commercetools releases (2026), TechCrunch (2025), Microsoft Learn (2026), Katapull and Dutch IT Channel (2025–2026) — the categories and the 2023–2026 timeline.
  - MACH Alliance (2020, 2026), W3Techs (2026), Eurostat (2026) — definitions, usage shares and the EDI-versus-web statistic.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: reframed the February 2027 pitches per consistency ruling 13 (consultancy composable rebuild about €3.2M; agency headless storefront rebuild about €240,000; no ERP-partner pitch); moved the CCV Shop sentence out of the inference callout; completed the Katapull timeline (Transus undated, Picqer eighth label); pointed scale stages to their owning chapter. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document references rephrased as Kestrel & Pine's records. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
