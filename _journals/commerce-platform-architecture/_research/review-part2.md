# Review log — Part II (CATALOG)

Editorial pass, 2026-11-07. Word counts measured before `## Sources and Evidence`. "Before" counts include the WHY IT MATTERS callout, which the coordinator later removed from every page by script; it was not reinstated.

| Page | Before | After |
| --- | --- | --- |
| part-2-intro | 1,301 | 1,097 |
| product-information (06) | 6,882 | 6,827 |
| pricing-architecture (07) | 6,981 (7,006 mid-pass) | 6,496 |
| commerce-promotions (08) | 6,494 | 6,415 |
| commerce-search-and-discovery (09) | 6,457 | 6,356 |
| inventory-and-availability (10) | 6,601 | about 6,580 |

Build: no errors. Render check: all six pages OK (0 failed mermaid, 0 unresolved links).

## Cross-page fix

- Removed reader-facing references to "the ledger" (the internal scenario ledger) in 06, 07, 08, 09 and 10; replaced with [[meet-kestrel-and-pine]] or plain wording.

## part-2-intro

- Defined system of record, SKU, GTIN and PIM on first use; tightened the lead and the five chapter summaries (still above the 500–800 part-intro target at about 1,100 words including the diagram; the author may cut further).

## 06 product-information

- Expanded PIM, WMS, EDI, GS1, CE marking, MDM/PLM and B2B on first use; defined landed cost.
- Fixed a ledger conflict: "crossed the line in 2023 ... marketplaces, a third country" is now 2021–2022 (marketplaces 2021, Germany 2022).
- Dated volatile platform limits "as of November 2026"; the commercetools Modular Catalog GA note (29 September 2026) could not be re-fetched (404) and is now attributed to "commercetools' 2026 release notes". Shopify 2,048-variant changelog (15 October 2025) verified.
- Clarified the bol 140-declines sentence; timetoread 26 → 30.

## 07 pricing-architecture

- Consistency ruling 3 applied: the ERP feeds no channel directly (no ERP→storefront link); it publishes wholesale and contract prices by event to the B2B catalogs and, from Q4 2027, the OMS.
- Corrected the derived DE gross price (€195.73 → €195.71) and the Omnibus fine wording (maximum fine at least 4% of turnover or €2 million).
- Verified ACM fines (published 11 June 2024, decided 2 May 2024, five shops) and the Bundeskartellamt 5 February 2026 prohibition; the overview does not state finality, so "not final" became "finality not stated"; added the €59 million initial disgorgement.
- Takeaway corrected: Amazon dropped price parity in 2013 after a German case (not "abandoned in the EU").
- Marketplace row of the 13 April table: connector rule now uses each marketplace country's price; €95 floor labeled illustrative.
- Expanded ERP, SKU, EDI, ORDERS/INVOIC, iPaaS, SaaS.
- Trimmed to 6,496 words: marketplace-law paragraph (dropped the 2022 EC commitments and its source), currency and tax paragraphs (dropped Shopify's $90.91 example and its source link), SAP/Adobe moment-of-selection evidence, platform B2B evidence, ownership paragraph, small lead cuts. Timetoread 28.

## 08 commerce-promotions

- Ruling 9 checked: Stacking Bug figures (2,860 orders; €43,000 + €5,600 + €3,000 ≈ €52,000) match the ledger.
- Expanded D2C, OMS, ERP, WMS, IFRS 15, idempotency key and webhook; replaced "per Omnibus" before its definition.
- Removed the sentence citing "the brief this chapter rests on".
- Starbucks FY2025 10-K figures and Amazon's 2025 subscription revenue could not be verified by fetch (EDGAR pages truncated before the notes); left as sourced to the primary filings. Timetoread 28.

## 09 commerce-search-and-discovery

- Fixed timing: the "Q1 2027" report was delivered in February but synonyms were added in March; now "mid-March 2027 ... the first-quarter search report so far".
- Expanded ERP, WMS, B2B; moved the PIM expansion to first use.
- Verified the Zalando Q3 2026 release (3 November 2026, "more than 22 million unique users") and the FTC rule (14 August 2024). Timetoread 28.

## 10 inventory-and-availability

- Oversell timeline aligned with the journey-peak-day ledger line: Milan Petrov zeroed the Ridgewalker in the connector by hand at 21:05 (replacing an invented "about 21:15 hourly push / 21:35").
- Coordinator item: made the post-Waypoint path explicit: WMS stock events reach the availability service through the iPaaS, not through the ERP (iPaaS expanded there).
- "Had all four in 2023" corrected (click-and-collect and wholesale allocations did not exist then).
- Corrected the ZEOS/NEXT quote to the press release's words ("a unified stock pool and an advanced order management system"); verified the Shopify reserved→committed changelog (5 August 2026).
- Removed the Sources entry citing internal "Research brief" documents; replaced with an author's-synthesis note.
- Ruling 10 checked: 41 installed apps (January 2027), three writing inventory. Timetoread 29.

## Open issues for the author or other parts

- The part intro is still above the 500–800-word target.
- 10 says the pre-Waypoint writers were "the ERP connector, the WMS feed and three apps"; the capability-map and integration-styles ledger lines count writers differently (six writers of Duiven stock; four flows into the platform). Reconcile in Part I/VI if the counts are quoted.
- 06's color story has three spellings ("MOSS GRN", "Moss", "olive") for four copies; the product-information ledger line says each of the four copies had "its own spelling". Minor; the ledger line could be read as three.
- Starbucks and Amazon 10-K figures (08) were not re-verified.
