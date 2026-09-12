---
title: Decide Who Decides, Before You Disagree
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Explain decision rights, boards, investment and operating teams, escalation, and constructive challenge.
permalink: pt-governance
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part II
---

> **KEY POINTS:**
>
> * **Make decision authority explicit before disagreement.** A suggestion from someone close to the owner can be heard as an instruction even when no authority was delegated.
> * **Support needs an accountable company counterpart.** Define who proposes, decides, funds and delivers an intervention, and where unresolved conflicts go.
> * **Reporting should improve decisions.** Use consistent evidence to expose trade-offs and changing assumptions rather than create a parallel management hierarchy.

<br>
A Technology Principal — a technology leader working for the investment firm, the owner, rather than for the company — tells a CTO that the company should move to a different cloud provider. The CTO hears an instruction from the owner. The Principal believes it was a suggestion. The CEO finds out after an engineering team has started planning the migration.

Nobody needed bad intentions for that to go wrong. Influence was exercised without anyone making the decision process explicit, and ownership amplifies the ambiguity: a remark from someone close to the investment partner carries more weight than their job title suggests. **Governance** is simply the arrangement that settles this in advance — who decides, who oversees, who is accountable.

Part I followed the money. Part II follows the authority, and this chapter comes first because every later disagreement — about incentives, about a rewrite, about a cost target — assumes somebody knows who is entitled to settle it. What follows is an operating design, not a statement of directors' legal duties in any particular jurisdiction.


## Each Forum Decides Something Different

The investment team develops and evaluates the investment case. A fund's investment committee makes investment decisions within its mandate. Operating professionals can contribute expertise and help companies execute. The company's board oversees matters within its authority, while executives lead the business. Lenders can have contractual rights that affect what any of these actors can do.

The survey of private equity investors by Gompers and colleagues documents attention to governance, financing, and value creation; it does not establish a uniform organization chart. [S04: PE practitioner survey](https://www.nber.org/papers/w21133) KKR's public description of Capstone, its in-house operating-support team, similarly places operating support in collaboration with investment teams, boards, and company management. This establishes a stated delivery model, not proof that every intervention succeeds. [S22: KKR Capstone description](https://www.kkr.com/approach/capstone)

For an individual engagement, replace the generic diagram with actual names and rights. Who recommends? Who decides? Who implements? Who supplies money? Who receives information? Who can escalate? One person may play several roles, but the roles still need to be distinguished.

## Write Down Who Decides What

The following is a proposed pattern to adapt to actual company documents. It is not an assertion that a Technology Principal has these rights.

| Decision | Company contribution | Principal's possible contribution | Approval to verify |
| --- | --- | --- | --- |
| Product priorities within an agreed budget | Product leader and CTO recommend; CEO resolves major trade-offs | Challenge assumptions and supply evidence | Executive delegation and any reserved matters (decisions the shareholder must approve) |
| Material technology investment | Management prepares options and financial case | Test technical feasibility and delivery dependencies | Board, shareholder, or financing approvals where required |
| CTO appointment | CEO defines need and process | Help assess candidates and context | Actual appointment authority |
| Cyber incident response | Designated incident leaders act under the response plan | Provide specialist access and ownership context | Emergency and disclosure protocols |
| Acquisition integration | Executives own the company integration plan | Assess sequencing, capacity, and reusable support | Transaction and operating governance |

That pattern is still generic. Filled in for Larkspur, the onboarding-automation decision looks like this:

| | Larkspur's actual answer |
| --- | --- |
| Decision | Spend €1 million automating customer onboarding |
| Who recommends | Priya, VP Product, with Alex, the CTO |
| Who resolves trade-offs | Ines, the CEO |
| Principal's contribution | Test whether the 80-hour implementation figure holds across customer types; supply comparable onboarding patterns |
| Whose approval is needed | Board, because the amount exceeds the CEO's €500,000 delegation |
| Response time | Two weeks — the budget cycle closes at month end |

Names and thresholds make the record usable. "Management recommends, the board approves" tells Alex nothing about whom to call on a Tuesday, or by when.

A useful record therefore names a response time. An escalation route that takes six weeks is inadequate for a financing deadline or service failure. Treating every architectural disagreement as an emergency has the opposite failure: it prevents company leadership from exercising judgment.

## Challenge the Outcome, Not the Design

Alex proposes rewriting Larkspur's scheduling engine because it is difficult to change. The board asks how that supports growth. Alex answers that the current stack is dated. The exchange produces heat but little information.

A better challenge asks for the constrained business outcome: which customer need cannot be served, how often the constraint bites, and what it costs. Alex can then compare a focused change, a staged replacement and the full rewrite. The CFO can compare their cash profiles against the €0.5 million the business actually has spare ([[pt-cash-and-constraints]]). The board can decide whether to fund an option and accept its risks.

The board has not become an architecture committee. It has required the connection between an investment and the business plan to be made explicit. The technical team retains responsibility for explaining feasible choices and their consequences.

The same discipline applies in reverse. “Cut engineering by 20%” is not a complete operating plan. Which work disappears? Which obligations remain? What will happen to customer commitments and operational coverage? If the decision is still to cut, its expected consequences should be recorded rather than quietly converted into impossible delivery promises.

## Support Can Become a Shadow Hierarchy

Direct access to engineers can be useful during diligence or a bounded intervention. It can become destructive when portfolio staff receive competing priorities from the Principal, the CTO, and the investment team. A parallel reporting line then exists without an explicit mandate or accountability.

An engagement charter can prevent this. It states the problem, company sponsor, working team, information access, deliverable, duration, and handback. It identifies whether the Principal is advising, facilitating, temporarily delivering, or formally acting in an executive role. If the role changes, the charter changes.

Hands-on work is not the same as taking over. A Principal might help diagnose a release failure with engineers, then return the improvement plan to the engineering leader. The test is whether company capability strengthens and responsibility remains understandable after the intervention ends.

## Reporting That Changes Decisions

A board report should connect material outcomes, interpretation, and decisions needed. A traffic-light dashboard without an evidence trail can conceal more than it reveals. “Green” might mean on time, within budget, lower risk, or simply no one has escalated a problem.

For a customer onboarding initiative, a compact report might show implementation time by cohort, the engineering effort per customer, contract-to-cash timing, the cost of the intervention, and an unresolved dependency. The narrative should explain whether observed changes are consistent with the hypothesis and what management wants to do next.

Keep reporting effort visible. Requiring every company to produce the same large monthly questionnaire can consume the capacity the owner wants to improve. Standard definitions can be valuable; the amount and cadence of reporting should still reflect materiality and available systems.

## Disagreement Without Evasion

A leader should be able to say: “We can deliver the cost target, but not the current roadmap with it. Here are the choices.” A Principal should be able to say: “The evidence no longer supports the original thesis.” A board should be able to decide against a recommendation while recording what it is accepting.

The difficult boundary is confidentiality. Coaching cannot carry an unlimited promise of secrecy if a material issue requires escalation under the engagement's obligations. Agree those boundaries early. Explain what information will be shared, with whom, and why; do not turn routine coaching into an undisclosed assessment channel.

Good governance is not the absence of disagreement. It is disagreement that reaches a decision someone is accountable for, fast enough to matter. It fails when nobody will say who decides, when bad news is slowed down, and when executives are held to choices someone else made. The incentives behind those behaviors are examined in [[pt-incentives]]; the Principal's operating charter in [[pt-technology-principal]].

*Unfamiliar terms are defined in the [[pt-glossary]].*
