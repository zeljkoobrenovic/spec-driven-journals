---
title: How Should Leaders Value Security and Resilience?
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

NIST's Cybersecurity Framework 2.0, published in February 2024, organizes outcomes around Govern, Identify, Protect, Detect, Respond, and Recover. It explicitly avoids prescribing one implementation for every organization. [S17: NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) That makes it a useful reference for consistent questions while leaving room for company-specific answers.

## Begin With What Must Continue Working

A software company may depend on accurate billing, access to customer records, trustworthy releases, and the ability to restore a service. A retailer may depend on payments, inventory, and order fulfillment. The security discussion should begin with these business functions and the people affected by failure.

For each critical function, ask what interruption, corruption, or unauthorized access would mean. How long can the business continue without it? Which customers face material harm? Which contracts, laws, or insurance conditions need specialist interpretation? What manual alternatives exist, and have they been tested?

An asset inventory is useful when it supports those questions. An inventory that counts systems without identifying their role in critical work can create an impression of completeness while missing the most consequential dependency.

## Evidence Has Different Strengths

A policy describes intended behavior. A configuration record describes a state at a point in time. A test shows what happened under particular conditions. An independent assessment can add another perspective but has a defined scope. None alone proves that the company will withstand every incident.

Consider backups. Evidence that backups run successfully is different from evidence that the company can restore the complete service, with usable data, within the required period. A restore test may reveal missing credentials, incompatible versions, or undocumented dependencies. The lesson is to test the operating outcome, not merely the presence of a control.

Similarly, a certification can be relevant evidence but should be read for entity, system, period, and exclusions. Treating a certification as a universal substitute for diligence mistakes an assurance artifact for the entire risk profile.

## Risk Economics Without Invented Profit

A fictional annual scenario has a 5% probability of a €4 million loss. The expected loss is €200,000. A proposed control is estimated to reduce the probability to 2%, making the modelled expected loss €80,000. The difference is €120,000 before control costs.

This is an illustration of a method, not an empirical estimate. If the probabilities are weak guesses, the result inherits their weakness. If losses are correlated or the company cannot survive a severe event, a simple expected value may be an inadequate decision rule. A small probability of catastrophic harm is not automatically acceptable because an average looks affordable.

Use ranges and explain what evidence would narrow them. State which scenarios the control addresses and which remain. Above all, do not add the €120,000 to realized EBITDA. It is a modelled change in risk exposure, not a booked operating gain.

## Security Work Needs an Owner and Funding

A diligence finding such as “identity controls are inadequate” is incomplete. Which systems and people are exposed? What is the material scenario? What action is feasible before closing, and what needs post-close implementation? Who has authority and capacity to carry it out?

The Principal can help obtain specialist judgment and communicate the implication to the investment team. The company needs accountable operating owners. The board needs to understand material residual risk. A consultant's recommendation does not transfer responsibility for the business to the consultant.

Some findings may affect transaction conditions, price, insurance, or whether the deal proceeds. Others may be appropriately accepted with an action plan. The distinction should follow materiality and evidence, not the desire to keep all findings the same color.

## Incident Response Is an Operating Capability

An incident can require simultaneous technical work, customer communication, legal judgment, financial decisions, and coordination with the owner. A response plan should name the decision process before urgency compresses it.

A practical exercise can test a plausible scenario: a critical service cannot be trusted, the cause is uncertain, a major customer needs an answer, and restoration may erase evidence. The exercise should reveal who can decide, which specialists are available, and how the team communicates uncertainty. It should not be staged merely to demonstrate that a plan exists.

Legal notification deadlines, sector requirements, and contractual duties vary and can change. In a live incident, the organization needs current advice for its jurisdictions and facts. This chapter supplies the operating questions; it does not substitute a universal deadline.

## Portfolio Support Can Increase or Reduce Concentration Risk

A shared specialist network and tested response process can give small companies access to scarce expertise. A common identity provider, administrator, or integration mechanism can also create a shared dependency. The support design should examine the new concentration it introduces.

Portfolio-level visibility does not require unrestricted access to customer data. Aggregate risk information, scoped evidence, and company-approved disclosures can support oversight. Raw production access should have a specific purpose and an explicit boundary.

Exit preparation should preserve the same discipline. Describe improvements with dates and test evidence. Disclose material unresolved issues through the appropriate process. An orderly data room is helpful; it is not equivalent to a resilient product.

The durable outcome is a company that can make better security decisions, detect and respond to failures, and continue serving customers within understood limits. That capability can support value without being converted into a fictional profit figure.
