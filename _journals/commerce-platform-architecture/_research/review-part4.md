# Review log — Part IV (FULFILLMENT)

Editorial pass, 2026-11-07. Scope: `part-4`, `warehouse-and-fulfillment`, `shipping-and-delivery`, `stores-and-omnichannel`, `returns-and-exchanges`, `customer-service-and-notifications`. Consistency items applied: 2 (Three-Status Order mechanism; chapter 19 already agreed with chapter 13 and was kept that way), 5 (GKS is hospitality-only; chapter 17 already said so, and the GKS 2.0 date was verified). No Peppol or Belgian e-invoicing claims appear in Part IV.

## Word counts (body before Sources; none over 7,000, so nothing was trimmed)

| Page | Before | After | timetoread |
| --- | --- | --- | --- |
| part-4 | 1,566 | 1,594 | 5 → 7 min |
| warehouse-and-fulfillment | 6,810 | 6,797 | 26 → 30 min |
| shipping-and-delivery | 6,494 | 6,475 | 25 → 28 min |
| stores-and-omnichannel | 6,859 | 6,814 | 26 → 30 min |
| returns-and-exchanges | 6,462 | 6,485 | 24 → 28 min |
| customer-service-and-notifications | 6,820 | 6,788 | 26 → 30 min |

## Changes per page

**part-4**
- WHY IT MATTERS: "In one year" became "Within three months" (Nov 2026 – Jan 2027), and "37 collection promises in one month" became the ledger's "37 items … already sold".
- "last wave left at 21:00" became "released its last pick wave at 21:00" (the ledger has the wave released at 21:00 and PostNL collecting at 22:30).
- WMS and POS expanded, "disposition" defined in KEY POINTS, W6 rephrased without the undefined term "despatch advice"; "a dozen messages" became "a string of messages".

**warehouse-and-fulfillment**
- WHY IT MATTERS rewritten from three sentences to two (the four-hour stall and roughly 8,000 missed promises, plus the €14,200 ASN chargeback, then the decision).
- Figure 2 is introduced as the late-2027 OMS design using Eva's order. The text says the platform, not an OMS, sent her order in April 2027, so the diagram was inconsistent with the text.
- iDEAL defined; the 21:00 wave and 22:30 PostNL collection relabeled from "assumptions" to Kestrel & Pine illustrations (they are ledger lines).

**shipping-and-delivery**
- WHY IT MATTERS cut to two sentences.
- "last pick wave leaves at 21:00" corrected to "releases".
- "the ship date had already slipped to Monday" (Black Friday) became "slipped by at least a day", because no ledger fact supports Monday.
- ACM expanded.

**stores-and-omnichannel**
- WHY IT MATTERS cut from four sentences to two.
- SaaS defined; the RFID definition moved to its first use; PCI DSS and ELSTER expanded.
- The KassenSichV amendment is now dated precisely (14 January 2026, verified on gesetze-im-internet.de). The GKS 2.0 rule (new hospitality businesses from 1 July 2026) was verified.
- Source subheadings changed from bold to italic, per the style guide.

**returns-and-exchanges**
- The post-Waypoint refund writer is now "the OMS through the same platform refund API", which matches the `journey-return-and-exchange` ledger line. It previously said "OMS directly against the PSP"; Figure 1's edge label and caption were adjusted to match.
- NRF 2025 figures are marked as projected or estimated (verified on nrf.com). iDEAL is defined.

**customer-service-and-notifications**
- WHY IT MATTERS cut from five sentences to two.
- Three-Status tickets: "five channels" corrected to "three channels". The table and the ledger list only e-mail, chat and phone.
- Eva's table now uses ledger times:
  - label 08:40 and collection 22:30 (it said "afternoon, handed over");
  - delivered 11:20 (it said 13:40);
  - return received 10:15 (it said 10:20).
- WhatsApp pricing corrected after checking Meta's page. Utility messages inside the service window were free from 1 July 2025 and are charged again from 1 October 2026. The 1,000 free tier applies to service messages only.
- OMS, 3PL and SP-API expanded at first use; source subheadings changed to italic.

## Spot-checks (WebFetch)
- Meta WhatsApp pricing: the claim was partly wrong and has been corrected.
- KassenSichV (dated 26 Sept 2017, last amended 14 Jan 2026): confirmed.
- Belgian GKS 2.0 (new hospitality businesses from 1 July 2026): confirmed.
- NRF 2025 ($849.9B projected, 19.3%, 9% fraudulent): confirmed.

## Build and render check
- The build reports no errors. Its only warnings are for unwritten pages (introduction, toolkit, glossary, bibliography).
- `render_check.py` prints OK for all six pages, with 0 failed diagrams and 0 unresolved links.

## Open issues for other parts or the author
1. **Three-Status "Not invoiced" mechanism (Part III).** The `tax-invoicing-and-ledger` ledger line says the status came from "the ERP connector's nightly invoice run failing on that order without alerting". Consistency item 2 rules that the ERP invoices on a WMS "order complete" message. Chapter 14 should follow item 2.
2. **Duiven's last carrier collection (Part IX).** The `journey-consumer-order` ledger line computes the late-2027 promise from "the warehouse's last carrier collection (illustrative: 20:30 at Duiven)". The `warehouse-and-fulfillment` line has the final wave at 21:00 and PostNL collecting at 22:30. Journey 37 should base its promise on the 21:00 last wave (Eva's 21:14 order still ships Wednesday and arrives Thursday), or explain the 20:30 figure.
3. **Part intro length.** All part intros run 1,300–1,950 words against the style guide's 500–800; part-4 is 1,594. It was left as is, consistent with its siblings; the author may want a book-wide decision.
4. **Ch19 voucher.** The €10 voucher on 14 December is a *(local detail)*, not in the ledger; fine as it stands.
