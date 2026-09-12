---
title: Who Gets to Decide After the Deal?
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
A Technology Principal tells a CTO that the company should move to a different cloud provider. The CTO hears an instruction from the owner. The Principal believes it was a suggestion. The CEO learns about the conversation after an engineering team has started planning the migration.

No one needs bad intentions for this arrangement to fail. The failure is that influence has been exercised without making the decision process explicit. Ownership intensifies the ambiguity: a suggestion from someone close to the investment partner can carry more weight than their formal job description suggests.

**Governance** is the arrangement for making decisions, overseeing them and holding people accountable. Good governance makes authority clear before a consequential disagreement. This chapter offers an operating design, not a statement of the legal duties of directors in every jurisdiction.

## Separate the Forums

The investment team develops and evaluates the investment case. A fund's investment committee makes investment decisions within its mandate. Operating professionals can contribute expertise and help companies execute. The company's board oversees matters within its authority, while executives lead the business. Lenders can have contractual rights that affect what any of these actors can do.

The survey of private equity investors by Gompers and colleagues documents attention to governance, financing, and value creation; it does not establish a uniform organization chart. [S04: PE practitioner survey](https://www.nber.org/papers/w21133) KKR's public description of Capstone similarly places operating support in collaboration with investment teams, boards, and company management. This establishes a stated delivery model, not proof that every intervention succeeds. [S22: KKR Capstone description](https://www.kkr.com/approach/capstone)

For an individual engagement, replace the generic diagram with actual names and rights. Who recommends? Who decides? Who implements? Who supplies money? Who receives information? Who can escalate? One person may play several roles, but the roles still need to be distinguished.

## A Decision-Rights Record

The following is a proposed pattern to adapt to actual company documents. It is not an assertion that a Technology Principal has these rights.

| Decision | Company contribution | Principal's possible contribution | Approval to verify |
| --- | --- | --- | --- |
| Product priorities within an agreed budget | Product leader and CTO recommend; CEO resolves major trade-offs | Challenge assumptions and supply evidence | Executive delegation and any reserved matters |
| Material technology investment | Management prepares options and financial case | Test technical feasibility and delivery dependencies | Board, shareholder, or financing approvals where required |
| CTO appointment | CEO defines need and process | Help assess candidates and context | Actual appointment authority |
| Cyber incident response | Designated incident leaders act under the response plan | Provide specialist access and ownership context | Emergency and disclosure protocols |
| Acquisition integration | Executives own the company integration plan | Assess sequencing, capacity, and reusable support | Transaction and operating governance |

A useful record also names a response time. An escalation route that takes six weeks is inadequate for a financing deadline or service failure. Conversely, treating every architectural disagreement as an emergency prevents company leadership from exercising judgment.

## Productive Challenge Requires a Decision

Imagine management proposes a rewrite because the current system is difficult to change. The board asks how it supports growth. Management answers that modern technology is necessary. The exchange produces heat but little information.

A better challenge asks for the constrained business outcome: which customer need cannot be served, how frequently the constraint occurs, and what it costs. The CTO can compare a focused change, a staged replacement, and the full rewrite. The CFO can compare cash profiles. The board can then decide whether to fund an option and accept its risks.

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

Governance is useful when it allows disagreement to reach a legitimate decision, with consequences understood. It fails when authority is obscured, bad news is delayed, or executives remain accountable for choices they were never allowed to make.

The incentives behind these behaviors are examined in [[pt-incentives]]. The role-specific operating charter is developed in [[pt-technology-principal]].
