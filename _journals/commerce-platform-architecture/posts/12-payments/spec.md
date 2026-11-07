---
status: accepted
revised: 2026-11-07
---

# Spec: Taking the Money: Payment Providers, Authorization, Capture and Refunds

## Intent

Answer contract 12 of PLAN.md for a reader new to commerce architecture: how does money move from the shopper to the merchant, and what can go wrong? The chapter names the parties behind a payment, explains the four stages (authorization, capture, settlement, payout) and the two backward flows (refund, chargeback), shows why the order must treat the payment service provider's webhook as external truth and keep its own small payment vocabulary, and makes one argument the whole book leans on: every action that moves money has one writer and one key. The Double Refund of January 2027 is the spine, told from the money side (chapter 18 tells it from the returns side). It covers payment methods by country with their different semantics, strong customer authentication and 3-D Secure, PCI DSS scope, basic fraud screening, the four ways to take payments, and the four payout feeds (online PSP, store terminals, marketplaces, wholesale receivables) that finance must reconcile. After reading, Noor Visser's stand-in can specify who may call the PSP, what key each call carries, and what the daily reconciliation compares.

## Audience

Readers new to commerce architecture. The engineer or product manager who must integrate a returns portal, an OMS or a checkout with a PSP benefits most; finance and operations leaders who need to understand why a refund is not an undo and why payouts never equal sales benefit next. Assumes general software literacy; defines PSP, issuer, acquirer, scheme, authorization, capture, settlement, payout, webhook, idempotency key, SCA, 3-D Secure, liability shift, merchant-initiated transaction, interchange, chargeback, PCI DSS, SAQ, hosted fields and receivable on first use.

## Success criteria

- [x] Opens with the exact callouts in order (IN THIS CHAPTER, YOU WILL; three KEY POINTS; one two-sentence WHY IT MATTERS; FAILURE PATTERNS with The Boomerang, The Message in a Bottle and The Lynchpin), then the lead and the "Where we are in the order's journey" paragraph placing the chapter at 21:13 on 13 April 2027 and at the refund variant on 22 April.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] A parties table, a four-stage table, a methods-by-country table with dated evidence, a requirements table (freshness, consistency, speed, availability) for the five order–PSP flows, a trade-off table for the four ways to take payments, and the "Across Scale Stages: When It Fits and When It Limits" table with Starting, Growing, Omnichannel and Group.
- [x] Three mermaid diagrams with captions: the four-stage money flow, the order's payment state vocabulary, and the Double Refund as a sequence showing two writers and no shared key.
- [x] Kestrel & Pine worked examples with ledger numbers: the Double Refund (212 returns, €19,400, January 2027), the Card-Testing Night (48,000 attempts, €2,900, 40 minutes), Eva's €235 iDEAL payment (#1072455, 21:13–21:14 on 13 April, paid out 15 April as an assumption), the €199 refund variant with the return id as key, Bergzicht's invoice due 9 May; Waypoint W5 explained without change.
- [x] Every company-specific claim carries a source and a year; PSP documentation pages are marked n.d., accessed November 2026; PSD3/PSR is stated as not yet in the Official Journal as of 7 November 2026; illustrative fees, payout timing and the Double Refund's day-by-day mechanism are labeled assumptions or illustrations.
- [x] "When It Goes Wrong" covers the duplicate refund, the lost outcome, the expired authorization and the provider outage, each with detection and recovery.
- [x] "What to Take Away" has the three tiers; "Questions to Ask" has 7 questions; the closing paragraph hands off to [[order-management]]; Sources and Evidence is grouped and ends with the fictional-merchant line.
- [x] Article at or under 6,500 words including tables.

## Non-goals

