---
status: accepted
revised: 2026-10-20
---

# Spec: Adyen: One Platform from Checkout to Settlement

## Intent

Explain what is architecturally distinctive about Adyen (gateway, risk and acquiring on one platform, which gives one identity per payment and one concentration of risk) and show, concretely, how an enterprise connects it to finance: account structure mapped to legal entities and payout profiles, references propagated into canonical events and the ledger, an idempotent webhook consumer, report-driven postings that keep journal types and record types apart, and a worked reconciliation of one settlement batch to the bank credit. The reader should leave able to design, or challenge, an Adyen-to-ledger integration and to judge when to use Adyen's platform product and how to hedge dependence on it.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and payments-platform leads who already understand the payment lifecycle (from [[payments-fundamentals]]) and need to own an Adyen integration's finance consequences. Controllers and treasury leads are secondary readers for the posting design and batch reconciliation.

## Success criteria

- [ ] Reader can state the three architectural consequences of the single platform (end-to-end `pspReference`, fees reported by the settling party, concentration) and cite where each is documented.
- [ ] Reader can apply a rule for creating merchant accounts (entity, settlement currency and payout profile, payout model, regulatory perimeter) and explain why brand and business model travel as data; Northmere's three-account design is shown and justified, with rejected alternatives.
- [ ] Reader can distinguish settlement details report journal types from payment accounting report record types, and map each journal type to a canonical event and an illustrative posting (flagged as illustrative).
- [ ] Reader can design an idempotent webhook consumer that meets Adyen's documented contract (10-second acknowledgment, HMAC, duplicates on eventCode + pspReference, no ordering guarantee, 30-day retries) and a cut-off rule for late events.
- [ ] Batch 1047 reconciles arithmetically from settled lines, refund, chargeback and fees to the €1,380.52 bank credit, with a balanced journal; the Lisbon booking's €1.74 fee is decomposed and the €420 chargeback appears 40 days after its stay.
- [ ] The APM unmatched problem is diagnosed with causes that are design choices, not vendor defects.
- [ ] Balance Platform use versus paying partners yourself is decided with explicit criteria, linking Stayloft's payout design and Tablekin's Stripe Connect counter-example.
- [ ] Dependency risk (68% of transactions) has concrete hedges and links [[vendor-portfolio-strategy]].

## Non-goals

- Re-teaching the payment lifecycle, interchange++, chargebacks or merchant of record — [[payments-fundamentals]] owns them.
- The group-wide clearing-account design and three-way match across all providers — [[payments-to-ledger]].
- Stripe's object model and Connect — [[stripe]].
- Vendor tiering and exit-plan method in general — [[vendor-portfolio-strategy]].
- Partner payout engine design — [[custom-finance-platforms]].
- Adyen's commercial metrics, share price or internal architecture.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Adyen's supervisory arrangements (De Nederlandsche Bank / ECB) were not primary-verified; the article states only the 2017 European banking license. Verify before print.
- The Euronext Amsterdam listing date (13 June 2018) rests on a secondary source; confirm on Adyen's investor site.
- Whether the Fee journal is one line per transaction or aggregated per batch is not stated in the docs; the article avoids asserting either.
- The ledger's "settlement on 14 March 2027" falls on a Sunday; the article reads it as the Settled booking date with the bank credit on 16 March. Neighbouring chapters should agree.

## Decision log

- **2026-10-18** — Made the merchant account the central design object (unit of payout, report and clearing account) rather than describing account structure generically; rejected per-brand-and-country accounts as multiplying reconciliation for no accounting reason.
- **2026-10-18** — Chose reports as the source of money postings and webhooks as the source of state and in-flight postings; rejected webhook-only accounting because webhooks are at-least-once, unordered and can arrive up to 30 days late.
- **2026-10-18** — Used a miniature eight-line batch for the worked reconciliation instead of aggregate statistics, so every number can be checked by hand; included FX and a commercial card to show what the IFR caps do not cover.
- **2026-10-18** — Decomposed the ledger's illustrative €1.74 fee into interchange, scheme fees, markup on the Settled line and a processing fee on the Fee journal, to teach both fee channels.

## Sources

- **Internal**
  - [[payments-fundamentals]], [[payments-to-ledger]], [[stripe]], [[custom-finance-platforms]], [[vendor-portfolio-strategy]], [[integration-architecture]], [[controls-and-auditability]] — neighboring ownership and terms.
  - `_research/brief-payments.md` Part 2 and Part 4; `_research/scenario-ledger.md`.
- **External**
  - Adyen Docs: account structure, capture, webhooks (handle, troubleshoot), settlement details report, aggregate settlement details report, payment accounting report, getting paid, dispute flow, platform structure, Balance Platform accounting report, transfer webhooks, payout lifecycle, issuing, financial products.
  - Regulation (EU) 2015/751 (interchange caps); Directive (EU) 2015/2366 (safeguarding); Regulation (EU) 2022/2554 (DORA); Federal Reserve order of 24 May 2021.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: marked the batch 1047 chargeback as an earlier €420 dispute, distinct from the June 2027 chargeback in the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: aligned the €1.74 fee table with the canonical split (scheme €0.21, line markup €0.23, €0.10 batch fee as the rest of the €0.33 markup) and the batch 1047 expense postings; added the €598.26 canonical net; hedged the 2017 license date; dated the first exit test November 2027. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Adyen: Single-Platform Acquiring and Platform Payments" to "Adyen: One Platform from Checkout to Settlement" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,768 → 7,826 prose words (opening now ties the chapter to Part II, [[stripe]] and [[payments-to-ledger]]); 4 headings renamed; chargeback stages split into their own paragraph; buried topic sentences moved first; no facts cut. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
