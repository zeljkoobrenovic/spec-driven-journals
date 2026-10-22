---
status: accepted
revised: 2026-10-22
---

# Spec: Meet Corvane: Two Marketplaces, One Group

## Intent

Introduce Corvane Group, the fictional travel group every chapter uses, as one authoritative page that all chapters agree with. The page gives the reader the group and its four businesses (Roomstead, Nookaway, Corvane Connect, Corvane Payments), their business models and 2026 volumes, the 2027 systems landscape as a context diagram, the cast with roles, the six problems Corvane starts 2027 with, the One Stay program, the named group platforms the chapters introduce (with owners, dates and owning chapters), and the recurring worked examples with canonical numbers and links to the chapters that work them. It labels Corvane as fictional throughout and states that Roomstead and Nookaway are not disguised real companies. After reading, a reader can open any chapter and recognize the people, systems and numbers in its opening scene.

Productscape domains: none directly; this is the Preface scenario page that frames all TAM and HSM domains.

## Audience

Every reader on a first pass through the Preface, and readers who jump into one chapter and need the scenario in a few minutes. Also future writers and reviewers, who use this page with `_research/scenario-ledger.md` as the consistency reference.

## Success criteria

- [ ] Corvane is labeled fictional in the KEY POINTS, the lead and the Sources section; the page says explicitly that Roomstead and Nookaway are not disguised Booking.com, Expedia, Airbnb, Vrbo or any other real company.
- [ ] Brand table, revenue split (€1.200B + €0.430B + €0.062B = €1.692B), fees (12% + 4%, host-only 17%, payout 48 h after check-in) and volumes match the ledger, including `[editor]` lines (shopping requests vs Pricegrid reads).
- [ ] A context-diagram illustration shows the 2027 baseline, with a table by area and business.
- [ ] Cast table covers all thirteen staff with role, pronouns and what they own; the five recurring partners and guests are introduced.
- [ ] The six 2027 problems are listed, tied to named failure patterns and to the chapters that work them.
- [ ] One Stay: approval date, budget, three scope tiers, the rejected "load Nookaway into Tally" proposal, governance, and a diagram.
- [ ] Every named group platform in the ledger (Corvane ID, Fathom, Levy, Plumbline, Gauge, Warden, Vouch, Stayline, Clause, Courier, Threadline, Harbor, Waypoint, place registry, Trip Intent Service) plus Ordinance, the group event backbone, Kiln, group Trialroom and Gangway appears with owner, status and chapter; overlaps (Plumbline used twice; Vouch vs Warden; Ordinance, place registry and Waypoint) are described without inventing a resolution.
- [ ] The eleven recurring worked examples each get one paragraph with canonical numbers and links to the chapters that use them (found by grepping `posts/`); the 3,500–5,500-word range is respected.

## Non-goals

- Industry history and real-company evidence ([[two-stay-marketplaces]], the case studies).
- Unit economics in depth ([[stays-marketplace-economics]]).
- Capability and context maps in depth ([[stays-capability-map]], [[stays-bounded-contexts]]).
- The internals of each One Stay platform (owned by the Part II–IX chapters).
- The convergence argument ([[converging-two-marketplaces]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether Vouch runs on Warden's components is not in the ledger.
- Owners of Stayline and the place registry are not recorded; the page says so.

## Decision log

- **2026-10-21** — Followed the shape of LISTED's `meet-veldmark` (glance, history, brands, volumes, landscape, people, problems, program, examples, how chapters use it) with callouts adapted to "IN THIS SECTION".
- **2026-10-21** — Added a "Group Platforms" table because One Stay's shared layer is named chapter by chapter; it gives readers one place to find each name's owner, date and chapter.
- **2026-10-21** — Gave the eleven canonical incidents a paragraph each and folded chapter-born stories into one linked paragraph to stay within the word range.
- **2026-10-21** — Re-read the ledger tail before finishing and added the late chapter additions (forum and board chairs, capability map v2, budget lines, Kiln, Experimentation Standard v1, Gangway, Lantern, Tideline, Partner Shield, Keystone Exit Plan; the registry/Waypoint split from the December 2027 review). No ledger append was needed.
- **2026-10-21** — Cited only the EU STR Regulation and the ViDA directive as external sources; the Spanish Supreme Court annulment is referenced through [[stays-regulation]], which sources it.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — all facts, including every "Additions by chapter" line.
  - Chapters 01–40 in `posts/` — grepped for each incident and platform name.
  - LISTED's `meet-veldmark` — structural model.
- **External**
  - [Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028) — EU Short-Term Rental Regulation.
  - [Council Directive (EU) 2025/516](http://publications.europa.eu/resource/celex/32025L0516) — ViDA.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: checked every figure, date and platform against the ledger; fixed chapter count, Part IX link, "two places" count and map v1/v2 labels; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 3,895 → 3,845 prose words; reference page kept whole (no sections or figures cut); opening callout tightened, two lines that repeated figure captions shortened, vendor-use disclaimer moved to the Sources note. *(AI-mediated session)*
- **2026-10-22** — Verified Lisbon tourist tax / Portuguese VAT against official sources. *(AI-mediated session)*
