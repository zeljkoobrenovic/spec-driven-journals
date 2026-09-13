---
title: A Transaction Changes Ownership Before It Changes Operations
date: 2026-09-12
author: Owned working manuscript
excerpt: "Plan the practical work of combining or separating businesses while keeping customers served and costs understood."
permalink: acquisitions-and-carveouts
timetoread: 8 min read
status: draft:orange
logo: "assets/images/14-acquisitions-and-carveouts/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/14-acquisitions-and-carveouts.png"
---

> **KEY POINTS:**
>
> * A transaction **changes ownership before it changes operations**. An acquisition needs a deliberate integration plan; a separation needs the capabilities to operate independently.
> * Combine activities for a **specific benefit**. Buying more products, customers or revenue does not by itself show that the existing business has improved.
> * **Fund the transition** and measure what survives it. Include shared-service dependencies, parallel operation, customer migration and costs that cannot yet be retired.

<br>
An **acquisition** is the purchase of a business or ownership interest in it. It can add customers and products to a group immediately. **Integration**, the work of making selected activities operate together, still has to be planned and carried out. A **carve-out**, the separation of a business from a larger parent, can transfer ownership legally while leaving essential operating dependencies behind.

For product and engineering leaders, both situations create the same underlying challenge: define which capabilities must work across a new boundary, who owns them, and what transition makes that possible. The transaction date is a change in ownership. Operational readiness is a separate condition.

This chapter closes Part III by bringing its questions together. An acquisition or separation tests the product logic, architecture, costs, security and organization against a transaction timetable that may leave little room for delay. [[teamsystem]] shows what accumulates when that is done repeatedly.

## Start With the Acquisition Thesis

A **buy-and-build** strategy uses a company as a base for further acquisitions. The initial base is often called the **platform company**, and a subsequent purchase an **add-on acquisition**. Here “platform” describes the business’s role in the acquisition strategy, rather than a software system. The proposed value may come from distribution, product breadth, capabilities, purchasing, overhead, or consolidation of fragmented markets. It can also depend partly on valuation differences between the platform and smaller acquisitions. That financial mechanism must be distinguished from **operating synergy**, a benefit created by combining activities, such as lowering a shared cost or improving the customer offering.

**Organic growth** concerns development within an existing business under a stated comparison, rather than simply revenue added by buying another business. A larger consolidated revenue number does not establish it. The TeamSystem case shows how acquisition dates and constructed full-year comparisons can change the apparent growth rate: [[teamsystem]]. A combined product catalogue is not necessarily a more useful customer proposition. A lower group cost ratio is not necessarily evidence that every acquired business improved.

Write the thesis in terms of the work customers or the company will do differently. If the thesis is cross-selling, identify overlapping customer needs and a practical way for the sales team to offer and support the additional products. If it is product integration, identify the shared workflow and data boundaries. If it is cost reduction, identify the actual assets, contracts, and roles that can be changed.

## The New Owner Changes the Integration Question

An acquisition is an event, not a single operating model. In one fictional Larkspur scenario, a buyout fund wants companies to share reporting while keeping separate products. In another, a corporate buyer expects Larkspur to serve its existing channel through a common offering. The product and engineering work differs because the intended benefit and authority differ.

For the first scenario, identify the limited information and services that need to be shared, and preserve clear local responsibility for customers. For the second, identify the interfaces, data permissions, support duties and product choices the combined offering requires. A minority corporate investment could fund a commercial partnership without authorizing this deeper integration.

For a carve-out, establish the future owner separately from the separation obligations. Whatever the owner’s label, someone must fund the replacement of the parent’s services before those services end. Product and engineering leaders should bring the independence budget into the transaction discussion while there is still time to change the scope, price or timetable.

## Choose the Depth of Integration

| Model | Potential value | Main question |
| --- | --- | --- |
| Preserve separate products | Retain focus and domain expertise | Which group capabilities justify common ownership? |
| Share selected services | Reduce repeated work or improve scarce capabilities | Does the service improve outcomes after transition and coordination costs? |
| Connect customer workflows | Make complementary products more useful | Can identity, data, contracts, support, and experience work together? |
| Consolidate products or platforms | Remove duplication and create one coherent offering | Can customers migrate without losing essential value? |

These are design options, not maturity levels. A company can sensibly choose different integration depths in different areas. Common security expectations do not require a common application architecture. A common brand may create customer expectations that the underlying products are not yet able to meet.

