---
title: What Would Make an AI Investment Worth Owning?
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Compare product value, internal productivity, disruption, data rights, and date-specific experimental evidence.
permalink: pt-data-and-ai
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **Separate product opportunity, operating improvement and competitive threat.** Each asks a different investment question and needs its own evidence.
> * **Measure the complete workflow.** Include review, correction, data preparation and ongoing operation, rather than treating model output or adoption as value.
> * **Keep experimental results attached to their conditions.** Tools, tasks and participants change. Test the local effect before turning estimated time savings into a financial commitment.

<br>
An AI strategy can contain three very different investment questions. Can AI improve the product customers buy? Can it improve how the company operates? Can it undermine the company's existing advantage?

Combining these into a single adoption target obscures the economics. A company can use AI extensively without creating value, create value through a narrow use case, or face disruption even if its own experiments work well.

The Technology Principal should help separate the questions and attach each to evidence, cost, and a decision. The analysis in this chapter is dated September 2026; the cited experiments describe particular earlier tools and populations.

## Start With the Customer's Work

Suppose customers spend hours classifying incoming documents before scheduling maintenance. An AI-assisted workflow could save time, but the product value depends on error costs, review effort, and how the output enters the customer's process.

The evaluation should compare the complete workflow with the current alternative. How many cases need correction? Which errors are difficult to detect? Does the customer trust the output enough to act? Is the new workflow faster after review and exception handling? Would the customer pay for it, and what would it cost to serve them?

Model cost per successful outcome rather than cost per model request alone. Include evaluation, human review, data preparation, monitoring, support, and fallback operations. A low inference bill can coexist with expensive failures and a weak product proposition.

## Data Can Be an Asset, a Constraint, or a Liability

A large dataset does not automatically create defensibility. Ask whether the company has rights to use it for the proposed purpose, whether it represents the relevant population, and whether its quality and update process support the task. Customer trust and contractual restrictions can matter as much as technical availability.

Separate access from ownership and training rights from other processing rights. A company that can display information to a user may not have every right needed to reuse it in a different AI service. Specialist review should resolve actual contractual and legal questions.

NIST's 2024 Generative AI Profile identifies risks and suggested management actions across the AI lifecycle. It is a voluntary framework reference, not evidence that a particular product is compliant or effective. [S18: NIST generative AI profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) Its practical contribution here is to make evaluation and risk management part of the product investment rather than an afterthought.

## Productivity Evidence Needs Its Experimental Conditions

A 2023 controlled experiment by Peng and colleagues asked developers to build a JavaScript HTTP server. Participants with GitHub Copilot completed that defined task 55.8% faster. The result supports a claim about that experimental task; it does not establish an equivalent reduction in a company's engineering budget. [S19: Peng et al., Copilot experiment](https://arxiv.org/abs/2302.06590)

METR's early-2025 randomized study examined experienced open-source developers working on their own repositories and found tasks took 19% longer with AI allowed. That result concerns a different population, setting, and tool period. [S20: METR early-2025 experiment](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

In February 2026, METR reported that its later experiment had serious selection and measurement problems: developers and tasks likely to benefit from AI were increasingly excluded, and concurrent agent use complicated time measurement. The researchers considered the new data a weak guide to the size of current productivity effects. [S21: METR 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)

These studies are not competing universal laws. Their differences show why context, task selection, tool version, and outcome definition belong in an investment decision. A favorable coding result is also only one part of delivery: product decisions, review, testing, integration, release, and customer adoption can become the limiting steps.

## Run a Company Experiment That Can Change a Decision

Define the proposed economic mechanism before buying licenses or promising savings. Perhaps the company wants to reduce time spent on routine support responses, accelerate a specific migration, or improve the quality of product discovery. Different goals need different measures.

Choose a bounded population and a credible comparison. Record task type, experience, tool and model version, time period, and quality criteria. Include the cost of reviewing output and correcting errors. Track whether the experiment changes what work people choose, because task substitution can make a simple before-and-after comparison misleading.

Predetermine what would justify continuation, expansion, redesign, or stopping. If quality falls below the product's requirements, a faster completion time is insufficient. If the team produces more useful work at the same cost, the result may be valuable even without a headcount reduction.

A pilot should also reveal the operating burden. Who updates evaluations when the model changes? Who handles regressions? What happens when the provider is unavailable or changes commercial terms? A product capability needs an owner beyond the enthusiastic initial demonstration.

## Do Not Underwrite Uncaptured Capacity as Cash

Suppose, fictionally, an intervention saves 1,000 hours of recurring work a quarter. The company still pays the same employees. The result is capacity, subject to the quality of the measurement. It becomes cash savings only through a further operating change, such as reducing external spending or avoiding planned hiring. It becomes revenue only if the capacity enables work customers buy.

The investment case should state which route is intended. Announcing an engineering reduction before demonstrating the mechanism can remove the expertise needed to capture any benefit and evaluate the output. That is an execution risk to test, not a claim that staffing can never change.

## Assess the Threat to the Existing Product

AI might make a feature easier for competitors to reproduce, reduce the customer's need for a workflow, or shift value toward a different interface. These are scenario hypotheses. They require customer evidence and a view of switching costs, distribution, trust, and the full task being performed.

A product's advantage may lie in reliable execution, specialized knowledge, regulatory integration, customer relationships, or embedded workflow rather than the difficulty of generating code. Conversely, an installed base does not guarantee that a new interface will preserve the company's role.

The Principal's market work should therefore test both opportunity and substitution. What would a new entrant need to replace the product's useful outcome? What would customers lose or gain? Which experiments can the company run before a threat becomes an urgent revenue problem?

AI investment becomes worth owning when it creates a dependable capability with a credible economic path, an accountable operating model, and evidence that survives changes in tools. Adoption is an input. The company's ability to create and retain customer value remains the outcome.
