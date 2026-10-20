---
status: accepted
revised: 2026-10-18
---

# Spec: Recover Before the Close: Resilience and Security for Finance

## Intent

Show a Chief Architect how to make finance systems resilient and secure, including at period end, by redesigning resilience around correctness rather than availability. The chapter ties criticality tiers and recovery objectives to money movement and the close calendar, defines business observability (money in flight, control totals as telemetry, SLOs versus invariants), explains why a database restore is the last resort for financial data, and introduces the financial incident with a playbook that corrects by entries and proves by reconciliation. It reads DORA at architecture level for Northmere Payments B.V. and covers finance-specific security concisely, building on the baseline in [[controls-and-auditability]].

## Audience

Chief Architects, finance-systems and payments architects, SRE and platform leads who support finance, CISOs and controllers who own incident decisions. They know SRE, DR and observability vocabulary; they need the finance and regulatory consequences made concrete.

## Success criteria

- [x] Defines financial incident, RTO, RPO, error budget and business observability, and distinguishes availability failures from correctness failures in a table.
- [x] Gives a four-tier criticality scheme tied to money movement, regulated funds and the close, with calendar-based elevation, and an RPO/RTO table across Northmere systems that separates SaaS, RISE and self-run responsibilities and explains the RPO window as an interface problem.
- [x] Covers resilience patterns for money movement, including tax-engine fallback, multi-PSP failover (with the stored-card token limit) and payout pausing as decisions needing finance's consent.
- [x] Covers period-end peak engineering: capacity profiles, freeze windows, critical-path monitoring.
- [x] Includes a money-in-flight observability architecture diagram, a financial SLO table that separates budgeted SLOs from invariants, and alert routing to owners including a close duty controller.
- [x] Works the illustrative quarter-end 2027 incident (Adyen webhook delay plus SFP duplicate key, 186,240 lines, €41,372,618.40) with timeline, correcting entries, impact assessment and DORA classification, and shows a restore test with reconciliation as the pass criterion.
- [x] Presents the financial incident playbook as a table and an incident response flow diagram.
- [x] Reads DORA obligations (Arts 3, 11, 12, 17–19, 24–26, 28, 30; Delegated Regulation 2025/301 time limits) at architecture level, phrased carefully, with exit strategies limited to critical or important functions.

## Non-goals

- The ITGC and security baseline (identity, SoD, privileged access, secrets) — [[controls-and-auditability]].
- Ledger internals, the reversal job and subledger signals — [[designing-financial-ledgers]].
- Vendor exit plans, Data Act switching and dependency budgets — [[vendor-portfolio-strategy]].
- Settlement matching design — [[payments-to-ledger]], [[traceability-and-reconciliation]].
- Organizational design of incident ownership — [[organizing-for-architecture]].
- Legal interpretation of DORA or UK operational-resilience rules.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- UK operational-resilience rules for Northmere Payments UK Ltd are mentioned only in general terms; the FCA regime was not verified in this session.
- PCI SAQ eligibility wording for pages embedding PSP-hosted fields changed after v4.0; the chapter tells the reader to confirm the current text rather than naming an SAQ.
- Whether DNB would identify Northmere Payments B.V. for TLPT is left open deliberately.

## Decision log

- **2026-10-18** — Made the incident start at a Northmere-owned edge rate limit, so Adyen's documented retry behavior works as designed and no failure is attributed to a real vendor.
- **2026-10-18** — Chose a duplicate that is balance-sheet only and corrected before the GL summary and soft close, to show reversal without re-post and a "not major" DORA classification reached on documented reasoning.
- **2026-10-18** — Recorded RPO/RTO figures as Northmere requirements with "per contract" for vendor commitments, rather than stating any vendor's DR service levels.
- **2026-10-18** — Treated completeness, clearing integrity and safeguarding as invariants without error budgets, and kept error budgets for timeliness only.

## Sources

- **Internal**
  - [[controls-and-auditability]] — security baseline, break-glass, evidence store, SFP remediation.
  - [[designing-financial-ledgers]] — reversal job, period states, money-in-flight signals, Lisbon rule table.
  - [[integration-architecture]] — delivery ledger, idempotency keys from business identity.
  - [[adyen]], [[payments-fundamentals]] — webhook consumer, concentration, token portability, PCI scope.
  - [[sap-s4hana]] — RISE shared responsibility.
- **External**
  - Regulation (EU) 2022/2554 (DORA) and Delegated Regulation (EU) 2025/301 on EUR-Lex; EIOPA DORA page.
  - Google SRE book (error budgets); Principles of Chaos Engineering; AWS DR whitepaper; OpenTelemetry.
  - Adyen webhook documentation; Stripe idempotency post; PCI SSC v4.0.1 announcement; ECB on verification of payee.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement/payout dates and chargeback references with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: Q4 2027 control-totals rule framed as a clause of STD-FIN-03 rather than a seventh standard; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Resilience, Observability, Security and Recovery for Finance Systems" to "Recover Before the Close: Resilience and Security for Finance" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
