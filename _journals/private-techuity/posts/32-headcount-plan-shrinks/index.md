---
title: "When the Headcount Plan Shrinks"
date: 2026-09-16
author: Željko Obrenović
excerpt: "Follow a product and engineering reduction from the investor’s request to an authorized, funded plan: the staffing baseline, the real source of the pressure, the alternatives, the cash by date, the work stopped, and what happens to the people who leave and the people who stay."
permalink: headcount-plan-shrinks
timetoread: 17 min read
---

> **IN THIS SECTION, YOU WILL:** Learn to turn a reduction request into an operating plan: find where the pressure actually comes from, compare the alternatives on cash by date, choose roles by the work that stops, and plan for the people who leave and the people who remain.

> **WHY INVESTORS CARE:** An investor bridging a company through a delayed round is putting new money at risk, and it wants that money to last; a reduction that saves less than it costs in the months that matter, or that removes the capacity the round is being priced on, protects nobody’s investment.

> **WHY YOU SHOULD CARE:** “Cut 20% of engineering” is a number, not a plan; the roles you keep, the work you stop and the dates the savings arrive decide whether the company survives the gap and what it can still deliver on the other side.


> **KEY POINTS:**
>
> * **Find the real source of the pressure.** A condition attached to the bridge, a director’s vote and an adviser’s benchmark are three different things; only the first two carry authority, and only the first sets a date. Answer each with the response it requires.
> * **Reconcile the reduction by date.** Notice periods delay the savings and severance arrives before them, so a reduction cannot replace money that is late; it can only make money that arrives last longer. Show cash by month under each plan before anyone is told.
> * **Choose roles by the work that stops, and plan for both sides of the door.** The people who leave need notice, severance and a record of what they knew; the people who remain need a published list of what is no longer expected of them, an on-call plan and the evidence that would restore the plan.

<br>
It is 1 October at fictional Larkspur, and the board review that [[the-financing-slipped]] scheduled is about to start. The written commitment for the €600,000 bridge arrived on 20 September, three weeks after the date the board had set, and it carries a condition: the existing investors will fund the bridge only if, by 31 October, the board has adopted an operating plan under which Larkspur’s cash stays above the agreed €400,000 reserve until at least 30 June without any proceeds from the delayed round. The round itself is where it was in August, a conversation whose closing keeps moving. Alex, the CTO, and Priya, the product leader, have costed the deeper reduction the board asked for. Now the board has to decide it.

This chapter continues that chapter’s scenario and stays deliberately separate from the shared Larkspur ledger that runs through [[first-hundred-days]] and [[handover-of-obligations]]: its cash, burn, people and dates are its own, and every figure is fictional. What the earlier chapter never stated, because its decision did not need it, is who works at Larkspur and what they cost. A reduction cannot be decided without that baseline, so it comes first.

## The Baseline the Earlier Decision Did Not Need

Larkspur has forty employees. Its monthly costs on 1 October, and the collected revenue they are set against, are these:

| Function | People | Monthly cost |
| --- | ---: | ---: |
| Engineering (Alex and sixteen engineers) | 17 | €140,000 |
| Product and design (Priya, two product managers, two designers) | 5 | €38,000 |
| Customer implementation and support | 8 | €48,000 |
| Sales and marketing | 6 | €48,000 |
| Finance, operations and administration (Ines, Sam and two staff) | 4 | €50,000 |
| **Payroll, fully loaded** | **40** | **€324,000** |
| Contract engineering on internal tooling (Reduction R1 ends it on 31 October) | | €50,000 |
| Cloud, offices, software, insurance and professional fees | | €76,000 |
| **Total monthly cost** | | **€450,000** |
| Collected revenue | | €250,000 |
| **Net monthly burn** | | **€200,000** |

The table reproduces the earlier chapter’s figures: a €200,000 burn, €150,000 once R1 removes the contractors from 1 November, and €500,000 of cash on 31 December without the bridge. “Fully loaded” means salary plus employer charges, benefits and the equipment and tools each person uses; it is the number that changes when a person leaves, and it is larger than the salary.

The engineers are organized around five pieces of work: four on the onboarding pilot, two finishing the recovery work that ends in December, five on the scheduling core (incidents, customer-committed changes and maintenance), three on the pricing and tax rules for the second country, where two customers signed in the summer with go-live promised for the first quarter, and two on a field-worker mobile app that has three beta customers, no revenue yet and a launch planned for the second quarter. One product manager and one designer work with the onboarding and core teams; the other product manager and designer belong to the mobile app.

