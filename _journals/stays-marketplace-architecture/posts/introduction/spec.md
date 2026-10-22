---
status: accepted
revised: 2026-10-22
---

# Spec: Introduction: Architecture for a Perishable Promise

## Intent

Open BOOKED with its argument and its map. The page states the central idea, that **a stays marketplace sells a perishable promise (a specific night, in a specific place, at a specific price) that someone else fulfills**, and that its architecture is judged by how reliably five conditions hold from the search result to check-out: the night is available, the price holds, the booking reaches the property or host, the money reaches the right party, and guest and host can trust each other. It explains why the book compares the OTA-style accommodation marketplace and the hosted-stays marketplace instead of merging them, and introduces the three grades of sharing (shared engine, shared contract, brand-specific). It then gives the reader the means to use the book: the ten parts as a learning path, a routing table from 18 concrete decisions to chapters, the five kinds of statement, the provenance of the material, Corvane in one paragraph, what the book leaves out, and the living-journal note. After reading, an architect knows where to start and how to weigh what they read.

Productscape domains covered: none as a product brick; the page is a preface over both models (TAM and HSM) and points to [[domain-coverage]] for the brick-to-chapter map.

## Audience

Chief and enterprise architects of travel groups, principal and staff engineers, search, pricing, payments, data and ML leads, and product and engineering directors of OTAs, hosted-stays and vacation-rental marketplaces, channel managers and PMS vendors. They are architecture-literate and need the book's argument and a route to the chapter for the decision on their desk, not definitions of caches or event streams.

## Success criteria

- [x] Opens with the IN THIS SECTION / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE callouts and exactly three KEY POINTS, followed by a scene that poses an architecture question (a family at a front desk with no booking) without using Corvane.
- [x] States the perishable-promise argument with its five conditions and the two marketplace types, cites one dated fact for convergence, and gives the three grades of sharing in a table.
- [x] Summarizes all ten parts faithfully from their part introductions, in one table with each part's argument, plus one diagram (illustrated) with a caption that states the point.
- [x] Has a routing table of 12–18 decisions, each starting chapter checked against that chapter's KEY POINTS, using only valid permalinks (plus allowed sibling links `entity-resolution`, `payments-fundamentals`, `designing-financial-ledgers`).
- [x] Explains the five kinds of statement in a table, with dated examples of why company and regulatory claims carry dates (Expedia's 2024 earnings releases; Spain's 2024 registry decree and its 2026 annulment).
- [x] States provenance: two generic Productscape models (34 and 21 bricks, 55 in total, 12 overlapping), not descriptions of Booking.com or Airbnb, linked to [[domain-coverage]]; no internal material.
- [x] Describes Corvane in one paragraph consistent with the ledger and [[meet-corvane]], names the three deliberately excluded gaps from [[domain-coverage]], and ends with the living-journal note and a hand-off to [[where-stay-platforms-go-wrong]].
- [x] 3,000–4,500 words before Sources and Evidence (about 4,450 excluding figure markup).

## Non-goals

- The failure patterns in depth — [[where-stay-platforms-go-wrong]].
- Corvane's brands, volumes, systems and cast — [[meet-corvane]].
- The brick-by-brick coverage map and the reasons for each exclusion — [[domain-coverage]].
- The marketplace taxonomy, history and economics — [[two-stay-marketplaces]] and [[stays-marketplace-economics]]; the convergence decision itself — [[converging-two-marketplaces]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- `glossary` and `bibliography` do not exist yet in this book; until they do, the build resolves those links to another journal. They must resolve in-journal before publication.
- The routing table was checked against chapter KEY POINTS as of 2026-10-21; if a chapter's scope changes, its row must change with it.

## Decision log

- **2026-10-21** — Modeled on LISTED's `introduction` (scene, audience, argument, organization, routing table, evidence, provenance, running example, living journal), with callouts relabeled "IN THIS SECTION" to match the book's other preface pages, and without a failure-patterns callout, as in LISTED's introduction.
- **2026-10-21** — Merged the part summaries into the organization table (one-sentence argument per part) instead of LISTED's paragraph per part, to stay within the 4,500-word cap.
- **2026-10-21** — Added a "Two Marketplaces, Compared, Not Merged" section with the three grades of sharing, because the hotels-versus-homes comparison is this book's organizing idea and the reader needs it before the parts.
- **2026-10-21** — Opened with a generic front-desk scene (Lost at the Front Desk) rather than a Corvane scene, so the argument stands before the fictional group is introduced.

## Sources

- **Internal**
  - `PLAN.md` (Positioning, Provenance, Structure, Preface contract); `_research/style-guide.md`; `_research/scenario-ledger.md`.
  - Part introductions [[part-1]] to [[part-10]]; the KEY POINTS of chapters 1–51; [[domain-coverage]]; [[meet-corvane]]; [[toolkit]].
- **External**
  - Booking Holdings Form 10-K for fiscal 2025 (2026).
  - Expedia Group Q4 2023 and Q1 2024 earnings releases (2024).
  - Real Decreto 1312/2024, Boletín Oficial del Estado (2024, updated 2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: aligned the sharing-grades table with capability map v2 (cancellation policy is a shared engine; stay rules and payment arrangement are shared contracts), American spelling, timetoread. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 3,398 → 3,341 prose words; excerpt split into two sentences; one paragraph-closing recap of Parts IX–X cut (the organization table and Figure 2 carry it); hand-off and failure-pattern lead tightened; no headings changed. *(AI-mediated session)*
