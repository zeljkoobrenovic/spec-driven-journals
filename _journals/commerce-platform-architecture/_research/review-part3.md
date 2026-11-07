# Review log — Part III (ORDER)

Reviewer pass, 2026-11-07. Started fresh (the previous reviewer made no edits). Mid-pass the coordinator removed every WHY IT MATTERS callout by script; my two-sentence rewrites of that callout are therefore gone and the openers now run IN THIS … YOU WILL → KEY POINTS → FAILURE PATTERNS.

## Rulings made (recorded in consistency-issues.md as items 18 and 19, ledger [editor-review] line appended)

- **Item 8, invoice per shipment vs per order:** per shipment, at dispatch, idempotent on the shipment id, each invoice carrying the one order number; wholesale invoiced per delivery. Matches chapters 22, 37, 39 already.
- **Item 12, Belgian Peppol customer:** Ardennes Trail Co., Namur; 40 Ridgewalker jackets × €95 = €3,800; ordered via B2B portal Wed 21 April 2027; shipped by bpost and invoiced over Peppol 23 April; due 23 May; earlier BT-10 rejection kept. Namur chosen over Ghent to keep journey 39's location and avoid confusion with chapter 35's "Request From Ghent".
- Items 1, 2, 4, 14 and 17 applied (see per page).

## Per page

**part-3-intro** (1,416 → 1,337 words; the drop is the coordinator's callout removal)
- Ardennes Trail Co. replaces "the Belgian wholesale customer in Ghent"; invoice "at dispatch of each shipment"; timetoread 4 → 6.
- Note for author: the intro is 1,337 words against the 500–800 target for part intros; not trimmed (brief trims only above 7,000).

**11-cart-and-checkout** (6,526 → 6,475)
- Eva's delivery promise fixed: the delivery-date block renders the static rule as "delivered Wednesday 14 April"; the parcel arrived on Thursday 15 April, a day late (was "before 22:00 means Thursday 15 April", contradicting the ledger and chapters 37/45).
- VAT, iDEAL and ERP defined at first use; item 4: storefront orders reach the OMS from 13 October 2027.
- Verified: Shopify Scripts retired 30 June 2026 (Shopify Help Center).

**12-payments** (6,494 → 6,456)
- Added the missing "The author's synthesis." tier (two first-person bullets had sat under "Depends on context").
- Double Refund sequence diagram no longer uses Eva's #1072455 and an April return id (the incident was January 2027).
- Stripe authorization window: "customer present" → "customer-initiated online" (verified on Stripe's page; card-present windows are 2–5 days).
- iDEAL and 3-D Secure glossed at first use; missing blank line before the SCA heading; timetoread 24 → 28.

**13-order-management** (6,549 → 6,447)
- Item 8 applied in the requirements table, the #1052877 replay and the take-away bullet.
- Removed the internal "Research brief … prepared for this book" source entry (not a citable source).
- 2022 Shopify webhook figure flagged as more than three years old.
- Verified: Fluent Commerce split-logic quotes.

**14-tax-invoicing-and-ledger** (6,797 → 7,033 after the rulings → 6,485 after trimming → 6,420 after callout removal)
- Item 8: new "One invoice per shipment, not per order" paragraph; document table, failure modes, stage table and synthesis say "per shipment".
- Item 12: Ardennes Trail Co. throughout (scene, VAT section, e-invoicing, heading, worked example).
- Items 2/14: #1052877 *Not invoiced* = ERP waiting for the WMS "order complete" message a short pick prevented (was "nightly run failed"); the failure-pattern bullet and "invoice that never came" aligned.
- Item 1: revenue recognized at delivery (D2C) and at delivery to the customer's site (wholesale); dispatch invoice with a month-end cut-off adjustment; Eva = April revenue because delivered 15 April.
- Items 5/17: Belgian mandate scope for a supplier without Belgian establishment hedged as not settled.
- OSS sentence corrected (destination VAT applies above €10,000; OSS is the reporting simplification).
- Trims: lead restatement, repeated Double Refund retellings, Choices prose that duplicated its table, US tax-engine detail, unverifiable Avalara document-type claim (now stated as common practice), order-confirmation paragraph.
- Verified: Rijksoverheid 11 September 2026 announcement of e-invoicing from 1 July 2030.

**39-journey-wholesale-order** (item 12 only)
- Peppol variant now: two weeks later, Wed 21 April, 40 Ridgewalker jackets, €3,800, shipped by bpost and invoiced 23 April, due 23 May.

## Build and render

- Build: no errors (one transient OSError from a parallel build on another journal; rerun clean).
- Render check: part-3, cart-and-checkout, commerce-payments, order-management, tax-invoicing-and-ledger, journey-wholesale-order — all OK, 0 problems.

## Open issues for other parts / the author

- **Journey 39 (Part IX):** says a foreign supplier without a Belgian establishment "is not itself obliged" (citing the FAQ); item 17 asks for the hedge. Also its Peppol table, timing ("late 2027" architecture with April 2027 dates) not reviewed.
- **Chapter 22 (Part V):** "The Belgian variant. A Belgian retailer among the 210 Belgian accounts…" is unnamed; should become Ardennes Trail Co. with item 19's figures.
- **Chapter 28 ledger line** still says revenue "recognized at shipment"; item 1 says delivery (Part VI reviewer).
- **Journey 37:** check it shows two invoices for any split and the per-shipment wording (already "one invoice per shipment" in its table).
- The tax-invoicing-and-ledger ledger line (Ghent, nightly run) and the journey-wholesale-order line (30 fleeces) are superseded by the [editor-review] Part III line; ledger lines are append-only so they remain.