## Three Pressures That Sound Alike

“The investors want a reduction” describes three different things at Larkspur, and a company leader has to answer each with a different response. [[decide-who-decides]] gives the general rule; here it is applied.

The first is a **funding condition**. The bridge commitment says the money arrives only if the plan holds the reserve to 30 June. That is a condition attached to cash, with a date, and the company either meets it or does without the money. It says nothing about headcount: a plan that met the date by other means would satisfy it just as well. Sam’s first job is to translate the condition into a number, and the arithmetic is short. With R1 and the bridge, cash on 31 December is €1.1 million and the burn is €150,000, so the reserve is reached about mid-May; to hold it to 30 June, spending between February and June must fall by at least €40,000 a month, more if the reduction itself costs money first.

The second is a **formal approval right**. Under Larkspur’s fictional shareholders’ agreement, adopting or materially changing the annual operating plan is a reserved matter that needs the consent of the director the lead investor appointed, and the operating plan is the board’s to approve in any case. A reduction changes what the plan funds, so it is the board’s decision, and the investor director’s consent is part of it. That is authority, exercised through a seat and a clause, and the response is to bring the board a decision it can take: the options, the cash by date and the consequences.

The third is **influence**. At the same meeting the investor director says that in the fund’s other companies a delayed round has meant a cut of about a fifth of engineering, and Morgan, the investor’s adviser, has seen the same. A fifth of Larkspur’s engineering payroll is about €28,000 a month. It would not meet the condition, and it would select people by a ratio rather than by the work the company is going to stop. A benchmark from other companies is information about those companies; it is not an instruction, and treating it as one would produce a smaller saving than the condition needs and a worse team than the plan can afford. Alex records it as one option to cost beside the others.

## The Alternatives, Costed on the Same Basis

Before a reduction, the board asks what else could close the gap. Several measures are already in force or easy to state, and the table puts them on one basis: the recurring monthly saving once it has fully arrived, the one-off cash it costs first, the first month in which the full saving appears, and what the company gives up. Every figure is fictional.

| Measure | Recurring saving a month | One-off cost | First full month | What it removes |
| --- | ---: | ---: | --- | --- |
| Hiring freeze (in force since August: the two deferred hires) | €0 further | €0 | — | Nothing more; the saving is already in the €200,000 burn |
| R1: contract engineering not renewed (decided) | €50,000 | €0 | November | Internal tooling work; protected work unaffected |
| Redeploy the two recovery engineers to the core team when the recovery work ends | €0 | €0 | — | Nothing; it fills a gap that a leaver would otherwise leave |
| Executive pay deferral of 15% until the round closes | About €6,000, repaid at closing | €0 | November | Nothing; it is a loan from four people to the company, not a saving, and the plan does not count it |
| Reduced hours across engineering | Depends on the jurisdiction’s short-time rules | €0 | — | Capacity from every team equally, including the protected onboarding and recovery work |
| A fifth of engineering, by ratio | About €28,000 | About €55,000 | February | Three or four engineers chosen by proportion, not by work stopped; the condition is not met |
| **R2: stop the mobile app, narrow the second country, eight roles in all** | **€72,000** | **€120,000** | **February** | The mobile app; further countries; the second-country go-live moves from the first quarter to September |
| R3: the level at which Larkspur runs on collected revenue alone | €150,000 | About €330,000 | February | About sixteen further roles, the second country entirely, half of implementation and support, and the onboarding pilot’s engineers |

Two rows need explanation. R3 is the number the board asked for in August, the cost level at which the company could continue with no new money at all: total costs of €250,000 against €250,000 of collected revenue, which means removing €150,000 a month beyond R1. It is worth knowing, and it is not a plan. At that level Larkspur would release the two second-country customers, cut the implementation and support team that the collected revenue depends on, and take the engineers off the onboarding pilot the round is being priced on. It also would not save January, for the reason the next section shows. R2 is the reduction the rest of this chapter follows: it removes whole pieces of work rather than a slice of every team, it meets the condition with a margin, and it keeps the protected obligations and the pilot intact.

## Reconcile the Reduction by Date

