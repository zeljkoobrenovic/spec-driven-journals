---
title: "The First Hundred Days: Turn Expectations Into a Funded Plan"
date: 2026-09-12
author: Owned working manuscript
excerpt: "Carry one diligence finding into a plan with named accountability, approved cash, protected engineer-weeks, decision dates and recorded deferrals, then let the day-100 review change the plan."
permalink: first-hundred-days
timetoread: 10 min read
logo: "assets/images/17-first-hundred-days/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/17-first-hundred-days.png"
---

> **IN THIS SECTION, YOU WILL:** Learn to carry a diligence finding into a plan with named accountability, approved cash, protected engineer-weeks and decision dates, and let the day-100 review change it.

> **WHY INVESTORS CARE:** The early period is when the investor learns whether the thesis survives contact with the company; a funded plan with dated reviews gives it evidence, and an untested list gives it only reassurance.

> **WHY YOU SHOULD CARE:** Expectations formed during the transaction either become a plan the company can fund and staff, or harden into commitments nobody tested; the early period decides which.


> **KEY POINTS:**
>
> * Use the early period to **establish a funded plan**, not to finish the transformation. A plan exists when each priority has an accountable person, approved cash, protected engineer-weeks, a decision date and a prerequisite, and when the deferred work has a recorded decision.
> * Carry the diligence findings in **by identifier**. Confirm each one with the people who will do the work; the transaction process worked with incomplete access, and management’s evidence should change funding and sequence when it differs.
> * **Review the plan, not its completion rate.** The day-100 review should change something: a revised assumption, a deferral kept or lifted, money moved from the reserve. Finishing every task is not the test.

<br>
New funding or an ownership change opens an early period in which expectations must become an agreed **operating plan**: what the business will do, who will do it and what resources it needs. A hundred days is a useful planning horizon. It is neither enough to transform most businesses nor the right deadline for every commitment.

The transaction introduces new assumptions and review dates, and it can introduce a new review timetable and expectations formed during diligence rather than inside the company. Confirm which of them change the company’s existing plan. This is when those expectations either become a plan the company can fund and staff, or harden into commitments nobody tested.

[[diligence-corrects-the-plan]] produced three material findings before the growth investment in fictional Larkspur closed. This chapter shows those findings becoming the company’s own plan: confirm the assumptions, fund a small set of priorities inside an authorized envelope, sequence their dependencies, establish baselines and let the review at day 100 change the plan. Every figure is fictional.

## What Actually Changed

This chapter follows one scenario: a growth investment whose thesis is that Larkspur can double onboarding volume without proportional growth in implementation staff. What changed is money, expectations and a review timetable. The Larkspur board has authorized an envelope for the first hundred days of up to €300,000 additional cash and 24 engineer-weeks; existing payroll stays in the operating budget. The fund’s investment committee approved the transaction terms; the board, not the investment committee, approves the operating plan and its funding.

Other arrangements change different things. A minority round may leave management in place and add an evidence milestone; a buyout changes control and adds financing obligations; a corporate acquisition adds a parent and integration decisions. [[raise-what-you-need]] compares those arrangements; the method below is the same, but begin with what changed in money, rights, dependencies and expectations. A further round does not necessarily replace the founder or management, and a buyout does not make every existing practice wrong.

## Confirm the Inherited Finding With the People Who Will Deliver It

**Due diligence**, the investigation supporting an investment decision, takes place with incomplete information and a transaction timetable. After **closing**, when the transaction legally completes, management can test assumptions more directly and involve people who were absent from the deal process.

Finding **D-3** arrives with its identifier, its record and a handoff: Priya records acceptance within ten days of closing, first review at day 90.

| D-3: onboarding depends on one specialist’s manual configuration | |
| --- | --- |
| Original assumption in the thesis | Onboarding volume doubles with the same implementation team. Revised during diligence to 1.5× for year one, with second-country expansion conditional on pilot evidence. |
| Diligence evidence | Five of the last twelve implementations sampled, one country, two quarters; three needed the same specialist’s manual work; about 80 hours per implementation. Morgan inferred a structural dependency; Alex reported that roughly 40% of the effort is poor customer data. The split was not established. |
| Management’s confirmation after closing | Priya, Alex and the implementation specialist reviewed the finding with the people who run implementations. The dependency is confirmed. Because the diligence sample covered one country and two quarters, management does not adopt the sampled 80 hours as the baseline; the baseline will be measured from actual customer records by day 20. Alex’s data-quality explanation stays on the record as the disagreement the pilot must resolve. |
| Funded response | ONB-1, the onboarding pilot: €180,000 committed to build one reusable setup step, 12 engineer-weeks, Priya accountable, cohort review at day 90. |

Two points matter for a reader whose own findings arrive in a report. First, the pilot was written into the plan as a funded condition during diligence, so it does not have to compete for money as a surprise. If a required investment was left out of **underwriting**, the financial and risk assessment used to justify the deal, make the funding issue explicit rather than handing it to the CTO as a delivery challenge with the financial model unchanged. Second, management did not endorse the finding as written; it kept the dependency, rejected the sampled figure as a baseline and set a date to replace it. That is confirmation, not ceremony.

