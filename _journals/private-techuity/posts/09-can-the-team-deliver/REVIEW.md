# Editorial review: Can the Software and the Team Deliver What Was Promised?

Reviewed 14 September 2026. Read the full article, summary and reader-facing comic text.

## Overall assessment

The article argues for assessing technology through business constraints, existing strengths and the funded transition needed to deliver a plan. It serves technical leaders particularly well, while retaining enough explanation for finance and product colleagues. The country-expansion example, pricing-module constraint and distinction between current payroll and additional migration spending are strong.

The chapter needs a firmer boundary with “Growth Into Design.” It announces an assessment task but also teaches implementation options, standardization and staged improvement. Some opening claims overstate what is unique to investor-backed companies, and a few technical definitions need sharper boundaries.

## Detailed feedback

- **Introduction and organization:** The second-country example integrates tax, support, contracts and software effectively. “In normal operations, engineering constraints are handled as they arise” is an unsupported caricature of ordinary engineering planning. Likewise, an investment case does not necessarily fix the destination: the book repeatedly invites leaders to revise it. Start with the particular promise made before this assessment.
- **Flow and scope:** Business capability → concrete constraint → technical debt → delivery evidence is a good assessment sequence. “Match the Commitment,” “A Rewrite Needs a Funded Transition,” “Standardization” and “Fund Learning” then increasingly enter the next chapter's decision territory. Keep the transition feasibility test here, but let the next chapter choose the design.
- **Clarity and terminology:** The three-week pricing bottleneck makes technical debt tangible without equating it to money owed. The text commendably records strengths rather than just defects. Enterprise architecture is reduced too narrowly to deciding which choices are group-wide or local; present this as one relevant enterprise-architecture question, not its whole purpose.
- **Technical check:** The reference to five DORA delivery metrics is current and supported by [DORA's own guide](https://dora.dev/guides/dora-metrics/). However, DORA's change lead time starts at commitment to version control, while the article later defines a general lead time “from starting a change.” Both measures can be useful; explicitly distinguish end-to-end work lead time from DORA change lead time to prevent inconsistent benchmarking.
- **Examples and precision:** The migration table totals €1.3m correctly. “Total before benefits begin” conflicts with the later instruction to define benefits before the whole program finishes unless this example assumes none during the eighteen months. Clarify the assumption or call it “total transition spending before benefit offsets.” Built and bought transitions share cost categories, but “the transition costs behave the same way” overstates equivalence in contracts, exit rights and vendor timing.
- **Pacing, tone and conclusion:** The respect for engineers' knowledge is a real strength. The closing pricing example is concrete but changes subjects from the opening country expansion and middle scheduling-engine rewrite. Too many separate problems weaken the continuous story.
- **Other formats:** Comic panel 4 teaches modular applications versus separately deployed services, a design comparison now developed in the next article rather than this one. Replace it with an assessment or transition-funding panel, or explicitly link the design discussion.

## Recommended changes

- **High impact — Give this chapter ownership of the assessment.** Produce a compact finding for the second-country plan: required capability, current evidence, preserved strength, constraint, uncertainty and transition resources. Let the following chapter choose among implementations using that finding.
- **High impact — Correct the broad opening and distinguish lead-time measures.** Suggested opening transition: “The expansion date has been proposed before the dependencies were assessed. Alex's task is to establish what the systems and team can support, and what must change in the plan.”
- **Medium impact — Clarify the transition table's timing.** Show the spending period and when the first benefit may appear, rather than implying every cost precedes every benefit.
- **Medium impact — Relocate standardization detail.** Put the group-versus-local design discussion with acquisition integration or “Growth Into Design,” leaving a question here about constraints a mandated standard creates.
- **Low impact — Use fewer fictional projects and align the comic.** Carry the country-expansion case through the assessment, using the pricing constraint only if it is a named dependency of that same case.

## Proposed structure

Promised expansion → required capabilities → strengths and constraints → evidence about delivery and knowledge → feasible transition and funding uncertainties → assessment handed to the design decision. Keep both chapters; their separation becomes useful once the handoff is concrete.
