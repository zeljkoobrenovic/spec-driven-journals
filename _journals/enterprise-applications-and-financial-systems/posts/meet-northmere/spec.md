---
status: accepted
revised: 2026-10-18
---

# Spec: Meet Northmere: Five Brands, One Set of Books

## Intent

Introduce Northmere Group, the fictional enterprise every chapter uses, in enough detail that a reader can follow any chapter's example without rereading the ledger: brands and business models, legal and licensed entities, systems landscape, volumes, cast, the seven 2027 problems, Program Keystone and the recurring worked examples. Make clear why the book uses a fictional composite and that it describes no real company. End with a map from Northmere's problems to the chapters that work on them.

## Audience

Architects and finance-transformation leaders starting the book, and readers who jump into a single chapter and need the scenario's context. Assumes architectural experience; explains business-model and regulatory terms briefly and links to the chapters that own them.

## Success criteria

- [ ] Opens with IN THIS SECTION and exactly three KEY POINTS.
- [ ] States clearly and early that Northmere is a fictional composite that generalizes patterns in multinational, multi-brand, technology-driven groups, not any real company.
- [ ] Explains agency, merchant, subscription/usage and marketplace payments facilitation briefly, including net presentation as agent, and links [[accounting-for-architects]].
- [ ] Describes Northmere Payments B.V. and Northmere Payments UK Ltd and why being an EMI (not a bank) matters architecturally.
- [ ] Includes a mermaid context diagram and a systems table that agree with the ledger (S/4HANA greenfield 2021, no Central Finance, FI-CA 2025, OneStream 2022, three integration technologies).
- [ ] Includes the volumes, the full cast table, the seven problems, Keystone Year 1/3/5 with budget and savings, and the four recurring worked examples with ledger amounts and dates.
- [ ] Includes a problem-to-chapter map across the four parts using only valid permalinks.
- [ ] Roughly 3,000–4,000 words.

## Non-goals

- Explaining the accounting of the examples ([[accounting-for-architects]]), the payment lifecycle ([[payments-fundamentals]]) or the landscape layers ([[finance-landscape]]).
- Adding new canonical facts; this page restates the ledger.
- Detailed vendor capability claims; Part II chapters own and source them.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should a one-page printable "Northmere card" (cast and numbers) be added to the [[toolkit]]?
- If the 2027 Q4 convergence decision is written in a chapter, update the landscape section to point to it.

## Decision log

- **2026-10-18** — Presented the ledger mostly as tables rather than prose, because readers return to this page as a reference.
- **2026-10-18** — Tagged each of the seven problems with its failure pattern from [[where-finance-architecture-goes-wrong]] to tie the two preface pages together.
- **2026-10-18** — Kept the context diagram to systems and their main flows (no integration-technology nodes) to stay under the node limit; the integration technologies are listed in the table.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — all facts on the page.
  - `_research/productscape-digest.md` — business-model explanations and the merchant-booking walkthrough shape.
  - [[where-finance-architecture-goes-wrong]] — pattern names used to tag the problems.
- **External**
  - None; vendor and regulatory facts are sourced in the chapters that own them.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: Wayfare rail ticket stated as merchant of record but agent (€6.72 net, at ticket issue); €420 chargeback dated per ledger; forward pointer to the Dec 2027 convergence decision; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed to "Meet Northmere: Five Brands, One Set of Books" at the author's request. *(AI-mediated session)*
