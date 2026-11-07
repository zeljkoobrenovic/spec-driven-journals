# Review log — Part VII (PLATFORM)

Editorial pass, 2026-11-07. Scope: `part-7-intro`, `29-commerce-architecture-styles`, `30-multi-tenancy-and-isolation`, `31-extensibility-and-app-ecosystems`, `32-storefront-architecture`, `33-peak-load-and-reliability`. Started fresh; the earlier interrupted reviewer had made no edits.

Rulings applied: item 10 (41 apps in January 2027, 34 apps by July 2027; never conflated with the 34 integrations; already correct on all pages); item 11 (opener format; the WHY IT MATTERS callout was later removed book-wide by the coordinator, so no page carries it now); item 13/13a/14 (February 2027 pitches: an outside consultancy's composable rebuild, about €3.2M over 18 months; the agency's headless storefront rebuild, about €240,000 over nine months; the ERP partner made no pitch; the enterprise suite is a costed review option, not a pitch).

Word counts (body before `## Sources and Evidence`), before → after:

| Page | Before | After |
| --- | --- | --- |
| part-7-intro | 1,632 | 1,577 (callout removed by the coordinator) |
| 29-commerce-architecture-styles | 6,497 | 6,522 |
| 30-multi-tenancy-and-isolation | 6,503 | 6,451 |
| 31-extensibility-and-app-ecosystems | 6,723 | 6,716 |
| 32-storefront-architecture | 6,189 | 6,153 |
| 33-peak-load-and-reliability | 6,577 | 6,519 |

No page was over 7,000 words, so nothing was trimmed for length. Part VII's intro, like every other part intro, is over the 500–800 target in the style guide. It was left as it is for consistency across the parts.

## part-7-intro
- Named the sources of the pitches per item 13 (the outside consultancy's composable rebuild, the agency's headless storefront).
- Changed "four platform proposals" to "four platform questions", and limited the "would have rebuilt the part that held" claim to the rebuild proposals, because the 41 apps were not a rebuild.
- Glossed "monolith" and "pool, silo and bridge". Replaced the unexpanded LCP, CLS and INP in the chapter list with plain wording.

## 29-commerce-architecture-styles
- Item 13: the scene now describes two pitches (the consultancy's composable rebuild and the agency's headless storefront rebuild). The review costed the composable rebuild beside an enterprise-suite option and stay and surround. The ERP partner is no longer presented as a pitcher.
- KEY POINTS: changed "fourteen engineers" to "nine engineers" (the ledger has 14 people in technology, of whom 9 are engineers).
- Rebuild comparison table: the Price Drift was credited to W3, which is product information. It is now Price Drift and Double Refund under W5 contracts and reconciliation. Removed "Message in a Bottle", which is a pattern, not an incident.
- Verified quotes against the sources: the Zalando 2025 post says "competing sources of truth", not "divergent versions of product data", and says the delay applied to stock and price events. The Shopify Packwerk quote now reads "the way Shopify's code actually functions in practice". The MACH principles page (three principles, no acronym) was confirmed.
- Expanded on first use: MACH, ERP, WMS, PIM, iPaaS and AWS. Defined idempotent handling and glossed CRUD, serverless, paved road, stream-aligned team and the strangler approach. Changed "outbox" to plain wording. Changed "neighbours" to "neighbors". Timetoread changed from 25 to 27.

## 30-multi-tenancy-and-isolation
- Shopify quote corrected from "might" to "may temporarily reduce API rate limits" (verified on shopify.dev). Plan restore rates of 100/200/1,000/2,000 points per second, the 1,000-point query cap and the cost of 10 per mutation were verified.
- 2027 plan table: the availability-service fallback now matches the ledger (the old chain with the ten-unit marketplace buffer). It had said "listings paused by hand".
- Changed "Shopify's 2026 annual report" to "FY2025 annual report".
- Expanded SaaS, AWS, ERP, OMS, PIM, 3PL and HTTP 429. Glossed Redis and Memcached as caches. American spelling (neighbor, center). Timetoread changed from 24 to 27.

## 31-extensibility-and-app-ecosystems
- Ledger conflict fixed: the text had named "the WMS feed's companion app" as one of the three stock-writing apps. Those three apps all lose write access by June 2027, yet the WMS feed remains the single writer. The third app is now an agency-installed inventory-sync app. Recorded as an `[editor-review]` ledger line.
- Adobe lifecycle text corrected against the policy page. The "one extra year for 2.4.6 and 2.4.7" claim was not supported and was removed. Added 2.4.7's general availability of 9 April 2024. The quote now matches the page: traffic is suspended and the storefront "will go offline". The page does not say "may be taken offline". Retirement of Shopify Scripts on 30 June 2026 was verified.
- Expanded WMS, ERP, PIM, OMS, SEO, PCI, SFRA and 3PL. Glossed Lighthouse. Rewrote the Spaghetti Junction failure-pattern line. Timetoread changed from 26 to 28.
- My earlier rewrite of WHY IT MATTERS is moot because the callout has since been removed book-wide.

## 32-storefront-architecture
- Item 13: the agency's headless proposal (€240,000, nine months, second runtime) already matched. No composable-pitch attribution appears on this page.
- Hydrogen quotes corrected against shopify.dev: "doesn't include checkout UI, because checkout stays on Shopify". "At no extra cost" is now attributed to Shopify's February 2023 Editions post, not to the 2026-10 documentation.
- Noor's timing changed from "three weeks into her job" to "in her second month". She started in January and the proposal came in February. Removed the meta phrase "per the ledger".
- Expanded PIM, SFRA, B2B, D2C, POS and W3C. Glossed edge runtime. Identified Commerce.com as formerly BigCommerce. Timetoread changed from 25 to 27.

## 33-peak-load-and-reliability
- The availability-service fallback now matches the ledger (the ten-unit marketplace buffer in force since December 2026).
- Removed the invented "predecessor's team". The 8,000 missed next-day orders were labeled an assumption, but they are a ledger figure from warehouse-and-fulfillment, so they are now labeled that way.
- Verified the Shopify BFCM 2025 figures ($14.6B; $5.1M a minute at 12:01 p.m. EST; 489M edge and 117M app-server requests a minute). Verified the Zalando 2020 post (7,200 orders a minute in 2019, test orders skipped at fulfillment, non-essential async processing paused in 2015, the Situation Room).
- Expanded SRE, SLA, OMS (at first use), D2C and EDI. Timetoread changed from 24 to 27.

## Build and render check
- `python3 _wiring/build.py`: no errors.
- `render_check.py` for all six permalinks: every page OK. Mermaid diagrams render (2–3 per page), with no unresolved links.

## Open issues for other parts or the author
- **Stock writers before W1.** The integration-styles ledger line says four flows wrote stock (the hourly ERP sync and three apps). Chapter 31 and its `[editor-review]` line now agree. Chapter 31's single-writer rule ("the WMS feed through the iPaaS") assumes that after Waypoint the iPaaS carries WMS stock directly, not through the ERP. Chapters 10 and 24 should say the same.
- **Pitch wording elsewhere.** Item 14 asks chapter 41 and `where-commerce-platforms-go-wrong` to drop the ERP partner as a pitcher. That is outside Part VII and has not been checked here.
- **Ownerless integrations.** Part VII does not cite the count, but the 13 versus 5 conflict (organizing-commerce-engineering) is still open for the Part X reviewer.
