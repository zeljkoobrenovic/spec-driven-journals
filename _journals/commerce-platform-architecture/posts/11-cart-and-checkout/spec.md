---
status: accepted
revised: 2026-11-07
---

# Spec: From Cart to Confirmation: Checkout Orchestration

## Intent

Teach a reader new to commerce what happens between "add to cart" and "order confirmed", and why checkout is the most protected part of a commerce platform. The chapter separates three things newcomers blur (the cart as a draft, the checkout as a clocked orchestration, the order as the resulting record), lists what checkout must call and how fresh each answer must be, explains the two rules that keep orders from being lost or duplicated when the shopper leaves for the bank's app (create the order exactly once with an idempotency key; treat the PSP's webhook as external truth), compares four ways to run a checkout, and reads Shopify's 2023–2026 withdrawal of editable checkout templates and scripts as the dated case for why platforms sandbox checkout. Eva's checkout at Kestrel & Pine, step by step with every system called, is the worked example. After reading, the reader can draw their own checkout's call sequence, say which answers come from copies, and judge an agency's proposal to customize checkout.

## Audience

Readers new to commerce architecture. The engineer or product manager who has just inherited a checkout (Noor Visser's position) benefits most; the ecommerce manager who asks for checkout changes and the finance lead who sees unpaid orders at month-end are the secondary readers. Terms explained on first use: cart, checkout, order, orchestration, PSP, webhook, idempotency key, 3-D Secure and strong customer authentication, express wallet, abandoned cart, conversion, PCI DSS and the self-assessment questionnaire, extension point, time budget, company account, contract price list, reverse charge, payment terms.

## Success criteria

- [x] The opener is one sentence under "IN THIS CHAPTER, YOU WILL", followed immediately by exactly three KEY POINTS, then the business and architect callouts and three failure patterns (The Phantom Stock, The Message in a Bottle, The Forked Platform) with chapter-specific reasons.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The business problem (abandonment, oversell, unpaid orders, card testing) comes before any component; every component is tied to a business consequence.
- [x] Contains: a cart/checkout/order contrast table, a step table of what checkout calls, a requirements table (freshness, consistency, latency, availability), a four-option trade-off table, the "Across Scale Stages: When It Fits and When It Limits" table with a judgement, three mermaid diagrams with captions (orchestration flowchart, order payment state diagram, Eva's checkout sequence), a "When It Goes Wrong" section with detection and recovery, "What to Take Away" in three tiers, Questions to Ask, and grouped Sources and Evidence.
- [x] Eva's checkout uses ledger facts only: 13 April 2027, 21:14, jacket €199 plus two pairs of socks at €18, €235 total, free shipping, iDEAL, order #1072455, delivery Thursday 15 April; the VAT split (€194.21 net, €40.79 VAT) is arithmetic on ledger prices at the NL 21% rate. The Black Friday Oversell (1,340 units, €96,000) and the Card-Testing Night (48,000 attempts, €2,900, 40 minutes) match the ledger.
- [x] Every company-specific claim is dated and sourced (Shopify changelog 2023-02-13, Shopify docs and help center accessed 2026-11, Shopify BFCM 2025 release, commercetools, Stripe and Mollie documentation accessed 2026-11, Baymard 2026 and 2024, PCI SSC 2025, Visa 2025); the one inference about Shopify's reasons is labeled "INFERENCE, NOT DOCUMENTED"; illustrative latencies, the conversion-point value and timings inside the checkout window are labeled as assumptions or illustrations.
- [x] Payments internals (authorization, capture, settlement, refunds, SCA detail) are left to [[commerce-payments]]; the order lifecycle to [[order-management]]; availability computation to [[inventory-and-availability]]; B2B objects to [[b2b-commerce]].
- [x] Length within the 6,500-word cap including tables; the three take-away tiers are present and honest.

## Non-goals

- How the PSP moves money, authorization windows in depth, 3-D Secure flows, refunds and disputes — [[commerce-payments]].
- The order state machine, order edits and the OMS — [[order-management]].
- Available-to-promise, reservations and the availability service — [[inventory-and-availability]].
- Promotion stacking and discount allocation — [[commerce-promotions]]; tax determination rules — [[tax-invoicing-and-ledger]].
- The delivery promise's data sources — [[shipping-and-delivery]].
- Company accounts, quotes, approvals, credit limits — [[b2b-commerce]].
- Extension mechanisms as a taxonomy and app governance — [[extensibility-and-app-ecosystems]]; API versioning — [[api-contracts-and-versioning]].
- Card testing, skimming and PCI scope in depth — [[commerce-security]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Shopify's 13 August 2024 date comes from the February 2023 changelog; the current developer page says only that in-checkout `checkout.liquid` is unsupported. A reviewer should confirm no later Shopify post changed the date.
- The chapter states (as an illustration) that Kestrel & Pine added two sanctioned checkout extensions in 2027; the ledger addition records this so [[extensibility-and-app-ecosystems]] and [[journey-consumer-order]] can reuse it.
- Whether Kestrel & Pine's platform creates the order before or after the iDEAL result is a reference-architecture choice the chapter makes for the example; it is recorded in the ledger addition so the journeys agree.

## Decision log

- **2026-11-07** — Used Shopify's checkout.liquid timeline rather than a survey of several vendors' extension models, because it is the only publicly dated sequence that shows a platform withdrawing checkout freedom step by step; other vendors appear only where their documentation states a mechanism (commercetools' two-second timeout).
- **2026-11-07** — Chose "create the order before the PSP's final answer, settle by webhook" as the recommended pattern, citing commercetools and Stripe, rather than presenting it as one option among equals, because iDEAL, Bancontact and 3-D Secure redirects make the asynchronous outcome the normal case for a European merchant; the take-aways say when the alternative is acceptable.
- **2026-11-07** — Kept the four checkout options at the level of "who runs the orchestration" rather than listing vendor products, to stay platform-neutral and to map the options onto the scale stages.
- **2026-11-07** — Treated B2B checkout in one section with four differences and a hand-off, rather than a parallel walkthrough of Bergzicht's order, which belongs to [[journey-wholesale-order]].

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Eva's order, the Oversell, the Card-Testing Night, the systems landscape, Waypoint W1, W2 and W4.
  - `_research/brief-checkout-payments-tax.md` — Part 1 (checkout as orchestration, Baymard, guest and wallets, the Shopify timeline), Part 4 (idempotency, webhooks, status models), Part 5 (PCI scope), Part 6 (card testing).
  - `_research/brief-shopify.md` — Part 4.1 (the checkout.liquid timeline table), 4.2 (Shop Pay), 4.5 (B2B payment terms), Part 5.2 (Functions limits).
  - `_research/brief-platform-engineering-scale.md` — Part 3.4 (extension points as named moments with time budgets), 5.4 (degradation).
  - `_research/brief-b2b-edi-erp.md` — Part 1 (company accounts, payment terms), Part 4.2 (Business Central connector ownership advice).
  - [[meet-kestrel-and-pine]] — cast, systems and incidents; [[commerce-payments]], [[order-management]], [[inventory-and-availability]] — neighbouring contracts.
- **External**
  - Shopify changelog (2023), developer documentation and help center (accessed 2026-11) — the checkout extensibility timeline, Functions limits, plan gating, Shop Pay share.
  - commercetools, Stripe and Mollie documentation (accessed 2026-11) — order-before-outcome flow, webhook guarantees, idempotency, session expiry.
  - Baymard Institute (2026, 2024) — abandonment rate and reasons, form-field benchmark.
  - PCI Security Standards Council (2025), Visa (2025), Regulation (EU) 2018/389 — payment-page scripts, enumeration monitoring, SCA.
  - Apple and Google developer documentation (accessed 2026-11) — express wallet flows.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Eva's delivery promise corrected to the static Wednesday 14 April (delivered a day late); VAT, iDEAL and ERP defined at first use; OMS seam date 13 October 2027. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