A reduction is often presented as a monthly saving. Cash does not arrive that way. Under Larkspur’s fictional employment terms, notice periods run from one to three months by length of service and are paid whether or not the person works them; severance is one month’s pay for every two full years of service with a minimum of one month, paid with the final salary; accrued leave is paid out. R2 gives notice to eight people on 31 October: two engineers, a designer and a product manager from the mobile app, two of the three second-country engineers, one sales role that existed for the second-country expansion and one administrative role. Their combined cost is €63,000 a month, and a further €9,000 of non-payroll spending stops with the app: its cloud environment, test devices and store fees.

Three of the eight leave the payroll on 30 November, three on 31 December and two on 31 January. The saving therefore ramps: about €20,000 in December, about €45,000 in January and the full €72,000 from February. The one-off costs run the other way: about €95,000 of severance, €15,000 of outplacement and legal cost and about €10,000 of accrued leave, €120,000 in all, paid with the final salaries between November and January. Sam’s cash table, with the bridge drawn on 15 November, reads:

| Month end | Burn before R2 | R2 saving | One-off cost | Cash |
| --- | ---: | ---: | ---: | ---: |
| October | €200,000 | — | — | €800,000 |
| November (bridge €600,000 received) | €150,000 | — | €30,000 | €1,220,000 |
| December | €150,000 | €20,000 | €45,000 | €1,045,000 |
| January | €150,000 | €45,000 | €45,000 | €895,000 |
| February | €150,000 | €72,000 | — | €817,000 |
| March | €150,000 | €72,000 | — | €739,000 |
| April | €150,000 | €72,000 | — | €661,000 |
| May | €150,000 | €72,000 | — | €583,000 |
| June | €150,000 | €72,000 | — | €505,000 |
| July | €150,000 | €72,000 | — | €427,000 |

<!-- illustration-placeholder
{
  "id": "cash-by-date-under-three-plans",
  "status": "pending",
  "asset": "assets/images/32-headcount-plan-shrinks/cash-by-date-under-three-plans.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the monthly cash table in Reconcile the Reduction by Date",
  "visual_goal": "Show that a reduction's savings arrive after its one-off costs, so it extends money that arrives but cannot replace money that is late: three simple cash lines against a reserve line.",
  "prompt": "Create one finished explanatory illustration for Owned, a practical book for product and engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background (#faf8f2), navy linework, muted teal and warm ochre. A simple calendar strip from October to August runs along the bottom. Three hand-drawn cash lines descend from the left toward a dashed horizontal line labeled RESERVE: one teal line labeled BRIDGE + REDUCTION dips slightly in November through January then flattens and reaches the reserve in August; one ochre line labeled BRIDGE ONLY falls steadily and reaches the reserve in May; one grey line labeled NO BRIDGE drops below the reserve in January. A small ochre wedge near November to January is labeled SEVERANCE FIRST, and a small teal wedge from February is labeled SAVINGS AFTER. Use only these labels: RESERVE, BRIDGE + REDUCTION, BRIDGE ONLY, NO BRIDGE, SEVERANCE FIRST, SAVINGS AFTER, and the month initials. No amounts, no numbers, no title, no photorealism, no dense text.",
  "alt": "Three cash lines against a reserve line: with the bridge and the reduction the cash reaches the reserve in August, with the bridge alone in May, and without the bridge it crosses the reserve in January; severance costs come before the savings.",
  "caption": "A reduction’s savings arrive after its costs. It makes money that arrives last longer; it cannot replace money that is late."
}
-->

Cash on 30 June is €505,000, above the reserve with a margin of about one month, and the reserve is reached in the second week of August. That meets the condition. Without R2 the same table shows €200,000 on 30 June and the reserve breached in mid-May, which is why the investors attached the condition. The third comparison is the one a board rarely asks for. Without the bridge, R2 or no R2, Larkspur is below the reserve in January: the one-off costs come first, and the first full month of saving is February. R2 with no bridge reaches the reserve about ten days earlier than R1 alone would have. **A reduction makes money that arrives last longer; it cannot replace money that is late**, because notice periods and severance put the cost in front of the saving. That is the sentence Sam puts at the top of the board paper, and it is the reason R3 is not the fallback if the bridge fails.

## The Decision, Recorded

The board meets on 15 October rather than waiting for its November date, because the condition’s date is 31 October and the notice periods have to start then for the savings to land by February. The record reads:

