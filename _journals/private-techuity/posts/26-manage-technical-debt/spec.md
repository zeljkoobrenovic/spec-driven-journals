---
status: accepted
revised: 2026-09-24
---

# Spec: Manage Technical Debt: Fund the Fix by the Cost, the Risk and the Speed It Buys

## Intent

Give a leader under investors a way to manage technical debt and the large projects that reduce it (refactors, rewrites, migrations, forced platform and vendor moves) as a running cost with three columns rather than as a backlog or a percentage: what the debt costs to carry each month, what risk it carries, and what it slows. Show how to put those three on figures the company already has, separate where the debt came from so each part has an owner and a remedy, present a reduction project to the board by the revenue it protects or enables, the cost or risk it removes and the decision it keeps open, and fund it in tranches, each released against a measured reduction in the carrying cost. The reader leaves able to answer "how much technical debt do we have" with a carrying cost, "why not a rewrite" with a transition plan, and "why fund work that changes nothing customers see" with the risk and speed columns.

The chapter is the fourth chapter of Part VI, after cloud costs and AI costs. It takes the *execution and funding over time* of debt-reduction work; the choice of design belongs to [[growth-into-design]], transition costing to [[can-the-team-deliver]], integration to [[acquisition-adds-work-first]].

## Context

Larkspur, the book's fictional scheduling-software company, has completed option B from [[growth-into-design]]: the country-specific billing rules were separated out of the invoicing module into a component Larkspur owns, the month-four replay passed, the second country went live in month eight, and the billing engineer now maintains the component. That project is the chapter's model of a tranche done right, and the module that remains is still fragile in other ways. The chapter adds a fictional **debt register** of four or five items across the estate (the remaining tangles in the invoicing module; a reporting stack on an unsupported framework version; the scheduling engine's single-node design that limits the largest customers; the AI feature's hard-coded prompt logic kept from the trial; a retiring vendor model with a dated notice from [[ai-worth-its-cost]]), each with its three-column carrying cost. Same people (Alex technology, Priya product, Ines the company, Sam finance, Morgan the investor's adviser). Every new figure is fictional; the shared Larkspur ledger is not touched, and the €300,000 expansion budget of the design chapter is not reused.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- **Three-column carrying cost, on figures the company has.** Define technical debt in plain words and put each register item on one table with three columns per month: cost carried (engineering hours on workarounds and the old stack's licences and hosting, labelled cash or cost-based estimate), risk carried (incidents, unsupported or insecure components, restore evidence from [[prove-you-can-restore]], a dated vendor retirement), and speed lost (lead time on the change types customers pay for, from the trace in [[fix-decisions-before-hiring]], and releases that cannot ship). No item is described by a count of issues, a percentage of the codebase or a "debt ratio". The reader can build the same table for their own estate.
- **Separate where the debt came from.** Sort the register by origin, deliberate dated shortcut, growth outrunning design, acquired system not yet integrated, ageing platform or retiring vendor, and state for each origin who owns it and what the remedy usually is. Say that a deliberate shortcut with a recorded date and owner is not a failure; an undated one is.
- **Present the project the way the board reads money.** For the chosen tranche, state what revenue it protects or enables, what cost or risk it removes and, only where a real dated decision is being kept open, what decision it preserves; use the three benefit kinds as the book's own vocabulary and cite the Grounded Architecture economics page, Fowler and Hohpe as sources, with the caveat that neither internal quality nor an option's value can be measured precisely, so the tranche is judged on the carrying-cost columns it moves. Explain why the board rarely sees the failures a fix prevented, citing Repenning and Sterman, and answer it with the register's before-and-after figures rather than with a plea.
- **Large projects are transitions funded in tranches.** Compare, for one register item, three ways to reduce it: a big-bang rewrite whose benefit arrives at the end, a tranche plan in which each stage releases a measured reduction in carrying cost and the next stage is funded by a gate, and living with it at a stated cost; show dual-running cost, the work that waits, and the point at which spent money no longer counts, as [[growth-into-design]] does. Name the anti-pattern of the rewrite with the benefit at the end and the one situation in which it is still right (a retiring platform with a hard date).
- **A recorded decision with a gate.** End with the funded first tranche: chosen option, alternatives rejected, funding, scarce capacity, who is authorized, the gate that releases the second tranche (a named reduction in each of the three columns, with what happens when it is met, missed or falls between), what waits, and the evidence that would stop or reprioritize; the register is revisited on a stated cadence, and items with a dated external deadline (vendor retirement, an unsupported version) are sequenced by the date, not by the size of their carrying cost.
- **Investor questions answered as they are asked.** Give the answers to "how much technical debt do we have", "why not just rewrite it" and "why are we funding work customers will not see", each pointing at the register, the tranche plan and the three columns.
- **House rules.** Status highlight and key points readable without prior study; terms explained at first use in each format (technical debt, refactor, migration, rewrite, dual running, tranche, unsupported version, carrying cost); the company leader's decision, authority and funding assumptions explicit; historical findings within source scope, fictional scenarios labelled; a meaningful counterargument (some debt is worth carrying to the exit and saying so is honest) with the evidence that would change the judgment; hand-off to Part VII; TL;DR and comic consistent with the article.

