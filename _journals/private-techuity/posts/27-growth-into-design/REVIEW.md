# Editorial review: Turn “We Expect Growth” Into a Design Decision

Reviewed 14 September 2026. Read the full article, summary and reader-facing comic text.

## Overall assessment

The chapter connects valuation assumptions to operating requirements, technical options and a funded transition. Its intended audience includes leaders of both internally built software and bought enterprise systems. The build/buy comparison, distinction between modularity and microservices, and warning against counting a valuation sensitivity and the same future savings twice are valuable.

The main weakness is that the promised design decision remains largely a catalogue of possibilities. The worked example calculates payback, but never compares two actual designs and selects one. A categorical opening and an oversimplified risk statement also conflict with the collection's more careful reasoning.

## Detailed feedback

- **Introduction and confirmed overstatement:** “The missing connection is specific to investor-backed companies” is untenable as written. Stable ownership and investor ownership are not opposites, and founder-owned companies also translate financial expectations into technical work. The chapter's distinctive setting is an investor's particular assumption arriving without its reasoning, not the existence of this translation problem.
- **Structure and flow:** The chain of definitions is clear, but the four-column table carries a large part of the article's instructional load. Readers must compare financial priorities, build options, buy options and trade-offs while also learning seven technical terms. This deserves either several smaller comparisons or one developed example.
- **Technical depth and clarity:** “Modular boundaries don't automatically require [microservices]” is a useful correction to fashionable architecture prescriptions. The supplier-upgrade and exit-cost discussion broadens the audience appropriately. “Most companies” use a bought core with built extensions and heavy customization is “the common way” flexibility is lost are unsupported prevalence claims; state them as patterns a reader may encounter.
- **Risk reasoning:** The final table row says an expensive rebuild to avoid an unlikely failure is not worth buying. Low probability alone cannot establish that conclusion: the recovery chapter explicitly explains why a rare catastrophic outcome can dominate a decision. Replace this rule with a comparison of impact, probability, alternatives, obligations and affordability. This is a substantive internal inconsistency, not a stylistic preference.
- **Examples and accuracy:** The €200,000 outlay and €100,000 annual net savings after a one-year implementation give about three years to simple payback under the stated assumptions. The 10× sensitivity produces €1m of enterprise value, with suitable qualifications about cash and net debt. Preserve these calculations. They explain financing but need to be attached to a specific configuration, integration or replacement choice.
- **Tone, pacing and ending:** The five-answer decision record is the right destination. At present it is blank in substance: the reader is told what to fill in after several alternatives, rather than shown a completed answer. The summary and comic repeat the opening's false stable-owner/investor contrast and likewise stop before choosing a design.

## Recommended changes

- **High impact — Complete one design decision.** Carry forward the previous chapter's assessed constraint. Compare, for example, supplier configuration, a company-owned integration and a core replacement against the same customer need, delivery date, ongoing responsibility and cash limit. Choose one under explicit assumptions and name the evidence that could reverse it.
- **High impact — Correct the risk shortcut and opening across formats.** Suggested risk wording: “Compare the dependency's possible impact and likelihood with the cost and effectiveness of the alternatives; include consequences the company cannot accept.” Suggested opening: “An investor's growth assumption has reached the team as a request for flexibility. Recover the business requirement before comparing designs.”
- **Medium impact — Reformat the build/buy table.** Keep a short overview, then two smaller tables or prose comparisons. Preserve the bought-system depth; cutting it would narrow the audience again.
- **Medium impact — Make the boundary with the prior chapter explicit.** That chapter establishes capability and transition constraints; this one should select among implementations using them. Remove repeated assessment explanations once the handoff exists.
- **Low impact — Reduce generalization and definition density.** Use “a common arrangement” where evidence cannot establish “most companies,” and define technical terms beside the option that uses them.

## Proposed structure

An assessed operating constraint → two or three implementation options → trade-offs and one selected design → cash/payback implications → completed five-answer record and review trigger. Retain the valuation sensitivity as a bounded illustration, not the centerpiece.
