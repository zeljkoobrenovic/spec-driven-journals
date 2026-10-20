---
status: accepted
revised: 2026-10-20
---

# Spec: Meet Veldmark: Four Brands, One Platform to Build

## Intent

Introduce Veldmark Group, the fictional marketplace group every chapter uses, as one authoritative page that all chapters agree with. The page gives the reader the brands and business models, the volumes, the 2027 systems landscape (as a context diagram), the cast, the eight problems Veldmark starts 2027 with, the Common Ground program and its decision timeline, and the five recurring worked examples with their canonical numbers. It labels Veldmark as fictional prominently and repeatedly, so no reader takes it for a disguised real group. After reading, a reader can open any chapter and recognize the people, systems and numbers in its opening scene.

## Audience

Every reader of the book, on first pass through the Preface, and readers who jump into a single chapter and need the scenario in five minutes. Also future writers and reviewers of the book, who use this page with the scenario ledger as the reference for consistency.

## Success criteria

- [ ] Veldmark is labeled fictional in the KEY POINTS, the lead and the Sources section; no real brand, product or executive is attributed to it.
- [ ] Brand table, revenue split and volumes match `_research/scenario-ledger.md` exactly (€1.31B; Safe Deal 11.6M transactions, ~€1.02B GMV, €75M).
- [ ] A context diagram shows the 2027 baseline landscape, with a table by area and brand.
- [ ] Cast table covers all seventeen ledger characters with role, pronouns and what they own.
- [ ] The eight 2027 problems are listed, tied to named failure patterns where they fit.
- [ ] Common Ground: budget, goals, principle "share platforms, not products", governance (advice forum, decision records), dated decision table and plateau diagram.
- [ ] The five recurring worked examples are given with canonical facts and the chapters that use them; timings agree with the editor's corrections (bike reserved 14:02).
- [ ] A problem-to-chapter map and a hand-off to [[part-1]].

## Non-goals

- Industry history and real-company evidence ([[industry-evolution]], Part IX cases).
- Marketplace classification and the profile register ([[marketplace-taxonomy]]).
- Capability map and context map details ([[business-capabilities]], [[bounded-contexts]]).
- The internals of each Common Ground platform (owned by the Part II–VII chapters).
- Chief Architect role and governance in depth ([[organizing-marketplace-engineering]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Resolved (editor, 19 Oct 2026): Veldmark operates in eight countries (NL, BE, PL, PT, DE, AT, FR, ES); see the [editor] ledger line.
- Ingrid's start date (Mon 1 Feb 2027) and reporting line (to Mateus Carvalho) are added here; ch. 24 implies a mid-February start.
- Motorvane's origin (founded vs acquired) is not in the ledger; the page says only that it launched in Germany in 2008.

## Decision log

- **2026-10-19** — Followed the shape of RECONCILED's Meet Northmere (glance, brands, landscape, people, problems, program, examples, how chapters use it) so the two books' running examples read alike; kept the house callouts and a failure-pattern callout.
- **2026-10-19** — Kept the page to scenario facts only, with no real-company claims, so the Sources section needs almost no external evidence (DVF is the one real dataset cited).
- **2026-10-19** — Included a dated decision table drawn from chapters' ledger additions, so readers can place each chapter's scene in the 2027 timeline; detail stays in the owning chapter.
- **2026-10-19** — Stated the Sunday-evening peak explicitly as a Veldmark illustration, per the writer brief.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — all facts, including every "Additions by chapter" line.
  - Existing chapters' opening scenes (01–46) — checked for the facts they rely on.
  - RECONCILED's `meet-northmere` page — structural model.
- **External**
  - [Demandes de valeurs foncières (DVF)](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/), DGFiP — the real dataset behind the fictional Valuo.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Tradeyard country history aligned with industry-evolution (BE and PT on their own copies of Yardstick; PL by acquisition); Ruhrblick's Pro 150 package named; all figures checked against the ledger and editor lines; American spelling (program). *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 2,754 → 2,740 prose words; lead now states the page's place in the Preface (failure patterns become Veldmark's problems; every chapter's scene draws on it); a few sentences tightened, one restatement of the "no contradictions" convention cut; no headings changed; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Title changed from "Four Marketplaces" to "Meet Veldmark: Four Brands, One Platform to Build", because the page counts three marketplaces plus Keybridge, an agent CRM (MAU row, "Four Brands, Four Business Models"); spec heading and PLAN.md updated; permalink unchanged. *(AI-mediated session)*