- **Chosen:** R2. Notices on 31 October; the plan adopted meets the bridge condition with cash of €505,000 at 30 June.
- **Rejected:** a fifth of engineering by ratio, because it saves €28,000 against a need of at least €40,000 and chooses people by proportion; R3, because it removes the revenue and the pilot the company exists to deliver and still does not hold January without the bridge; reduced hours, because they take capacity from the protected onboarding and recovery work as much as from anything else; and waiting for the round, because the round is an expression of interest and the condition’s date is 31 October.
- **Funding:** €120,000 of one-off cost from operating cash inside the adopted plan; the savings as tabled; the bridge drawn on 15 November once the plan is adopted.
- **Scarce capacity:** the one engineer who will remain on the second-country rules; Priya’s time for two customer renegotiations; Alex’s time for eight individual conversations and the transfer test below.
- **Authorized:** the Larkspur board, with the investor director’s consent under the reserved matter, on 15 October. Ines gives the individual notices within the adopted plan and the applicable employment law; Alex and Priya select the roles by the work that stops, not by a ranking of people.
- **Reviews:** 1 December, on notices served, the bridge drawn, the transfer test and the second customer’s answer; 1 February, the first full month of saving reconciled against the table; 1 April, the round’s stage under the restart rule from [[the-financing-slipped]].
- **Evidence that would change the decision:** a signed subscription agreement for the round that the board authorizes counting does not reverse R2, because the notices will have been served and the people will have left; it stops any further reduction and reopens the mobile app only as a new proposal with its own case. The bridge failing its own conditions does not trigger R3; it puts a different question to the board, whether Larkspur can be financed by someone else or sold on the terms available, which [[handover-of-obligations]] takes up. The second customer terminating narrows the remaining engineer’s work to one customer and removes that customer from Sam’s forecast. Incidents rising for two consecutive months after the on-call change cut the customer-committed change list before anyone is hired.

A record like this is what distinguishes a decision from a number. It shows the condition being met, the alternatives that were not chosen and why, and the evidence that would change the plan, which a later board, or a later owner, can check.

## The Team After the Plan

The reduction is chosen by work, so the organization that results can be described by work. From 1 February Larkspur has twelve engineers besides Alex: four on the onboarding pilot, and eight on a core team that now includes the second-country rules and the two engineers redeployed from the recovery work when it ends in December. Product and design are Priya, one product manager and one designer, both with the onboarding and core teams. Implementation and support are unchanged, because the collected revenue depends on them.

<!-- illustration-placeholder
{
  "id": "team-by-work-before-and-after",
  "status": "pending",
  "asset": "assets/images/32-headcount-plan-shrinks/team-by-work-before-and-after.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the first paragraph of The Team After the Plan",
  "visual_goal": "Show a team described by its work before and after a reduction: five work streams becoming two, with one stream stopped, one narrowed and one redeployed, and the protected work unchanged.",
  "prompt": "Create one finished explanatory illustration for Owned, a practical book for product and engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background (#faf8f2), navy linework, muted teal for continuing work and warm ochre for work that stops or changes. On the left, five small labeled desks or work benches: ONBOARDING, RECOVERY, CORE, SECOND COUNTRY, MOBILE APP. A simple arrow leads to the right, where two larger benches remain: ONBOARDING (unchanged, teal) and CORE (teal, visibly larger, with a small tag SECOND COUNTRY attached). Between them, the RECOVERY bench folds into CORE with a curved arrow labeled REDEPLOYED, the SECOND COUNTRY bench shrinks with a tag NARROWED, and the MOBILE APP bench is covered with an ochre cloth and a tag STOPPED. Use only these labels. No people faces, no amounts, no numbers, no title, no photorealism, no dense text.",
  "alt": "Five work streams before a reduction become two afterwards: onboarding unchanged, the recovery pair redeployed into a larger core team that now carries the narrowed second-country work, and the mobile app stopped.",
  "caption": "Describe the team after a reduction by the work it keeps, the work it stops and the work it absorbs."
}
-->

Three things had to be decided for that team to be real rather than drawn.

**Work stopped.** The mobile app stops on 15 December. Its code is frozen and archived with a written record of what works, what does not and which defects are open, so that a later decision to restart it starts from evidence rather than memory. The store listing is withdrawn, the three beta customers are told on 3 November and moved back to the web product with their data exported by the closing date, and the two sales prospects whose interest depended on the app come out of the forecast. Further countries stop too: the remaining second-country engineer serves the two signed customers and no others, and Sam removes expansion from every forecast until the round closes and a new decision is taken.

