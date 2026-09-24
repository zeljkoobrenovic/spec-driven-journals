---
status: accepted
revised: 2026-09-24
---

# Spec: Critically Evaluate AI Costs: Measure the Return per Task and per Period

## Intent

Show a leader under investors how to read the running cost and the return of AI the company already runs, in the product it sells and in the tools its staff use, the way [[cheaper-cloud-bill]] reads a cloud bill: choose a unit of useful customer work, put every figure on one comparable basis, separate why the cost changed (usage, rates, the way the feature is built), decide how much to commit under a stated demand range, and record the exposure that remains. The reader leaves able to compute the return on an AI feature or tool per period from figures they actually have, to say what would make it stop paying, and to answer an investor who asks for "the AI ROI" with a number that has a unit, a period and a condition attached.

The chapter is the third chapter of Part VI, after cloud costs and resilience. It continues [[ai-strategy-three-questions]], whose product trial and support pilot it takes as having passed, and it complements [[scale-the-team-with-ai]], which measures capacity; this chapter measures money.

## Context

Larkspur, the book's fictional scheduling-software company, is in 2027. The document-sorting feature that three customers trialled at €300 a month each (running cost about €60 a month per customer at trial volume) passed its release gate on 11 December 2026 and is in general release to paying customers. The support assistant from the same chapter is rolled out to six agents (licences about €3,600 a year, evaluation upkeep about €4,400 a year). The coding and setup pilots of [[scale-the-team-with-ai]] have ended and their gate results are stated as assumptions, not re-argued. The people are the same (Alex technology, Priya product, Ines the company, Sam finance, Morgan the investor's adviser). Every new figure is fictional; the shared Larkspur ledger is not touched.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- **A unit that explains the business.** For the product feature, cost and return are expressed per useful customer task (a document sorted and accepted without correction), never per token or per model call alone; for the internal tools, per ticket resolved and per change completed, inheriting the definitions of [[scale-the-team-with-ai]]. Explain token, model call, inference and context at first use, and show why the same feature's token cost per task rises as prompts, retrieved context and retries grow, even when the price per token falls.
- **One comparable basis.** A table puts the feature's monthly figures on one basis: price paid by the customer, model and hosting charges, evaluation and monitoring upkeep, the share of engineering time that keeps it working, and support load, for at least two dated months, so that a margin per customer and per task can be read off and compared.
- **Separate why the cost changed.** Decompose a cost change into usage (more customers, more documents per customer), rates (vendor price per token, up or down) and construction (longer prompts, more context, retries, a larger model chosen for quality), as the cloud chapter separates usage, rates and architecture. Each cause has a different owner and a different remedy, stated.
- **Return with a unit, a period and a condition.** Define return on investment (ROI) in ordinary words, compute it for the feature and for one internal tool for a stated period, separate customer value from revenue from cash, and state the condition under which it holds (quality above the release threshold, review effort below its limit). Every ROI figure in every format carries its period and its condition; none is presented as a permanent property of the feature.
- **A commitment decision under a demand range.** The vendor offers a committed-spend discount for a year. Decide how much to commit against a stated range of expected usage, show the cost at the low, expected and high ends with and without the commitment, treat a committed minimum as an obligation like the cloud chapter's minimum spend, and check what an ownership change or a vendor price change does to it. Record the decision with chosen option, alternatives rejected, funding, who is authorized, a dated review and the evidence that would reopen it.
- **The stop and reprice rules.** State, before the review, what would make the feature stop paying: a token cost per task above a named fraction of the price, quality below the threshold, a vendor price rise above a named level, or customers declining the price at renewal, and what the response to each is (reprice, change the construction, change model, withdraw). Tie the customer promise to the trial's conditions, not to open-ended continuation.
- **Investor questions answered as they are asked.** Give the leader answers to "what is our AI ROI", "why is the AI bill growing faster than revenue" and "should we commit to a bigger contract" that each point at the unit, the decomposition and the commitment decision above rather than at a single number.
- **House rules.** Status highlight and key points readable without prior study; terms explained in each format; the company leader's decision, authority and funding assumptions explicit; historical findings within source scope, fictional scenarios labelled; a meaningful counterargument (a feature can be worth keeping at a loss for a period if it wins renewals, but only with a dated limit and the loss stated) with the evidence that would change the judgment; hand-off to Part VII; TL;DR and comic consistent with the article.

