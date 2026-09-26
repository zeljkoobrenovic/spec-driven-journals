---
status: accepted
revised: 2026-09-23
---

# Spec: Grounded Architecture Across a Portfolio

## Intent

Add one optional Appendix chapter that applies the author's Grounded Architecture framework to technology oversight and value creation across an investment portfolio. Establish the central analogy — a portfolio poses the same understanding problem as architecture practice in a large, decentralized group — and the central distinction: the data and people foundations transfer largely unchanged, while the operating model must be adapted to the investor's role, decision rights, company autonomy and investment objectives. Close with the reciprocal benefit for a company that adopts the framework itself.

## Audience

Investor operating teams and technology operating partners designing portfolio-level technology oversight; company product and technology leaders whose investor is building such a capability, or who are considering the framework for their own management. Assume no prior knowledge of Grounded Architecture: define its three elements before relying on them, and define portfolio, portfolio company and operating team as the book does elsewhere.

## Success criteria

- State the argument in one sentence and repeat it: reuse the foundations for understanding technology and people; adapt the mechanisms for making decisions and taking action.
- Compare a decentralized group and a portfolio explicitly, separating dimensions that concern understanding (transferable) from those that concern authority, money and incentives (adaptation required).
- Data pillar: explain Lightweight Architectural Analytics, the sources every software company already has, the two levels of reading (local management and portfolio understanding), the proposal to reuse methods and tooling rather than centralize data, the maps-versus-dashboards distinction, and the "not to replace judgment with dashboards" purpose. Warn against repeated manual reporting and ranking scorecards.
- People pillar: explain identifying who owns, knows and works with whom (partly from the same data), the difference between a directory and a collaborative network, the connector role without centralization, legible purposes of contact, and written terms for shared expertise. Link to the learning, capability and operating-partner chapters.
- Operating model: state that a portfolio is not one organization; map the framework's general principles onto the portfolio setting, including the required change to "in the organization's best interests"; adapt nudges, economic incentives and mandates to their portfolio sources of authority and cost; recommend deciding the mix per company and writing rules of engagement; connect transformation support to the value creation plan.
- Include one explicitly fictional, independent example (Tidewater) that illustrates the proposal without claiming results.
- Present the reciprocal benefit as potential benefits a company controls, with the risk of closer steering and the book's existing protections.
- Cite the framework pages inline with stable identifiers (S106, S110–S115) and state in a limits section that the framework is the author's own, describes a practice rather than measured outcomes, and that the portfolio extension is this appendix's proposal.
- Use the book's opening learning objective and exactly three KEY POINTS, Questions to Consider and To Probe Further. Aim for 3,600–4,800 words, with at most two comparison tables.
- Add a chapter hero logo, a matching black-and-white navigation icon and four explanatory figures in the book’s visual style, with descriptive alt text, captions and recorded prompts and provenance.
- Place the article in a new Appendix section after Part VI and before Reference Material, in source folder `grounded-architecture-portfolio` with permalink `grounded-architecture-portfolio`. Retain all existing permalinks and the 35 numbered main chapters.

## Non-goals

A tutorial on implementing the analytics tooling; a survey of portfolio-monitoring products; a claim that the framework improves investment returns; a restatement of the operating-model blueprints or the operating-partner chapter; a restoration of the discontinued Productscapes appendix. No summary or comic in this revision.

## Modalities

- Article: `index.md` with a chapter hero logo, a navigation icon and four explanatory figures in the book’s ivory, navy, teal and ochre style: the two settings compared, reuse the method and keep the data, connector not controller, and the governance mix per company. Prompts and review notes are in `_research/generate-grounded-architecture-portfolio-artwork-20260923.json`.

## Open questions

- Whether the appendix should later split into three chapters (data, people, operating model) if the author extends any pillar substantially; a single chapter was chosen to keep the central comparison intact.
- Whether to add a Tidewater rules-of-engagement record to the toolkit.

## Decision log

- 2026-09-23: One chapter rather than three. The argument depends on holding the three pillars against each other; at roughly 4,300 words the article is within the range of the book's long chapters.
- 2026-09-23: Recreate the Appendix section (removed 2026-09-21 when its two articles moved into Part IV) rather than place the article in Part IV or Reference Material. The article is a framework application, not a step in the reader's journey and not a reference record.
- 2026-09-23: Register the framework pages as separate identifiers (S110–S115) rather than fold them into S108, so each cited claim points to the page that carries it.
- 2026-09-23: Use a new fictional investor (Tidewater) independent of Larkspur and Northline, so the example can span nine companies without touching the existing scenario chain.

## Sources

- **Internal**
  - [[have-your-numbers-ready]] — the measure record, the labelling rule and the internal-and-shared boundary the data pillar reuses (replaced the removed data-foundations appendix on 2026-09-25).
  - [[learn-through-investors-network]], [[help-that-changes-capability]], [[useful-engagement]] — the portfolio equivalents of the people pillar's forums, shared expertise and written terms.
  - [[operating-model-blueprints]], [[tech-operating-partner]], [[decide-who-decides]] — the working arrangements, connector role and decision rights the operating model adapts to.
- **External**
  - Željko Obrenović, *Grounded Architecture* — framework foundations (S110), analytics (S106), collaborative networks (S111), operating model introduction (S112), operating-model principles (S113), governance (S114), transforming organizations (S115). All consulted 2026-09-23; the analytics page was first consulted 2026-09-22 for the data-foundations chapter.

## Changelog

- 2026-09-23 (artwork): Add the author-requested hero logo, navigation icon and four inline figures; figures continue no prior numbering (1–4). Article text unchanged apart from the figure insertions and front matter.
- 2026-09-23: Initial spec and article written in the same session from the author's brief. Status `accepted`. Configuration, root index, reading guide, bibliography, source register, glossary, README and STRUCTURE updated; build, manuscript export and validation run.
