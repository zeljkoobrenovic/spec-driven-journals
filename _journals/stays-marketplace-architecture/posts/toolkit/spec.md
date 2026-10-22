---
status: accepted
revised: 2026-10-22
---

# Spec: Field Kit: Templates for the Stays Architect

## Intent

Give the reader a set of practical, copyable templates for the records a Chief Architect keeps when one group runs an accommodation marketplace and a hosted-stays marketplace. Each template comes from the chapter that teaches it, keeps that chapter's terms and fields, carries a **hotel column and a home column wherever the two marketplace types differ** (and says so where they do not), and is filled in once with a short Corvane example whose numbers, names and dates match the owning chapter and the scenario ledger. A reader should be able to start from the design or decision on their desk, copy one record, see which fields carry ownership, versions, clocks and money, and know which mistakes make the record useless.

Productscape domains covered: none directly. The page is the working form of decisions taught across Parts I–IX; the brick-by-brick mapping lives in [[domain-coverage]].

## Audience

Group and enterprise architects of travel groups, principal engineers, and the leads of supply and connectivity, availability, checkout and reservations, payments and finance engineering, tax, trust and safety, regulatory affairs and reliability. Product, finance and regulatory leaders use Tools 1, 7, 8, 9, 11 and 13 as discussion documents.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; three KEY POINTS; three failure patterns with exact names; `<br>`; a lead on how to use the templates; a table of contents (Tool | Use it when | Chapter).
- [x] Contains the fourteen templates in the PLAN contract, each as a `## Tool N` section with purpose, "use it when", a copyable table or fill-in block, a Corvane example, common mistakes and a Learn more `[[link]]` to the owning chapter.
- [x] Ten or more templates carry a hotel-versus-home column or table; the ADR states that its form is the same for both and requires a hotels-and-homes section.
- [x] Corvane examples use ledger and chapter figures exactly: 16/6/26 and 23/6/20 map totals; Miradouro's 37 plans / 168 products → 17 / 74 and €137.60; Carmen's 730 rows and €1,360 Feria stay; Switchyard's ±60% sibling band, 07:14:03 hold against €141, 4-hour expiry, 10-minute delivery escalation; Pricegrid's 3.2 billion hot cells, 532 cells, 45 s lag, 91.4% → 95.8%; the checkout attempt contract (30 s / 35 s / 5 min / 30 min) and the 212 duplicates; Stayline's clocks and Miradouro's July 2027 failures; `NKW-MODERATE v3` and the €340 / €220 strike example; the Novak funds flow (€1,271.20, €1,041.60, €141.13, €32.47, €56, 171 days); Lisbon tourist tax via Levy; the Turia replay (16:24 receipts, €31,640 of €48,540, 1,140 → 310); `es-and-vut-v3` and the 3,180 / 2,480 / 1,240 replay; December 2027 journey SLOs and Black Friday D2; the boutique-hotel pilot and Clause grade change; Clause as the ADR example.
- [x] One diagram (illustrated) shows how the records reference each other, and one draws the funds-flow example; cross-links use only valid permalinks.
- [x] Short Sources and Evidence section with dated sources and the closing fictional-Corvane sentence; article under about 9,000 words, tables dominating.

## Non-goals

- Re-teaching the reasoning behind each template; each tool summarizes and links to its chapter.
- The context map ([[stays-bounded-contexts]]), event catalog ([[event-driven-stays]]) and metric definitions ([[marketplace-intelligence]]), which are linked, not reproduced.
- Definitions of terms ([[glossary]]) and the source list by topic ([[bibliography]]).
- Downloadable file formats (spreadsheets, document templates).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[organizing-stays-engineering]] was written in parallel; Tool 14 was aligned with its three decision classes (T, C, G) and mandatory reviewers. Its example uses the Clause decision recorded in [[changes-and-cancellations]] and [[converging-two-marketplaces]], taken before the class split; confirm the class wording if that chapter later classifies Clause.
- The off-platform payment policy in Tool 10 has no canonical identifier in [[stays-trust-and-safety]]; the card names it descriptively. If that chapter or [[travel-fraud]] later assigns policy IDs, use them here.
- The Lisbon child-exemption age (under 13 in the ledger) is flagged in [[taxes-on-stays]] for verification against the municipal regulation; Tool 9 repeats that caveat.

## Decision log

- **2026-10-21** — Chose the fourteen templates in the PLAN contract and no others; ordered them by the book's parts so a reader can move between a tool and its chapter in reading order, with the convergence card and ADR last because they cite the others.
- **2026-10-21** — Added a hotel-versus-home table to each template where the two types differ, rather than a separate comparison section, so the difference sits next to the field it changes.
- **2026-10-21** — Used fenced blocks only where the record is a literal artifact (connectivity contract, trust card, convergence card, ADR) and tables elsewhere; drew the funds-flow example as a mermaid figure because the template is itself a diagram.
- **2026-10-21** — Chose the Clause decision as the ADR example because it supersedes part of Context Map v1, which shows the "supersede, do not edit" rule on a real Corvane record.

## Sources

- **Internal**
  - [[stays-capability-map]], [[converging-two-marketplaces]] — scores, grades, map v1 and v2, placement tests, cross-type routing.
  - [[rates-and-availability-model]], [[connectivity-and-channel-managers]], [[calendar-sync]], [[availability-engine]] — ARI model, Switchyard contract, Calendar Sync v2, Pricegrid design and metrics.
  - [[checkout-orchestration]], [[reservation-lifecycle]], [[changes-and-cancellations]] — attempt contract, Stayline clocks and delivery states, Clause and Disruption Policy v1.
  - [[merchant-and-agency-models]], [[taxes-on-stays]] — arrangement record, three-arrangement example, Levy and the Novak ledger entries.
  - [[stays-trust-and-safety]], [[stays-regulation]], [[global-scale-and-reliability]] — Warden and the Turia replay, Ordinance and the Spanish replay, journey SLOs and Black Friday.
- **External**
  - Regulation (EU) 2024/1028; Regulation (EU) 2022/2065; Regulation (EU) 2019/1150; Council Directives (EU) 2025/516 and 2021/514.
  - Google, *The Site Reliability Workbook* (2018); Booking.com Reservations API and Expedia Rapid cancellation-policy documentation (n.d.); Stripe idempotent requests (n.d.).
  - Michael Nygard, *Documenting Architecture Decisions* (2011); Andrew Harmel-Law, *Scaling the Practice of Architecture, Conversationally* (2021); DDD Crew, *Core Domain Charts* (n.d.).
  - The LISTED toolkit — page format and tool structure.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Lisbon under-13 child exemption marked as a Corvane assumption and the €4 rate hedged as of 2026; removed an unsupported 7-day first-price check from the Switchyard example; American spelling (program, canceled). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 4,885 → 4,630 prose words; lead conventions list folded into two paragraphs (the identifier and hotel-and-home conventions repeated the KEY POINTS); Tool 1 and Tool 2 purposes no longer repeat their template fields; duplicate map-totals paragraph in Tool 13 and duplicate leg-field line in Tool 8 removed; "Using the Toolkit Over Time" cut to the review calendar (incident list repeated KEY POINTS). Spec: map v2 totals corrected to 23/6/20 per the scenario ledger. *(AI-mediated session)*
- **2026-10-22** — Fixed a cross-reference: the sharing rule is Figure 5 of stays-capability-map. *(AI-mediated session)*
- **2026-10-22** — Verified Lisbon tourist tax / Portuguese VAT against official sources. *(AI-mediated session)*

- **2026-10-22** — Removed the first-price check from Tool 3's guards (author decision, matches chapter 08). *(AI-mediated session)*
