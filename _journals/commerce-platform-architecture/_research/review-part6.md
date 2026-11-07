# Review log — Part VI (INTEGRATION)

Reviewer pass of 2026-11-07. Word counts are measured before `## Sources and Evidence`. No page was over 7,000 words, so nothing was trimmed for length.

**Note:** the author later dropped the WHY IT MATTERS callout from every page, and the coordinator removed it by script. The WHY IT MATTERS edits listed below therefore no longer exist on the pages, and the after counts are from before that removal.

Spot-checked with WebFetch, all confirmed: OpenAPI 3.2.1 (10 September 2026); Stripe current version `2026-10-28.endive` and header/account pinning; Shopify HTTPS webhooks (8 retries over 4 hours, deletion after 8 consecutive failures for API-created subscriptions, 5-second total timeout); Mollie webhooks (10 calls over about 26 hours, id-only payload).

## part-6-intro (1,646 → 1,629)
- WHY IT MATTERS shortened. It is still two sentences.
- iPaaS and PSP are now expanded where Eva's order is introduced.
- Trimmed to the author's new target for part intros (about 1,500 words). The page was 1,555 words after the WHY IT MATTERS callout was removed and is now 1,488. Cut: two lead sentences that repeated themselves, the incident sentence that repeated the failure patterns, and a sentence in the Figure 1 caption that repeated the lead.

## 24-integration-styles (6,847 → 6,873)
- "Omnichannel stage" is now defined on first use.
- Daily order volume corrected from "about 1,100" to "about 950". The ledger's 2026 totals are (293,000 + 43,000 + 9,400) ÷ 365. Fixed in two places.
- Post-Waypoint stock path (reported by the Part VII reviewer): the order narrative and the inventory excerpt now say that WMS stock events reach the availability service through the iPaaS, and that availability reaches the platform and the connector the same way. The ERP is no longer on the stock path.
- The second writer in the App That Wrote Stock is now "the hourly ERP sync, carrying the WMS's figure", to match the ledger.
- Item 16: the 13-of-34 ownerless count is now dated to January 2027 in KEY POINTS, the inventory table and the scene paragraph. The inventory section adds that 5 were still unowned in April 2027, after the ownership map, and links [[organizing-commerce-engineering]]. The Part VI intro dates the 13 to January 2027 in three places.

## 25-events-consistency-and-reconciliation (6,719 → 6,752)
- WHY IT MATTERS: the claim "for two months the platform promised stock on 390 variants" had no source. It now says the May 2027 check found 390 variants that differed.
- The DLQ (dead-letter queue) paragraph said Black Friday orders "failed … went nowhere". It now says no order was lost, matching the ledger and chapter 24.
- The Double Refund trigger now follows the payments chapter's ledger line: customers saw the Duiven scan and asked support.
- "None of the 41 apps" is now "none of the apps" (consistency item 10: 34 apps after governance).
- The Walmart 2020 source is flagged as old in the In Practice section.
- Spelling changed to American: catalog, cataloged.

## 26-api-contracts-and-versioning (6,703 → 6,691)
- WHY IT MATTERS cut from four sentences to two (item 11).
- IETF/RFC and "2xx" are now explained.
- The Zalando 2015 and InfoQ 2016 sources are flagged as old.
- "mould" is now "mold".

## 27-identity-and-master-data (6,499 → 6,530)
- CDP and MDM are now expanded where first used (the responsibilities table).
- GDPR, GLN/GS1, EAN-13 and ASIN are now expanded.
- The opener was already compliant. All ledger figures were checked (410k/38k/165k/61k; 21,000/4,100/96,000; June/July 2027).

## 28-commerce-data-and-analytics (6,206 → 6,237)
- **Item 1:** W7 net sales are now recognized at delivery (D2C and marketplace) and at delivery to the customer's distribution center (wholesale), under IFRS 15. The chapter states that "shipped" is the operational milestone. Previously it said "recognized at shipment".
- WHY IT MATTERS cut from four sentences to two.
- BI, WMS, D2C, PSP and VAT are now expanded.
- The text said "BI on operational copies … this is Kestrel & Pine in 2024", but the ledger says the warehouse existed from 2024. The sentence now describes how reporting still worked in early 2027.
- All three counts and the bridge arithmetic were checked against the ledger. They are correct.

## Ledger
- Added one `[editor-review]` line covering three points: ownerless integrations per item 16 (13 in January 2027, 5 in April 2027); net-sales recognition at delivery; about 950 orders a day.

## Open issues for other parts / the author
1. **Item 16, for chapters 34, 35, 44 and where-commerce-platforms-go-wrong:** each must date its count of unowned integrations (13 in January 2027, 5 in April 2027). Chapter 44's 14/9/6/5 breakdown is also different from chapter 24's 14/9/11.
2. **Ledger, commerce-data-and-analytics line:** it still says "recognized at shipment". My editor-review line supersedes it. Chapters 14, 37 and 39 should be checked against item 1.
3. **Part intros:** resolved. The author set the target at about 1,500 words.
4. **timetoread on chapters 24–28** is 22–26 min against roughly 20 min of prose (tables excluded) or roughly 29 min with everything counted. Left unchanged as within tolerance.
