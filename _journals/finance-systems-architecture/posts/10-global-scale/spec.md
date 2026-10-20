---
status: accepted
revised: 2026-10-20
---

# Spec: Global by Design: Entities, Currencies, Jurisdictions and Brands

## Intent

Show what operating across many legal entities, currencies, jurisdictions and brands demands of a finance architecture, and give the reader a model that turns these from close-week clean-up into governed data and designed flows. The chapter owns the **legal entity model**, **intercompany**, the **multi-currency model** and **multi-GAAP**, and previews indirect tax at platform scale, Pillar Two data needs and licensed-entity constraints. After reading, an architect should be able to separate brand, entity, market, business model and currency in their own estate, specify an intercompany flow end to end, and name who owns exchange rates and when they are applied.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders in multinational groups. They know systems well; they need the accounting, tax and regulatory consequences of entity and currency design made concrete, and the vendor differences (SAP, Oracle, Workday) compared at the level that matters for cross-ERP design.

## Success criteria

- [ ] The reader can explain why brand, legal entity, market, business model and currency are separate dimensions, with a table showing what breaks when two are conflated.
- [ ] The reader can compare how SAP S/4HANA (company code, leading and extension ledgers), Oracle Fusion (legal entity, balancing segment, primary and secondary ledgers) and Workday (company, book codes, intercompany profiles) represent an entity, with sourced claims.
- [ ] The reader can list the six things every intercompany flow needs and follow a worked royalty example through journal entries, consolidation (including an FX-driven elimination difference) and netting, with a currency flow diagram.
- [ ] The reader can distinguish transaction, settlement, functional and group currencies; commercial, provider and accounting rates; revaluation versus translation; and who owns each.
- [ ] The reader can describe the multi-GAAP patterns and why the leading-ledger standard is hard to reverse.
- [ ] The reader keeps accounting, tax (VAT/ViDA, DAC7, DST, US marketplace facilitator) and regulatory (safeguarding) treatments of one transaction separate.
- [ ] The reader can name the data Pillar Two needs and why it depends on the entity register and clean intercompany.
- [ ] Dates for ViDA, Pillar Two, e-invoicing and safeguarding carry their evidence status and "as of 2026" framing.

## Non-goals

- Accounting mechanics of double entry, revenue recognition and FX accounting in depth — [[accounting-for-architects]].
- Consolidation engine design and elimination mechanics — [[onestream]]; convergence of ERPs — [[multiple-erps]].
- E-invoicing/CTC and tax-engine architecture in depth — [[satellite-platforms]].
- The full market-launch kit and business-model templates — [[brands-entities-markets]] (Brazil is a preview only).
- Payment regulation and safeguarding mechanics — [[payments-fundamentals]].
- Build-versus-buy of the intercompany originator or rate service — [[build-versus-buy]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Brazil's indirect-tax reform transition rules and electronic fiscal document requirements were not verified for this edition; the Brazil table defers them to design-time verification and to [[brands-entities-markets]].
- Oracle Fusion Intercompany module detail and SAP intercompany app names were not verified; described at capability level.
- Northmere's ultimate parent jurisdiction (relevant to Pillar Two side-by-side relief) is not in the ledger; the chapter leaves it open.
- Body runs about 8,300 words including tables (about 6,200 of prose), above the Part I guide, because the contract spans entity, intercompany, currency, GAAP, local, tax, Pillar Two and licensed-entity topics. Candidate for a review trim.

## Decision log

- **2026-10-18** — Organized the chapter around five independent dimensions (entity, brand, market, model, currency) rather than around regulations, so new mandates read as data requirements on the same model.
- **2026-10-18** — Chose an intercompany royalty (Stayloft Inc. to Stayloft B.V., USD invoice, EUR functional) as the worked example over a Lisbon-booking variant, because it shows journal entries, translation-driven elimination differences and netting in one flow; the Lisbon booking is used for the rate-family and four-treatments tables instead.
- **2026-10-18** — Made the elimination difference the teaching point (a policy outcome, not an error) and recorded two acceptable designs instead of prescribing one.
- **2026-10-18** — Cut a first draft of about 12,000 words to about 8,300 by removing a rate-sourcing trade-off table, an entity-granularity table and duplicated failure modes.

## Sources

- **Internal**
  - [[meet-northmere]], scenario ledger — entity, currency and system facts.
  - [[accounting-for-architects]], [[onestream]], [[satellite-platforms]], [[brands-entities-markets]] — neighbors whose ownership this chapter respects.
- **External**
  - SAP Learning lessons on organizational units, ledgers and currency types; Oracle 26C ledger and legal-entity documentation; Workday Financial Management datasheet and consolidations guide — ERP entity models.
  - IFRS Foundation, IAS 21 — functional currency, translation.
  - European Commission ViDA page; VAT Directive Art. 226; PSD2 Art. 10; Irish Revenue Pillar Two dates — regulatory facts.
  - Big-4, law-firm and vendor summaries (BDO, EY, PwC, CMS, KPMG, Avalara, Vertex, Clifford Chance) — time-sensitive dates, marked as secondary.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: entity split aligned to 55 SAP company codes / 12 Fusion entities in 3 primary ledgers / 4 Workday companies; royalty example re-computed on the canonical March rates (1.0900 closing, 1.0860 average); multi-GAAP ledger facts aligned with sap-s4hana and oracle-fusion; Pillar Two parent wording aligned with the Dutch ultimate parent. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Many Entities, Currencies, Jurisdictions and Brands" to "Global by Design: Entities, Currencies, Jurisdictions and Brands" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,777 → 6,812 prose words (fact-dense chapter; gain is in structure and openings); lead now opens from [[integration-architecture]]'s pipes and names what Part II, [[brands-entities-markets]] and [[build-versus-buy]] take from this chapter; matching/netting and rate-ownership/rate-sources paragraphs split; topic sentences sharpened; no headings renamed, nothing deleted. *(AI-mediated session)*
