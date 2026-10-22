---
status: accepted
revised: 2026-10-22
---

# Spec: Built for the Next Shock: Evolving the Platform Over a Decade

## Intent

Close Part IX by answering how a Chief Architect keeps a vehicle data and dealer SaaS platform coherent over ten years of regulation, market shocks, ownership changes and technology shifts. The chapter restates the book's argument on one page, then replaces the target-state roadmap with three tools: **stressor analysis** (stressors, attractors, residues, counted to find the structures that survive most futures), **options** with written triggers, and **vehicle-platform fitness functions** reported to the board instead of milestones. It lays out the Year 1 / Year 3 / Year 5 path as gates expressed in fitness-function terms and hands the reader to Part X's case studies. After reading, an architect can run a stressor workshop, count residues, write an option register and a twelve-line scorecard with owners and 2027 baselines.

Owns: **stressor analysis (vehicle)** and **fitness function (vehicle)**.

Productscape bricks covered: all, through the residuality model (`residuality.json`: the seven stressors `rdwoutage`, `freedata`, `portalconsolidation`, `bpmchange`, `evshift`, `acquisitions`, `privacy`, and the naive/residual architectures) and the persona strategy horizons (Y1/Y3/Y5 of `udlr`, `dhld`, `lsco`, `ivnd`, `dcli`).

## Audience

Group chief architects, CTOs and engineering directors of vehicle-data companies, dealer-software vendors and portals who must defend a multi-year platform program to a board or owner and steer it when the plan meets reality. They know architecture governance; they need the vehicle-specific stressors, residues and measures.

## Success criteria

- [ ] Restates the book's argument in four sentences and a Part-by-Part table of durable structures.
- [ ] Defines stressor, attractor, residue, naive/residual architecture, option and fitness function, citing O'Reilly and Ford et al.
- [ ] Presents a stressor table that starts from the digest's seven stressors and adds research-backed ones, each with dated public evidence, attractor, what breaks at Axleby and the residue.
- [ ] Counts residues across stressors and runs one combined stressor (Showroomly sale + portal feed restriction + customer exit) that exposes at least one real gap.
- [ ] Gives an option register with premium, trigger and owner, plus options deliberately closed.
- [ ] States the Year 1/3/5 path with exit criteria as fitness-function thresholds, consistent with the ledger's One Dossier dates.
- [ ] Gives a twelve-row fitness-function scorecard using ledger baselines (publish lag, correction propagation, lead delivery, segment bias, €0.031 lookup, double submissions, Charter coverage, customer-detected incidents…), with owners and guarded failure patterns.
- [ ] Includes failure handling for long-term governance, a trade-off table, a market comparison of where stressors land, the Chief Architect's view, questions and a hand-off to [[part-10]].

## Non-goals

- Sourcing decisions and the data-rights test: [[build-buy-or-partner]].
- Portfolio integration sequencing and capability map v2: [[one-platform-from-many-products]].
- Team topology and governance forums: [[organizing-engineering]].
- Migration mechanics (strangler, parallel run, client sunset policy): [[modernizing-the-platform]].
- AI use cases and the agent permission model: [[ai-in-dealer-workflows]].
- Re-teaching residuality theory in depth.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether the EU Data Act's switching rules apply to SaaS dealer software in practice is the author's reading; S16 is framed accordingly.
- COM(2025) 179 was not adopted as of October 2026; S14 and its option may need revision.
- The US EPA battery-monitor rule status is subject to political change.
- Option premiums are assumptions; the €14 million Year 1 residue share is an Axleby illustration.
- Neighboring Part IX chapters (45–48) were not yet written; terminology for capability map v2, the agent permission model and the client sunset policy should be checked once they exist.

## Decision log

- **2026-10-22** — Opened with the board's two questions (what still pays off; what separation costs) and let the DriveDesk Outage arrive mid-exercise, so the method is shown to work on a real 2027 incident rather than asserted.
- **2026-10-22** — Kept the digest's seven stressors and added nine research-backed ones (market spike, divestment, data-source repricing, supplier error, DMS attack, connected-car data, register reform, AI agents, cheap switching) rather than replacing the model's list, so the Productscape provenance stays visible.
- **2026-10-22** — Made separability (S8, S16) the gap One Dossier missed and used Turnstile's single DVLA key as the concrete failure of the combined test, rather than a generic carve-out discussion.
- **2026-10-22** — Expressed the Year 1/3/5 path as fitness-function gates instead of feature lists, and capped the scorecard at twelve functions.

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-data-ecosystem]] — the One Dossier program and the ecosystem failure table that hands stressor analysis to this chapter.
  - [[vehicle-identity]], [[provenance-and-data-quality]], [[data-licensing-and-governance]], [[billing-and-metering]] — the four high-count residues.
  - [[listing-syndication]], [[observability-and-data-operations]], [[leads-and-crm]], [[valuation-engine]], [[scale-and-cost]], [[registration-and-trade-services]] — fitness-function baselines.
  - [[dms-integration]], [[reliability-and-dependencies]], [[case-vwe]], [[case-cdk-global]] — DriveDesk Outage, CDK record and the divestment lesson.
- **External**
  - Barry M. O'Reilly, *Residues* (2024) — stressors, attractors, residues.
  - Ford, Parsons, Kua, Sadalage, *Building Evolutionary Architectures* (2017; 2nd ed. 2022) — fitness functions.
  - Regulation (EU) 2023/2854, 2023/1542; COM(2025) 179 (EPRS briefing, 2026); CJEU C-319/22 and C-413/23 P; FTC GM order (2026) — regulatory stressors.
  - Auto Trader RPI (2024) and FY2026 results; Manheim index (2022); Hertz 8-K (2024); CDK-outage SEC filings (2024); Emerce (2025); Bundeskartellamt (2026); Journal de l'Automobile (2026) — market, channel and ownership stressors.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned with 45–48 (separability and the integration contract, residues vs v2 kernel tier, v2 webhooks Q3 2028, Connect XML paid extensions, external-agent policy); hand-off to part-10; timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (neighboring). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