**Customer commitments revised.** The two second-country contracts promised go-live in the first quarter and allow the customer to terminate if it slips past 30 June. With one engineer instead of three, go-live moves to 30 September. Priya renegotiates both before the notices are served, so that no customer learns of the change from a departing engineer. The first customer accepts September with three months’ subscription waived, about €9,000 that was never in the collected revenue because the customer is not yet live. The second has not decided by 31 October; the plan carries that as a risk with no revenue counted from either customer until go-live, and the December review records the answer.

**Knowledge transferred, inside the notice period.** The two departing second-country engineers hold the mapping between the country’s tax rules and Larkspur’s configuration. The transfer test from [[fix-decisions-before-hiring]] applies: before they leave, the remaining engineer releases one rule change alone, and the written mapping is reviewed against the release. The test is scheduled for the second week of December. If it fails, the notice period of one departing engineer is extended, paid, until it passes; the cost of that extension is the price of not discovering in March that the mapping lived in someone’s head. The mobile app needs no transfer, because nobody is going to change it; it needs the state-of-work record.

## The People Who Leave

A reduction chosen by work still ends in eight individual conversations, and the record of what the company owes each person is part of the plan, not an afterthought. At Larkspur the terms are the fictional ones above: notice paid in full, whether worked or not; severance on the stated formula; accrued leave paid out; a written reference; and outplacement support at the company’s cost. Each person also holds share options, and [[different-bets]] explained why the leaver terms decide what those are worth: Larkspur’s board treats the eight as good leavers, so vested options can be exercised for twelve months after leaving rather than lapsing in ninety days, and unvested options lapse. None of this compensates for a job lost in the middle of a winter. It is what the company can do, it is written down, and it is the same for all eight.

The order of the day matters. On 31 October each of the eight is told individually in the morning, by the leader they work for, with Ines present or available, before anyone else in the company hears. Nobody learns their fate from a calendar invitation or a changed access badge. Where a person is asked to work part of the notice for the transfer test, that is agreed with them, not announced for them.

