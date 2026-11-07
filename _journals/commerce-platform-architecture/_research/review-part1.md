# Review log — Part I (editorial pass, 2026-11-07)

Scope: `part-1`, `journey-of-an-order`, `commerce-business-models`, `commerce-capability-map`, `boundaries-and-systems-of-record`, `commerce-platform-landscape`. Previous reviewer's work discarded; reviewed from scratch. Build clean; render check OK on all six pages (0 failed mermaid, 0 unresolved links).

## Ruling recorded

- **Consistency item 13 → item 14:** two February 2027 pitches: an outside consultancy's composable rebuild (~€3.2M, 18 months) and the agency's headless storefront rebuild on the current platform (~€240,000, nine months). The ERP partner made no pitch. Noor declined both; W4. `[editor-review]` line appended to the ledger.

## Word counts (body before Sources and Evidence)

| Page | Before | After |
| --- | --- | --- |
| part-1 | 1,326 | 1,335 |
| journey-of-an-order | 6,776 | 6,909 |
| commerce-business-models | 6,689 | 6,801 |
| commerce-capability-map | 6,811 | 6,860 |
| boundaries-and-systems-of-record | 6,884 | 6,923 |
| commerce-platform-landscape | 6,792 | 6,837 |

All are under 7,000, so nothing needed trimming. The part intro runs over the 500–900 word target, like every other part intro in the book. I left it alone.

## Changes per page

**part-1**: the chapter summary now describes the February pitches as ruling 14 defines them.

**journey-of-an-order**
- Eva's delivery promise now matches the ledger. Under the static 22:00 rule she was promised Wednesday 14 April and the parcel arrived Thursday 15 April, so the promise was broken by a day. The old text said the promise was kept. The take-away now names this case.
- Step 6 notes that the order is created with the payment *pending* before the iDEAL webhook arrives (cart-and-checkout ledger line).
- The stock lag is now "up to" an hour and fifteen minutes.
- Defined theme, 3PL, marketplace connector and bol.

**commerce-business-models**
- Shopify Basic is €28 a month, or €21 when paid yearly. The old text said €21.
- Germany (2022) moved from the Omnichannel stage list to the Growing stage list.
- The wholesale contribution is "less than half" the D2C contribution (€36 vs €79), not "a third".
- The Double Refund is now attributed to two tools (the returns portal and the PSP console), not to two business lines.
- Defined punchout, parity rules, repricing, tenancy and ASN. The undefined "Evolve" tier became Shopware's €1M GMV threshold.

**commerce-capability-map**
- The empty boxes now match the ledger and Figure 3: four (product information, order management, availability, identity). The delivery promise is described as ownerless only on paper.
- The scale-stage table now links to `commerce-business-models`, the chapter that owns the stages.
- Defined theme, headless, Peppol and BI.

**boundaries-and-systems-of-record**
- The Three-Status Order mechanism now follows the ledger: the socks line was waiting on replenishment, and the ERP invoices on the WMS's "order complete" message.
- Wholesale prices now move by price events with effective dates (ruling 3 and the pricing ledger line).
- **The Walmart/Confluent quote was not verbatim.** I replaced it with the source's wording, checked against the page, and added the date (May 2020).

**commerce-platform-landscape**
- (A WHY IT MATTERS rewrite made in this pass was later superseded: the author dropped the callout book-wide and the coordinator removed it by script.)
- The scene and the analysis are rewritten to follow ruling 14: the consultancy's composable pitch and the agency's headless pitch. The ERP-module pitch is gone. The headless pitch is answered by the Core Web Vitals finding from `storefront-architecture`.
- The CCV Shop sentence moved out of the INFERENCE callout.
- Katapull timeline: Transus's joining date is not public, and Picqer is the eighth label. Highbiza's role is now given.
- Scale-stage ownership attributed correctly.

## Spot-checks (WebFetch, 2026-11-07)

- Baymard 70.22% across 50 studies and the reasons 40/20/18/17%: **verified** (page updated 28 October 2026).
- Mollie iDEAL (auto-capture, no chargeback, 15-minute session): **verified**.
- Lightspeed FY2026 transaction revenue $815.1M and subscription revenue $370.7M (21 May 2026): **verified**.
- Walmart partition quote: **paraphrased in the original text; corrected.**
- Shopify EUR prices: taken from the brief (VERIFIED); this exposed the €21/€28 mismatch.

## Open issues for others

- **Chapter 41 (`build-buy-or-assemble`)** still says "the agency proposed a composable rebuild" and "the ERP partner proposed an enterprise suite". Per ruling 14, the composable rebuild is the consultancy's, and the suite is at most an option the review costed.
- **Chapter 29 (`commerce-architecture-styles`)** has "the ERP partner's enterprise suite" as a pitch.
- **`where-commerce-platforms-go-wrong`** (around line 224) has three pitches, including "the ERP partner's suite", and "declined all three". It needs to match ruling 14.
- **Chapter 32** already matches.
- The Part I intros keep the book-wide "eight of ten incidents were one fact with no owner" claim. The commerce-scaling-stages ledger line uses "eight of ten" for a different claim (Growing-stage designs). Both can be true, but the Part X reviewer may want to check that the two claims do not read as the same number.
- "judgement" (the closing boilerplate) vs "judgment" (chapter 05's body) is a book-wide spelling choice that someone needs to settle.
