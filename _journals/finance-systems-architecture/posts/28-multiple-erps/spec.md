---
status: accepted
revised: 2026-10-20
---

# Spec: Converge or Coexist: Living with More Than One ERP

## Intent

Answer whether an enterprise running several ERPs should converge, federate or tier them. The chapter separates what must be one thing across every ledger (chart semantics, entity register, rates, close calendar, evidence standard) from what may be several (the ledgers themselves). It defines five coexistence patterns, gives the criteria that choose between them, and shows how to price convergence against the realistic alternative. It also supplies an ERP-side playbook for acquisitions. Through Northmere it takes the Keystone 2027 Q4 decision explicitly (accounting hub, conditional on a volume proof), with Dana's reasoning and recorded reversal conditions, and reconciles the platform chapters' separate leanings into one group decision.

## Audience

Chief and enterprise architects, finance-systems architects and finance-transformation leaders who inherit multi-ERP estates through acquisitions or business-model diversity, and the CFOs and controllers who fund convergence. They should leave able to classify each ledger by pattern, defend a tier with entry criteria, and challenge a convergence business case.

## Success criteria

- [ ] Reader can name the four causes of multi-ERP estates and say which is a durable reason for a second ledger.
- [ ] Reader can state why "one ERP" is the wrong goal and list the five "ones" that are mandatory.
- [ ] Reader can describe the five patterns (single instance, two-tier, central-finance replication, accounting hub, consolidation-only federation), with diagrams, and the two-tier integration contract (table).
- [ ] Reader can apply the seven-criterion table to choose a pattern for a given ledger.
- [ ] Reader can build a convergence break-even against the realistic alternative, as in the Wayfare worked example ($5.4M/yr keep, $24M one-off, 6.2 vs 3.9 years).
- [ ] The Northmere 2027 Q4 decision is stated explicitly, with reasoning, per-brand outcomes and four reversal conditions consistent with [[sap-s4hana]], [[oracle-fusion]] and [[workday]].
- [ ] Reader can run the M&A playbook: day-1 TB load, ICFR exclusion limit (SEC FAQ Q3), 12-month wrap, converge-or-keep test.
- [ ] Every vendor claim is sourced; Central Finance mechanics marked practitioner-documented.

## Non-goals

- SAP, Oracle and Workday internals ([[sap-s4hana]], [[oracle-fusion]], [[workday]]).
- Accounting-engine and ledger design ([[designing-financial-ledgers]]); canonical event model ([[loosely-coupled-domains]]).
- Migration stage gates and cut-over mechanics ([[incremental-modernization]], [[modernization-patterns]]).
- Sourcing method and TCO method in general ([[build-versus-buy]]); consolidation mechanics ([[onestream]]).
- Capability overlap beyond ledgers ([[redundancy-and-coupling]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Central Finance mechanics (AIF, non-SAP inbound) rest on practitioner sources; recheck against SAP documentation for the release cited.
- Two-tier evidence is vendor and partner material; no independent study of two-tier economics was found.
- The H1 2028 volume-proof outcome and the Q1 2028 Tablekin review are future events in the scenario; later chapters must stay consistent with the decision recorded here.

## Decision log

- **2026-10-18** — Chose route B (accounting hub, Northmere-built engine generalized from SFP) for the Keystone decision, because chapters 14, 15 and 36 point to it and it addresses posting-logic location, the group's actual problem.
- **2026-10-18** — Combined the separate fallbacks of chapters 15 and 17 into one: if the volume proof fails, Oracle Accounting Hub for Wayfare plus Central Finance for finished documents.
- **2026-10-18** — Priced Wayfare convergence against the realistic alternative (Accounting Hub on Fusion) rather than against doing nothing, to teach the break-even error most cases make.
- **2026-10-18** — Treated "one ERP" as a property (one set of books) and made the five "ones" mandatory regardless of pattern.

## Sources

- **Internal**
  - `_research/brief-sap.md`, `brief-oracle.md`, `brief-workday.md`, `brief-ea-integration-ledger.md`; `_research/scenario-ledger.md`.
  - [[sap-s4hana]], [[oracle-fusion]], [[workday]], [[onestream]], [[build-versus-buy]], [[modernization-patterns]], [[global-scale]], [[target-and-transition-states]], [[designing-financial-ledgers]].
- **External**
  - SAP Learning and SAP Community pages on two-tier ERP; SAP blogs on Central Finance replication.
  - Oracle, *How Oracle Accounting Hub Cloud Works* (26C); Oracle EPM SAP integration documentation.
  - Workday, *Accounting Center* product page.
  - SEC Office of the Chief Accountant, ICFR FAQ (revised 2007), Question 3.
  - eWeek (2012) on NetSuite two-tier; TechTarget on postmodern and composable ERP.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: entity split corrected to 55 SAP company codes / 3 Fusion primary ledgers / 4 Workday companies (67 codes after convergence); SFP subledger go-live 1 Nov 2027; Tablekin recommendation dated June 2027; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Multiple ERPs, One Finance Core: Coexistence and Convergence" to "Converge or Coexist: Living with More Than One ERP" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,693 → 5,727 prose words; opening now ties the chapter to Part III's question and names what it builds on ([[systems-of-record]]) and what carries it out ([[incremental-modernization]]); "Operating Multiple ERPs Well" renamed "Enforcing the Five 'Ones'"; first sentences tightened in six paragraphs. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
