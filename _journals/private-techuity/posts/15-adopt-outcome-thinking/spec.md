---
status: accepted
revised: 2026-09-24
---

# Spec: Adopt Outcome Thinking: Balance Customer and Business KPIs

## Intent

Open Part IV with the practice that keeps a company building things that create real value for customers while connecting that value, explicitly and on an honest clock, to the business results and investor metrics the plan is held to. The chapter delivers an artifact rather than a culture: an **outcome record** with one key customer outcome in the customer's language, one key business outcome the leadership agrees on, the causal chain between them (drivers, leading and input metrics, lagging results), the investor metric each business outcome feeds and the horizon on which it moves, and the split between what product influences and what sales and customer success own. Every later chapter of Part IV uses that record: priorities are set against it, the revenue chain is tested through it, AI questions are sorted by it, capability is sized to it. The reader leaves able to answer an investor's "what is your north star", "why is product not judged on this quarter's revenue" and "which of our metrics does product actually move", and to say no to a loud request with the record rather than with a fight.

The chapter is a translation for leaders under investors of the author's product-management operating model ([[outcomes]], [[goals-and-questions]], [[lanes]], [[balanced-roadmap]], [[business-collaboration]]) and of the customer-and-business KPI pyramids of the Productscape domain model, written in the book's third-person, evidence-first voice rather than the journal's first person.

## Context

