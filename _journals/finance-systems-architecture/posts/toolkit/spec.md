---
status: accepted
revised: 2026-10-18
---

# Spec: Working Papers: Templates for the Finance Architect

## Intent

Give the reader a set of practical, copyable templates for the records a Chief Architect uses to keep a finance estate coherent, provable and changeable. Each template is derived from the chapter that teaches it, keeps that chapter's terminology, and is filled in once with a short Northmere example that agrees with the chapter and the scenario ledger. The page should let a reader start from the decision on their desk, copy one record, and know which fields carry ownership, evidence and dates, and which common mistakes to avoid. It also delivers the instruments other chapters promise "in the toolkit": the control impact assessment and waiver ([[architecture-governance]], [[controls-and-auditability]]), the reconciliation design card ([[traceability-and-reconciliation]]), the blank agent control card ([[ai-in-finance]]) and the set listed in [[long-term-evolution]].

## Audience

Chief and enterprise architects, finance-systems, integration and data architects, and finance-transformation leads who need working forms for portfolio, governance, integration, ledger, reconciliation, migration and operational decisions. Controllers and SOX leads use Tools 4, 9, 13 and 14 as walkthrough documents.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; three KEY POINTS; two to three failure patterns with exact names; `<br>`; an intro on how to use the templates; a table of contents (Tool | Use it when | Chapter).
- [x] Contains 14 tools, each as a `## Tool N: Name` section with purpose (2–3 sentences), when to use, the template (table or fenced block), a short Northmere example, three common mistakes and a closing Learn more line linking the owning chapter.
- [x] Covers at least the instruments [[long-term-evolution]] lists: capability map, SoR matrix, decision record, vendor scorecard, canonical event specification, reconciliation design card, cut-over checklist, debt register, agent control card.
- [x] Every template field traces to the owning chapter (ADR anatomy and waiver rules from ch. 34; envelope and semantic rules from ch. 30; ten interface requirements and catalog fields from ch. 09; catalog columns and matching decisions from ch. 31 and 18; parallel-run exit criteria from ch. 12; five-part fitness function and three-column register from ch. 39; playbook phases from ch. 40; card fields from ch. 42; nine layers from ch. 32).
- [x] Northmere examples use ledger figures and dates (Lisbon booking amounts and batch 1047, ADR-0007 and W-2027-004, VR-01, INT-0412, the 30 Sep–1 Oct 2027 duplicate, Brazil kit, `apm-triage`).
- [x] One mermaid diagram shows how the records reference each other; cross-links use only valid permalinks.
- [x] Short Sources and Evidence section and the fictional-Northmere sentence.

## Non-goals

- Re-teaching the reasoning behind each template; each tool summarizes and links to its chapter.
- Principle-writing guidance and the overlap register, owned by [[principles-standards-reference]] and [[redundancy-and-coupling]] (linked, not reproduced).
- Definitions of terms ([[glossary]]) and the source list by topic ([[bibliography]]).
- Downloadable file formats (spreadsheets, document templates).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Chapters differ on the 2028 FI-CA merchant invoicing move ([[systems-of-record]]: cohort cut-over from the May 2028 cycle; [[finance-transformation]]: a Q2 2028 parallel run with SFP as book of record). The toolkit avoids that example; the editor should reconcile the two chapters.
- Should a principle card become a fifteenth tool, or a vendor release-intake note be added for [[architecture-governance]]?

## Decision log

- **2026-10-18** — Chose 14 tools and merged the vendor scorecard with the exit-plan card (one vendor lifecycle) and the debt register with the fitness function card (the register requires its fitness functions); dropped a separate principle card because [[principles-standards-reference]] already gives its five-part anatomy as a contrast table.
- **2026-10-18** — Ordered tools by stage (understand, decide, design, change, run) rather than chapter order, and kept chapter links in the table of contents so readers can go either way.
- **2026-10-18** — Wrote templates as tables where fields need guidance and as fenced blocks where the record is a literal artifact (ADR, waiver, YAML contracts, posting rule, runbook), so they can be copied as they are.
- **2026-10-18** — Built Tool 10 on the gates (G0–G3), T-counted runbook and two rollback points of [[incremental-modernization]], with the parallel-run exit criteria of [[modernization-patterns]] folded into G1, and used the EEA cohort cut-over of 1 November 2029 as the example; rejected the FI-CA invoicing move and the 2027 SFP subledger cut-over because their dates are either inconsistent across chapters or fall in a quarter-end month.

## Sources

- **Internal**
  - [[capability-mapping]], [[application-portfolio]], [[systems-of-record]] — map, heat map, fact sheet, TIME, TCO, SoR columns and conflict rules.
  - [[architecture-governance]], [[build-versus-buy]], [[vendor-portfolio-strategy]] — ADR fields, ADR-0007, waivers, scorecard, exit-plan elements and maturity.
  - [[loosely-coupled-domains]], [[integration-architecture]], [[designing-financial-ledgers]] — envelope, semantic rules, interface requirements, INT-0412, posting rules.
  - [[traceability-and-reconciliation]], [[blackline]] — R1–R9 catalog, matching-rule decisions, risk tiers, cause codes.
  - [[modernization-patterns]], [[incremental-modernization]], [[finance-transformation]], [[brands-entities-markets]] — exit criteria, stage gates and runbook, blackout calendar, go/no-go, nine layers, Brazil kit.
  - [[technical-debt-and-fitness]], [[resilience-and-security]], [[ai-in-finance]] — register, fitness catalog, incident playbook, agent control card.
- **External**
  - Michael Nygard, *Documenting Architecture Decisions* (2011) and MADR — ADR anatomy.
  - Martin Fowler, *Accounting Patterns* — Posting Rule.
  - Regulations (EU) 2022/2554 (DORA) and 2023/2854 (Data Act) — exit and switching requirements.
  - The private-techuity (OWNED) toolkit — page format and callout structure.

## Changelog

- **2026-10-18** — Initial spec and page: 14 templates with Northmere examples. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: SFP subledger cut-over date set to 1 November 2027; calendar rule wording clarified where relevant. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Toolkit: Templates for the Finance Architect" to "Working Papers: Templates for the Finance Architect" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the mermaid diagram with a generated illustration (article-illustrator), captions unchanged. *(AI-mediated session)*