- The cart, checkout steps, the authentication detour inside checkout and creating the order before the PSP's answer — [[cart-and-checkout]] owns them; this chapter starts at the payment request.
- VAT, the invoice, the credit note, revenue recognition and what the ERP posts — [[tax-invoicing-and-ledger]].
- Returns policy, RMAs, inspection, dispositions and refund timing from the returns side — [[returns-and-exchanges]]; this chapter only fixes the refund's writer and key.
- Card testing defenses in depth, account takeover, skimming and the shared-responsibility model — [[commerce-security]]; fraud scoring — [[fraud-prevention]] in LISTED.
- Interchange economics, payment orchestration, tokens and the payments sub-ledger in depth — [[payments-fundamentals]], [[adyen]], [[stripe]], [[payments-to-ledger]] and [[designing-financial-ledgers]] in RECONCILED; the chapter links rather than re-teaches.
- Terminal selection and store refunds — [[stores-and-omnichannel]]; credit limits and payment terms — [[b2b-commerce]]; marketplace payouts — [[marketplaces-and-channel-integration]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Double Refund's day-by-day mechanism (support refunding in the PSP console in response to "where is my refund" contacts between carrier delivery and inspection) is appended to the ledger as an illustration; [[returns-and-exchanges]] and [[journey-return-and-exchange]] should reuse it rather than invent a different trigger.
- Kestrel & Pine's PSP fees and payout schedule are assumptions modeled on Adyen's public documentation; if a later chapter needs exact fee lines, they should be added to the ledger once.
- Whether iDEAL's transition to Wero changes refund or session semantics for merchants is not documented on the scheme's site as of November 2026; revisit before the 2027 edition.
- PSD3/PSR adoption and application dates should be re-checked against the Official Journal before publication.

## Decision log

- **2026-11-07** — Made "one writer, one key" and the webhook-as-external-truth rule the spine, rather than a tour of PSP products, because the newcomer's decisions are about who may call the PSP and how the order learns the result; Adyen, Stripe and Mollie documentation were chosen as evidence because they publish precise, quotable semantics, not as recommendations.
- **2026-11-07** — Told the Double Refund from the money side with a sequence diagram and left the returns-side fix (one refund path, refund on inspection) to chapter 18, to avoid two chapters teaching the same scene.
- **2026-11-07** — Kept SCA, PCI DSS and fraud to what shapes the architecture (the detour, the liability flag, SAQ scope, the kill switch) and linked chapter 34 and RECONCILED for depth; rejected a full PCI requirements walkthrough as outside a newcomer's altitude.
- **2026-11-07** — Added the "four feeds" section (stores, wholesale, marketplaces, online) so the chapter explains why Waypoint's W5 makes finance a daily batch, rather than leaving payouts to chapter 14 alone.

## Sources

- **Internal**
  - `PLAN.md` contract 12 and the neighbouring contracts 11, 13, 14, 18, 34.
  - `_research/scenario-ledger.md` — the PSP and terminal provider, the Double Refund, the Card-Testing Night, Eva's jacket, Bergzicht's reorder, Waypoint W5.
  - `_research/brief-checkout-payments-tax.md` — Parts 2 to 6: PSP stages, methods by country, SCA and PSD3, idempotency and webhooks, PCI DSS, fraud basics.
  - `_research/brief-security-privacy-regulation.md` — PCI scope and shared responsibility, PSD2/PSD3 status.
  - `_research/brief-shopify.md` — Shopify Payments as orchestration over licensed PSPs.
  - [[meet-kestrel-and-pine]], [[cart-and-checkout]], [[events-consistency-and-reconciliation]], [[erp-and-back-office-integration]], [[stores-and-omnichannel]], [[journey-consumer-order]].
- **External**
  - Adyen, Stripe and Mollie developer documentation, n.d., accessed 2026-11 — authorization and capture windows, refunds, disputes, webhooks, idempotency, payouts, PCI guides, card testing.
  - Shopify payment terms, processor list and Form 10-K for fiscal 2025 (2026-02-11) — a platform's payments as a wrapper over PSPs.
  - Dutch Payments Association (2025-02-18), Bancontact Payconiq Company (2025-02-12), EHI via Ecommerce News (2024), ECB SPACE 2024 — method usage by country.
  - Directive (EU) 2015/2366, Delegated Regulation (EU) 2018/389, Regulation (EU) 2015/751, Regulation (EU) 2024/886, European Parliament press release (2025-11-21), Council state of play (2026-10-29) — the regulatory frame and its dates.
  - PCI Security Standards Council (2024-06-11, 2025-01-30), EMVCo (n.d.), Visa VAMP fact sheet (2025-05) — card-industry rules and thresholds.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: added the missing author's-synthesis tier; Double Refund diagram no longer reuses Eva's order number; Stripe authorization window wording corrected (customer-initiated, not customer-present); iDEAL and 3-D Secure defined at first use; timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
