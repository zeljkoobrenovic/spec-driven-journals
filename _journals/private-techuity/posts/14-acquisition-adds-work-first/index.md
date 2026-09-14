---
title: "An Acquisition Adds Work Before It Adds Value"
date: 2026-09-12
author: Owned working manuscript
excerpt: "Plan the practical work of combining or separating businesses while keeping customers served and costs understood."
permalink: acquisition-adds-work-first
timetoread: 8 min read
logo: "assets/images/14-acquisition-adds-work-first/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/14-acquisition-adds-work-first.png"
---

> **KEY POINTS:**
>
> * A transaction **changes ownership before it changes operations**. An acquisition needs a deliberate integration plan; a separation needs the capabilities to operate independently.
> * Combine activities for a **specific benefit**. Buying more products, customers or revenue does not by itself show that the existing business has improved.
> * **Fund the transition** and measure what survives it. Include shared-service dependencies, parallel operation, customer migration and costs that cannot yet be retired.

<br>
An **acquisition** is the purchase of a business or an ownership interest in it. It can add customers and products to a group immediately. **Integration**, the work of making selected activities operate together, still has to be planned and done. A **carve-out**, the separation of a business from a larger parent, can transfer ownership legally while leaving essential operating dependencies behind.

Both are usually investor decisions: an owner pursuing further purchases, or a seller separating a unit to realize its value. The transaction is agreed on the investor’s timetable and priced on assumptions about combined savings and separation costs that product and engineering leaders may never have been asked about. Their work begins when those assumptions become operating obligations.

Both situations pose the same challenge: define which capabilities must work across a new boundary, who owns them, and what transition makes that possible. The transaction date changes ownership. Operational readiness is a separate condition.

This chapter closes Part III by bringing its questions together. An acquisition or separation tests product logic, architecture, costs, security and organization against a transaction timetable with little room for delay. [[teamsystem]] shows what accumulates when that happens repeatedly.

## Start With the Acquisition Thesis

A **buy-and-build** strategy uses a company as a base for further acquisitions. The base is often called the **platform company** and each later purchase an **add-on acquisition**; “platform” here describes the business’s role in the strategy, not a software system. The proposed value may come from distribution, product breadth, capabilities, purchasing, overhead or consolidation of a fragmented market. It can also depend partly on valuation differences between the platform and the smaller companies it buys. That financial mechanism is distinct from **operating synergy**, a benefit created by combining activities, such as a lower shared cost or a better customer offering.

**Organic growth** means development within an existing business under a stated comparison, not revenue added by buying another business. A larger consolidated revenue number doesn't establish it. The TeamSystem case shows how acquisition dates and constructed full-year comparisons can change the apparent growth rate: [[teamsystem]]. A combined product catalogue isn't necessarily a more useful customer proposition, and a lower group cost ratio isn't evidence that every acquired business improved.

Write the thesis in terms of what customers or the company will do differently. If the thesis is cross-selling, identify overlapping customer needs and a practical way for the sales team to offer and support the additional products. If it's product integration, identify the shared workflow and data boundaries. If it's cost reduction, identify the actual assets, contracts and roles that can change.

## The New Owner Changes the Integration Question

An acquisition is an event, not an operating model. In one fictional Larkspur scenario, a buyout fund wants its companies to share reporting while keeping separate products. In another, a corporate buyer expects Larkspur to serve its existing channel through a common offering. The product and engineering work differs because the intended benefit and the authority differ.

In the first scenario, identify the limited information and services that need sharing, and keep clear local responsibility for customers. In the second, identify the interfaces, data permissions, support duties and product choices the combined offering requires. A minority corporate investment could fund a commercial partnership without authorizing this deeper integration.

For a carve-out, settle the future owner separately from the separation obligations. Whatever the owner’s label, someone must fund the replacement of the parent’s services before those services end. Product and engineering leaders should bring the independence budget into the transaction discussion while there’s still time to change the scope, price or timetable.

