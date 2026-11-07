# Review log — Part V (CHANNELS)

Editorial pass, 2026-11-07. Fresh start (the earlier reviewer made no edits). Word counts before Sources and Evidence; none was over 7,000, so no trim was required. The small increases come from acronym expansions and ruling wording.

| Page | Before | After |
| --- | --- | --- |
| part-5-intro | 1,486 | 1,495 |
| 20 marketplaces-and-channel-integration | 6,909 | 6,951 |
| 21 b2b-commerce | 6,936 | 6,971 |
| 22 edi-and-e-invoicing | 6,490 | 6,553 |
| 23 erp-and-back-office-integration | 6,488 | 6,633 |

Render check: all five pages print OK (2 mermaid diagrams each, 0 failed, 0 unresolved). Build is clean.

## part-5-intro
- Failure patterns cut from four to three (The Long Fuse dropped; its e-invoicing date folded into The Pulled Rug bullet).
- Item 3: Figure 1 gains an "ERP → B2B portal: wholesale prices and credit as events" edge; caption now says the ERP "feeds no channel directly".
- EDI and ERP expanded on first use.
- Length (1,495) is above the style guide's 500–800 for part intros, but in line with every other part intro (1,150–1,950); left as is.

## 20 marketplaces-and-channel-integration
- WHY IT MATTERS rewritten from five sentences to two.
- Item 7: the "assumed 15% commission" is now labeled as the most common referral rate on Amazon's US pricing page (verified with WebFetch: 15% for most categories; $39.99/month; clothing bands 5/10/17%).
- bol: dropped "version 10 as of November 2026" for the Retailer API. The bol news item "Offers API v10 stops on 1 February 2027" (3 Nov 2026) is verified, but its link slug refers to v11, so the "current version" claim could not be confirmed.
- TikTok Shop: the NL/BE/AT/PL launch on 15 June 2026 is verified (newsroom, 28 May 2026); the 31 March 2025 DE/FR/IT date is marked "widely reported".
- Acronyms expanded: WMS, ERP, OMS, PIM, iPaaS, SaaS, D2C, SLA, FBM, FBA, ZEOS, MWS; available-to-promise defined at first use.
- timetoread changed from 25 to 30 min.

## 21 b2b-commerce
- WHY IT MATTERS rewritten from four sentences to two.
- Item 3: added that the ERP publishes wholesale and contract prices as price events to the OMS and B2B catalogs and feeds no channel directly; the recommendation and the De Kaap table now say "as price events".
- Figure 2: the over-limit amount is corrected from €1,520 to €1,184. The diagram shows contract prices (€6,384), and €9,800 + €6,384 is €16,184. The table's €1,520 "at list" is correct and stays.
- Acronyms and terms expanded: ERP, EDI, OMS, WMS, RFQ, OCI, cXML, Peppol, tenant, metafields, available-to-promise.
- timetoread changed from 25 to 30 min.

## 22 edi-and-e-invoicing
- Item 5: the mandate table's "Touches Kestrel & Pine?" cell for Belgium now says the customers' bookkeeping expects Peppol and that the obligation for a Dutch supplier is not settled. The newcomer reading uses the ruling's wording and notes the FAQ's "the law is still being amended on this point" (verified with WebFetch).
- Bergzicht worked example: removed "a Ridgewalker at €95 wholesale" as its contract price. The ledger leaves per-unit contract prices unfixed, and €95 is the list wholesale price.
- Belgian variant: changed "the same day" to "the same month", so the page stays compatible whichever way item 12 is ruled (Ghent, 21 April, versus Ardennes Trail Co., 6 April).
- Acronyms expanded: VAN, ASN (at the Chargeback's first mention), SSCC (forward gloss), VAT, SMEs, ViDA.
- Verified with WebFetch: the Netherlands plan (11 Sept 2026: 1 July 2030 invoicing, 1 July 2031 reporting, bill before summer 2027) and Peppol BIS 3.0.21 (published 20 May 2026, mandatory 17 Aug 2026).
- timetoread changed from 25 to 28 min.

## 23 erp-and-back-office-integration
- Item 3: "feeds no channel" becomes "feeds no channel directly", with the price, terms and credit events spelled out (Setting the scene, Figure 1 edge and caption, Figure 2 caption, synthesis). The master-data table splits prices to match the pricing-architecture ledger line: wholesale and contract prices are owned by the ERP and published as events; consumer prices are owned by the platform's market price lists.
- Item 1: the shipments row no longer says the shipment "triggers revenue recognition". Revenue is recognized at delivery, and Eva's revenue is now "recognized at delivery on 15 April".
- Price Drift in "When It Goes Wrong": the page no longer blames a partner mapping change. It now follows the ledger: one failed push was reported as a success, and the storefront sold at €179 for nine days.
- Batch-window example: "Black Friday's 31,000" changed to "11,500 (31,000 in the week)".
- Acronyms expanded: WMS and OMS in KEY POINTS, VAT, Peppol, MDM/PLM, INVOIC; dunning defined.
- timetoread changed from 25 to 28 min.

## Open issues for other reviewers or the author
1. **ASN Chargeback mechanism conflict.** The edi-and-e-invoicing ledger line says the ERP generated the DESADV at release with ERP pallet numbers, while the WMS printed its own labels. The journey-wholesale-order line says the consultant's mapping assumed one product group per pallet after a guideline revision. Chapter 22 follows its own (owning) line. The Part IX reviewer should align journey 39. Recorded in the ledger.
2. **Item 12 (Belgian Peppol customer)** is still OPEN. Chapter 22's Belgian variant is unnamed and dated only "the same month"; once the ruling exists, it can name the customer.
3. **Bergzicht EDI orders under the OMS.** Chapter 22 creates the 6 April 2027 order in the ERP ("OMS not live until Q4 2027"), which is consistent with item 4's seam dates. The journey-wholesale-order ledger line has the OMS keying EDI creation in April. That is for the Part IX reviewer.
4. **Part intro length.** Every part intro is above the style guide's 500–800 words. The author should either relax the guide or trim all intros together.
