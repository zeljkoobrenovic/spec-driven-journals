---
status: accepted
revised: 2026-11-07
---

# Spec: Rules Turned Into Requirements: Consumer, Payment, Invoicing and Platform Regulation

> Working doc for chapter 36 of *ORDERED: Architecting Commerce Platforms*. Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Give a reader with no legal background a method for reading regulation as architecture: scope (role, size, place), the data requirement (a field, a history, a document, a clock), the system of record that owns it, the channels that show it, a test, and a date with an owner. The chapter's durable claims: most rules that reach a shop are data requirements, so they land in the PIM, the OMS, the price history and the ERP rather than in page templates; dates slip but scope does not, and transposition multiplies the calendar; a hosted platform absorbs some obligations and never all. The centerpiece is Kestrel & Pine's regulatory calendar for 2027, with application dates as of November 2026 from official sources, and the Long Fuse is the pattern it defeats. After reading, the reader can place their own company on the calendar and turn any row into a requirement card.

## Audience

Newcomers to commerce architecture. Benefits most: an engineering or product lead who receives regulatory demands through customers, marketplaces and auditors and wants one door instead of four; a finance or operations owner who will own calendar rows. Also useful to an architect deciding which Waypoint-style hubs regulation justifies.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (directive vs regulation, transposition, application date, right of withdrawal, prior price, GPSR, responsible person, DSA trader traceability, EAA and WCAG, SCA, verification of payee, e-invoice and Peppol, ViDA, EPR, ESPR and digital product passport, NIS2, AI Act Art. 50, Data Act switching, economic nexus, INFORM Act).
- [ ] The regulatory calendar is one table, as of November 2026, with an official source per row, the application date, what it requires of Kestrel & Pine, an owner and a status; every date matches the official text cited in Sources (Consumer Rights Directive, Omnibus, PSD2 RTS, Instant Payments, DSA, GPSR, EAA, Data Act, Belgium and Germany e-invoicing, ESPR, PPWR, AI Act and its Omnibus, NIS2 and the Dutch Cbw, CRA, ViDA, Dutch 2030 plan).
- [ ] The method is shown as a table (rule, data requirement, system of record, channels, test) and as a diagram; the Long Fuse has its own diagram and five evidence-backed lessons.
- [ ] The scene uses four real rules arriving through four doors at Kestrel & Pine (GPSR listing rejections, the accessibility audit, the refused Belgian PDF, the ESPR end-of-season decision), with ledger facts (310 employees, Peppol since January 2026, 39% of returns not resold as new, 1,200 new variants per season) and illustrative details labeled.
- [ ] The ESPR Article 25 scope (large enterprises from 19 July 2026, medium from 2030, micro and small exempt; "unsold" includes withdrawal returns) is stated from the verified text.
- [ ] A requirements table for the compliance data flows, a trade-off table across four ways to run compliance and the "Across Scale Stages" table are present; US contrasts are brief and sourced.
- [ ] The three take-away tiers are present and honest; Questions to Ask has 6–10 items; Sources are grouped with years.
- [ ] Article length between 4,000 and 6,500 words including tables (the calendar table is the largest single element).

## Non-goals

- GDPR, consent, cookies, retention, data subject requests, international transfers: [[privacy-and-customer-data]].
- PCI DSS and security controls: [[commerce-security]].
- The e-invoicing mandates in detail (formats, Peppol, clearance models): [[edi-and-e-invoicing]]; the invoice as a legal document and US sales tax mechanics: [[tax-invoicing-and-ledger]].
- The prior-price computation and price history design: [[pricing-architecture]]; review provenance: [[commerce-search-and-discovery]]; withdrawal mechanics in the returns flow: [[returns-and-exchanges]].
- The marketplace operator's obligations under the DSA: LISTED's [[marketplace-regulation]].
- AI Act implications for agents: [[ai-and-agentic-commerce]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The ESPR delegated act for textiles and the digital product passport timetable were not verified; the chapter labels "around 2027" as an assumption and tells the reader to check the Commission's working plan.
- Dutch and Belgian packaging registers (Verpact, Fost Plus) are mentioned as existing but not verified; only Germany's LUCID is sourced.
- Whether PSD3/PSR were formally adopted after the Council's 29 October 2026 note was not checked; the chapter says pending.
- Whether a Dutch company with a Belgian store counts as established in Belgium for the e-invoicing mandate is left to a tax adviser, consistent with chapter 22.
- The Digital Fairness Act and the Digital Omnibus (data) are listed as pending without dates because no adopted text existed at the research cut-off.

## Decision log

- **2026-11-07** — Chose "read a law as a requirement" (scope, data, system of record, channels, test, date, owner) as the spine and the 2027 calendar as the centerpiece, over a survey of instruments, so the reader leaves with a method and an artifact rather than a list.
- **2026-11-07** — Set the scene as four rules arriving through four doors in 2024–2026 instead of one incident, because the Long Fuse is a pattern of discovery, not a single failure.
- **2026-11-07** — Dropped the "Systems touched" column from the calendar after a length pass; the method table carries the mapping, and the calendar keeps date, rule, requirement, owner and status.
- **2026-11-07** — Kept the United States to one section as the contrast (tax by court decision, seller disclosure by statute, accessibility by lawsuit, privacy by opt-out) because Kestrel & Pine does not sell there.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the company's size, Peppol since January 2026, return figures, the cast.
  - [[edi-and-e-invoicing]] and [[tax-invoicing-and-ledger]] — the mandate calendar and the refused-PDF story from finance's side.
  - [[pricing-architecture]] — the prior-price Black Friday test.
  - [[commerce-security]] and [[privacy-and-customer-data]] — the other two trust chapters.
  - [[boundaries-and-systems-of-record]] — the entity–owner table the requirement cards attach to.
- **External**
  - Official Journal texts via the EU Publications Office: Directive 2011/83/EU; Directive (EU) 2019/2161; Directive (EU) 2015/2366 and Delegated Regulation (EU) 2018/389; Regulation (EU) 2024/886; Regulation (EU) 2022/2065; Regulation (EU) 2023/988; Regulation (EU) 2024/1781 (Article 25 and Annex VII verified 2026-11); Regulation (EU) 2025/40; Directive (EU) 2019/882; Directive (EU) 2022/2555; Regulation (EU) 2024/2847; Regulation (EU) 2024/1689 and Regulation (EU) 2026/1744; Regulation (EU) 2023/2854; Council Directive (EU) 2025/516; appeal C-703/25 P.
  - Council of the EU state-of-play note 15005/26 (2026-10-29); European Parliament press release (2025-11-21).
  - FPS Finance Belgium (2024-09-18, 2025-12-18, FAQ); Bundesministerium der Finanzen FAQ; Rijksoverheid (2026-07-07, 2026-09-11); Zentrale Stelle Verpackungsregister.
  - PCI Security Standards Council (2025-03-26); Cornell LII, *South Dakota v. Wayfair* (2018); FTC INFORM Act page and fake-reviews press release (2024-08-14); US DOJ ADA web rule; California AG, Sephora (2022-08-24); UsableNet (2025-12); IAPP (2025); Kelley Drye via JD Supra (2026-03-13).
  - Research briefs `_research/brief-security-privacy-regulation.md` (Parts 3 and 4) and `_research/brief-b2b-edi-erp.md` (Part 3).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: ESPR newsletter set to June 2026 to match the ledger, Belgian e-invoicing hedged (consistency item 5), WHY IT MATTERS rewritten, Eva's price claim corrected, acronyms expanded. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
