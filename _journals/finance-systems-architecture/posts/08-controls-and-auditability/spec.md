---
status: accepted
revised: 2026-10-20
---

# Spec: Controls by Design, Not by Audit Season

## Intent

Make this the book's authoritative chapter on how controls and audit requirements shape finance architecture. The reader should leave able to speak the auditor's vocabulary precisely (ICFR, SOX 302/404, COSO 2013, AS 2201, key controls, application controls, ITGCs, IPE, SoD, SOC 1 Type II, CUECs) and, more importantly, to turn each term into a design decision. The spine is Northmere's FY2026 significant deficiency on the Stayloft Finance Platform payout engine, remediated as architecture (enforcing pipeline, SoD in deployment, payout rules as approved versioned data, access reviews, tamper-evident logging), not as sign-off paperwork. The chapter argues that the cheapest control evidence is a by-product of normal operation.

## Audience

Chief and enterprise architects, finance-systems and platform engineering leaders who build or own custom finance platforms or configure SaaS finance platforms, and who meet Internal Controls and the external auditor mainly when something has gone wrong. Secondary: heads of internal controls who need a shared language with engineering.

## Success criteria

- [x] Defines ICFR, material weakness vs significant deficiency, control taxonomy (preventive/detective, manual/automated/IT-dependent manual, entity/process/application/ITGC), the four ITGC domains, IPE and key reports, SoD and sensitive access, SOC 1 Type I/II, CUECs, CSOCs, bridge letters, evidence by design and CCM.
- [x] Explains the reliance chain (ITGCs make automated controls and reports reliable) with a diagram, and applies it to the SFP finding.
- [x] Shows the SFP remediation as five architectural parts, with a rule lifecycle diagram, a sequence diagram, an end-to-end architecture diagram and a dated remediation plan that leaves time to test before 31 December 2027.
- [x] Works the Lisbon booking (€600, 15% commission, €510 payout) through an unapproved 12% override to show why rule approval is a revenue control.
- [x] Includes a cross-system SoD table spanning SAP, Workday, Oracle, Stripe, OneStream, Coupa, Kyriba and SFP, with engineering rights treated as sensitive access.
- [x] Includes a SOC 1/CUEC table for BlackLine, OneStream, Workday, Stripe and Adyen, with only verified vendor assurance claims and explicit "not confirmed" where public sources were silent.
- [x] States Provision 29 accurately (dates, material controls, no change to auditor scope, comply-or-explain, not "UK SOX") and that no EU-wide SOX exists.
- [x] Covers the security baseline, data residency (transfers, not location) and GDPR Art. 17(3) vs statutory retention with a ledger-pseudonymization pattern; includes a trade-off table, Chief Architect's view, questions to ask and sources.

## Non-goals

- Ledger internals (immutability mechanics, posting rules, bi-temporality): [[designing-financial-ledgers]].
- Reconciliation catalog and audit walkthrough design: [[traceability-and-reconciliation]], [[blackline]].
- Full security architecture, DORA, resilience and incident response: [[resilience-and-security]].
- Payments-to-ledger and safeguarding reconciliation: [[payments-to-ledger]].
- Agentic and AI controls in depth: [[ai-in-finance]].
- Accounting mechanics: [[accounting-for-architects]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- BlackLine's and OneStream's SOC 1 Type II scope could not be confirmed from public sources in October 2026; re-check before manuscript lock (web search budget ran out in the authoring session).
- AS 2201 wording is cited from general knowledge (PCAOB page returned HTTP 403); verify definitions against the standard text.
- SEC semiannual reporting proposal status (May 2026) is time-sensitive.

## Decision log

- **2026-10-18** — Anchored the chapter on one remediation worked in depth rather than a survey of control types; the remediation carries ITGCs, SoD, configuration-as-data and evidence by design in one story.
- **2026-10-18** — Made "population from the system of action" the decisive detail of change management, over the more common focus on approvals, because it is what makes evidence complete.
- **2026-10-18** — Treated Provision 29 in a short sub-section with a clear "Northmere is not subject" note, rather than a parallel UK track, to avoid implying a UK SOX regime.
- **2026-10-18** — Accepted ~8,900 words including tables (~6,800 prose) because the contract owns six terms and the brief asks for the authoritative controls chapter.

## Sources

- **Internal**
  - `_research/brief-accounting-controls-regulation.md` §3 and §5 — control vocabulary, SOC reports, Provision 29, retention, GDPR.
  - `_research/productscape-digest.md` §1.4 (access governance, control monitoring bricks) and §5.7 (SOX lead persona and KPIs).
  - `_research/scenario-ledger.md` — the FY2026 significant deficiency, cast, Lisbon booking.
- **External**
  - Workday, Stripe and Adyen trust/compliance pages (checked October 2026) — SOC 1 Type II / ISAE 3402 evidence.
  - FRC UK Corporate Governance Code page — Provision 29 dates and auditor scope.
  - GDPR Article 17 — erasure exceptions.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: five mandatory control requirements tied to STD-FIN-05 (SoD by design, mandatory 1 Apr 2027) and STD-FIN-06 agent control card (Q3 2027); acronyms PSP, ICT expanded. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Controls, Auditability and Security by Design" to "Controls by Design, Not by Audit Season" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,886 → 6,934 prose words; lead now states the chapter's place in Part I (builds on [[part-1]] and [[finance-data-architecture]], feeds the ledger, platform and AI chapters); 1 subheading renamed; SEC semiannual note moved to the 302 bullet; first sentences brought forward. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
