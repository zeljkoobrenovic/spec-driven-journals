---
status: accepted
revised: 2026-11-07
---

# Spec: Case: commercetools, Shopware and the Composable Movement

## Intent

Test the composable promise against the dated public record of the vendors that made it: commercetools from its 2024 leadership change through its February 2025 cuts to its 2026 agentic layer and standalone modules; Shopware's opposite path of pulling integration and payments into the platform; Adobe's deployment options, the Mage-OS fork and Commerce.com's rename; and the MACH Alliance's three rewrites of its principles, read against its own 2026 survey. The reader should be able to say what composable promised, what its champions now sell, what a full assembly costs and who pays it, and under which conditions assembling commerce from parts is right. The case supports the book's recommendation for Omnichannel-stage merchants and Kestrel & Pine's Waypoint program: keep the core, add capabilities as owned services beside it.

## Audience

Readers new to commerce architecture who will meet the word "composable" in a replatforming pitch, an analyst chart or a conference talk within their first months. Engineers and product managers deciding whether to adopt a capability as a separate service benefit most; leaders who must judge a consultancy's composable proposal get the cost table, the fit table and the questions.

## Success criteria

- [x] The 2020 definition of MACH, the December 2023 restatement, the August 2025 five principles and the November 2026 three principles are quoted side by side with dates and sources, and the dropped words (microservices, headless) are named.
- [x] commercetools' turn is given as a dated table (July 2024, February 2025, January 2026, April 2026, June 2026, July 2026, October 2026) with each row sourced to a release or TechCrunch; the reasons for the turn are presented only as a labeled inference.
- [x] Shopware's path (bootstrapped to 2022, PayPal's stake, GMV-based pricing and the €1 million fair-use line, EHI market position, Nexus and Payments in June 2026, the August 2026 management change) is dated and sourced, and the reading that it responds to composable is labeled as inference.
- [x] Every vendor fact carries a year or "accessed 2026-11"; sources older than three years (EPAM 2020, Shopware 2022) are flagged; no proprietary internals are invented for any company.
- [x] The alliance's February 2026 survey is presented with its caveats, and the 37% integration-complexity finding is identified as the finding against interest.
- [x] A cost table (storefront, joins, upgrades, separate services, licenses, people, exit) and a fit table (scale stage, differentiation, team shape, vendor count, reason to move) give conditions, not verdicts.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] One short Kestrel & Pine paragraph ties the case to the February 2027 pitch and to W1–W5 with ledger figures; no scene section and no "Across Scale Stages" section, as the case format allows.
- [x] A "Where the evidence stops" section precedes "What to Take Away"; the three take-away tiers are present; two mermaid diagrams with captions; six to eight questions; grouped Sources and Evidence; 4,500–6,000 words.

## Non-goals

- The platform categories, pricing models and the 2023–2026 timeline as a market map — [[commerce-platform-landscape]].
- Composable as an engineering style, and the modular monolith and microservices evidence — [[commerce-architecture-styles]]; Shopify's monolith — [[case-shopify]]; Zalando's microservices — [[case-zalando]].
- The decision method and total cost of ownership — [[build-buy-or-assemble]]; migration mechanics — [[replatforming-and-migration]].
- Extension mechanisms and the Forked Platform — [[extensibility-and-app-ecosystems]]; headless storefront delivery — [[storefront-architecture]].
- Agentic commerce protocols and their availability — [[ai-and-agentic-commerce]]; the chapter names AgenticLift and "Autonomous Commerce" only as evidence of the vendors' vocabulary.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The commercetools CEO handover from Andrew Burton to Doug McNary was not found in a release; if one exists, the table should carry its date.
- commercetools' April 2026 ("500+ enterprises", $100 billion, 600 million orders) and July 2026 ("more than 600", $110 billion, 700 million) figures are not reconciled by the vendor; a reviewer should check whether a later release defines the units.
- The general-availability date of Adobe Commerce as a Cloud Service rests on partner reports; an Adobe release would replace them.
- No independent cost study of composable versus platform-plus-layers was found; if one with a stated method appears, the cost section should cite it.

## Decision log

- **2026-11-07** — Organized the case around the vendors' own dated words (releases, pricing pages, the alliance's principles pages) rather than press commentary, because the argument that the champions corrected themselves is only persuasive from primary sources.
- **2026-11-07** — Paired commercetools with Shopware as opposite paths rather than as two composable vendors, because the contrast shows that open source and composable are independent axes.
- **2026-11-07** — Kept the MACH survey's favorable AI figures with their caveats rather than omitting them, so the reader learns to read a commissioned survey and why the 37% integration-complexity figure is the one to keep.

## Sources

- **Internal**
  - [[commerce-platform-landscape]] — the categories, pricing and timeline the case builds on, and the February 2027 pitch it refers back to.
  - [[meet-kestrel-and-pine]] — the team size, the agency retainer, the 34 integrations and W1–W5.
  - [[commerce-architecture-styles]], [[build-buy-or-assemble]], [[case-shopify]] — the chapters that own the design, decision and Shopify material.
  - `_research/brief-platform-landscape.md` (Parts 1.3–1.5 and 3) — the verified vendor and MACH facts; the commercetools June, July and October 2026 releases were fetched and verified in this session.
- **External**
  - EPAM (2020) and MACH Alliance (2023, 2025, 2026) — the three formulations of the principles and the 2026 survey.
  - commercetools releases (2024, 2026) and TechCrunch (2025); Shopware releases and pricing (2022, 2025–2026) and Ecommerce News Europe (2025); Adobe Experience League (2026), Rightpoint (2025), Mage-OS (2022–2026); Digital Commerce 360 (2025) and the Commerce.com SEC exhibit (2026) — the dated vendor record.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: February 2027 pitch attribution corrected (item 13a). *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