Larkspur, the book's fictional scheduling-software company, at the start of the shared chain that the chapters [[diligence-corrects-the-plan]], [[first-hundred-days]], [[cannot-fund-everything]], [[roadmap-to-revenue]] and [[handover-of-obligations]] follow (canonical facts in `_research/shared-scenario-record.md`, which the article must not contradict): setting up a new customer, called onboarding, takes about 80 hours of a specialist's time on the baseline of twelve implementations; the customer waits a median of about ten weeks from signed contract to first real schedule; the diligence finding D-3 says setup depends on one specialist; the initiative ONB-1 (€180,000, twelve engineer-weeks, €30,000 a year maintenance) targets the setup work; the day-90 cohort of eight came in at 62 hours; gate 2 at month six needs ≤ 50 hours and a median wait of eight weeks or less; capacity at €75 an hour is capacity, never cash, until a dated conversion; the investor's thesis includes a second country and later a third. Same people (Alex technology, Priya product, Ines the company, Sam finance, Morgan the investor's adviser). The chapter writes the outcome record those chapters later execute and measure; it introduces no new shared figures.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance or product-management background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- **Outcomes, not outputs, defined so a newcomer can apply it.** Define outcome (a measurable change in the customer's or the company's reality), output (what was shipped), key performance indicator (KPI), leading and lagging indicator, and vanity metric in plain words at first use. Give the test for a strong customer metric: it would still matter if the product changed completely, and customers confirm they would pay, renew or expand to get it. Show the contrast table "what this says / what it does not say" (shipping still matters; usage counts only when it connects to value; product is judged over quarters and years but is still accountable).
- **One customer outcome, one business outcome, agreed.** For Larkspur, name the key customer outcome in the customer's language (a new customer scheduling real work within weeks of signing, without Larkspur's specialist doing the setup by hand) with its metric (median weeks from contract to first real schedule; setup hours per customer as the driver) and the key business outcome the leadership agrees on (retention and expansion of paying customers, feeding the investor's second-country thesis), and show Ines getting the executive team and the investor director to agree on the one business result product optimizes for, so the roadmap is not a treaty negotiation.
- **Two pyramids and the chain between them.** Build the customer-outcome pyramid and the business-outcome pyramid (top, drivers, leading inputs, lagging confirmations; every non-leaf node with at least two children, as the Productscape model requires), connect the nodes where they reinforce each other, and mark which business nodes product influences directly and which belong to sales, marketing or customer success. Apply the removal test: a node whose removal changes what a team does next week is a causal model; one that changes only a slide is deckware.
- **The investor bridge, on an honest clock.** Define annual recurring revenue (ARR), net revenue retention (NRR), gross margin and cash conversion in plain words, state which of them the business outcome feeds and on what horizon (product moves NRR over quarters and years; sales moves this quarter's bookings), and show the negotiation with the investor about grading product on its natural horizon while still reporting the lagging indicators when they arrive. Relate the metrics to what Parts I and II already defined (revenue, EBITDA, cash, the valuation multiple, the thesis) rather than introducing a parallel vocabulary.
- **Balance as an allocation.** Show customer value before value capture (over-monetization announces itself as churn), and show the roadmap as an allocation across innovation, iteration and operation decided before ranking, with the outcome record deciding what enters each slice; hand the ranking and the cash and capacity limits to [[cannot-fund-everything]] without repeating it.
- **Outcome-centricity has a price list.** State, with Cutler, that it is a causal model plus habits, not a mindset: a few durable outcome lanes per team with a couple of metrics and a weekly rhythm; goals mixed across learning, shipping and outcome types and kept as a habit; powerful ideas imperfectly measured preferred to perfect measures of weak ideas, with the measurement bar improving over time rather than filtering for small ideas. Name the anti-patterns (feature factory, vanity dashboard, afterthought metric, measurement veto, grading product on the sales clock, deckware pyramid).
- **The recorded outcome record.** End with Larkspur's record: customer outcome and metric, business outcome and metric, the pyramids' top three levels, the investor metric and horizon, what product does not own, the lanes and their input metrics for the next two quarters, who agreed (Ines, Priya, Alex, Sam, the investor director) and the review cadence; and say which later chapters test each part of it (priorities in [[cannot-fund-everything]], the chain in [[roadmap-to-revenue]], the gates in [[first-hundred-days]]).
- **Investor questions answered as they are asked.** "What is your north star", "why is product not judged on this quarter's ARR", and "which of our metrics does product actually move", each pointing at the record.
- **House rules.** Status highlight and key points readable without prior study; terms explained at first use in each format; the company leader's decision, authority and funding assumptions explicit; fictional scenarios labelled and consistent with the shared ledger; a meaningful counterargument (an investor with a short holding period can reasonably want lagging results sooner; the answer is a dated plan with leading indicators reported now, not a refusal) with the evidence that would change the judgment; hand-off to [[cannot-fund-everything]]; TL;DR and comic consistent with the article.

## Non-goals

- Not a product-management textbook, a discovery or research method, or an OKR manual; the chapter delivers the outcome record and the investor bridge, and links the journal records and sources for the rest.
- Not the prioritization arithmetic (that is [[cannot-fund-everything]]), not the pilot measurement and its six kinds of benefit (that is [[roadmap-to-revenue]]), not team topology or coaching.
- Not a claim that outcome practice guarantees results; no invented study results, no prevalence claims about what companies "usually" measure, no new figures in the shared ledger.

## Modalities

- [ ] `checklist.md` — not used in this journal's main chapters.
- [x] `summary.md` — TL;DR of 300–500 words with one overview visual.
- [ ] `dialog.md` — not used.
- [x] `comics.md` — comic pages of three stacked strips, same cast as the neighbouring chapters, reaching the agreed outcome record causally.

## Open questions

- Whether the SaaS metric definitions (ARR, NRR, gross margin, cash conversion) also go into the glossary.
- Whether to register the external sources (Build What Matters, EMPOWERED, TBM 435, the North Star Playbook, Outcomes Over Output) as S-ids or cite them inline and through the journal records.

## Decision log

- 2026-09-24: The author asked for a first chapter of Part IV on adopting an outcome culture and product thinking, balancing customer and business KPIs, motivated as one of the best frameworks for building what creates real customer value while connecting it explicitly to business KPIs and investor metrics; inspiration: the author's grounded-product-management journal and the Productscape start packages (customers, products, teams, objectives, with customer- and business-outcome KPI pyramids per customer type), plus conventional product-management literature.
- 2026-09-24: Author's choices from the proposal: title "Adopt Outcome Thinking: Balance Customer and Business KPIs" (rejected: the longer "Adopt Outcome Culture and Product Thinking: …", and "Judge Work by Outcomes: …"); the shared onboarding chain carries the outcome record (rejected: a separate example); the SaaS investor metrics are named and defined explicitly (rejected: staying with the book's existing finance terms only). Suggestions accepted into the contract: deliver an artifact rather than a culture; make the chapter the frame for Part IV with one forward link from each later chapter; the investor bridge with horizons as the distinctive part; balance as an allocation; Cutler's corrective against "mindset" talk.
- 2026-09-24: The Productscape overview page is script-rendered and unreadable by fetch; its KPI pyramid model was taken from the local toolkit reference (`productscape/skills/_references/domain-model.md`) and the travel-accommodations example (customer-outcome and business-outcome pyramids per persona; team metrics linked by name to pyramid nodes).

## Sources

- Author's intent from the 24 September 2026 conversation (no `INPUT.md`).
- The author's grounded-product-management journal: [[outcomes]] (Build What Matters: outcome pair, strong metrics, two pyramids, time horizons), [[goals-and-questions]] and [[lanes]] (Cutler, TBM 435: causal model, lanes, mixed goals, powerful ideas imperfectly measured, removal test), [[balanced-roadmap]] (innovation, iteration, operation allocation), [[business-collaboration]] (EMPOWERED: partnership, not stakeholder management), [[team-objectives]].
- Productscape domain model, local toolkit reference `productscape/skills/_references/domain-model.md` (KPI pyramid model: customerOutcomes and businessOutcomes per persona, shape invariant, team metrics linked by name) and the travel-accommodations example (search-to-book conversion; net booked room-night contribution), read 24 September 2026.
- John Cutler, [TBM 435: 20 Unfiltered Operating Takes](https://cutlefish.substack.com/p/tbm-435-20-unfiltered-operating-takes), The Beautiful Mess, 8 August 2026, fetched 24 September 2026.
- Amplitude, [The North Star Playbook](https://amplitude.com/north-star) (John Cutler co-author), fetched 24 September 2026: North Star metric with input metrics; used as a teaching tool per Cutler's caveat.
- Ben Foster and Rajesh Nerlikar, *Build What Matters* (2020), and Marty Cagan with Chris Jones, *EMPOWERED* (2020), through the journal records above; Josh Seiden, *Outcomes Over Output* (2019), candidate for Probe Further after fetching.
- Book records: [[cannot-fund-everything]], [[roadmap-to-revenue]], [[first-hundred-days]], [[diligence-corrects-the-plan]], [[three-different-returns]] and [[obligations-before-budget]] (the finance terms already defined), [[different-bets]] (investor incentives and horizons).

## Changelog

- 2026-09-24: Status `accepted` at the author's instruction (“all of it”) after the article, TL;DR, comic, figures, logo, icon and Probe Further were produced; the folder-placement open question is resolved by the renumbering.
- 2026-09-24: Created as `draft` after the author answered the title, scenario and investor-layer questions. No `index.md` yet.
