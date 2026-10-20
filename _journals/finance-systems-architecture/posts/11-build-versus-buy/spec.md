---
status: accepted
revised: 2026-10-18
---

# Spec: Build, Buy or Compose: Choosing What to Own

## Intent

Give the Chief Architect a repeatable method for sourcing finance capabilities and for selecting vendors without letting the vendor set the terms. The reader should leave with the sourcing spectrum (build, buy, buy-and-extend, compose, outsource as a service), three per-capability tests (differentiation, volume and variability, controls burden) combined in a decision tree, a seven-to-ten-year cost of ownership with build, run, change, control and exit lines, a selection process with gates (capability requirements and knock-outs, scripted demonstrations on the enterprise's hardest scenarios, reference calls, proof of concept, integration and data-exit test, contract terms including EU Data Act and DORA exit, weighted score), the pitfalls of weighted scoring, fit-to-standard and its demands on Finance, and post-acquisition rules (converge, keep, wrap). The chapter owns the *method*; [[workday]] owns the platform-level Tablekin trade-off and Dana's conditional recommendation, and this chapter must agree with it.

## Audience

Chief and enterprise architects, finance-systems leads, procurement and finance-transformation leaders who run or sponsor sourcing decisions and vendor selections, and controllers who must live with the result.

## Success criteria

- [ ] Reader can apply the three tests per level-2 capability and explain why a build needs differentiation plus one other test, and why a commodity that a package cannot carry goes to compose, not build.
- [ ] Reader can build a seven-to-ten-year cost comparison with build, run, change, control and exit lines, state the range, and explain why a TCO usually disqualifies rather than selects (Tablekin A/B/C: 21.4 / 20.5 / 18.2 $M, overlapping ranges).
- [ ] Reader can see the method applied to three Northmere cases: Tablekin (a rationalization, not a build-or-buy question), SFP 2012 (right build, wrong scope, controls never costed) and OneStream 2022 (good selection; bundled reconciliation module and thin exit terms as The Borrowed Roadmap).
- [ ] Reader can run a selection with knock-outs, scripted hardest-scenario demos (the €420 chargeback, the $1,029 Tablekin invoice, the Lisbon booking, period-end peak, reprocessing, new entity, audit trace), a PoC with pre-written success criteria, and a data exit test.
- [ ] Reader can state the EU Data Act switching terms (Art. 25, 26, 29, 31) and DORA's third-party and exit provisions (Art. 28(3), 28(4), 28(8), 30(3)(f)) and when they apply at Northmere (Northmere Payments B.V.).
- [ ] Reader can spot three weighted-scoring pitfalls in a worked score sheet (knock-out hidden by compensation, a tie that flips under a five-point weight shift, weights set after demos).
- [ ] Reader can apply the post-acquisition rules (wrap within twelve months; converge, keep as a tier, or keep wrapped).
- [ ] Article has three mermaid diagrams, trade-off tables, Chief Architect's view, Questions to ask and Sources and Evidence.

## Non-goals

- Custom platform reasons, burdens, boundaries and the SFP component classification ([[custom-finance-platforms]]).
- Workday product depth and the A/B/C platform trade-off table ([[workday]]).
- Two-tier ERP, coexistence patterns and convergence economics ([[multiple-erps]]).
- Vendor tiering, concentration risk and portfolio-wide exit plans ([[vendor-portfolio-strategy]]).
- Migration patterns and cut-over ([[modernization-patterns]]); TCO components and TIME ([[application-portfolio]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Tablekin decision is conditional (worktag mapping by rule, Accounting Center PoC, Q4 2027 convergence pattern); revisit after the Q1 2028 review.
- The OneStream renewal date differs between [[application-portfolio]] (31 Dec 2027) and [[onestream]] (Q2 2028); this chapter avoids the date. Editor to reconcile.
- Whether finance SaaS is "data processing service" under the Data Act is stated as common practitioner reading, not verified against a recital; confirm before print.

## Decision log

- **2026-10-18** — Made the capability, not the system, the unit of decision, so Tablekin resolves as a rationalization question and SFP's 2012 build is criticized for scope rather than for building.
- **2026-10-18** — Set the scene in January 2027 so this chapter's method feeds the February 2027 design-authority session described in [[workday]], keeping the recommendation (Option C, conditional; B fallback) in one place.
- **2026-10-18** — Used an anonymized e-invoicing gateway selection (vendors P, Q, R) for the scoring example to avoid scoring real vendors on invented numbers.
- **2026-10-18** — Merged the spectrum and trade-off tables to stay within length.

## Sources

- **Internal**
  - [[custom-finance-platforms]], [[workday]], [[application-portfolio]], [[onestream]], [[controls-and-auditability]], [[multiple-erps]], [[vendor-portfolio-strategy]], [[modernization-patterns]].
  - `_research/brief-ea-integration-ledger.md` §1.4, §1.5, §5; platform briefs (sap §4–5, oracle §5 and §8.4, workday §3.1 and §7, blackline-onestream A8); `productscape-digest.md` §1.7, §4.2, §7, §8.
- **External**
  - Regulation (EU) 2023/2854 (Data Act) and Regulation (EU) 2022/2554 (DORA), EUR-Lex — verified article text.
  - SAP Learning, SAP Activate Explore phase and fit-to-standard workshops; SAP, S/4HANA release and maintenance strategy (2022).
  - TechTarget, postmodern to composable ERP (secondary for Gartner); Latham & Watkins on Data Act switching; The Register on Birmingham City Council (2026).

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: SFP cost of owning aligned with the ledger ($18.5M incl. $4.1M finance operations), TCO range sentence corrected, CUEC expanded. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Build, Buy or Compose: Vendor Selection and Portfolio Rationalization" to "Build, Buy or Compose: Choosing What to Own" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
