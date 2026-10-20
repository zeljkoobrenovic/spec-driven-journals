---
status: accepted
revised: 2026-10-20
---

# Spec: Payments for Finance Architects: Eleven Reasons the Numbers Disagree

## Intent

Give finance architects the payments knowledge they need before they connect payments to the ledger. The chapter treats a payment as a chain of separately timed events (authorization, authentication, capture, clearing, settlement, payout, refund, dispute) performed by parties who hold different money and bear different risks. It separates merchant of record from principal-versus-agent. It shows how pricing, payment methods, tokens, FX, marketplace models and regulation each change what the ledger must explain. It ends with eleven concrete reasons why provider payouts and bookings do not reconcile on their own, which is the bridge to Part III. After reading it, an architect should see that the reconciliation problem is designed upstream in payments choices and should know which of those choices to govern.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders. They know systems well but meet payments mainly as a settlement file. Secondary readers are controllers and payments product leads who need a shared vocabulary.

## Success criteria

- [ ] Reader can name each party in a card payment and say who holds the money, who bears which risk, and who is merchant of record (party table and Northmere flow table).
- [ ] Reader can trace the Lisbon €600 booking through every lifecycle step with dates, canonical events and the €1.74 fee (step table and sequence diagram), using ledger-consistent figures.
- [ ] Reader can explain the €420 chargeback lifecycle, including its timing across periods and the recovery from the partner, consistent with the accounting chapter's canonical dates.
- [ ] Reader can explain IC++ versus blended pricing, the EU interchange caps and their exclusions, and why fees need an accrual and a true-up.
- [ ] Reader can contrast APM semantics (capture, finality, disputes, settlement) and PSP versus network tokens, including portability.
- [ ] Reader knows the regulatory status as of October 2026: PSD2 SCA exemptions, PSD3/PSR not yet adopted, PCI DSS v4.0.1 scope logic, PSD2 Art. 10 and EMD Art. 7 safeguarding, the Instant Payments date for EMIs, and DORA.
- [ ] Reader can weigh single PSP, direct multi-PSP, third-party orchestrator and PSP-native orchestration (trade-off table), and knows that orchestration does not unify settlement.
- [ ] The "Eleven reasons payments do not reconcile themselves" section maps each reason to a documented mechanism and hands off to [[payments-to-ledger]].

## Non-goals

- Journal entries and the revenue-recognition judgment: owned by [[accounting-for-architects]].
- Adyen's account structure, reports and journal types in depth: owned by [[adyen]].
- Stripe's object model, Connect charge types and Billing: owned by [[stripe]].
- Clearing-account design, the three-way match and the suspense remediation: owned by [[payments-to-ledger]].
- Vendor tiering and exit planning: owned by [[vendor-portfolio-strategy]]. DORA operations: owned by [[resilience-and-security]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- PSD3/PSR: recheck adoption and Official Journal publication before print. The chapter states that it is not in force as of October 2026.
- The 14 March 2027 payout date in the ledger falls on a Sunday, two days after a Friday sale. The chapter labels it illustrative and notes the calendar effect. A ledger owner should decide whether to keep it.
- The dispute and return rules for Pix and UPI were not verified, so the chapter flags them as "verify per market".
- UK CASS 15 is cited from a secondary source, so confirm it against FCA PS25/12 before print.
- The PCI SAQ A eligibility wording has changed since v4.0.1; recheck it before print.

## Decision log

- **2026-10-18** — Built the chapter around two traced transactions (the €600 booking and the €420 chargeback) rather than a catalog of concepts, because timing and netting only become clear with dates. A generic "card payment" walkthrough was rejected.
- **2026-10-18** — Made "holds the money / bears the risk / merchant of record" the organizing frame for parties. The frame shows explicitly why Northmere is merchant of record yet an agent for revenue, in line with the editor's canonical policy note.
- **2026-10-18** — Aligned the €420 chargeback with the dates the accounting chapter recorded in the ledger (booked 2 Apr, stay 1–4 May, payout 7 May, chargeback 13 Jun, resolved 26 Jul), and chose the "lost" outcome. An earlier draft with different dates was discarded.
- **2026-10-18** — Named orchestration vendors only by their own self-descriptions, with Stripe Orchestration's documented limits. CellPoint Digital (unverified) and any vendor ranking were left out.

## Sources

- **Internal**
  - `_research/brief-payments.md` Parts 1 and 4, misconceptions and cautions — primary factual base.
  - `_research/productscape-digest.md` §1.2 and §6 — money-movement capabilities, "ledger-ready before launch", the settlement and chargeback concept.
  - `_research/brief-accounting-controls-regulation.md` §2.4, §4.7–4.9 — safeguarding, DORA, PSD3 themes.
  - [[meet-northmere]], [[accounting-for-architects]] — scenario and accounting alignment.
- **External**
  - Adyen and Stripe documentation (settlement and payout reports, capture, disputes, balance transactions, Connect, Orchestration).
  - EUR-Lex: Delegated Regulation 2018/389, Regulation 2015/751, Directive 2015/2366, Directive 2009/110/EC (Art. 7 fetched this session), Regulation 2024/886.
  - European Parliament Legislative Train and Matheson (April 2026) on PSD3/PSR status.
  - PCI SSC on v4.0.1 dates.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Added a one-sentence cross-reference to the new Part V case study [[case-uber-payments]]. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: split the €0.33 markup into €0.23 line-level and €0.10 batch-level fee (canonical €1.74 breakdown), corrected the settlement-report label in Figure 3, expanded NPCI, American spelling of license. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Payments for Finance Architects: The Lifecycle of Money Movement" to "Payments for Finance Architects: Eleven Reasons the Numbers Disagree" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 5 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,474 → 7,466 prose words; Tokens section moved next to Multiple Providers and Orchestration; lead now places the chapter in Part II and names the Part III hand-off; first sentences of the FX, PSD3/PSR, PCI DSS, instant-payments and eleven-reasons paragraphs now state their point; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
