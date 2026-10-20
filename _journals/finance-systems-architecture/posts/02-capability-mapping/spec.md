---
status: accepted
revised: 2026-10-20
---

# Spec: Map What Finance Does Before What Runs It

## Intent

Give the reader a way to describe what finance must be able to do independently of which system, team or process does it, and a second decomposition (bounded contexts) that turns that description into software and team boundaries. The chapter delivers a usable three-level finance capability map, a heat-mapping method, a finance context map with explicit relationship patterns, and a capability → application → team trace that exposes ownership gaps. After reading, an architect can run a capability mapping exercise with Finance and use the result in portfolio, convergence and ownership decisions.

## Audience

Chief and enterprise architects, finance-systems architects and finance-transformation leads who need a stable planning frame for a multi-brand, multi-ERP finance estate. They know architecture; they may not know business-architecture conventions (BIZBOK) or how DDD context mapping applies to finance.

## Success criteria

- [ ] Reader can distinguish capability, value stream, process, application and organization unit (contrast table) and explain why R2R/O2C/P2P are not capabilities.
- [ ] Reader can apply the naming rules and recognize the common modeling mistakes (system, department, verb, "how" in "what", per-brand, vendor catalog, uneven granularity).
- [ ] The chapter contains a three-level finance capability map (10 level-1 groups, 45 level-2 capabilities with one-sentence definitions, selected level 3) and a mermaid overview.
- [ ] Reader can heat-map capabilities on importance, maturity, duplication and cost with defined scales; the Northmere heat map shows the four ledger overlaps (payouts ×2, billing ×3, reconciliation in three tools, tax determination in Vertex and Oracle) and distinguishes them from decided duplication.
- [ ] Reader can identify finance bounded contexts, draw a context map using customer-supplier, conformist, anticorruption layer, open-host service and published language, and say where ACLs are worth building.
- [ ] Reader can explain how capability maps and bounded contexts complement each other and read the many-to-many mapping as a diagnostic.
- [ ] Reader can trace capabilities to applications to teams and name the four kinds of ownership gap.
- [ ] Reader can plan a capability mapping exercise with Finance: who attends, how long, what to avoid.

## Non-goals

- Portfolio disposition, TIME and TCO — [[application-portfolio]].
- The overlap register and coupling taxonomy in depth — [[redundancy-and-coupling]].
- Canonical event design and the adapter kit — [[loosely-coupled-domains]].
- System-of-record matrix and authority hand-off — [[systems-of-record]].
- End-to-end process steps and metrics — [[finance-processes]].
- Team topology design — [[organizing-for-architecture]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should Financial Event Management (10.1) stay on the business capability map or move to a technical capability view? Kept for now, with the rationale stated.
- The current BIZBOK Guide version (v13 vs v14) was not verified; the definitions are cited from the v12 glossary as reproduced by GCcollab.
- Whether Northmere Ads' ad-billing service should be a fifth overlap is left as a recorded workshop judgment.

## Decision log

- **2026-10-18** — Ten level-1 groups following Finance's domains of accountability rather than ERP modules; Controls and Finance Data promoted to level 1; payment acceptance drawn outside the map. Rejected: a vendor-module skeleton (The Borrowed Roadmap) and R2R/O2C/P2P as level-1 boxes.
- **2026-10-18** — Highlighted only the four ledger overlaps as undecided duplication; brand-ledger GL duplication and the split subledger shown on the heat map but framed as decided transition states owned by other chapters.
- **2026-10-18** — Heat-map importance scale uses Differentiating / Critical / Commodity, borrowing Evans's core vs generic subdomain distinction and adding "Critical" for finance's non-differentiating but material capabilities.
- **2026-10-18** — Reconciliation and close not modeled as their own bounded contexts; BlackLine treated as a generic subdomain, to avoid teams building a second ledger.

## Sources

- **Internal**
  - [[meet-northmere]], scenario ledger — overlaps, systems, cast, volumes.
  - [[application-portfolio]], [[redundancy-and-coupling]], [[loosely-coupled-domains]], [[systems-of-record]] — neighboring ownership.
  - Research: brief-ea-integration-ledger (§1.3 BIZBOK, §1.10 Conway, §1.11 DDD); productscape digest §1 (24 capability bricks, 6 groups) and §1.7.
- **External**
  - Business Architecture Guild, BIZBOK Guide (v12 glossary via GCcollab) — capability and value-stream definitions.
  - Eric Evans, *DDD Reference* (2015) — bounded context, context-mapping patterns, core and generic subdomains.
  - Martin Fowler, "Bounded Context" (2014) and "Conway's Law" (2022).
  - Skelton and Pais, *Team Topologies*, 2nd ed. (2025).

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: American spelling (modeling), mapping workbooks count aligned to the ledger (14). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Map Capabilities Before Systems" to "Map What Finance Does Before What Runs It" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,854 → 5,789 prose words; lead now ties the chapter to [[chief-architect-role]] and the chapters that consume the map; "The map" renamed "Ten groups, 45 capabilities"; two announce-only lines cut; several first sentences now state their point. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
