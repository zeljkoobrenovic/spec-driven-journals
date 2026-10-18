---
status: accepted
revised: 2026-10-18
---

# Spec: From Customer Transaction to Financial Statement

## Intent

Open Part III by showing the finance estate as one system: one customer transaction followed from the operational event to the published 10-Q and 10-K, hop by hop. For each hop the reader should see the system, the record, the identifier carried, the invariant that must hold, the control that proves it, the timing (event date, accounting date, period, reporting date) and the consequence of a break. The chapter owns the **end-to-end financial event chain**. It turns the single-platform views of Part II into one chain table that an architect can reuse as a walkthrough template and as a test.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and controllers or internal-control leads who know the individual platforms (Part II) but have never had to prove the path between them. Secondary readers: finance-transformation leaders deciding where acquired brands should join the group's books.

## Success criteria

- [x] The Lisbon booking (€600, 12 Mar 2027; batch 1047 on Sun 14 Mar; bank credit Tue 16 Mar; stay completed 21 Apr; payout instructed 22 Apr and settled Mon 26 Apr) is traced through eleven hops, from the booking platform to FinDB, with the entity split (Stayloft B.V. and Northmere Payments B.V.), the intercompany entries, translation to USD, elimination and the Q1 and Q2 10-Q effects.
- [x] One table states, for every hop: system, record, identifier, invariant, control, timing and failure consequence.
- [x] A sequence diagram and a timeline diagram show the chain and its periods.
- [x] Amounts agree with the scenario ledger and with [[accounting-for-architects]], [[adyen]] and [[stripe]]; the corrected dates are used.
- [x] The Tablekin $1,029 invoice is traced as a contrasting, shorter chain (Stripe Billing → Workday → OneStream), and the Wayfare €84 rail ticket briefly (Fusion), with the architectural differences stated.
- [x] A trade-off table compares where a brand's chain joins the group (GL via subledger, consolidation only, accounting hub, per-transaction posting).
- [x] "What must hold true at every hop" is given as a checklist of invariants.
- [x] Northmere's 2027 breaks are listed by hop, each pointing to the chapter that fixes it; the chapter hands off to [[payments-to-ledger]].

## Non-goals

- The accounting of each entry and principal-versus-agent ([[accounting-for-architects]]).
- Posting-engine internals, period states and summarization design ([[designing-financial-ledgers]]).
- Matching rules and the €14 million suspense program ([[blackline]], [[payments-to-ledger]]).
- Consolidation mechanics in general ([[onestream]]); data platform and tie-out design ([[finance-data-flows]]).
- The reconciliation catalog and audit walkthrough design ([[traceability-and-reconciliation]]); authority per data element ([[systems-of-record]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Earlier chapters still show the pre-correction dates (settled 14 Mar, payout settled 24 Apr) and [[blackline]] uses a different batch number (412), merchant reference and bank date for the Lisbon match; an editorial pass should align them with the ledger and with [[adyen]] (batch 1047, credit 16 Mar).
- The illustrative IC++ split of the €1.74 differs between [[payments-fundamentals]] and [[adyen]]; this chapter uses the [[adyen]] split (commission €1.64 on the Settled line, €0.10 on the Fee line).
- Whether safeguarded cash is presented as restricted cash is left as a stated policy judgment.
- The 10-K deadline (60 days for large accelerated filers) was confirmed through practitioner summaries of SEC rules; re-check against the SEC's Form 10-K instructions before print.

## Decision log

- **2026-10-18** — Organized the chapter as eleven numbered hops plus one master table, rather than by platform, because the contract asks for the chain and the platforms are owned by Part II.
- **2026-10-18** — Used the three Adyen clearing accounts from [[adyen]] rather than [[accounting-for-architects]]'s single PSP clearing account, and said so, so the trace matches production design without contradicting the simplified teaching entries.
- **2026-10-18** — Chose illustrative USD rates (March average 1.0860, 31 March closing 1.0900, April average 1.0820 from [[accounting-for-architects]], 30 April closing 1.0840) and showed the funds-held roll-forward FX line, because translation is where a disclosure most visibly fails to foot.
- **2026-10-18** — Framed the trade-off as "where the brand's chain first meets a group-owned control", rather than repeating the convergence debate owned by [[multiple-erps]].

## Sources

- **Internal**
  - [[accounting-for-architects]], [[designing-financial-ledgers]], [[custom-finance-platforms]] — entries, engine, summarization and control totals.
  - [[adyen]], [[stripe]], [[payments-fundamentals]], [[blackline]], [[onestream]], [[oracle-fusion]], [[workday]], [[satellite-platforms]], [[finance-data-architecture]] — platform hops and Northmere facts.
  - `_research/productscape-digest.md` §2.1 and §3.4; `_research/scenario-ledger.md`.
- **External**
  - SEC, Form 10-Q filing deadlines; Deloitte DART Revenue Roadmap 15.2 (ASC 606 disaggregation); IAS 21; PSD2 Article 10; Adyen and Stripe reconciliation documentation; Fowler, "Bitemporal History".

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement/payout dates and chargeback references with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: joined a stray paragraph break, American spelling in Figure 1 and throughout; verified Lisbon dates, both €420 chargebacks and Wayfare agent treatment. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
