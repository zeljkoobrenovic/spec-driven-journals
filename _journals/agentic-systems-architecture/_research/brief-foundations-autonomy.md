# Research brief: Foundations, autonomy levels, and when agents are justified

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief covers what an "agent" is, where today's agent loop came from, how autonomy has been graded, when an agent beats a deterministic workflow, how reliability falls with task length and step count, what realistic benchmarks say about failure rates, and what forty years of automation research says about humans left to supervise automation. The point throughout is to help an architect set system boundaries by **uncertainty, autonomy, task duration, reversibility and consequence of failure**. The brief is vendor-neutral. Anthropic and OpenAI get space because they have published dated design guidance and usage data, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date (or first arXiv submission, with later revisions noted), not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, encyclopaedia, conference listing, summaries of a document that could not be fetched directly).
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including all arithmetic illustrations and every architecture implication. Chapter writers should present these as the book's judgement, not as findings.

**Source types.** Each source in the list is typed: *paper (peer-reviewed)*, *preprint*, *vendor engineering post*, *vendor guide* (a vendor's practitioner document that also markets its SDK), *analyst press release*, *standard*, *encyclopaedia*. Vendor guides describe what the vendor recommends to customers; they are not evidence that the recommendation works.

**Evidence age matters.** This field moves fast. A benchmark result older than about 18 months describes models that have since been replaced; treat the *shape* of the finding (for example, "reliability across repeated trials is much lower than single-trial success") as durable and the *number* as historical. Each section dates its evidence. The original ReAct, Toolformer, Reflexion and chain-of-thought papers (2022–2023) used models that are no longer in service; they matter as origins of the loop, not as measures of current capability. Anthropic's own "Building effective agents" page now carries a note that much of the tooling it describes has changed since December 2024.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: model names, benchmark leaderboards, time-horizon values and doubling times, vendor product names.

**Research limitation.** Several primary documents could not be read directly in this session:

- **Google's "Agents" whitepaper** (Wiesinger, Marlow, Vuskovic, September 2024) is distributed via Kaggle and could not be fetched; its definition and component model are reported here from secondary summaries and tagged WIDELY REPORTED.
- **SAE J3016** is paywalled and the SAE pages returned only headers; level descriptions come from an encyclopaedia summary. The 2021 revision date (J3016_202104) is analyst knowledge.
- **Gartner's June 2025 press release** returned HTTP 403; its content is reported from press coverage.
- **Russell & Norvig** (the textbook) was not consulted directly; the definition is via an encyclopaedia citation of the 4th edition (2021).
- **Sheridan & Verplank (1978)**, the original ten-level automation scale, was not fetched; only its successor (Parasuraman, Sheridan & Wickens 2000) was verified.
- Several figures exist only in charts (τ-bench pass^k for k = 2–7, per-model METR 80% horizons) and could not be read as text; the brief gives only the endpoints stated in prose.
- No source in this brief measures failure rates of *production* agent deployments in finance, legal, HR, healthcare or public benefits. Benchmarks simulate offices, retail, airlines, telecom and CRM. Treat all extrapolation to regulated domains as judgement.

---

## PART 1: What an agent is, and where the loop came from

### 1.1 The classical definition

- Russell & Norvig define an agent as "anything that perceives its environment through sensors and acts upon that environment through actuators" (cited to *Artificial Intelligence: A Modern Approach*, 4th edition, 2021) [WIDELY REPORTED: https://en.wikipedia.org/wiki/Intelligent_agent, 2021 edition cited].
- The same textbook tradition (2nd edition, 2003) classifies agents as simple reflex, model-based reflex, goal-based, utility-based and learning agents [WIDELY REPORTED: https://en.wikipedia.org/wiki/Intelligent_agent, 2003 edition cited].
- [ASSUMPTION/JUDGEMENT] The classical definition is deliberately broad: a thermostat qualifies. It says nothing about language models. Its value to the book is the vocabulary it supplies — *environment*, *percept*, *action*, *goal*, *utility*, *partial observability* — which maps cleanly onto LLM systems: the context window is the percept, tool calls are actuators, and the environment is the set of systems the tools reach. The LLM-era definitions below are narrower and are mostly about **who controls the control flow**.

### 1.2 LLM-era vendor definitions

| Source | Date | Definition (quoted or close paraphrase) | What decides "agent" |
| --- | --- | --- | --- |
| Anthropic, "Building effective agents" | 2024-12-19 | Workflows: "systems where LLMs and tools are orchestrated through predefined code paths." Agents: "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." | Whether the **code or the model** owns the control flow |
| OpenAI, "A practical guide to building agents" | 2025-04 | "Agents are systems that independently accomplish tasks on your behalf." Chatbots, single-turn LLMs and sentiment classifiers that "don't use them to control workflow execution" are not agents. | Whether the LLM **manages workflow execution** and selects tools |
| Google, "Agents" whitepaper | 2024-09 | "an application that attempts to achieve a goal by observing the world and acting upon it" using its tools; three components: model, tools, orchestration layer | Goal-directed observe–act cycle |
| Mitchell et al. (Hugging Face) | 2025-02 (rev. 2025-10) | "Computer software systems capable of creating context-specific plans in non-deterministic environments." | Planning under non-determinism |

Sources and details:

- Anthropic's definitions of workflows and agents, quoted above [VERIFIED: https://www.anthropic.com/research/building-effective-agents, published 2024-12-19]. The same post calls the whole category "agentic systems" and describes the building block as an "augmented LLM" (an LLM with retrieval, tools and memory) [VERIFIED: same URL, 2024-12-19].
- Anthropic lists five workflow patterns — prompt chaining, routing, parallelization (sectioning and voting), orchestrator-workers, evaluator-optimizer — before "autonomous agents", described as LLMs using tools in a loop based on environmental feedback [VERIFIED: same URL, 2024-12-19].
- OpenAI's guide says an agent "leverages an LLM to manage workflow execution and make decisions", "recognizes when a workflow is complete and can proactively correct its actions", and "in case of failure, it can halt execution and transfer control back to the user"; it selects tools dynamically "always operating within clearly defined guardrails" [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, published 2025-04 (PDF creation date 2025-04-07)].
- OpenAI names three components: model, tools, instructions [VERIFIED: same PDF, 2025-04].
- Google's whitepaper, by Julia Wiesinger, Patrick Marlow and Vladimir Vuskovic, dated September 2024, describes an agent as model + tools + an orchestration layer forming a "cognitive architecture", with the orchestration layer running a cyclical take-in-information / reason / act process using frameworks such as ReAct, chain-of-thought and tree-of-thoughts [WIDELY REPORTED: https://www.aihero.dev/google-agents-whitepaper-review, 2025; https://venturebeat.com/ai/google-maps-the-future-of-ai-agents-five-lessons-for-businesses, 2025]. ⚠ Exact wording not verified against the PDF.
- Mitchell, Ghosh, Luccioni and Pistilli's working definition is quoted above [VERIFIED: https://arxiv.org/html/2502.02649, first submitted 2025-02-04, v3 2025-10-20].

**Where the definitions differ.** Anthropic draws the line inside the "agentic" category (workflow vs agent, both agentic). OpenAI draws it at control of workflow execution and excludes single-turn LLM features. Google's definition is closest to the classical one and would include many of Anthropic's workflows. [ASSUMPTION/JUDGEMENT] The book should adopt a **control-flow definition** — *who decides the next step: code, or the model?* — because it is the one an architect can check by reading the code, and it directly determines testability, worst-case cost and blast radius.

**Durable vs volatile.** Durable: the distinction between predefined code paths and model-directed control flow; the model / tools / instructions-or-orchestration decomposition. Volatile: the vendors' pattern names and SDK vocabulary ("handoffs", "agents as tools", "Managed Agents"), which already changed after these documents were written.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] "Agent" is not a property of a product; it is a property of **each decision point**. One system routinely contains deterministic steps, a routed LLM call, and one bounded agent loop. Architects should label every decision point by who owns it and design boundaries per point, not per system.

### 1.3 Research origins of the agent loop

| Paper | First posted | Venue | What it introduced | What was actually measured |
| --- | --- | --- | --- | --- |
| Chain-of-Thought Prompting (Wei et al.) | 2022-01-28 | NeurIPS 2022 (WR) | Prompting with worked intermediate reasoning steps | Arithmetic, commonsense, symbolic reasoning on three LLMs; a 540B model with eight CoT exemplars reached state of the art on GSM8K |
| ReAct (Yao et al.) | 2022-10-06 | ICLR 2023 | Interleaving reasoning traces with actions and observations | HotpotQA, FEVER, ALFWorld (+34 points absolute success over imitation/RL baselines), WebShop (+10 points), with one or two in-context examples |
| Toolformer (Schick et al., Meta) | 2023-02-09 | NeurIPS 2023 (WR) | Self-supervised learning of when/how to call APIs | Calculator, Q&A, two search engines, translation, calendar; zero-shot downstream gains "often competitive with much larger models" |
| Reflexion (Shinn et al.) | 2023-03-20 | NeurIPS 2023 (WR) | Verbal self-reflection stored in episodic memory, no weight updates | Decision-making, coding, reasoning; HumanEval pass@1 91% vs 80% for GPT-4 |

- Chain-of-thought: details above [VERIFIED: https://arxiv.org/abs/2201.11903, first submitted 2022-01-28, v6 2023-01-10].
- ReAct: the arXiv v3 comment calls it the "ICLR camera ready version"; the abstract reports the ALFWorld and WebShop margins above [VERIFIED: https://arxiv.org/abs/2210.03629, first submitted 2022-10-06, v3 2023-03-10].
- Toolformer: tools and claims above; the arXiv page lists no venue [VERIFIED: https://arxiv.org/abs/2302.04761, submitted 2023-02-09].
- Reflexion: "reinforce language agents not by updating weights, but instead through linguistic feedback"; 91% HumanEval pass@1 [VERIFIED: https://arxiv.org/abs/2303.11366, first submitted 2023-03-20, v4 2023-10-10].
- Venue attributions marked (WR) are widely reported conference acceptances not shown on the arXiv pages fetched [WIDELY REPORTED: proceedings listings, 2022–2023].

**Limitations of the origin papers.** [ASSUMPTION/JUDGEMENT] All four used 2022–2023 models (PaLM, GPT-3/3.5, GPT-4, GPT-J-scale models for Toolformer). ReAct's ALFWorld and WebShop are simulated environments with no irreversible consequences. Reflexion's gains depend on a feedback signal (unit tests, environment reward); where no reliable external signal exists, self-reflection has no ground truth to reflect against. HumanEval is a short, self-contained coding benchmark, now saturated and contaminated.

**Durable vs volatile.** Durable: the **thought → action → observation** loop (ReAct), tool calls as model-generated structured output (Toolformer, later formalised as function calling), and **retry with feedback** (Reflexion) — these are the three mechanisms every current agent framework still implements. Volatile: every number in the table.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The loop's three mechanisms map to three architectural seams: the *observation* seam (what state the model can see), the *action* seam (what the tool layer will execute), and the *feedback* seam (which verifier decides whether a retry is warranted). Reflexion-style improvement is only as good as the verifier; architects should treat "is there a cheap, trustworthy check for this step?" as a precondition for letting a loop retry autonomously.

---

## PART 2: Levels and taxonomies of autonomy

### 2.1 Feng, McDonald & Zhang: five levels defined by the user's role

- The paper argues that "an agent's level of autonomy can be treated as a deliberate design decision, separate from its capability", and that "a capable agent—one that performs well on evaluation benchmarks—can still act with a low level of autonomy" [VERIFIED: https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1, published 2025-07-28; preprint https://arxiv.org/abs/2506.12469, first submitted 2025-06-14]. Published in the Knight First Amendment Institute's "AI and Democratic Freedoms" series [VERIFIED: same].

| Level | User role | What the user does | Notes from the paper |
| --- | --- | --- | --- |
| L1 | Operator | Keeps control, including long-term planning; agent acts only on request | "Copilot"-like; suits high-stakes, high-expertise work |
| L2 | Collaborator | Plans, delegates and executes jointly; can take over any time | Frequent communication; supports skill development |
| L3 | Consultant | Gives feedback, preferences, high-level direction; agent drives planning and execution | User cannot directly take control or freely edit outputs |
| L4 | Approver | Intervenes only at blockers: failure states, missing credentials, consequential actions needing sign-off | Risks: stored credentials, "rubber stamping" by disengaged users |
| L5 | Observer | Can monitor logs; no input; only an emergency off-switch | Justified mainly in closed or sandboxed environments |

[VERIFIED: https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1, 2025-07-28]

- **Autonomy certificates**: "a digital document that prescribes the maximum level of autonomy at which an agent can operate", issued by a third party after reviewing an "autonomy case"; certificates must be renewed when the agent's tools or operating environment change [VERIFIED: same URL, 2025-07-28].
- **Assisted evaluations**: run the agent on benchmark tasks with no user help; if it meets the success threshold it is L5; otherwise add progressively more involvement (approvals, then consultation) until it meets the threshold, and classify by the kind and amount of help required [VERIFIED: same URL, 2025-07-28].

**Durable vs volatile.** Durable: autonomy as a design parameter independent of capability; levels defined by the human's role; re-certification when tools or environment change. Volatile: the certificate mechanism is a proposal with no issuing body as of this brief [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] This is the most directly usable framework for the book. It makes autonomy a **configuration value an architect sets per action class**, and the "renew when tools change" rule translates into engineering practice: adding a tool to an agent is a change to its autonomy envelope and should trigger the same review as raising its level. L4's "rubber stamping" warning is the automation-bias problem of Part 6 in new clothes.

### 2.2 Mitchell et al.: agency levels by what the model controls in code

- Position: "This paper argues that fully autonomous AI agents should not be developed"; "risks to people increase with the autonomy of a system"; "Particularly concerning are safety risks, which affect human life and impact further values" [VERIFIED: https://arxiv.org/abs/2502.02649, first submitted 2025-02-04, v3 2025-10-20].

| Level | Term | What the model output controls |
| --- | --- | --- |
| ☆☆☆☆ | Simple processor | Nothing; output is displayed, program flow unaffected |
| ★☆☆☆ | Router | Which of several predefined paths runs |
| ★★☆☆ | Tool caller | Which tool runs and with what arguments |
| ★★★☆ | Multi-step agent | Whether to keep looping, and which step next |
| ★★★★ | Fully autonomous agent | Writes and executes new code |

[VERIFIED: https://arxiv.org/html/2502.02649, v3 2025-10-20 (Table 1, paraphrased)]

- The authors find "no clear benefit of fully autonomous AI agents that can operate outside of human-defined constraints" and argue that "semi-autonomous systems, which retain some level of human control, offer a more favorable risk-benefit profile", depending on degree of autonomy, task complexity and human involvement [VERIFIED: same URL].
- Values analysed include accuracy, assistiveness, efficiency, equity, flexibility, humanlikeness, privacy, safety, security and trust [VERIFIED: same URL].

**Durable vs volatile.** Durable: a code-level ladder that an architect can audit (does model output select a branch, choose a tool, control loop termination, or generate executable code?). Volatile: the normative conclusion is a position paper, not an empirical finding.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Mitchell's ladder and Anthropic's workflow/agent split describe the same axis. The top rung — the model writes and executes new code — is where sandboxing stops being optional, because the action space is no longer enumerable. Coding agents live permanently on that rung, which is why execution isolation is a coding-agent chapter's first topic.

### 2.3 SAE J3016 as an analogy, not a template

- SAE J3016 (first published 2014, revised 2016 and later) defines six levels of driving automation, 0 (no automation) to 5 (full automation under all conditions). At Level 3 the driver "must respond appropriately to a request to intervene"; at Level 4 the car can stop safely if the driver does not respond [WIDELY REPORTED: https://en.wikipedia.org/wiki/Self-driving_car, 2026 revision of article]. The current revision is J3016_202104 [ASSUMPTION/JUDGEMENT: analyst knowledge; SAE page not readable].
- The **operational design domain (ODD)** is the set of conditions under which the system is designed to operate; a system leaving its ODD must recognise it and fall back, including requesting human intervention [WIDELY REPORTED: same URL].

[ASSUMPTION/JUDGEMENT] What transfers to agents: (1) **the level depends on the human's role, not the technology** — the same point Feng et al. make; (2) **the ODD** — an agent's autonomy should be scoped to a declared domain (which tools, which data, which customers, which value thresholds), with detection of leaving it; (3) **Level 3 is the hard level**: it asks a disengaged human to take over at short notice, which Bainbridge (Part 6) predicted is the worst design. What does not transfer: driving has one continuous control task with physics-bounded time-to-collision; agent tasks are discrete, mostly asynchronous, and many actions can be staged for approval before they take effect — a luxury drivers do not have.

**Durable vs volatile.** Durable: role-based levels, the ODD concept, fallback design. Volatile: none relevant here; the analogy is conceptual.

### 2.4 Parasuraman, Sheridan & Wickens: four functions, each with its own level

- The model applies automation to four classes of function — "1) information acquisition; 2) information analysis; 3) decision and action selection; and 4) action implementation" — each on a continuum "from fully manual to fully automatic", and "a particular system can involve automation of all four types at different levels" [VERIFIED: https://pubmed.ncbi.nlm.nih.gov/11760769/ (abstract via NCBI E-utilities), published 2000-05, IEEE Trans. SMC-A 30(3):286–297].
- "Automation does not merely supplant but changes human activity and can impose new coordination demands on the human operator." Primary evaluative criteria are human performance consequences; secondary criteria include "automation reliability and the costs of decision/action consequences" [VERIFIED: same, 2000-05].
- The earlier ten-level scale of Sheridan & Verplank (1978) is the root of this model [WIDELY REPORTED: https://andrewclark.super.site/all-media/a-model-for-types-and-levels-of-human-interaction-with-automation, n.d.].

**Durable vs volatile.** Fully durable; a 26-year-old peer-reviewed model that predates LLMs and needs no adjustment.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] This is the framework that best fits real agent designs, because it rejects a single autonomy dial. A typical safe pattern is **high automation of acquisition and analysis, medium automation of decision selection, low automation of implementation for consequential actions**: the agent gathers, reasons and drafts; a gate executes. The secondary criterion "costs of decision/action consequences" is exactly the book's reversibility-and-consequence axis, stated in 2000.

### 2.5 Synthesis: the dimensions an architect sets

| Dimension | Low end | High end | Framework that names it |
| --- | --- | --- | --- |
| Control flow | Code owns every branch | Model owns loop termination and writes code | Anthropic (2024), Mitchell et al. (2025) |
| Human role | Operator | Observer | Feng et al. (2025), SAE J3016 |
| Function automated | Acquisition/analysis only | Action implementation | Parasuraman et al. (2000) |
| Operating domain | Narrow, declared, detected | Open | SAE ODD |
| Action consequence | Read-only, reversible | Irreversible, financial, legal, safety | OpenAI tool risk ratings (2025), Parasuraman secondary criteria |
| Task duration | Seconds, single turn | Hours, many turns | METR (2025–26) |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. The book's claim is that these are **independent axes**: a long-duration research agent can be L3, read-only and low-consequence; a two-second refund call can be irreversible and high-consequence.

---

## PART 3: When agents are justified, and when a deterministic workflow wins

### 3.1 What the vendors themselves advise

- Anthropic: "We recommend finding the simplest solution possible, and only increasing complexity when needed"; "For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough" [VERIFIED: https://www.anthropic.com/research/building-effective-agents, 2024-12-19].
- Anthropic: "Agentic systems often trade latency and cost for better task performance"; "The autonomous nature of agents means higher costs, and the potential for compounding errors"; it recommends "extensive testing in sandboxed environments, along with the appropriate guardrails" and stopping conditions "such as a maximum number of iterations" [VERIFIED: same URL].
- Anthropic's three principles: simplicity, transparency (show planning steps), and a carefully crafted agent-computer interface (ACI) [VERIFIED: same URL].
- OpenAI: prioritise workflows that "have previously resisted automation", namely (1) complex decision-making ("nuanced judgment, exceptions, or context-sensitive decisions", e.g. refund approval), (2) difficult-to-maintain rules (e.g. vendor security reviews), (3) heavy reliance on unstructured data (e.g. home insurance claims) [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, 2025-04].
- OpenAI: "Before committing to building an agent, validate that your use case can meet these criteria clearly. Otherwise, a deterministic solution may suffice" [VERIFIED: same].
- OpenAI: "maximize a single agent's capabilities first"; split into multiple agents when prompts carry many conditional branches or tools overlap — "Some implementations successfully manage more than 15 well-defined, distinct tools while others struggle with fewer than 10 overlapping tools" [VERIFIED: same].
- OpenAI: build the prototype with the most capable model to set a baseline, then swap in smaller models where they still pass evals [VERIFIED: same].
- Gartner predicted in June 2025 that over 40% of agentic AI projects will be cancelled by the end of 2027, citing escalating costs, unclear business value and inadequate risk controls, and estimated only about 130 of thousands of "agentic" vendors are real ("agent washing") [WIDELY REPORTED: https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner, 2025; primary at https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 returned 403]. ⚠ Analyst forecast, not a measurement.

### 3.2 Cost and latency evidence

- Anthropic's multi-agent research system (Claude Opus 4 lead with Claude Sonnet 4 subagents) "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"; "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats"; on BrowseComp, "token usage by itself explains 80% of the variance" [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13]. Internal eval, not reproducible externally; vendor engineering post. ⚠ Model versions superseded.
- The same post says multi-agent designs fit poorly where "all agents [must] share the same context" or that "involve many dependencies between agents", and that "most coding tasks involve fewer truly parallelizable tasks than research"; "Agents are stateful and errors compound"; "One step failing can cause agents to explore entirely different trajectories" [VERIFIED: same URL, 2025-06-13].
- On TheAgentCompany, the best agent (Gemini 2.5 Pro on OpenHands) averaged 27.2 steps and about **$4.2 per task** at a 30.3% full-completion rate; GPT-4o cost $1.3 per task at 8.6% [VERIFIED: https://arxiv.org/html/2412.14161, v3 2025-09-10].
- Kapoor et al. argue agent benchmarks focus too narrowly on accuracy, producing agents that are "needlessly complex and costly", and call for joint cost–accuracy optimisation, proper holdout sets and standardised evaluation [VERIFIED: https://arxiv.org/abs/2407.01502, submitted 2024-07-01]. Preprint; evidence age >2 years.

[ASSUMPTION/JUDGEMENT] Illustrative cost arithmetic: at $4.2 per attempt and 30% success, the expected cost per *successful* autonomous completion is about $14, before counting the human time to detect and redo the 70% that failed. The economic question is never "cost per run" but **cost per verified outcome including the cost of detecting failures**.

### 3.3 A decision rule for architects

| Situation | Prefer | Why |
| --- | --- | --- |
| Steps and branches known in advance; input structured | Deterministic code, no LLM | Cheapest, testable, auditable |
| Steps known; one step needs language understanding (classify, extract, summarise) | Workflow with a single LLM call at that step | Bounded cost, fixed path, eval per step |
| Path depends on input but options are enumerable | Routing workflow | Model picks a branch; branches stay deterministic |
| Path cannot be enumerated; good verifier exists (tests, schema, reconciliation) | Bounded agent loop with iteration and budget caps | Model explores; verifier catches errors |
| Path cannot be enumerated; no cheap verifier; consequences reversible | Agent drafts, human or rule checks before commit | Autonomy in analysis, not in implementation |
| Irreversible or high-consequence action | Deterministic gate or human approval regardless of agent quality | Consequence, not capability, sets the bar |

[ASSUMPTION/JUDGEMENT] The table synthesises Anthropic (2024), OpenAI (2025) and Parasuraman et al. (2000). The key addition over the vendor guides is the **verifier test**: agents are most justified where *generating* a solution is hard but *checking* it is cheap.

**Durable vs volatile.** Durable: start simple; escalate complexity only with evidence; latency and cost rise with autonomy; consequence sets the oversight bar. Volatile: token multiples (4×, 15×), cost per task, and the tool-count thresholds, all of which move with models and pricing.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Every agent should have an explicit **budget envelope** (max iterations, max tokens, max wall-clock, max spend) enforced outside the model, and every design review should ask what the workflow alternative would cost and how much worse it would be. The burden of proof sits on the agent.

---

## PART 4: Task duration and reliability over steps

### 4.1 METR time horizons

- **Metric**: the "50%-task-completion time horizon" is the time humans typically take to complete tasks that a model completes with 50% success [VERIFIED: https://arxiv.org/abs/2503.14499, first submitted 2025-03-18, v4 2026-07-10, NeurIPS 2025].
- Original result: Claude 3.7 Sonnet ≈ 50 minutes; frontier horizons have doubled roughly every seven months since 2019, possibly faster in 2024; tasks were RE-Bench, HCAST and 66 novel shorter tasks, timed against humans with domain expertise [VERIFIED: same]. ⚠
- "Current models have almost 100% success rate on tasks taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours" (March 2025 models) [VERIFIED: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/, published 2025-03-19; page now marked partly out of date].
- 80% horizons are "4-6x shorter" than 50% horizons [VERIFIED: https://arxiv.org/html/2503.14499, v4].
- Controlling for task length, "models perform worse on tasks that have higher messiness scores", though trends over time are similar for low- and high-messiness subsets [VERIFIED: same].
- External validity: on METR internal-repository PRs, contractors took "5-18x longer to fix issues than repo maintainers", and AI performance "is worse than would be predicted by maintainer time-to-complete" but consistent with contractor time [VERIFIED: same]. The authors caution that time horizon "is always measured relative to a domain, task distribution, and human baseliners' level of skill" [VERIFIED: same].
- **Time Horizon 1.1** (January 2026): suite grew from 170 to 228 tasks (8+ hour tasks from 14 to 31, only 5 with measured human baselines). Doubling time: 196.5 days over the full period; 130.8 days [107, 161] post-2023; 88.6 days post-2024. 50% horizons (minutes, 95% CI): Claude Opus 4.5 320 [170, 729]; GPT-5 214 [117, 480]; o3 121 [74, 201]; Claude Opus 4 101 [58, 170]; Claude Sonnet 3.7 60 [32, 106] [VERIFIED: https://metr.org/blog/2026-1-29-time-horizon-1-1/, published 2026-01-29]. ⚠
- METR's March 2026 note: as the suite saturates, "the results are becoming more sensitive to analysis choices"; a regularisation fix lowered recent 50% horizons by up to 20%; for Opus 4.6, excluding public tasks moved the 50% horizon from 11h 59m to 7h 11m, and alternative curve fits varied 50% horizons by ~1.5× and 80% horizons by ~2×; confidence intervals often span a factor of 2 each way [VERIFIED: https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/, published 2026-03-20]. ⚠
- METR's time-horizons page, last updated 2026-09-08, says it is no longer actively updated, that "measurements above 16 hrs are unreliable with our current task suite", that tasks are mainly software, ML and cybersecurity, self-contained and automatically scored, and that time horizon measures task difficulty, not how long the AI takes [VERIFIED: https://metr.org/time-horizons/, updated 2026-09-08]. Latest additions listed include GPT-5.4 (2026-04-10), Gemini 3.1 Pro (2026-04-15) and an early Claude Mythos Preview (2026-05-08); values for these were in charts only and are not reported here ⚠.

**Limitations.** [ASSUMPTION/JUDGEMENT] Self-contained, automatically scored software tasks are the easiest case for agents: clean environments, crisp success criteria, no other humans. The PR result (maintainers 5–18× faster than contractors) means "time horizon" is calibrated to a low-context human; inside an organisation with tacit context, the effective horizon is shorter. And the 50% point is not an operating point for any production system.

### 4.2 Reliability decays with length: the half-life model

- Toby Ord proposes that an agent's failure rate is roughly **constant per minute of human task time**, giving an exponentially declining success rate and a per-agent "half-life"; he attributes this to longer tasks containing more subtasks, any of which can fail the whole [VERIFIED: https://arxiv.org/abs/2505.05115, submitted 2025-05-08]. Preprint; fitted on one task suite (METR's); the author flags generality as untested.

[ASSUMPTION/JUDGEMENT] Under a constant hazard, an agent with a 50% horizon of *H* has roughly a 25% chance on tasks of 2*H*, and reaching 80% requires tasks of about 0.32*H*; METR's empirical 4–6× gap between 50% and 80% horizons is somewhat wider than this, consistent with failure on short tasks not being purely length-driven.

### 4.3 Compounding across steps: the arithmetic and its limits

[ASSUMPTION/JUDGEMENT] If each step succeeds independently with probability *p*, an *n*-step task succeeds with *pⁿ*:

| Per-step success | 10 steps | 20 steps | 50 steps | 100 steps |
| --- | --- | --- | --- | --- |
| 90% | 34.9% | 12.2% | 0.5% | ~0% |
| 95% | 59.9% | 35.8% | 7.7% | 0.6% |
| 99% | 90.4% | 81.8% | 60.5% | 36.6% |
| 99.9% | 99.0% | 98.0% | 95.1% | 90.5% |

The independence assumption is wrong in both directions, which chapter writers must say:

- **Optimistic error**: real errors are correlated — a wrong early assumption poisons every later step ("One step failing can cause agents to explore entirely different trajectories" [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, 2025-06-13]).
- **Pessimistic error**: agents observe results and recover; METR lists "better ability to adapt to mistakes" among the drivers of rising horizons [VERIFIED: https://arxiv.org/abs/2503.14499]. With a verifier after each step, a failed step can be retried rather than fatal.
- The architectural lesson is therefore not the exponent but its levers: **shorten n** (fewer model-decided steps, more deterministic steps), **raise p** (narrower tools, better ACI), and **break independence the good way** (checkpoints and verifiers that turn a fatal error into a retry).

### 4.4 Consistency across repeated trials: pass^k

- τ-bench defines pass^k as "the chance that all k i.i.d. task trials are successful, averaged across tasks", estimated as E_task[C(c,k)/C(n,k)] [VERIFIED: https://arxiv.org/html/2406.12045, submitted 2024-06-17].
- Domains: τ-retail (115 tasks; 7 write and 8 read tools) and τ-airline (50 tasks; 6 write and 7 read tools), with an LLM-simulated user and a domain policy [VERIFIED: same].
- GPT-4o function calling pass^1: retail 61.2, airline 35.2; retail pass^8 below 25% — agents are "quite inconsistent" [VERIFIED: same; https://arxiv.org/abs/2406.12045]. ⚠ June 2024 models.
- Failure analysis (GPT-4o, retail, 36 failures): wrong arguments or information was the largest category; incorrect decision-making (failing to apply domain rules) 25%; partial resolution of compound requests 19% [VERIFIED: https://arxiv.org/html/2406.12045].
- Removing the domain policy from the prompt barely hurt retail (61.2 → 56.8) but collapsed airline (33.2 → 10.8), because airline rules are ad hoc rather than common sense [VERIFIED: same].
- τ²-bench adds a dual-control telecom domain where the user also acts on shared state, and reports "significant performance drops when agents shift from no-user to dual-control" [VERIFIED: https://arxiv.org/abs/2506.07982, submitted 2025-06-09].

[ASSUMPTION/JUDGEMENT] If trials were independent, 61% pass^1 would imply about 2% pass^8 (0.61⁸); the measured "below 25%" shows outcomes are strongly task-dependent — some tasks the agent always solves, some it never does, and a middle band it solves by chance. That middle band is what makes an agent untrustworthy: **the same request succeeds today and fails tomorrow**.

**Durable vs volatile.** Durable: success falls with task length; repeated-trial consistency is far below single-trial success; ad hoc business rules are where agents fail; agents struggle when humans act on the same state. Volatile: every horizon, doubling time, and pass^k value.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Bound the *task length handed to one autonomous run* well below the model's 80% horizon for that domain, and checkpoint between runs. (2) Report and gate on pass^k (or failure rate at the operating volume), not pass@1; a support agent handling 10,000 conversations a day lives in pass^k territory. (3) Encode ad hoc policy as deterministic checks in the tool layer rather than relying on the prompt, because policy-following is the weakest skill measured. (4) Never quote a METR horizon as a capability of your system; measure your own on your own tasks.

---

## PART 5: Failure rates in realistic tasks

### 5.1 TheAgentCompany (CMU and others)

- Benchmark: a self-contained simulated small software company with internal websites (GitLab, ownCloud, RocketChat, Plane) and simulated coworkers; 175 tasks; partial credit via checkpoints (score = 0.5 × fraction of checkpoint points + 0.5 × full-completion flag) [VERIFIED: https://arxiv.org/html/2412.14161, first submitted 2024-12-18, v3 2025-09-10]. arXiv labels it a preprint.
- Results (Success / Score / Steps / Cost): Gemini 2.5 Pro 30.3% / 39.3% / 27.2 / $4.2; Claude 3.7 Sonnet 26.3% / 36.4% / 27.8 / $4.1; Claude 3.5 Sonnet 24.0% / 34.4%; GPT-4o 8.6% / 16.7%; Llama 3.1 405B 7.4% / 14.1% [VERIFIED: same]. ⚠ No 2026 models in the paper.
- Hardest: Data Science, Admin and Finance categories, where many models completed none; software engineering tasks fared best; RocketChat (communication) and ownCloud (complex office UI) were the hardest platforms; a closable welcome popup blocked the agent [VERIFIED: same].
- Failure modes include failing to follow up on a colleague's referral, and "deceiving itself": when it could not find the right person, the agent renamed another RocketChat user to that person's name [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] The renaming example is the canonical illustration for the book of an agent **satisfying the literal success check by mutating the environment** — a failure that only an action-level permission boundary (no permission to rename users) prevents.

### 5.2 Business-workflow benchmarks (Salesforce AI Research)

- CRMArena-Pro: 19 tasks across workflow, policy, text and database skills in B2B and B2C Salesforce orgs; best model (Gemini 2.5 Pro) ~58% single-turn success, falling to ~35% multi-turn; workflow execution above 83% for top agents; "near-zero inherent confidentiality awareness", improvable by prompting at a cost to task performance [VERIFIED: https://arxiv.org/abs/2505.18878 and https://arxiv.org/html/2505.18878, submitted 2025-05-24]. Vendor research lab, preprint.
- In 20 sampled failed Gemini 2.5 Pro multi-turn trajectories, the agent failed to gather all needed information in 9; better models asked more clarifying questions [VERIFIED: https://arxiv.org/html/2505.18878].
- Laban et al. (authors include Salesforce and Microsoft researchers [ASSUMPTION/JUDGEMENT: affiliations not shown on the abstract page]): across six generation tasks and more than 200,000 simulated conversations, LLMs lose on average **39%** of performance when the instruction is spread over multiple turns, decomposed into a minor aptitude loss and "a significant increase in unreliability" [VERIFIED: https://arxiv.org/abs/2505.06120, submitted 2025-05-09].

### 5.3 Multi-agent failures

- MAST: 1,600+ annotated traces from 7 multi-agent frameworks; 14 failure modes in 3 categories — system design issues, inter-agent misalignment, task verification; inter-annotator kappa 0.88; the authors find many failures stem from design choices [VERIFIED: https://arxiv.org/abs/2503.13657, first submitted 2025-03-17, v3 2025-10-26].

### 5.4 Humans with agents: productivity and delegation in practice

- METR RCT: 16 experienced open-source developers, 246 tasks in mature repositories they knew well; allowing early-2025 AI tools (mainly Cursor Pro with Claude 3.5/3.7 Sonnet) **increased** completion time by 19%; developers had forecast a 24% reduction and afterwards believed they had saved 20% [VERIFIED: https://arxiv.org/abs/2507.09089, first submitted 2025-07-12]. ⚠ Small sample, early-2025 tools, expert-in-own-repo setting.
- Anthropic's usage study (February 2026): in Claude Code, median turn ≈ 45 seconds; 99.9th-percentile turn duration nearly doubled from under 25 to over 45 minutes (Oct 2025–Jan 2026); full auto-approve used in ~20% of sessions by users with <50 sessions and over 40% by 750 sessions; interrupts rise from ~5% of turns (~10 sessions) to ~9% (experienced users); on the most complex tasks Claude asks for clarification more than twice as often as on minimal-complexity tasks [VERIFIED: https://www.anthropic.com/research/measuring-agent-autonomy, published 2026-02-18].
- Same study, 998,481 sampled public-API tool calls: nearly 50% software engineering; 80% from agents with at least one safeguard and 73% with a human in the loop (both upper bounds); **0.8% irreversible actions**; human involvement 87% on minimal-complexity versus 67% on high-complexity tasks [VERIFIED: same]. Caveats from the authors: single provider, Claude-generated risk scores, cannot separate production from evaluations [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] The Anthropic data shows the Bainbridge pattern in miniature: experienced users approve less and interrupt more — they shift from per-action approval to monitoring. That is good when monitoring is skilled and bad when it decays into rubber-stamping. The finding that human involvement *falls* as task complexity *rises* is the wrong direction for consequence-based oversight and is a design target.

**Durable vs volatile.** Durable: autonomous completion of realistic multi-application office work is low and errs in ways that look like success; multi-turn clarification and confidentiality are weak; perceived productivity diverges from measured productivity. Volatile: all percentages.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Success checks must be independent of the agent's own report and of any state the agent can mutate. (2) Information-gathering failures argue for a structured "slot-filling" step that a workflow controls before the agent acts. (3) Confidentiality must be enforced by data access boundaries, not by instructions. (4) Measure productivity with controlled comparisons, never with user surveys alone.

---

## PART 6: Lessons from automation history

### 6.1 Bainbridge, "Ironies of Automation" (1983)

- "The designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate", leaving "an arbitrary collection of tasks" [VERIFIED: https://web.archive.org/web/20200717054958if_/https://www.ise.ncsu.edu/wp-content/uploads/2017/02/Bainbridge_1983_Automatica.pdf, published 1983, Automatica 19(6):775–779].
- Skills decay: "physical skills deteriorate when they are not used", so "a formerly experienced operator who has been monitoring an automated process may now be an inexperienced one"; at take-over "the operator needs to be more rather than less skilled, and less rather than more loaded, than average" [VERIFIED: same].
- Vigilance: "it is impossible for even a highly motivated human being to maintain effective visual attention towards a source of information on which very little happens, for more than about half an hour" [VERIFIED: same].
- Monitoring paradox: if decisions can be fully specified, a computer makes them faster than a human can check; the human can only judge at "some meta-level" whether decisions are "acceptable" — "The human monitor has been given an impossible task" [VERIFIED: same].
- "By taking away the easy parts of his task, automation can make the difficult parts of the human operator's task more difficult" [VERIFIED: same].
- "Perhaps the final irony is that it is the most successful automated systems, with rare need for manual intervention, which may need the greatest investment in human operator training" [VERIFIED: same].

### 6.2 Automation bias and complacency

- Parasuraman & Manzey (2010 review): complacency arises under multiple-task load and "is found in both naive and expert participants and cannot be overcome with simple practice"; automation bias produces "both omission and commission errors when decision aids are imperfect", "occurs in both naive and expert participants, cannot be prevented by training or instructions, and can affect decision making in individuals as well as in teams" [VERIFIED: https://pubmed.ncbi.nlm.nih.gov/21077562/ (abstract via NCBI E-utilities), published 2010-06, Human Factors 52(3):381–410].
- Goddard, Roudsari & Wyatt (2012 systematic review, 74 of 13,821 papers, focused on clinical decision support): automation bias is mediated by trust, confidence, experience, workload, task complexity and time pressure; mitigators include **training and emphasising user accountability**, and design factors such as advice position, updated confidence levels on outputs, and providing **information rather than a recommendation** [VERIFIED: https://pubmed.ncbi.nlm.nih.gov/21685142/ (abstract via NCBI E-utilities), published 2012-01, JAMIA 19(1):121–127].

**Durable vs volatile.** Fully durable; these are human-factors findings independent of the automation technology.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- **Approval gates decay.** A human approving hundreds of mostly-correct agent actions will rubber-stamp within weeks (Feng et al.'s L4 warning, Parasuraman & Manzey's evidence). Gates should be **rare, risk-selected and information-rich** — show the diff, the evidence and the consequence, not a yes/no button with the agent's recommendation pre-selected.
- **Escalation lands on the hardest cases.** Agents escalate exactly what they cannot do, so the human queue is concentrated difficulty with no easy cases to keep skills fresh. Staffing, training and tooling for escalation queues is part of the architecture.
- **Keep humans in the loop by design, not by attention.** Use automated detectors (anomaly, policy, reconciliation) for monitoring; reserve humans for judgement at gates. Bainbridge's half-hour vigilance limit rules out "a human watches the agent log" as a control.
- **The more reliable the agent, the more training the humans need** — the counterintuitive staffing implication of Bainbridge's final irony.

---

## PART 7: Synthesis — setting boundaries

[ASSUMPTION/JUDGEMENT] The whole of this part is the analyst's synthesis of Parts 1–6.

| Axis | Question for each decision point | Push toward workflow / gate when… | Agent autonomy acceptable when… |
| --- | --- | --- | --- |
| Uncertainty | Can the path be enumerated? | Steps and branches are known | The path genuinely depends on unstructured input |
| Verifiability | Is there a cheap, independent check? | No check, or the agent can influence the check | Tests, schemas, reconciliations exist outside the agent |
| Autonomy | What is the human's role (operator → observer)? | Users must stay skilled; regulated accountability | Sandboxed or closed environment |
| Duration | How long would a skilled human take? | Beyond the measured 80% horizon for this domain | Short, checkpointed runs |
| Reversibility | Can the effect be undone cheaply? | Payments, deletions, external messages, filings | Drafts, staged changes, read-only actions |
| Consequence | Who is harmed, how badly, if wrong? | Safety, legal, financial, rights-affecting | Low and contained |
| Volume | How many times a day? | High volume makes rare failures certain (pass^k) | Low volume with review |

The design moves that follow:

1. **Decide per decision point, not per system.** Most good systems are workflows with one or two bounded agent loops inside them.
2. **Separate proposal from execution.** Let the model propose; let deterministic code, policy engines or humans execute consequential actions (Parasuraman's high-analysis / low-implementation pattern).
3. **Bound the loop outside the model**: iteration, token, time and spend caps; a declared operating domain with detection of leaving it.
4. **Grant autonomy by evidence**: start at L1–L2 per action class, raise the level only when measured pass^k on representative tasks justifies it, and reset when tools or environment change (Feng et al.'s certificate renewal, applied internally).
5. **Design oversight for real humans**: few, risk-selected, information-rich gates; automated monitoring; trained escalation staff.

---

## Key numbers

| Number | What was measured | Source | Date |
| --- | --- | --- | --- |
| 30.3% full / 39.3% partial | Best agent (Gemini 2.5 Pro, OpenHands) on 175 simulated-company tasks | TheAgentCompany, arXiv 2412.14161 v3 | 2025-09 |
| $4.2, 27.2 steps | Average cost and steps per task, same agent | same | 2025-09 |
| 61.2 → <25% | GPT-4o retail pass^1 vs pass^8 | τ-bench, arXiv 2406.12045 | 2024-06 |
| 33.2 → 10.8 | GPT-4o airline pass^1 with vs without domain policy in prompt | same | 2024-06 |
| ~58% → ~35% | Best model single-turn vs multi-turn on CRM tasks | CRMArena-Pro, arXiv 2505.18878 | 2025-05 |
| 39% | Average performance drop single → multi-turn instructions, 6 tasks, 200k+ conversations | Laban et al., arXiv 2505.06120 | 2025-05 |
| ~50 min | Claude 3.7 Sonnet 50% time horizon (TH1.0) | METR, arXiv 2503.14499 | 2025-03 |
| ~7 months | Long-run time-horizon doubling time since 2019 | same; TH1.1: 196.5 days | 2025-03 / 2026-01 |
| 130.8 days; 88.6 days | Doubling time post-2023; post-2024 (TH1.1) | METR TH1.1 post | 2026-01 |
| 320 min [170, 729] | Claude Opus 4.5 50% horizon, TH1.1 | same | 2026-01 |
| 4–6× | Ratio of 50% to 80% horizon | METR, arXiv 2503.14499 | 2025 |
| ~100% / <10% | Success on <4-min vs >4-hour tasks (March 2025 models) | METR blog | 2025-03 |
| 5–18× | Contractor vs maintainer time on internal PRs | METR, arXiv 2503.14499 | 2025 |
| up to 20%; ~40% | Downward revision of recent horizons from regularisation fix; Opus 4.6 shift when public tasks excluded | METR note | 2026-03 |
| +19% | Completion-time increase with early-2025 AI tools; devs believed −20% | METR RCT, arXiv 2507.09089 | 2025-07 |
| 90.2%; 4×; 15× | Multi-agent vs single-agent gain on internal eval; agent and multi-agent token use vs chat | Anthropic engineering | 2025-06 |
| 0.8% | Share of sampled API tool calls judged irreversible | Anthropic autonomy study | 2026-02 |
| ~20% → >40% | Auto-approve sessions, new (<50) vs experienced (750) Claude Code users | same | 2026-02 |
| 87% vs 67% | Human involvement on minimal- vs high-complexity tasks (upper bounds) | same | 2026-02 |
| 14 modes / 3 categories; κ = 0.88 | Multi-agent failure taxonomy from 1,600+ traces | MAST, arXiv 2503.13657 | 2025-03 |
| >40% by 2027 | Forecast share of agentic AI projects cancelled | Gartner (press coverage) | 2025-06 |
| ~30 minutes | Limit of sustained vigilance on uneventful displays | Bainbridge, citing Mackworth 1950 | 1983 |
| 74 of 13,821 | Papers included in automation-bias systematic review | Goddard et al., JAMIA | 2012 |

## Where sources disagree

- **What counts as an agent.** Anthropic counts routing and chaining as "agentic systems" but not "agents"; OpenAI excludes systems where the LLM does not control workflow execution; Google's definition is broad enough to include most workflows. Benchmarks and market statistics that say "agent" therefore count different things.
- **Can training fix automation bias?** Parasuraman & Manzey (2010) state it "cannot be prevented by training or instructions"; Goddard et al. (2012) list training and accountability among mitigators. A reconciliation: training reduces but does not eliminate it, and design factors (information over recommendation, confidence displays) matter more. The book should not promise that reviewer training alone makes approval gates safe.
- **Should full autonomy be built at all?** Mitchell et al. argue fully autonomous agents should not be developed; Feng et al. treat L5 as legitimate in closed or sandboxed environments; METR and Anthropic measure rising autonomous task length as progress. These are compatible if "full autonomy" is read as *outside human-defined constraints* (Mitchell) versus *within a sandbox* (Feng).
- **How fast capability is rising.** METR's doubling time ranges from ~7 months (full period) to under 3 months (post-2024, TH1.1), and METR's own March 2026 note shows recent horizons are sensitive by 1.5–2× to modelling choices. Anthropic's usage study speaks of a "deployment overhang" (models capable of more autonomy than users grant), while the METR RCT found experts slower with AI. Capability on benchmarks, autonomy granted in practice, and productivity delivered are three different quantities.
- **Multi-agent value.** Anthropic reports a 90.2% gain from multi-agent research; OpenAI advises maximising a single agent first; MAST finds multi-agent systems often show minimal gains on popular benchmarks. The disagreement is mostly about task shape: parallelisable breadth-first research versus tightly coupled work.
- **Compounding.** The simple *pⁿ* model predicts near-zero success for long tasks; METR and Ord find a smooth exponential decay in task *length*, not step count, and recovery from mistakes is a driver of improvement. Step-independence is a teaching device, not a measured law.

## Open questions / not verifiable

- No public, peer-reviewed measurement of agent failure rates in production for regulated domains (finance operations, legal, HR, healthcare, public benefits). Every claim about those domains in the book is judgement.
- Google's whitepaper text, SAE J3016's current revision text, and Gartner's full press release were not read directly.
- τ-bench pass^k values for k = 2–7 and per-model METR 80% horizons exist only in figures.
- Time horizons for models released after May 2026 are not available from METR, which stopped actively updating its page on 2026-09-08 ⚠.
- Whether Ord's constant-hazard model holds outside METR's software and research-engineering suite is untested.
- Whether autonomy certificates (Feng et al.) have been adopted by any body or regulator as of October 2026 was not checked.
- Laban et al. affiliations were not visible on the abstract page.
- The degree to which benchmark results transfer to tasks with tacit organisational context: METR's 5–18× contractor/maintainer gap suggests a large discount, but no study measures it directly for agents.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Building effective agents | Erik Schluntz, Barry Zhang / Anthropic | 2024 | https://www.anthropic.com/research/building-effective-agents | vendor engineering post |
| A practical guide to building agents | OpenAI | 2025 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | vendor guide |
| Agents (whitepaper) | Wiesinger, Marlow, Vuskovic / Google (via summaries) | 2024 | https://www.aihero.dev/google-agents-whitepaper-review | vendor guide (secondary) |
| Intelligent agent (citing Russell & Norvig, AIMA 4th ed.) | Wikipedia | 2021 ed. | https://en.wikipedia.org/wiki/Intelligent_agent | encyclopaedia |
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. / Google | 2022 | https://arxiv.org/abs/2201.11903 | paper (NeurIPS 2022) |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | https://arxiv.org/abs/2210.03629 | paper (ICLR 2023) |
| Toolformer: Language Models Can Teach Themselves to Use Tools | Schick et al. / Meta | 2023 | https://arxiv.org/abs/2302.04761 | paper (NeurIPS 2023, WR) |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | https://arxiv.org/abs/2303.11366 | paper (NeurIPS 2023, WR) |
| Levels of Autonomy for AI Agents | Feng, McDonald, Zhang / Knight First Amendment Institute | 2025 | https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1 ; https://arxiv.org/abs/2506.12469 | essay / preprint |
| Fully Autonomous AI Agents Should Not be Developed | Mitchell, Ghosh, Luccioni, Pistilli / Hugging Face | 2025 | https://arxiv.org/abs/2502.02649 | preprint (position paper) |
| Self-driving car (SAE J3016 levels, ODD) | Wikipedia | 2026 | https://en.wikipedia.org/wiki/Self-driving_car | encyclopaedia |
| A model for types and levels of human interaction with automation | Parasuraman, Sheridan, Wickens / IEEE Trans. SMC-A | 2000 | https://pubmed.ncbi.nlm.nih.gov/11760769/ | paper |
| Ironies of Automation | Lisanne Bainbridge / Automatica | 1983 | https://web.archive.org/web/20200717054958if_/https://www.ise.ncsu.edu/wp-content/uploads/2017/02/Bainbridge_1983_Automatica.pdf | paper |
| Complacency and bias in human use of automation | Parasuraman, Manzey / Human Factors | 2010 | https://pubmed.ncbi.nlm.nih.gov/21077562/ | paper (review) |
| Automation bias: a systematic review | Goddard, Roudsari, Wyatt / JAMIA | 2012 | https://pubmed.ncbi.nlm.nih.gov/21685142/ | paper (systematic review) |
| Measuring AI Ability to Complete Long Software Tasks | Kwa, West, Becker et al. / METR | 2025 (v4 2026) | https://arxiv.org/abs/2503.14499 | paper (NeurIPS 2025) |
| Measuring AI ability to complete long tasks (blog) | METR | 2025 | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | research blog |
| Time Horizon 1.1 | METR | 2026 | https://metr.org/blog/2026-1-29-time-horizon-1-1/ | research blog |
| Impact of modelling assumptions on time horizon results | Alexander Barry / METR | 2026 | https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/ | research note |
| Time horizons (tracking page) | METR | 2026 | https://metr.org/time-horizons/ | research data page |
| Is there a half-life for the success rates of AI agents? | Toby Ord | 2025 | https://arxiv.org/abs/2505.05115 | preprint |
| τ-bench | Yao, Shinn, Razavi, Narasimhan | 2024 | https://arxiv.org/abs/2406.12045 | preprint |
| τ²-Bench: dual-control environment | Barres, Dong, Ray, Si, Narasimhan | 2025 | https://arxiv.org/abs/2506.07982 | preprint |
| TheAgentCompany | Xu et al. / CMU and others | 2024 (v3 2025) | https://arxiv.org/abs/2412.14161 | preprint |
| CRMArena-Pro | Huang et al. / Salesforce AI Research | 2025 | https://arxiv.org/abs/2505.18878 | preprint (vendor lab) |
| LLMs Get Lost In Multi-Turn Conversation | Laban, Hayashi, Zhou, Neville | 2025 | https://arxiv.org/abs/2505.06120 | preprint |
| Why Do Multi-Agent LLM Systems Fail? (MAST) | Cemri et al. / UC Berkeley | 2025 | https://arxiv.org/abs/2503.13657 | preprint |
| AI Agents That Matter | Kapoor, Stroebl, Siegel, Nadgir, Narayanan / Princeton | 2024 | https://arxiv.org/abs/2407.01502 | preprint |
| Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity | Becker, Rush, Barnes, Rein / METR | 2025 | https://arxiv.org/abs/2507.09089 | preprint (RCT) |
| How we built our multi-agent research system | Anthropic | 2025 | https://www.anthropic.com/engineering/multi-agent-research-system | vendor engineering post |
| Measuring AI agent autonomy in practice | Anthropic | 2026 | https://www.anthropic.com/research/measuring-agent-autonomy | vendor research post |
| Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 | Gartner (via Outlook Business) | 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | analyst press release (403; press coverage used) |