The Skype case in [[hilton-and-skype]] shows why ownership of essential technology can be a transaction issue. **Intellectual property (IP)** means legal rights concerning assets such as software and inventions. Skype’s filings before the sale describe settling a dispute and acquiring core technology rights, alongside investment in the product and its supporting systems. [S27: Skype registration filing](https://www.sec.gov/Archives/edgar/data/1498209/000119312511096544/ds1a.htm) The lesson is to inspect the capability boundary, not just the source code.

![Separate operations, shared services and a combined product represent different integration choices.](assets/images/14-acquisitions-and-carveouts/integration-depth-by-benefit.jpeg)
**Figure 1:** *Choose the depth of integration needed for the expected benefit and fund its transition.*

## Integration Consumes the Capacity It Promises to Free

The same engineers may be needed to deliver the current roadmap, maintain service, support due diligence for the next acquisition, and integrate the last one. A value-creation plan that allocates their time independently to every initiative creates fictional capacity.

Build a shared dependency and capacity view. Identify work that must precede other work, the people who cannot be duplicated, and the cost of delayed customer commitments. Acquisition cadence should be tested against this capacity. An attractive target can still be difficult to absorb now.

Integration estimates should include data cleanup, customer communication, training, running old and new systems together, contract changes, helping customers move, and retiring the old systems. A platform is not retired when its replacement launches. It is retired when the remaining customer and operating obligations have been resolved.

## The Carve-Out Has an Independence Bill

A division can rely on a parent for identity, networks, finance systems, procurement, licenses, customer contracts, support, security, and employment services. Its historical accounts may contain allocations that do not represent the cost of operating independently.

A **transition services agreement**, or TSA, can provide temporary access to services after separation. Its scope, price, duration, service levels, and exit conditions need examination. A TSA buys time; it does not perform the separation.

The technology plan should distinguish three stages: **Day 1 continuity**, keeping services working on the first day of separate ownership; establishing independent operations; and making later improvements. Trying to optimize every system before separation can put continuity at risk. Conversely, reproducing the parent's setup without questioning its cost can create a permanently expensive business.

In a fictional example, a division's allocated **information technology (IT)** cost is €400,000 a year. Standalone operations require €700,000, plus €300,000 of separation work. The acquisition model must account for the €300,000 recurring difference and the one-time investment. Describing the division's historical margin without that bridge would overstate the resources available to the new company.

![A separated business must replace shared services or make explicit arrangements to keep using them.](assets/images/14-acquisitions-and-carveouts/carveout-hidden-dependencies.jpeg)
**Figure 2:** *Independence requires working capabilities, rights and funding beyond the ownership transfer.*

## Investigate Rights and Dependencies Before the Purchase

**Due diligence** is the investigation that informs the investment decision. For a transaction, it should include evidence of who owns and can use code, data, trademarks, licenses and contracts. Identify services that can continue only with a supplier's or parent's agreement. Test whether customer data can be separated accurately and whether the business can operate if a parent-provided service ends.

Use qualified specialists for legal rights, employment arrangements, privacy, and transaction restrictions. Before closing, planning and information sharing must follow applicable permissions and legal constraints. Operational enthusiasm is not authority to combine systems or direct the target's business early.

A material separation risk can change price, financing, transaction conditions, or the feasibility of the investment. It should not be hidden in a technical appendix because the deal team already likes the company.

## Measure the Customer and Cash Results

An integration scorecard should track the particular mechanism. For cross-selling, measure qualified demand and incremental contribution, not simply accounts contacted. For product consolidation, track migration completion, retained functionality, customer loss, service quality, and retired costs. For a carve-out, track independence milestones and stranded obligations.

Finance should reconcile acquired earnings, organic change, one-time costs, and realized synergies. A recurring cost reduction that appears in both companies' plans should be counted once. A revenue opportunity should not be treated as realized simply because the products now share an owner.

Company leaders need to make the transition feasible and its claimed benefits verifiable. An investor’s adviser can bring patterns and specialists from other acquisitions; the company still needs **an accountable owner for each part** of the operating plan.

Completing a transaction changes ownership. Completing the operating transition requires evidence that customers can still use the product, responsibilities are clear and the expected costs or dependencies have actually been removed. The two milestones can be far apart.

Part III has examined which investments the company needs and what delivering them requires. Part IV explores the people, expertise and connections an investor may provide to help: [[part-4]] and [[technology-principal]].