## Non-goals

- Not a repeat of the three AI investment questions, the trial design or the support pilot; those are taken as done and linked.
- Not a capacity or headcount argument; that is [[scale-the-team-with-ai]].
- Not a vendor or model comparison, a price list, or a forecast of token prices; figures illustrate the method and are labelled fictional. No prevalence claims about AI margins in general.
- Not a data-protection or security treatment beyond what the commitment decision needs; the NIST profile is linked, not taught.

## Modalities

- [ ] `checklist.md` — not used in this journal's main chapters.
- [x] `summary.md` — TL;DR of 300–500 words with one overview visual.
- [ ] `dialog.md` — not used.
- [x] `comics.md` — comic pages of three stacked strips, same cast as the neighbouring chapters, reaching the commitment decision causally.

## Open questions

- Which external sources to register: [S16] FinOps unit economics already exists and fits; a vendor pricing page or a published token-pricing history would need fetching and dating before use, and the chapter may do without it by keeping all prices fictional.
- Whether the internal-tool return uses the support assistant (figures exist in [[ai-strategy-three-questions]]) or the coding tool (figures exist in [[scale-the-team-with-ai]]); the default is the support assistant, whose annual figures are already stated, with the coding tool mentioned once.

## Decision log

- 2026-09-24: The author asked for an AI chapter in SUSTAIN about AI return on investment and token costs. Scope is both AI in the product and internal tools (author's choice over product-only or tools-only), the scenario continues the AI strategy chapter's product example (author's choice over a separate example), and the endpoint is a recorded commitment decision under a demand range like the cloud chapter (author's choice over a method-only chapter).
- 2026-09-24: Title form follows the SUSTAIN neighbours' imperative-plus-claim pattern. First title “Keep AI Worth Its Cost: Tokens Are a Running Cost, Not a Licence” was rejected by the author as unclear (it compressed the part name and the licence-versus-usage point into jargon); replaced by “Critically Evaluate AI Costs: Measure the Return per Task and per Period”, which parallels the cloud chapter and names the method. Also considered: “Measure AI Return on Investment: The Bill Grows With Use and With How You Build”, “Track AI Running Costs: A Usage Bill Moves After You Approve It”.
- 2026-09-24: Placed third in Part VI so that the unit-cost method arrives from the cloud chapter and the quality prerequisite from the resilience chapter before both are applied to AI.

## Sources

- Author's intent from the 24 September 2026 conversation (no `INPUT.md`).
- [[ai-strategy-three-questions]] — the document-sorting trial (€300 price, about €60 running cost per customer at trial volume, quality and review thresholds, release gate 11 December 2026) and the support assistant's annual figures; this chapter continues them.
- [[cheaper-cloud-bill]] — the unit, the comparable basis, the usage/rates/architecture decomposition, the commitment decision under a demand range and the minimum-spend treatment this chapter mirrors.
- [[scale-the-team-with-ai]] — the capacity definitions the internal-tool return inherits.
- [[prove-you-can-restore]] — quality as a prerequisite before a saving is counted.
- Bibliography: [S16] FinOps unit economics; [S18] NIST generative AI profile (linked only). Further sources only after verification.

## Changelog

- 2026-09-24: Status `accepted` at the author's instruction (“all of it”) after the article, TL;DR, comic, figures, logo, icon and Probe Further were produced; the folder-placement open question is resolved by the renumbering.
- 2026-09-24: Retitled at the author's request (see decision log); permalink `ai-worth-its-cost` unchanged.
- 2026-09-24: Created as `draft` from the author's intent; scope, scenario and endpoint decisions recorded. No `index.md` yet.
