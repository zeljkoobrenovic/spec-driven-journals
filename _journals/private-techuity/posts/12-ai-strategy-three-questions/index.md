---
title: "An AI Strategy Hides Three Investment Questions"
date: 2026-09-12
author: Owned working manuscript
excerpt: "Examine three AI questions: better products, better internal work and threats to the business customers already buy from."
permalink: ai-strategy-three-questions
timetoread: 8 min read
logo: "assets/images/12-ai-strategy-three-questions/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/12-ai-strategy-three-questions.png"
---

> **KEY POINTS:**
>
> * Separate **product opportunity, operating improvement and competitive threat**. Each asks a different investment question, needs its own evidence, and reaches beyond product and engineering.
> * Measure the **complete workflow**. Include review, correction, data preparation and ongoing operation, so that using a tool is not mistaken for getting a useful result.
> * Keep **experimental results attached to their conditions**. Tools, tasks and participants change. Test the local effect before turning estimated time savings into a financial commitment.

<br>
An investor asks for an “AI strategy.” The product team sees a new customer feature, the finance team expects lower costs, and the CEO worries about a competitor replacing the product. These are **three different investment questions**: a product opportunity, an operating improvement and a competitive threat.

Rolling the three into a single adoption target **obscures the economics**. A company can use AI extensively without creating value, create value through a narrow use case, or face disruption even if its own experiments work well.

The request also reaches beyond the product. AI can change what the company is worth, what a buyer will pay for it, and whether the investment case survives a competitor’s product replacing it. Product and engineering leaders are being asked **a valuation question dressed as a technology question**, and a headline commitment can be made on the company’s behalf before anyone has examined the work.

That pressure is why AI gets its own chapter, even though the earlier chapters on product value, engineering, cloud economics and security supply most of the tools it uses. Almost every investor now holds some expectation about AI, as a line in the investment thesis, a question at each board meeting or an assumption in the exit story, so the **push to commit is stronger** here than for most technology topics. The same attention brings **hype, shifting vocabulary and claims that are hard to check**. Where expectations run high and evidence is muddled, a way to sort the questions is worth more than another opinion about the technology.

Three terms recur. **Artificial intelligence (AI)** here means software that classifies information, makes predictions or generates content from learned patterns. **Generative AI** produces text, images or code. An **AI model** is the component that learns those patterns from data and produces the outputs; its output needs evaluating in the task where it will be used.

The chapter looks at customer uses first, then the data they need, the evidence on internal productivity and the threat to the existing product, before turning to the shape an AI strategy needs across the whole company. The value chain from [[roadmap-to-revenue]] and the uncertainty discussed in [[prove-you-can-restore]] stay useful throughout, and an investor’s adviser can help within the boundaries described in [[investors-adviser]]. At each step the aim is to **separate the questions and attach each to evidence, cost and a decision**. The analysis is dated September 2026; the cited experiments describe particular earlier tools and populations.

## Start With the Customer's Work

Suppose customers spend hours classifying incoming documents before scheduling maintenance. An AI-assisted workflow could save time, but the product value depends on error costs, review effort, and how the output enters the customer's process.

Compare the complete workflow with the current alternative. How many cases need correction? Which errors are hard to detect? Does the customer trust the output enough to act on it? Is the new workflow still faster after review and exception handling? Would the customer pay for it, and what would it cost to serve them?

Estimate the cost per successful outcome rather than the cost per model request alone. Include evaluation, human review, data preparation, monitoring, support and fallback operations. **Inference**, running a trained model to produce an output, can be cheap while review is expensive, mistakes are common and the customer gains little.

![AI can create a product opportunity, improve an operating workflow or threaten the current product; each question needs its own evidence.](assets/images/12-ai-strategy-three-questions/three-ai-investment-questions.jpeg)
**Figure 1:** *Separate the investment questions before choosing an experiment or making a commitment.*

## Data Can Be an Asset, a Constraint or a Liability

A large dataset doesn't automatically give the company an advantage competitors will struggle to copy. Ask whether the company has the rights to use it for the proposed purpose, whether it represents the relevant population, and whether its quality and update process support the task. Customer trust and contractual restrictions can matter as much as technical availability.

Separate access from ownership, and training rights from other processing rights. A company that may display information to a user may not have every right needed to reuse it in a different AI service. Leave the actual contractual and legal questions to specialist review.

The US National Institute of Standards and Technology (**NIST**) identifies risks and suggested management actions across the AI lifecycle in its 2024 Generative AI Profile. It's a voluntary reference, not evidence that a particular product is compliant or effective. [S18: NIST generative AI profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) Its practical use here is to make evaluation and risk management part of the product investment rather than an afterthought.