## Non-goals

- Not a second treatment of the design choice (configure, own the boundary, replace the core); that stays in [[growth-into-design]] and is linked.
- Not a code-quality or architecture tutorial, a tooling recommendation, or a metric such as a debt ratio or a static-analysis score; the chapter's measures are the three carrying-cost columns.
- Not a cloud-provider migration, which is handled by reference to [[cheaper-cloud-bill]], and not a treatment of an acquired system's integration, which is [[acquisition-adds-work-first]].
- No prevalence claims about how much debt companies "typically" carry; no invented study results; the downtime-cost figures on the inspiration page are not reused.

## Modalities

- [ ] `checklist.md` — not used in this journal's main chapters.
- [x] `summary.md` — TL;DR of 300–500 words with one overview visual.
- [ ] `dialog.md` — not used.
- [x] `comics.md` — comic pages of three stacked strips, same cast as the neighbouring chapters, reaching the first tranche decision causally.

## Open questions

- Which register item carries the tranche comparison: the scheduling engine's single-node design (speed and opportunity dominate) or the unsupported reporting stack (risk and a hard date dominate). Default: the scheduling engine for the tranche comparison, with the reporting stack as the dated item that is sequenced first regardless of size, so both kinds appear.
- Whether to register the three external sources in the bibliography as new S-ids (they were fetched and verified on 24 September 2026; see Sources) or cite them inline only.

## Decision log

- 2026-09-24: The author asked for a SUSTAIN chapter on technical-debt management and similar projects (big refactors, migrations), taking the Grounded Architecture economics page as inspiration. The author's correction to the first proposal: the chapter is not only about cutting cost but about reducing risk (an old stack can be unstable and insecure) and creating opportunity (moving and releasing faster); hence the three-column carrying cost and the title. Author's choices: continue the design chapter's completed project as the model tranche rather than a separate example; scope includes own-code debt and platform or vendor migrations; the inspiration page's frameworks (top line and bottom line, options, the debt ROI compounding of operating cost, delay and instability) are absorbed into the book's vocabulary and cited rather than presented as named frameworks.
- 2026-09-24: Title chosen by the author from three candidates: "Manage Technical Debt: Fund the Fix by the Cost, the Risk and the Speed It Buys". Rejected: "…: Pay Down What Costs You, Risks You and Slows You"; "…: Fund the Fix by What It Removes and What It Frees"; the earlier cost-only "…: Fund the Fix by the Cost It Removes".
- 2026-09-24: Placed fourth in Part VI so the unit-cost and commitment methods (cloud, AI) and the quality prerequisite (resilience) precede it.

## Sources

- Author's intent from the 24 September 2026 conversation (no `INPUT.md`).
- [Grounded Architecture: Economics](https://grounded-architecture.io/economics), the author's own framework page, fetched 24 September 2026: ROI and options metaphors, the top-line/bottom-line value framework, the technical-debt ROI compounding (extra operating cost, cost of delay, instability cost) and the unsustainable-code spiral. Linked also through [[grounded-architecture-portfolio]].
- Martin Fowler, [Is High Quality Software Worth the Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html), 29 May 2019, fetched 24 September 2026: internal quality lowers the cost of later change; the author's caveat that delivered functionality cannot be measured precisely.
- Gregor Hohpe, [Architecture: Selling Options](https://architectelevator.com/architecture/architecture-options/), 17 October 2016, fetched 24 September 2026: architecture as deferring a decision at a known price; value rises with uncertainty.
- Nelson P. Repenning and John D. Sterman, [Nobody Ever Gets Credit for Fixing Problems that Never Happened: Creating and Sustaining Process Improvement](https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf), California Management Review 43(4), Summer 2001, fetched 24 September 2026 (first page confirmed): why improvement work is under-invested when its benefit is invisible.
- [[growth-into-design]] (the completed option B, its replay gate and fallback), [[fix-decisions-before-hiring]] (the trace and lead time), [[prove-you-can-restore]] (restore evidence as the risk column), [[ai-worth-its-cost]] (the retiring-model notice), [[can-the-team-deliver]] (transition costing), [[acquisition-adds-work-first]] (integration as a boundary transition), [[teamsystem]] (acquired systems not yet working together).

## Changelog

- 2026-09-24: Status `accepted` at the author's instruction (“all of it”) after the article, TL;DR, comic, figures, logo, icon and Probe Further were produced; the folder-placement open question is resolved by the renumbering.
- 2026-09-24 (order): Moved to open Part VI at the author's request, because its three-column register frames the part and the other three chapters each deepen one column; the opening paragraph and the closing hand-off now point forward to [[prove-you-can-restore]], [[cheaper-cloud-bill]] and [[ai-worth-its-cost]]. Article otherwise unchanged; folder to be renumbered `26-manage-technical-debt`.
- 2026-09-24: Created as `draft` after the author validated the approach; scenario, scope, framing and title decisions recorded. No `index.md` yet.