## Choose the Depth of Integration

| Model | Potential value | Main question |
| --- | --- | --- |
| Preserve separate products | Retain focus and domain expertise | Which group capabilities justify common ownership? |
| Share selected services | Reduce repeated work or improve scarce capabilities | Does the service improve outcomes after transition and coordination costs? |
| Connect customer workflows | Make complementary products more useful | Can identity, data, contracts, support, and experience work together? |
| Consolidate products or platforms | Remove duplication and create one coherent offering | Can customers migrate without losing essential value? |

These are design options, not maturity levels. A company can sensibly choose different depths in different areas. Common security expectations don't require a common application architecture. A common brand may create customer expectations the underlying products can't yet meet.

The Skype case in [[hilton-and-skype]] shows why ownership of essential technology can be a transaction issue. **Intellectual property (IP)** means legal rights over assets such as software and inventions. Skype’s filings before the sale describe settling a dispute and acquiring core technology rights, alongside investment in the product and its supporting systems. [S27: Skype registration filing](https://www.sec.gov/Archives/edgar/data/1498209/000119312511096544/ds1a.htm) The lesson is to inspect the capability boundary, not just the source code.

![Separate operations, shared services and a combined product represent different integration choices.](assets/images/14-acquisition-adds-work-first/integration-depth-by-benefit.jpeg)
**Figure 1:** *Choose the depth of integration needed for the expected benefit and fund its transition.*

## Integration Consumes the Capacity It Promises to Free

The same engineers may be needed to deliver the current roadmap, keep the service running, support due diligence for the next acquisition and integrate the last one. A value-creation plan that allocates their time to every initiative independently creates fictional capacity.

Build a single dependency and capacity view. Identify work that must come first, the people who can't be duplicated, and the cost of delayed customer commitments. Test the acquisition cadence against this capacity. An attractive target can still be hard to absorb right now.

Integration estimates should include data cleanup, customer communication, training, running old and new systems together, contract changes, helping customers move and retiring the old systems. A platform isn't retired when its replacement launches. It's retired when the remaining customer and operating obligations have been resolved.

## The Carve-Out Has an Independence Bill

A division can rely on its parent for identity, networks, finance systems, procurement, licenses, customer contracts, support, security and employment services. Its historical accounts may carry allocations that don't reflect the cost of operating alone.

A **transition services agreement**, or TSA, provides temporary access to services after separation. Examine its scope, price, duration, service levels and exit conditions. A TSA buys time; it doesn't perform the separation.

The technology plan should distinguish three stages: **Day 1 continuity**, keeping services working on the first day of separate ownership; establishing independent operations; and making later improvements. Trying to optimize every system before separation can put continuity at risk. Reproducing the parent's setup without questioning its cost can create a permanently expensive business.

In a fictional example, a division's allocated **information technology (IT)** cost is €400,000 a year. Standalone operations need €700,000, plus €300,000 of separation work. The acquisition model must account for the €300,000 recurring difference and the one-time investment. Describing the division's historical margin without that bridge would overstate the resources available to the new company.

![A separated business must replace shared services or make explicit arrangements to keep using them.](assets/images/14-acquisition-adds-work-first/carveout-hidden-dependencies.jpeg)
**Figure 2:** *Independence requires working capabilities, rights and funding beyond the ownership transfer.*

## Investigate Rights and Dependencies Before the Purchase

**Due diligence** is the investigation that informs the investment decision. For a transaction, it should include evidence of who owns and can use the code, data, trademarks, licenses and contracts. Identify services that continue only with a supplier's or parent's agreement. Test whether customer data can be separated accurately and whether the business can run if a parent-provided service ends.

Use qualified specialists for legal rights, employment arrangements, privacy and transaction restrictions. Before closing, planning and information sharing must follow the applicable permissions and legal constraints. Operational enthusiasm isn't authority to combine systems or direct the target's business early.

A material separation risk can change the price, financing, conditions or feasibility of the investment. It shouldn't be buried in a technical appendix because the deal team already likes the company.

## Measure the Customer and Cash Results

An integration scorecard should track the specific mechanism. For cross-selling, measure qualified demand and incremental contribution, not accounts contacted. For product consolidation, track migration completion, retained functionality, customer loss, service quality and retired costs. For a carve-out, track independence milestones and stranded obligations.

Finance should reconcile acquired earnings, organic change, one-time costs and realized synergies. A recurring cost reduction that appears in both companies' plans counts once. A revenue opportunity isn't realized because the products now share an owner.

Company leaders need to make the transition feasible and its claimed benefits verifiable. An investor’s adviser can bring patterns and specialists from other acquisitions; the company still needs **an accountable owner for each part** of the operating plan.

Completing a transaction changes ownership. Completing the operating transition requires evidence that customers can still use the product, responsibilities are clear and the expected costs or dependencies have actually gone. The two milestones can be far apart.

Part III has examined which investments the company needs and what delivering them requires. Part IV explores the people, expertise and connections an investor may provide to help: [[part-4]] and [[investors-adviser]].

## Questions to Consider

1. *For the acquisition or separation closest to your company, what specific benefit is expected, and what will customers or the company do differently to realize it?*
2. *Which depth of integration does each area need: separate products, shared services, connected workflows or consolidation? Who chose, and why?*
3. *What is the single capacity view across your roadmap, ongoing service, integration and diligence for the next deal? Where are the same people counted twice?*
4. *If your business were separated from its parent tomorrow, which services would stop, what would replacing them cost and who has funded that?*
5. *What rights to code, data, licences and contracts does your company actually hold, and which depend on someone else’s continued agreement?*
6. *How does your integration scorecard distinguish realized synergies from benefits counted in both companies’ plans?*

## To Probe Further

- **[The Big Idea: The New M&A Playbook](https://hbr.org/2011/03/the-big-idea-the-new-ma-playbook)** — Clayton Christensen, Richard Alton, Curtis Rising and Andrew Waldeck, Harvard Business Review, 2011.<br>*Distinguishes acquisitions that improve current performance from those that change the business model, a direct complement to this chapter's advice to write the thesis as what changes.*
- **[Pricing and value creation in private equity-backed buy-and-build strategies](https://doi.org/10.1016/j.jcorpfin.2022.102285)** — Benjamin Hammer, Nikolaus Marcotty-Dehm, Denis Schweizer and Bernhard Schwetzler, Journal of Corporate Finance, 2022.<br>*Evidence from 3,399 buyouts on where buy-and-build returns come from, including the valuation-multiple mechanism this chapter separates from operating synergy, with only the abstract open.*
- **[The Art of Transition Service Agreement Negotiations](https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions/articles/recommendations-for-transition-service-agreement-negotiations.html)** — Deloitte, 2024.<br>*An adviser's guidance on scoping, pricing and exit conditions for a transition services agreement, useful for the questions to ask before a carve-out's independence bill is fixed.*
- **[Open Source Audits in Merger and Acquisition Transactions](https://www.linuxfoundation.org/blog/blog/open-source-audits-merger-acquisition-transactions-get-free-ebook)** — Ibrahim Haddad, The Linux Foundation, 2018; free ebook.<br>*Explains how a code audit establishes which open-source components a target uses under which licences, turning this chapter's who-can-use-the-code question into a concrete diligence step.*
- **[Premerger Notification and the Merger Review Process](https://www.ftc.gov/advice-guidance/competition-guidance/guide-antitrust-laws/mergers/premerger-notification-merger-review-process)** — United States Federal Trade Commission, living page.<br>*The regulator's plain-language guide to the pre-closing waiting period, which explains why integration planning has legal limits, the point this chapter makes about enthusiasm not being authority.*