## Productivity Evidence Comes With Its Conditions

A **controlled experiment** compares outcomes under different conditions, such as doing a task with and without a tool. One run in 2022 and published by Peng and colleagues in 2023 asked developers to build a small **server**, software that receives and answers web requests, in JavaScript. Among participants who completed the task, those given GitHub Copilot, an AI coding assistant, took 55.8% less time on average. That supports a claim about the experimental task, not an equivalent cut in a company's engineering budget. [S19: Peng et al., Copilot experiment](https://arxiv.org/abs/2302.06590)

**METR**, an AI evaluation research organization, ran an early-2025 **randomized study**, assigning tasks to conditions by chance, with experienced developers working on their own **open-source projects**, software whose licenses let others use, change and share the code. Tasks took 19% longer when AI was allowed. That's a different population, setting and tool period. [S20: METR early-2025 experiment](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

In February 2026, METR reported that its follow-up experiment had serious selection and measurement problems: developers and tasks likely to benefit from AI were increasingly excluded, and running several AI agents at once, systems that carry out tasks on a user’s behalf, complicated time measurement. The researchers called the new data a weak guide to the size of current productivity effects. [S21: METR 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)

These studies aren't competing universal laws. Their differences show why context, task selection, tool version and outcome definition belong in an investment decision. A favorable coding result is also only one part of delivery: product decisions, review, testing, integration, release and customer adoption can become the limiting steps.

## Separate a Funding Demonstration From a Product Commitment

In a fictional Larkspur funding round, an investor wants an AI demonstration before the next meeting. Priya and Alex can agree a bounded demonstration while recording what it doesn't yet establish: customer demand, reliable performance, permission to use production data and the full cost of serving customers. The financing conversation shouldn't silently turn the demonstration into a promised launch.

Under an expansion plan, the test becomes whether the use case works repeatedly across customers and their different data. A corporate investor may offer a valuable dataset while seeking access to the company’s customer information in return. Treat each direction of access as a separate decision with its own purpose, authority and operating responsibility.

The leader’s commitment should state which question the experiment answers and **which decision follows a positive, negative or uncertain result**. If the investor expects a staffing reduction, test the complete workflow and **the feasible change in expenditure** before booking a saving. A funding narrative can't supply the evidence the operating case lacks.

## Run an Experiment That Can Change a Decision

Define the economic mechanism before buying licenses or promising savings. Perhaps the company wants to cut time spent on routine support responses, speed up a specific migration or improve product discovery. Different goals need different measures.

Choose a defined group of tasks and participants and a credible comparison. Record task type, experience, tool and model version, time period and quality criteria. Include the cost of reviewing output and correcting errors. Track whether the experiment changes which work people choose, because task substitution can make a simple before-and-after comparison misleading.

Decide in advance what would justify continuing, expanding, redesigning or stopping. If quality falls below the product's requirements, faster completion isn't enough. If the team produces more useful work at the same cost, the result may be valuable even without reducing headcount.

A pilot should also reveal the operating burden. Who updates evaluations when the model changes? Who handles **regressions**, cases where an update makes previously acceptable behavior worse? What happens when the provider is unavailable or changes its commercial terms? A product capability needs an owner who outlasts the enthusiastic first demonstration.

![A baseline and an AI-assisted workflow are compared across preparation, production, review, correction and delivery.](assets/images/12-ai-strategy-three-questions/measure-the-whole-ai-workflow.jpeg)
**Figure 2:** *Measure the complete local workflow and its output before converting a task result into a financial promise.*

## Explain How Saved Time Will Be Used

Suppose, fictionally, an intervention saves 1,000 hours of recurring work a quarter. The company still pays the same employees. What it has gained is capacity, subject to the quality of the measurement. Capacity becomes cash savings only through a further operating change, such as cutting external spending or avoiding planned hiring. It becomes revenue only if it enables work customers buy.

The investment case should say which route is intended. Announcing an engineering reduction before demonstrating the mechanism can remove the expertise needed to capture the benefit and evaluate the output. That's an execution risk to test, not a claim that staffing can never change.

## Assess the Threat to the Product You Already Sell

AI might make a feature easier for competitors to reproduce, reduce the customer's need for a workflow or shift value toward a different interface. These are hypotheses. Testing them needs customer evidence and a view of **switching costs**, the money and effort needed to move to another product, along with access to customers, trust and the full task being performed.

A product's advantage may lie in reliable execution, specialized knowledge, regulatory integration, customer relationships or embedded workflow rather than in the difficulty of generating code. Conversely, an existing customer base doesn't guarantee that a new interface will preserve the company's role.