**The employment process belongs to a jurisdiction, and the thresholds decide the calendar.** In the European Union, the collective redundancies directive applies from ten dismissals over thirty days in an establishment of twenty to a hundred workers, ten per cent in one of a hundred to three hundred, and thirty in a larger one, or twenty over ninety days where a member state chooses that test; an employer within it must consult the workers’ representatives in good time with a view to reaching an agreement, notify the competent public authority in writing, and the dismissals take effect not earlier than thirty days after that notification. [S77: Council Directive 98/59/EC](https://www.legislation.gov.uk/eudr/1998/59) In the United States, the federal statute applies to employers with a hundred or more employees, defines a plant closing by fifty or more job losses at one site and a mass layoff by a third of the workforce and at least fifty employees, or five hundred, and requires sixty days’ written notice. [S78: US WARN Act, 29 U.S.C. §§ 2101–2102](https://www.law.cornell.edu/uscode/text/29/2101) Eight people in an establishment of forty sit below the directive’s lowest band and forty employees sit below the US statute’s threshold, but member states may set lower thresholds, national law governs individual dismissals and works councils in any case, and this book does not say which law governs Larkspur. What it says is that the calendar in the cash table assumes individual notice with no collective procedure, that Larkspur’s counsel confirms the assumption before the date is fixed, and that if the assumption is wrong every date moves by at least the consultation period. A reduction planned without that check has a saving date nobody can rely on.

## The People Who Remain

Thirty-two people are still at Larkspur on 1 February, and the plan has to say what it expects of them. The failure to avoid is the silent one: the work of eight people distributed over the rest by omission, so that the reduction saves €72,000 on paper and costs the company its next four resignations.

So the stopped list is published, not implied. The remaining engineers are told, in writing, what is no longer expected: no mobile app, no support for its beta after 15 December, no country beyond the two signed customers, and on the core team only customer-committed changes and the maintenance the incidents demand. The on-call rota, which drew on ten engineers, now draws on eight; each person carries one week in eight instead of one in ten, and the December and February reviews look at the incident count before anything else, because the evidence that would change the plan includes it. The executives’ pay deferral is announced with the plan, as a deferral, not as a sacrifice that others are asked to match. And the team is told what would restore the plan: cash received from the round, or a commitment the board authorizes counting under the restart rule, and what that would and would not reopen.

The people who remain draw conclusions of their own, and some leave; the reading list at the end includes the research on that. A company cannot promise them stability it does not have. It can tell them which plan is running, why, and what the next review will decide, and it can make sure that the same dated cash table sits behind the board paper, the investor update and the team briefing. A team that hears “the round is nearly done” in October and watches eight colleagues leave in November has learned something about its leaders that no later update repairs.

## Two Variations on the Same Decision

**A profitable company pursuing a higher margin.** Under a buyout, the pressure may be a margin target in the value-creation plan rather than a cash date, and the reduction is proposed when nothing is late. The authority is the same board and the same reserved matters; what is missing is the latest useful date that cash supplies, so the discipline has to come from the comparison instead: the recurring saving against the revenue it puts at risk, the one-off cost against the year-one net, and the capacity removed against the work that will actually stop. The support-location consolidation in [[different-bets]] is that comparison, worked through to a staged decision; a margin target with no stopped list attached is the “cut engineering by 20%” of [[decide-who-decides]], a number that is not yet a plan.

**A consolidation after an acquisition.** When two companies are combined, the transaction may have priced a saving from duplicated roles. The reduction then has a date the deal set, and the danger is releasing the people who hold the acquired product’s knowledge before the receiving team has passed the transfer test in [[fix-decisions-before-hiring]]. [[acquisition-adds-work-first]] gives the completion test: a duplicated cost is saved when it has actually ended, and it ends when the merged system runs without the people who used to run the old one, not on the synergy date. Rules on employees transferring with a business, and on consultation, vary by jurisdiction and can constrain which roles may change and when; take that advice before the synergy date is fixed, not after.

In every version, continued ownership is the scenario to plan for. If the round never closes, the reduction is what Larkspur is, and the record above is what its next board, its next investor or its buyer inherits. [[handover-of-obligations]] follows that record through whatever event comes next: who receives cash, who keeps an interest, and how the obligations that survived the reduction, the two customer contracts, the frozen app and the deferred hires, are handed over with the company rather than discovered afterwards.

## Questions to Consider

1. *Where does the reduction pressure on your company actually come from: a condition attached to money, a right someone holds under the agreements, or a benchmark somebody quoted? What response does each one require?*
2. *If you gave notice on the last day of this month, in which month would the full saving first appear, and what would the reserve look like in the months before it?*
3. *Which pieces of work would stop entirely, and has that list been written down for the people who remain, or will they discover it when they are asked to do it anyway?*

## To Probe Further

- **[Layoffs That Don’t Break Your Company](https://hbr.org/2018/05/layoffs-that-dont-break-your-company)** — Sandra J. Sucher and Shalene Gupta, Harvard Business Review, May–June 2018.<br>*Argues that routine reductions damage engagement and profitability over the long run and describes companies that plan their workforce changes differently, a counterweight to treating a reduction as the default response to a delayed round.*
- **[Keeping Your Headcount When All About You Are Losing Theirs: Downsizing, Voluntary Turnover Rates, and the Moderating Role of HR Practices](https://doi.org/10.5465/amj.2008.31767250)** — Charlie O. Trevor and Anthony J. Nyberg, Academy of Management Journal 51(2), 2008, pp. 259–276.<br>*Evidence that downsizing is followed by higher voluntary turnover among the people who remain, and that some employment practices soften the effect; the research behind this chapter’s warning about the silent redistribution of work.*
- **[Causes and Effects of Employee Downsizing: A Review and Synthesis](https://doi.org/10.1177/0149206309346735)** — Deepak K. Datta, James P. Guthrie, Dynah Basuil and Alankrita Pandey, Journal of Management 36(1), 2010, pp. 281–348.<br>*A review of the research on why companies reduce headcount and what follows for employees and for company results, useful for checking a claimed benefit against what has actually been observed.*
- **[Managing the Effects of Layoffs on Survivors](https://doi.org/10.2307/41166691)** — Joel Brockner, California Management Review 34(2), 1992, pp. 9–28.<br>*An older paper on how the people who remain react to the fairness and the handling of a reduction, which is why this chapter spends as much time on them as on the people who leave.*
