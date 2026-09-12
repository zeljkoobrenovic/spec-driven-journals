---
title: Security Is an Investment Under Uncertainty, Not a Cost
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Treat risk reduction as a governed investment under uncertainty, distinct from booked profit or an absence of incidents.
permalink: pt-security-and-resilience
timetoread: 5 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **Start with the business functions that must keep working.** Identify who would be affected by interruption, corruption or unauthorized access before choosing controls.
> * **Risk estimates are uncertain decision inputs.** A modeled reduction in possible losses is not earnings, and a completed checklist is not proof of resilience.
> * **Recovery needs practiced capability and clear ownership.** Fund response, test restoration and make responsibility for remaining risks explicit.

<br>
Security is often asked to justify itself through a loss that has not occurred. That creates two temptations: invent a precise amount of “risk avoided,” or retreat into a checklist that says little about business exposure.

A better approach treats security and resilience as decisions under uncertainty. The company identifies material failure scenarios, the controls and response capabilities that matter, the investment required, and who accepts the remaining risk. Some obligations must be met regardless of a simplified financial model.

Every other chapter in this part argues for work that produces a benefit. This one argues for work whose success looks like nothing happening — which is why it needs its own way of being valued, and why its number must never be added to earnings.

NIST's Cybersecurity Framework 2.0, published in February 2024, organizes outcomes around Govern, Identify, Protect, Detect, Respond, and Recover. It explicitly avoids prescribing one implementation for every organization. [S17: NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) That makes it a useful reference for consistent questions while leaving room for company-specific answers.

## Begin With What Must Keep Working

Larkspur's customers are maintenance businesses that dispatch engineers each morning. If the scheduling service is unavailable at 6am, vans do not leave. That, not the CVE count, is where the security discussion starts: the business functions customers depend on, and the people affected when they fail. A retailer's equivalents are payments, inventory and fulfillment.

For each critical function, ask what interruption, corruption, or unauthorized access would mean. How long can the business continue without it? Which customers face material harm? Which contracts, laws, or insurance conditions need specialist interpretation? What manual alternatives exist, and have they been tested?

An asset inventory is useful when it supports those questions. An inventory that counts systems without identifying their role in critical work can create an impression of completeness while missing the most consequential dependency.

## A Policy, a Config and a Test Are Different Proofs

A policy describes intended behavior. A configuration record describes a state at a point in time. A test shows what happened under particular conditions. An independent assessment can add another perspective but has a defined scope. None alone proves that the company will withstand every incident.

Larkspur's diligence found that backups had run without error for three years, and that no one had attempted a full restore in that time. When the team tried, it took eleven hours and stopped twice: a credential no current employee held, and a database version no longer available. Backups running is evidence about backups. Restoring the service is evidence about the business. Test the operating outcome, not the presence of a control.

A certification deserves the same reading — for entity, system, period and exclusions. A certificate says one system passed one set of tests on one date. It is not a statement about the whole company today.

## Put a Number on Risk Without Faking a Profit

Suppose a prolonged Larkspur outage would cost €4 million in contractual credits, remediation and lost customers, and the team estimates a 5% annual chance of one. The expected loss is €200,000 a year. A proposed control is estimated to cut the probability to 2%, leaving €80,000 — a €120,000 difference, before what the control costs.

The method is only as good as the two guesses inside it. If the probabilities are weak, so is the answer; state them as ranges and say what evidence would narrow them. And expected value is the wrong rule where losses are correlated or a severe event would end the company: **a 2% chance of not surviving is not made acceptable by an affordable-looking average.**

State which scenarios the control addresses and which remain. Above all, do not add the €120,000 to realized EBITDA. It is a modelled change in risk exposure, not a booked operating gain.

## Security Work Needs an Owner and Funding

A diligence finding such as “identity controls are inadequate” is incomplete. Which systems and people are exposed? What is the material scenario? What action is feasible before closing, and what needs post-close implementation? Who has authority and capacity to carry it out?

The Principal can help obtain specialist judgment and communicate the implication to the investment team. The company needs accountable operating owners. The board needs to understand material residual risk. A consultant's recommendation does not transfer responsibility for the business to the consultant.

Some findings may affect transaction conditions, price, insurance, or whether the deal proceeds. Others may be appropriately accepted with an action plan. The distinction should follow materiality and evidence, not the desire to keep all findings the same color.

## Incident Response Is an Operating Capability

An incident can require simultaneous technical work, customer communication, legal judgment, financial decisions, and coordination with the owner. A response plan should name the decision process before urgency compresses it.

A practical exercise can test a plausible scenario. Larkspur's: the scheduling service is returning wrong engineer assignments, nobody yet knows why, the largest customer wants an answer within the hour, and restoring from backup may destroy the evidence needed to find the cause. The exercise should reveal who can decide, which specialists are available, and how the team communicates uncertainty. It should not be staged merely to demonstrate that a plan exists.

Legal notification deadlines, sector requirements, and contractual duties vary and can change. In a live incident, the organization needs current advice for its jurisdictions and facts. This chapter supplies the operating questions; it does not substitute a universal deadline.

## Shared Support Can Spread Risk or Concentrate It

A shared specialist network and tested response process can give small companies access to scarce expertise. A common identity provider, administrator, or integration mechanism can also create a shared dependency. The support design should examine the new concentration it introduces.

Portfolio-level visibility does not require unrestricted access to customer data. Aggregate risk information, scoped evidence, and company-approved disclosures can support oversight. Raw production access should have a specific purpose and an explicit boundary.

Exit preparation should preserve the same discipline. Describe improvements with dates and test evidence. Disclose material unresolved issues through the appropriate process. An orderly data room is helpful; it is not equivalent to a resilient product.

The outcome worth funding is a company that notices failures, responds to them, and keeps serving customers inside limits it has actually tested. That is worth real money. It still should not be written into the earnings as if it were profit.

*Unfamiliar terms are defined in the [[pt-glossary]].*