The other two findings were confirmed the same way: **D-5**, the scheduling engine is understood by two people, and **D-6**, there is no evidence the service can be restored completely.

## A Funded Plan for the First Hundred Days

A starting proposal is to select three to five important early moves. That is a useful constraint on attention, not a universal optimum; a company in distress or a carve-out with a hard separation date may need a different structure. Larkspur’s three priorities fit the envelope. All figures are fictional.

| Priority | Accountable | Additional cash | Engineer-weeks | Decision date | Prerequisite |
| --- | --- | ---: | ---: | --- | --- |
| ONB-1: onboarding pilot (from D-3) | Priya | €180,000 committed; about €90,000 spent within the period | 12 | Day 90 cohort review | Baseline from actual customer records by day 20 |
| KNW-1: second engineer able to release and recover the scheduling engine (from D-5) | Alex | €0 (specialist time protected) | 4 | Day 60 demonstration | None |
| REC-1: restore test against the recovery objective (from D-6) | Alex, with the operations lead | €80,000 | 4 | Day 45 test; retest by day 90 | Restore environment and access |
| **Total** | | **€260,000** | **20** | | Reserve: €40,000 and 4 engineer-weeks |

The envelope was €300,000 and 24 engineer-weeks; the plan commits €260,000 and 20 engineer-weeks and leaves a reserve of €40,000 and 4 engineer-weeks for what the reviews find. The cash column counts commitments, not spending: ONB-1 commits €180,000 even though only about €90,000 is spent before day 100. The recovery objective REC-1 tests against is the one agreed in [[prove-you-can-restore]]: dispatch must resume within four hours of a failure, with no more than fifteen minutes of lost schedule updates. It is an agreed fictional objective, not a legal standard.

**Unselected work remains visible.** A short priority list is not permission to defer a material risk without a decision. Larkspur deferred three items, each with a decision recorded: the customer portal (research only, not yet funded), second-country expansion (conditional on ONB-1 evidence, as agreed during diligence) and hiring two implementation specialists (about €300,000 a year recurring, pending pilot evidence). Distinguish active priorities, accepted risks, monitored conditions and later opportunities; each deferred material risk still needs someone authorized to say it is accepted or monitored.

The decision, in full. The chosen plan is the three priorities above. Rejected alternatives: funding the portal now (its benefit is still uncertain and its engineer-weeks exceed what remains), hiring the two specialists now (recurring cost before the effort split is known) and starting the second country (the thesis assumption it depends on is the one under test). Funding is €260,000 of the €300,000 the board authorized. The scarce capacity is 20 of 24 engineer-weeks, plus the two specialists whose time cannot be spent twice: the implementation specialist on ONB-1 and the scheduling specialist on KNW-1. The board is authorized to approve the plan; Priya and Alex are accountable for the results. The evidence that would change the plan: the ONB-1 cohort’s measured effort and its split between data quality and product limitation, the day-45 restore, and the day-60 demonstration.

This plan does not promise that the second country is open by day 100. It creates the evidence needed to **fund and sequence that expansion**. A short early plan should reduce uncertainty and establish capability, not disguise a multi-year program as a quick win.

![Ideas become operating commitments when outcomes, responsibility, funding, capacity and review dates are agreed.](assets/images/17-first-hundred-days/priorities-become-commitments.jpeg)
**Figure 1:** *An early priority list becomes a plan through explicit decisions and resources.*

## Sequence the Dependencies and Accept Imperfect Baselines

Map dependencies before promising parallel delivery. REC-1 cannot start until the restore environment and access exist, which is why its cash is committed first and its test sits at day 45, leaving time for a retest. ONB-1 cannot measure the pilot cohort against a baseline that does not yet exist, so the baseline from actual records is due by day 20 and the cohort follows it. KNW-1 needs the scheduling specialist’s time protected for four weeks; that time comes out of the same operating budget that keeps the service running, so nothing else may claim it. A plan that uses the same people twice is not ambitious; its resource arithmetic is incomplete.

Separate actions useful under several plausible plans from investments that depend on an assumption still being tested. REC-1 and KNW-1 are worthwhile whether or not the second country opens. ONB-1 is the learning step that improves the larger decision, which is why it was funded first and expansion was not.

![Projects that depend on the same specialist or prerequisite need deliberate sequencing.](assets/images/17-first-hundred-days/dependencies-before-parallel-projects.jpeg)
**Figure 2:** *Adding projects cannot create the capacity or prerequisites they depend on.*

A **baseline** is the starting measurement used to judge later changes. Early baselines are imperfect. Document their weaknesses rather than waiting for a perfect dashboard: define the population, period and data source, and preserve the original version when definitions improve. For onboarding, measure internal effort and customer waiting time separately, because a process can use fewer internal hours while leaving the customer waiting just as long. For costs, distinguish identified savings from realized expenditure, and agree with Sam how economic claims will be reconciled so a local improvement is not counted twice across the plan.

## Investor Support Inside the Plan