The product leader’s market work, with the investor’s adviser where useful, should test both opportunity and substitution. What would a new entrant need to replace the product's useful outcome? What would customers lose or gain? Which experiments can the company run before a threat becomes an urgent revenue problem?

## Treat AI as an Operating Model, Not a Feature Roadmap

So far the three questions have been examined from where product and engineering leaders sit. That's also where most companies make their first mistake: **they treat AI as a product and engineering topic**. The investor asks for an AI strategy, the request lands with the technology leader, and the answer comes back as a feature roadmap and a coding-assistant pilot. The rest of the business adopts whatever tools it finds.

Yet those other functions are often **where the operating question is largest**. Marketing, sales, customer service, data, legal and finance each run workflows shaped like the ones above: routine work, review, correction and a result somebody depends on. Each carries its own risks, such as a customer-facing error, a contractual limit on data use or a regulatory obligation a tool can't see. An AI strategy that covers only the product **can't answer an investor who expects the whole company to work differently**, and can't see a threat arriving through the sales or service channel.

The alternative is **an org-wide operating model**. Each function sets **its own AI goals** in the terms of its own work: cases resolved, proposals produced, contracts reviewed, sales cycles shortened. Each names a **champion**, one person who owns those goals, runs the local experiments and reports what the evidence shows. Each has **a seat where the strategy is set**, so trade-offs between functions are made openly rather than by whoever bought licenses first. Product and engineering keep the customer product and the shared platform, evaluation and data questions, but as **one function among several**, not the owner of the whole topic.

This is more structure than a small company can staff at once, and a champion without time or authority becomes a reporting layer rather than a source of decisions. **Start with the two or three functions** where the workflow is largest or the investor's expectation most specific, apply the same experiment discipline, and extend the model as evidence arrives. The test of an AI strategy is **whether every function can state its goal, its owner and its evidence**, not how long the product roadmap is.

Whatever the function, assess an AI investment through the complete task: what improves, how quality is checked, what the workflow costs and who maintains it as the technology changes. Record the tools and dates so later readers know which evidence still applies.

Even a useful tool depends on people who can evaluate, operate and improve it. The next chapter examines the organization needed to sustain technology work: [[fix-decisions-before-hiring]].

## Questions to Consider

1. *When your investor asks for an “AI strategy”, which of the three questions are they asking: product opportunity, operating improvement or competitive threat? Which one is your company answering?*
2. *For your most promising AI use case, what is the cost per successful outcome once review, correction, data preparation and monitoring are included?*
3. *What rights does your company hold to the data it plans to use, and for which purposes? Which of those assumptions has a specialist checked?*
4. *If a productivity pilot saved 1,000 hours a quarter, what would your company do with them, and which route to a financial result is being promised?*
5. *Which AI-related commitments has your company made to investors that a demonstration cannot support?*
6. *What would a competitor need in order to reproduce your product’s useful outcome, and which experiments could test that before the threat becomes urgent?*
7. *Which functions outside product and engineering have their own AI goal, a named champion and a seat where the strategy is set? Which are adopting tools on their own?*

## To Probe Further

- **[Generative AI at Work](https://www.nber.org/papers/w31161)** — Erik Brynjolfsson, Danielle Li and Lindsey Raymond, National Bureau of Economic Research working paper, 2023.<br>*A study of 5,179 support agents given an AI assistant, which shows the operating-improvement question examined outside engineering with the full workflow measured rather than tool usage.*
- **[Navigating the Jagged Technological Frontier](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)** — Fabrizio Dell'Acqua and colleagues, Harvard Business School working paper, 2023 (later in Organization Science).<br>*A field experiment with 758 consultants that supports the chapter's point that productivity results stay attached to the task, and shows what a bounded experiment looks like.*
- **[Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html)** — United States Census Bureau, May 2026.<br>*A public baseline for AI adoption by company size and sector, useful when an investor's expectation seems out of step with what companies actually report.*
- **[Disruptive Technologies: Catching the Wave](https://hbr.org/1995/01/disruptive-technologies-catching-the-wave)** — Joseph Bower and Clayton Christensen, Harvard Business Review, 1995.<br>*The article that introduced disruptive technology, which gives the chapter's competitive-threat question a structure by asking which customers a substitute serves first.*
- **[ISO/IEC 42001:2023 — Artificial intelligence management system](https://www.iso.org/standard/81230.html)** — International Organization for Standardization and International Electrotechnical Commission, 2023.<br>*A paid standard whose structure of policies, roles, risk assessment and supplier oversight maps closely to the org-wide AI operating model this chapter argues for.*
