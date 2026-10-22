---
status: accepted
revised: 2026-10-22
---

# Spec: Domain Coverage: From Productscape Models to Chapters

## Intent

A Reference page that makes the book's planning auditable. It maps every root group, group and product brick of the two Productscape reference models (TAM, the OTA-style travel accommodations marketplace, 34 bricks; HSM, the hosted-stays marketplace, 21 bricks) to the chapters that cover it, marked *primary* (owns the brick's purpose and terms) or *also* (covers a module, uses it, or compares it). It reproduces the overlap matrix (12 same, 15 partial, 7 only TAM, 3 only HSM, consistent with [[stays-capability-map]]) with the chapter where each difference is argued, lists the seven [ADDED] domains with reasons and owners, places the other gaps from the digest's 27-row list, and names the three gaps the book deliberately leaves out, each with a reason. It ends with a short method for readers who start from their own capability map. After reading, a reader can find the chapter for any capability and tell whether a hotel-versus-home difference is real or an artifact of how a model was drawn.

Productscape domains covered: **all** bricks of both models, row by row (TAM `home`, `dest`, `srch`, `mapb`, `pers`, `deal`, `ssav`, `prop`, `room`, `book`, `acct`, `trip`, `msgc`, `self`, `reve`, `extr`, `onbo`, `cont`, `medi`, `invt`, `cald`, `rsrv`, `prom`, `rate`, `perf`, `rept`, `paym`, `sett`, `supp`, `trst`, `conn`, `mkli`, `geoa`, `idam`; HSM `insp`, `srch`, `list`, `wish`, `book`, `trip`, `grev`, `hono`, `lista`, `cala`, `pric`, `opco`, `coho`, `host`, `idvr`, `trst`, `paym`, `reso`, `comp`, `data`, `apix`), and the residuality stressors `licn`, `insv`, `fire`, `evac`, `coho`, `strd`, `midt`.

## Audience

Readers who arrive with their own capability map (enterprise architects, chief architects, product and engineering directors) and want to find the right chapter fast; reviewers checking that the book covers the domain; future writers extending the book.

## Success criteria

- [x] Provenance: both model paths, what they are (generic reference models) and are not (descriptions of Booking.com or Airbnb); KPI values illustrative and not quoted; brand-name leaks replaced with neutral terms.
- [x] Every one of the 55 bricks appears in a coverage table with its id, group, root group, a primary chapter and, where relevant, "also" chapters, all as valid `[[permalink]]` links.
- [x] States explicitly that no brick is uncovered, and notes the three with thin coverage (`apix`, `idvr`, `medi`) and why.
- [x] Overlap matrix with same / partial / only-TAM / only-HSM, counts matching [[stays-capability-map]], and the chapter where each difference is argued.
- [x] The seven [ADDED] domains, each with model traces, reason and owning chapter; the remaining digest gaps placed in chapters; three deliberate omissions with reasons.
- [x] A "How to Use This Map" section of five steps for readers starting from their own map.
- [x] Three KEY POINTS, one failure pattern, no Corvane scene; 3,000–6,000 words.

## Non-goals

- Re-arguing the capability map or the sharing rule ([[stays-capability-map]]), the context map ([[stays-bounded-contexts]]) or the convergence decision ([[converging-two-marketplaces]]).
- Company-specific claims; the chapters carry them with dated sources.
- Model KPI values, data catalogs, deployment replicas or value-stream details.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only.

## Open questions

- Chapters 42–51 were not yet written when this page was built; their rows rely on PLAN contracts. Re-check `demand-channels` (TAM `home`, `deal`, HSM `insp`, distribution) and `evolving-the-platform` (combined stressors) once those chapters exist.
- `rsrv` primary ownership is split between [[extranets-and-host-tools]] (work queue) and [[reservation-lifecycle]] (no-shows, exceptions); revisit if either chapter changes scope.

## Decision log

- **2026-10-21** — Primary vs also per brick, chosen by which chapter owns the brick's purpose; where modules split across chapters, the split is named in the cell.
- **2026-10-21** — [[stays-capability-map]] and [[stays-bounded-contexts]] cover all bricks at map level and are stated once, not repeated in 55 rows.
- **2026-10-21** — The 27 digest gaps are handled in three tiers: 7 added domains, 17 covered inside chapters, 3 deliberately left out (partner CRM, managed-travel accounts and policy, connected trips).
- **2026-10-21** — No Corvane scene; the page is a lookup table and stays company-neutral.

## Sources

- Internal: [[stays-capability-map]], [[stays-bounded-contexts]], every chapter spec's "Productscape domains covered" line, `PLAN.md` contract "Domains" fields.
- `_research/productscape-digest.md` §1, §3, §4, §5, §10, §12.
- Productscape models: `productscape-examples/_config/product-domains/marketplaces/travel-accommodations-marketplace/` and `.../hosted-stays-marketplace/` (v1.0, 2026).
- O'Reilly, *Residues* (Leanpub, 2024).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: stressor rows aligned with chapter content (`insv` to stays-capability-map and evolving-the-platform; combined stressor and destination operating state to evolving-the-platform), payment state feed added to event-driven-stays, timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: prose 2,140 → 2,063 words; all tables unchanged; opening, overlap-matrix interpretation and gap-section lead-ins tightened; no headings renamed. *(AI-mediated session)*

- **2026-10-22** — "five teams" → "several teams" (author decision). *(AI-mediated session)*