ONB-1 uses outside specialist support, agreed through the **engagement charter** developed in [[useful-engagement]]: the specialist’s days, the company engineering effort, the customer sessions, Priya as the accountable company leader, an investor-side sponsor named by role and a review at week six. The charter is where that chapter completes the example; here it matters only that the support is inside the plan’s capacity, not added on top of it. Coordinate any investor-sponsored intervention through company leadership and one capacity view, and make the purpose of any assessment clear to the people involved.

## Review the Plan, Not Its Completion Rate

At day 100 the board asked what was learned and what the company can now do, not how many tasks were complete. The results, all fictional:

- **REC-1.** The day-45 restore took eleven hours and failed the business test: a missing credential and an unavailable database version, the same two obstacles as in [[prove-you-can-restore]]. Corrected and retested at day 85, dispatch resumed within the four-hour objective with under fifteen minutes of lost updates. A pass at day 45 would have been a worse result than this one, because the plan would have contained no evidence that the obstacles existed.
- **KNW-1.** Passed at day 60: a second engineer released and recovered the scheduling engine without the specialist.
- **ONB-1.** Cohort of eight customers. Effort fell from 80 to 62 hours per implementation, not the 50 the teaching model in [[roadmap-to-revenue]] assumed. About 40% of the remaining hours traced to customer data quality, so Alex’s explanation was partly supported and Morgan’s structural explanation was not wrong either. Customer waiting time was unchanged, which the separate measurement made visible.

The review changed the plan. The board kept second-country expansion deferred for one more quarter, because 62 hours with unchanged customer waiting time does not yet support 1.5× volume with the same team. It funded a data-quality step from the reserve, €40,000 and 4 engineer-weeks, because the measured split now pointed there rather than at more product work. Hiring the two specialists stays deferred. The handover record carries D-3 and ONB-1 forward with the baseline, the actual cost to date, the observed result and the open work.

Completing every planned task is not success if the tasks addressed the wrong constraint. Revising a major assumption is a valuable outcome even when it reduces the original growth forecast, and the review should reward that judgment rather than the preservation of the transaction story. The early period should leave a plan whose accountable leaders understand the work, whose funding and capacity are credible, and whose assumptions can be reviewed.

The plan above assumes the money it was built on arrives when expected. The next chapter takes the same kind of dated plan and asks what changes when financing slips: [[the-financing-slipped]]. The continuing obligations this plan creates, including D-3 with its baseline and open work, are handed to the next owner in [[handover-of-obligations]].

## Questions to Consider

1. *What changed for your company at the last transaction: money, rights, dependencies or expectations? Which review dates did it introduce?*
2. *Which diligence findings did the people who will deliver the plan confirm, which did they change, and did any change the funding or the sequence?*
3. *For each early priority, can you name the accountable person, the approved cash, the protected engineer-weeks, the decision date and the prerequisite? Which material risks were deferred, and who decided?*
4. *What did your last review change? If the answer is nothing, was that because the plan was right or because completion was the only thing measured?*

## To Probe Further

- **[The First 90 Days, Updated and Expanded](https://store.hbr.org/product/the-first-90-days-updated-and-expanded-proven-strategies-for-getting-up-to-speed-faster-and-smarter/11323)** — Michael D. Watkins, Harvard Business Review Press, 2013.<br>*It covers the part this chapter leaves out, the leader’s own transition, including how to renegotiate expectations with the people who now hold authority over you.*
- **[Private Equity’s Road Map to Profits](https://www.bain.com/contentassets/d7f768bd07d24539a55d069662ffc090/private_equitys_road_map_to_profits_bainbrief_2007.pdf)** — Chris Bierly, Graham Elton and Chul-Joon Park, Bain & Company, 2006.<br>*It shows the 100-day plan from the owner’s side, with the caveat that Bain sells this work, so it describes practice rather than proving results.*
- **[Value Creation in Private Equity](https://www.ebrd.com/home/news-and-events/publications/economics/working-papers/value-creation-in-private-equity.html)** — Markus Biesinger, Çağatay Bircan and Alexander Ljungqvist, European Bank for Reconstruction and Development Working Paper 242, 2020.<br>*Evidence from the confidential value-creation plans of 1,580 deals that execution of the plan, rather than its type, is associated with returns; it does not show that any planning template causes them.*
- **[How to Measure Anything: Finding the Value of Intangibles in Business](https://www.wiley.com/en-us/How+to+Measure+Anything:+Finding+the+Value+of+Intangibles+in+Business,+3rd+Edition-p-9781118539279)** — Douglas W. Hubbard, Wiley, 3rd edition, 2014.<br>*It supports two of the post’s moves, measuring before the story hardens and funding the next learning step when it can improve the larger decision.*
- **[Making Work Visible: Exposing Time Theft to Optimize Work and Flow](https://itrevolution.com/product/making-work-visible/)** — Dominica DeGrandis, IT Revolution, 2nd edition, 2022.<br>*Its five ways capacity disappears are a practical companion to the post’s warning that a plan using the same people twice has incomplete resource arithmetic.*
