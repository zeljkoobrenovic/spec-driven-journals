---
status: accepted
revised: 2026-11-07
---

# Spec: The Way Back: Returns, Exchanges, Refunds and Reverse Logistics

## Intent

Answer contract 18 of PLAN.md for a reader new to commerce architecture: how does a return travel back through the systems, and how do you make sure the money, the stock and the books all agree? The chapter walks the nine steps of a return (request, eligibility, label, transit, receiving, inspection, disposition, settlement, stock), teaches the two-record model (the return that owns intent and money; the reverse fulfillment that owns work and stock, joined by the disposition), reads the EU 14-day right of withdrawal as data requirements with its article references and dates, lays out the four decisions (who runs the customer's side, which event releases the refund, which single system issues it, how exchanges work) with trade-off tables, covers marketplace and store returns as externally started events, and places it all across the four scale stages. Eva's exchange from M to L (19–22 April 2027) and the Double Refund from the returns side are the spine. After reading, Noor Visser's stand-in can write the returns integration contract: trigger, writer, key, restock rule, and the four dates per line.

## Audience

Readers new to commerce architecture. The engineer or product manager who must connect a returns portal, a warehouse and a payment provider benefits most; operations and finance leaders who need to understand why "refund on request" and "refund on inspection" are architecture decisions benefit next. Assumes general software literacy; defines return rate, bracketing, returns portal, RMA, reverse fulfillment, disposition, exchange, reverse logistics, right of withdrawal, idempotency key, credit note and availability service on first use.

## Success criteria

- [x] Opens with the exact callouts in order (IN THIS CHAPTER, YOU WILL; three KEY POINTS; one two-sentence WHY IT MATTERS; FAILURE PATTERNS with The Boomerang, Schrödinger's Order and The Phantom Stock), then the lead and the "Where we are in the order's journey" paragraph placing the chapter on 19–22 April 2027.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] A nine-step return table, a requirements table (freshness, consistency, speed, availability) for six return flows, a refund-trigger table with the legal position per trigger, a trade-off table for the four ways to run returns, and the "Across Scale Stages: When It Fits and When It Limits" table with Starting, Growing, Omnichannel and Group.
- [x] Two mermaid diagrams with captions (the six-system return loop and the return lifecycle as a state diagram with dispositions), plus Eva's exchange as a dated event table across systems.
- [x] The 14-day right of withdrawal quoted from Directive 2011/83/EU with Articles 6(1)(h)–(i), 9(1), 9(2)(b), 10, 13(1)–(3), 14(1)–(2) and 16, the adoption date (25 October 2011), the Official Journal date (22 November 2011) and the application date (13 June 2014), and read as four dates per order line.
- [x] Kestrel & Pine worked examples with ledger numbers: 72,000 return parcels, 24% item and 19% order return rate, 28% exchanges, 61% resold as new, the returns portal (€650/month + €0.95), the Double Refund (212, €19,400), Eva's exchange (#1072455, 19–22 April, return R-20270419-1), the refund variant (€199 by iDEAL transfer, credit note), the 190 jackets refunded at the wrong price (promotions ledger addition), Waypoint W1 and W5 explained without change.
- [x] Every company-specific claim carries a source and a year; vendor portal claims are marked n.d., accessed November 2026 and volatile; Coresight's 2023 survey is flagged as small and old; illustrative hours, bench staffing and the disposition split are labeled.
- [x] "When It Goes Wrong" covers the double refund, the refund without a return, the phantom restock, the return with no record, the exchange shipped before the return exists, the missed legal deadline and the three-system status, each with detection and recovery.
- [x] "What to Take Away" has the three tiers; "Questions to Ask" has 9 questions; the closing paragraph hands off to [[customer-service-and-notifications]]; Sources and Evidence is grouped and ends with the fictional-merchant line.
- [x] Article at or under 6,500 words including tables.

## Non-goals

- Refund mechanics at the PSP (asynchronous refunds, failed refunds, chargebacks, idempotency keys in depth) — [[commerce-payments]]; this chapter fixes only the trigger, the writer and the key.
- The credit note, VAT on returns and what the ERP posts — [[tax-invoicing-and-ledger]].
- Warehouse receiving, put-away and the fulfillment-order handshake — [[warehouse-and-fulfillment]]; this chapter uses the disposition as the warehouse's output.
- Return-in-store mechanics and the POS — [[stores-and-omnichannel]]; marketplace return feeds and fees — [[marketplaces-and-channel-integration]].
- The full consumer-law calendar (Omnibus price rules, accessibility, GPSR) — [[commerce-regulation]]; only the withdrawal right is treated here.
- Notifications and the status page for returns — [[customer-service-and-notifications]]; the step-by-step journey — [[journey-return-and-exchange]].
- Return fraud scoring in depth — [[fraud-prevention]] in LISTED.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter sets Kestrel & Pine's policy as free returns within 14 days of delivery in all three countries, refund on inspection, and exchanges as held orders released on a resellable disposition, and names Eva's return R-20270419-1; these are appended to the ledger so [[journey-return-and-exchange]] and [[customer-service-and-notifications]] reuse them.
- The illustrative disposition split beyond the ledger's 61% resold as new (27% resold after processing, 9% recycled or donated, 3% missing or wrong item) is appended to the ledger; a later chapter may want a cost per disposition.
- The directive is cited from the Publications Office consolidated text; a reviewer should confirm the quoted article wording against the current consolidated version before publication.
- Whether the Amazon prepaid-return mandate for all US seller-fulfilled returns took effect in February or December 2026 is unresolved in the brief and deliberately not stated.

## Decision log

- **2026-11-07** — Made the two-record model and the refund-trigger decision the spine, rather than a tour of returns portals, because the newcomer's costly mistake (the Double Refund) comes from an unchosen trigger and writer, not from the wrong vendor; Shopify's and commercetools' public models were chosen as evidence because they document the split explicitly.
- **2026-11-07** — Told the Double Refund from the returns side (what the agent saw, why the portal was late) and left the PSP-side mechanics to chapter 12, which carries the sequence diagram, to avoid duplicating the scene.
- **2026-11-07** — Quoted the directive's articles directly rather than paraphrasing, and added the adoption, publication and application dates, because the contract asks for official references and the clocks become data requirements only when the exact triggers are known.
- **2026-11-07** — Used a dated event table rather than a third mermaid sequence for Eva's exchange, keeping the state diagram and the system loop as the two structural figures and the table as the worked example; rejected a fourth diagram as repetition of chapter 12's refund sequence.

## Sources

- **Internal**
  - `PLAN.md` contract 18 and the neighbouring contracts 12, 13, 14, 15, 17, 19, 20, 36, 38.
  - `_research/scenario-ledger.md` — returns volumes and rates, the returns portal, the Double Refund, Eva's jacket and exchange, Waypoint W1 and W5, the promotions addition on refund amounts.
  - `_research/brief-inventory-fulfillment-returns.md` — Part 5: return rates, portals, the return data model, the 14-day right, marketplace returns; Part 2.1 for commercetools' return states.
  - `_research/brief-security-privacy-regulation.md` — Part 3.1 on the Consumer Rights Directive and its application date; refund abuse.
  - `_research/brief-checkout-payments-tax.md` — refund semantics referenced from chapter 12.
  - [[meet-kestrel-and-pine]], [[commerce-payments]], [[warehouse-and-fulfillment]], [[stores-and-omnichannel]], [[marketplaces-and-channel-integration]], [[events-consistency-and-reconciliation]], [[journey-of-an-order]].
- **External**
  - Shopify developer documentation (returns apps, reverse fulfillment order dispositions), n.d., accessed 2026-11 — the two-record model.
  - commercetools Orders API, n.d., accessed 2026-11 — return item states.
  - Directive 2011/83/EU, Official Journal 2011-11-22 — the right of withdrawal.
  - NRF with Appriss Retail (2023-12-22) and Happy Returns (2024-12-05, 2025-10-15); Coresight (2023-04-04) — return rates and economics.
  - Amazon seller guidance (2025-04-15); Zalando ZEOS announcement (2024-11-21) — marketplace returns.
  - Loop, Narvar, Returnista, Happy Returns vendor sites, n.d., accessed 2026-11 — the returns-portal category.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: post-Waypoint refund writer aligned with the journey ledger (OMS through the platform refund API), NRF 2025 figures marked as projections, iDEAL defined. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
