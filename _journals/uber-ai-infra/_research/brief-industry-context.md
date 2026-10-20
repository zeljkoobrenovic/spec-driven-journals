# Brief: Wider Industry and Research Context

Research brief for the "Uber's AI infra" journal. It lists external references a reader can follow to go deeper on each journal topic. **Every URL below was fetched and checked on 20 Oct 2026.** Each summary paraphrases what the page itself says. Where a page could not be fetched, the item is in "Not verified" at the end and must not be cited until someone checks it.

Each record's "To Probe Further" section can draw on the entries for its topic. Some entries serve several topics, so they are cross-referenced.

---

## 1. Harness- and model-agnostic AI gateways

**LiteLLM (Technology Radar blip)** — Thoughtworks Technology Radar, Languages & Frameworks, ring **Trial** (Assess Apr 2024; Trial Oct 2024, Nov 2025, Apr 2026 / Vol. 34).
https://www.thoughtworks.com/en-us/radar/languages-and-frameworks/litellm
The blip traces LiteLLM's growth from a "thin abstraction layer" into a full AI gateway. The April 2026 update calls it a "sensible default" for request tracing, access control and guardrails. It also warns that provider-specific features can bring coupling back, and that `drop_params` can silently drop parameters. *Supports:* an independent, opinionated view that a gateway is now standard architecture, together with the abstraction's limits.

**LiteLLM AI Gateway (docs)** — LiteLLM / BerriAI, product documentation (undated, current).
https://docs.litellm.ai/docs/simple_proxy
This is a self-hosted proxy that exposes one "OpenAI-compatible endpoint for 100+ LLM providers". It issues virtual keys, each with its own allowed models, budgets and rate limits, and it records the cost of every request. Load balancing, retries and fallbacks move traffic away from a failing provider. *Supports:* a concrete reference for the gateway's functions (routing, keys, per-request cost attribution). Also topic 11.

**Cloudflare AI Gateway (docs)** — Cloudflare Developers (undated, current).
https://developers.cloudflare.com/ai-gateway/
The page presents a managed gateway for monitoring and governing AI applications. Its features are analytics, logging, caching, rate limiting, and retry and fallback routing across providers such as OpenAI, Anthropic, Gemini and Workers AI. *Supports:* the managed-service form of the same pattern; useful when a record contrasts building a gateway with buying one.

**Kong AI Gateway (docs)** — Kong Developer docs (undated, current).
https://developer.konghq.com/ai-gateway/
Kong's gateway offers multiple LLM providers behind one API. It can publish existing APIs as MCP tools that agents can discover. It manages token budgets through AI rate limiting, and it calculates the cost of each request and enforces spend limits. *Supports:* the convergence of the LLM gateway and the MCP gateway into one control point, plus token governance (topics 2 and 11).

## 2. MCP, the MCP gateway, and MCP-vs-CLI token efficiency

**Model Context Protocol Specification (version 2025-11-25)** — modelcontextprotocol.io.
https://modelcontextprotocol.io/specification/2025-11-25
This is the authoritative protocol definition. It uses JSON-RPC 2.0 messages between hosts, clients and servers. Servers offer resources, prompts and tools; clients can offer sampling, roots and elicitation. The trust-and-safety section says tools are arbitrary code execution, says tool descriptions should be treated as untrusted unless they come from a trusted server, and requires user consent. *Supports:* the baseline vocabulary for the MCP gateway record.

**Security Best Practices (MCP spec, 2025-11-25)** — modelcontextprotocol.io.
https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices
The guide covers named attacks with mitigations: confused deputy through MCP proxy servers, token passthrough (explicitly forbidden), SSRF during OAuth discovery, session hijacking, local MCP server compromise, OAuth URL validation, stdio-proxy escalation, and scope minimisation. *Supports:* why an organisation centralises MCP behind a gateway that does per-client consent, validates token audience, controls egress and grants least-privilege scopes.

**Code execution with MCP: Building more efficient agents** — Adam Jones and Conor Kelly, Anthropic Engineering, 4 Nov 2025.
https://www.anthropic.com/engineering/code-execution-with-mcp
The post argues that two things waste tokens and time: loading every MCP tool definition up front, and routing every intermediate result through the model. Presenting MCP servers as code APIs lets the agent load only the tools it needs and filter data before it reaches the model. In the post's Google Drive to Salesforce example, usage drops from 150,000 to 2,000 tokens (98.7%). *Supports:* the token-efficiency case for CLI- or code-style tool access over raw MCP tool lists.

**MCP by default (Technology Radar blip)** — Thoughtworks, Techniques, ring **Caution**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/mcp-by-default
Thoughtworks advises against making MCP the default integration layer. Each protocol layer can lose fidelity (an "abstraction tax"), and the loss compounds on complex APIs. A well-designed CLI with clear help text, JSON output and predictable errors often serves agents better. Teams should choose MCP only where its governance and interoperability benefits justify the extra complexity. The blip argues from fidelity and overhead, not token counts. *Supports:* the counterweight in the MCP-vs-CLI discussion.

## 3. Skills monorepo, shared instructions, and AGENTS.md

**Equipping agents for the real world with Agent Skills** — Barry Zhang, Keith Lazuka and Mahesh Murag, Anthropic Engineering, 16 Oct 2025.
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
The post introduces skills: folders with a `SKILL.md` that agents load through progressive disclosure. At startup the agent sees only each skill's name and description; it loads the full file, and any linked files, only when a task needs them. A skill can therefore hold far more detail without filling the context window. *Supports:* the design rationale for a shared skills monorepo.

**Agent Skills Overview (open standard)** — agentskills.io (originally developed by Anthropic, released as an open standard).
https://agentskills.io/
The site defines the format (`SKILL.md` with `name` and `description`, plus optional `scripts/`, `references/`, `assets/`) and the three loading stages: discovery, activation, execution. Its client showcase lists many agents that support it, including Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, VS Code, Goose and OpenHands. *Supports:* the claim that skills are portable across harnesses, which matters for a harness-agnostic platform.

**AGENTS.md** — agents.md, stewarded by the Agentic AI Foundation (Linux Foundation).
https://agents.md/
The site describes AGENTS.md as "a simple, open format for guiding coding agents", a README for agents, and says "over 60k open-source projects" use it. *Supports:* the per-repository instruction layer that sits under a central skills repository.

**Curated shared instructions for software teams (Technology Radar blip)** — Thoughtworks, Techniques, ring **Adopt**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/curated-shared-instructions-for-software-teams
The blip calls it an emerging anti-pattern for each developer to write prompts from scratch. Teams should maintain curated AI guidance as a shared engineering resource and place files such as CLAUDE.md or AGENTS.md in service templates, so new repositories inherit current practice. *Supports:* treating the skills monorepo as a curated, owned asset rather than a free-for-all. (The same radar's Techniques page also lists "Agent instruction bloat" under Caution and "Agent Skills" and "Progressive context disclosure" under Trial: https://www.thoughtworks.com/radar/techniques.)

## 4. Context engineering and the context graph

**Effective context engineering for AI agents** — Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield (Anthropic Applied AI), Anthropic Engineering, 29 Sep 2025.
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
The post frames context engineering as the step beyond prompt engineering: curating everything the model sees. The model's attention budget is finite and recall degrades as context grows, so context should be small and high-signal, with token-efficient tools and just-in-time retrieval. For long tasks it recommends compaction, structured note-taking and sub-agents. *Supports:* the context graph record and the "engineer as context engineer" role (topic 12).

**Context graph (Technology Radar blip)** — Thoughtworks, Techniques, ring **Assess**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/context-graph
A context graph stores the reasoning behind decisions (rules, exceptions, prior cases, evidence, outcomes) as connected nodes that AI systems can query. Unlike GraphRAG, it timestamps each relationship, so outdated facts are marked invalid instead of overwritten. This suits agents that need memory across sessions and an auditable decision trail. *Supports:* an independent industry framing of the same term the episode uses.

## 5. Background agents on cloud development environments

**Minions: Stripe's one-shot, end-to-end coding agents** — Alistair Gray, Stripe Dev Blog, 9 Feb 2026.
https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
Stripe reports that more than a thousand PRs a week are merged from minion-produced code, and humans review all of it. Each run starts on an isolated, pre-warmed devbox, ready in about 10 seconds. The agents use more than 400 tools through Toolshed, a central internal MCP server, and get at most two CI rounds. *Supports:* the closest peer to Uber's background agents on cloud dev environments, and a second MCP-gateway example.

**Minions: Stripe's one-shot, end-to-end coding agents—Part 2** — Alistair Gray, Stripe Dev Blog, 19 Feb 2026.
https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
Devboxes are AWS EC2 instances kept warm in a pool. Work is defined as "blueprints": code-defined state machines that mix deterministic steps (such as linters) with agent steps (such as implementing the task). Toolshed has grown to nearly 500 tools. *Supports:* the deterministic-plus-agentic workflow shape; inner-loop validation (topic 6).

**1,500+ PRs Later: Spotify's Journey with Our Background Coding Agent (Honk, Part 1)** — Max Charas and Marc Bruggmann, Spotify Engineering, 6 Nov 2025.
https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1
Spotify's Fleet Management already applied automated changes across its repositories; since mid-2024 about half of Spotify's PRs have come from it. Honk replaces hand-written migration scripts with prompts and has produced more than 1,500 merged PRs, with 60–90% time savings on migrations. The authors say output is hard to predict and that performance, safety and cost still need work. *Supports:* background agents, and continuous automated maintenance (topic 9).

**Background Coding Agents: Context Engineering (Honk, Part 2)** — Max Charas and Marc Bruggmann, Spotify Engineering, 24 Nov 2025.
https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2
Spotify moved from open-source tools and its own agent loop to Claude Code for complex migrations. Reliable, mergeable PRs depend on tailoring instructions to the agent, saying when not to act, giving concrete examples, and defining verifiable goals. The toolset is deliberately small (a verify tool, restricted Git, allowlisted Bash), because each added tool makes behaviour less predictable. *Supports:* context engineering in practice (topics 4 and 12).

**GitHub Copilot: Meet the new coding agent** — Thomas Dohmke, The GitHub Blog, 19 May 2025 (updated 23 May 2025).
https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
You assign the agent an issue; it works in the background on GitHub Actions and commits to a draft PR, and session logs show its reasoning and validation steps. Existing safeguards still apply: it can push only to branches it creates, and its PRs need human approval before CI/CD workflows run. *Supports:* the vendor-hosted form of background agents and its default guardrails.

**Codex Cloud** — OpenAI, ChatGPT Learn docs (undated, current; redirected from developers.openai.com/codex/cloud).
https://learn.chatgpt.com/docs/cloud
Codex Cloud runs delegated coding tasks remotely, each in its own workspace, and tasks keep running while the user's machine sleeps. The user reviews the changed files and test results, asks for follow-ups, then commits or opens a PR. *Supports:* a second vendor-hosted comparison point.

## 6. Inner-loop validation and agent self-verification in sandboxes

**Background Coding Agents: Predictable Results Through Strong Feedback Loops (Honk, Part 3)** — Max Charas and Marc Bruggmann, Spotify Engineering, 9 Dec 2025.
https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3
Deterministic verifiers (format, build, test) run before the agent opens a PR. An LLM judge then compares the diff against the original prompt to catch out-of-scope changes. The agent runs tightly sandboxed, with limited permissions, few binaries and minimal access to other systems, which the authors tie to both predictability and security. *Supports:* the self-verification record.

**Feedback sensors for coding agents (Technology Radar blip)** — Thoughtworks, Techniques, ring **Trial**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/feedback-sensors-for-coding-agents
Teams connect compilers, linters and test suites to agent workflows so that failures make the agent correct itself, which cuts routine human review. The checks are best run during the session, before commit. *Supports:* moving validation into the agent's inner loop.

**Sandboxed execution for coding agents (Technology Radar blip)** — Thoughtworks, Techniques, ring **Trial**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/sandboxed-execution-for-coding-agents
The blip treats sandboxing (limits on files, network and resources) as a baseline for autonomous agents, and it weighs ephemeral against persistent sandboxes on security, cost and workflow continuity. *Supports:* the sandbox design choices.

**Sandboxes Concepts Guide** — Signadot docs (undated, current).
https://www.signadot.com/docs/concepts/sandbox
A sandbox isolates request flows inside a shared Kubernetes cluster by using a unique routing key sent in a supported header. Requests that carry the key are routed to the sandbox's changed services. This works only if every service on the path propagates the header, usually through OpenTelemetry-style context propagation in application code. *Supports:* how an agent can validate a change against real dependencies without a full copy of the environment.

## 7. AI-assisted code review and risk scoring

**Modern Code Review: A Case Study at Google** — Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko and Alberto Bacchelli, ICSE-SEIP 2018.
https://research.google/pubs/modern-code-review-a-case-study-at-google/
The study uses 12 interviews, a survey of 44 respondents and logs for 9 million reviewed changes to explain why Google adopted code review and how the practice evolved. (The paper also reports figures on small changes and fast reviews; the abstract page does not, so check the PDF before quoting numbers.) *Supports:* the pre-AI baseline of what review is for.

**Resolving code review comments with ML** — Alexander Frömmgen and Lera Kharatyan, Google Research Blog, 23 May 2023.
https://research.google/blog/resolving-code-review-comments-with-ml/
Google's model addresses 52% of reviewer comments in offline evaluation at a 50% target precision. Authors apply 40–50% of the suggested edits they preview. *Supports:* an early large-scale data point on ML in the review loop.

**Diff Risk Score: AI-driven risk-aware software development** — Meta Engineering blog (no individual byline), 6 Aug 2025.
https://engineering.fb.com/2025/08/06/developer-tools/diff-risk-score-drs-ai-risk-aware-software-development-meta/
DRS, built on a fine-tuned Llama model, estimates how likely a diff is to cause a production incident (SEV) and highlights risky code. It replaced blanket code freezes with risk-gated "unfreezes", letting more than 10,000 changes ship during a 2024 partner event. *Supports:* the closest public analogue to risk scoring on AI-generated PRs.

**Moving Faster and Reducing Risk: Using LLMs in Release Deployment** — Rui Abreu, Vijayaraghavan Murali, Peter C. Rigby, Chandra Maddila et al. (Meta), arXiv 2410.06351, 8 Oct 2024.
https://arxiv.org/abs/2410.06351
The paper introduces the DRS models and compares them with a production logistic-regression baseline at gating thresholds (top 5%, 10% and 50% riskiest diffs). Risk-aligned generative LLMs (iCodeLlama-34B, iDiffLlama-13B) beat the baseline at catching SEVs. *Supports:* the research basis for risk-tiered review.

## 8. PR volume, review load, and the productivity evidence

**DORA 2025 State of AI-assisted Software Development Report** — Derek DeBellis, Nathen Harvey, Gene Kim et al., DORA / Google, 2025.
https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
The report draws on survey responses from nearly 5,000 technology professionals and more than 100 hours of qualitative data. Its central finding is that AI is an "amplifier": it magnifies the strengths of high-performing organisations and the dysfunctions of struggling ones. *Supports:* why platform investment, not tool rollout, decides the outcome (topics 10 and 12).

**DORA Capabilities: Platform engineering** — dora.dev (current).
https://dora.dev/capabilities/platform-engineering/
When platform quality is high, the effect of AI adoption on organisational performance is "strong and positive"; when quality is low, it is negligible. A good internal platform keeps AI speed-ups from being lost to downstream bottlenecks. *Supports:* "platform engineering is the foundation for AI" (topic 10).

**The AI Productivity Paradox Report 2025** — Faros AI, 23 Jul 2025.
https://www.faros.ai/blog/ai-software-engineering
Telemetry from more than 10,000 engineers on 1,255 teams shows that with high AI adoption, PR review time rose 91% and average PR size rose 154%. *Supports:* review becoming the bottleneck, and the case for AI-assisted review and risk tiers (topic 7). The data is correlational.

**AI Copilot Code Quality: 2025 Look Back at 12 Months of Data** — GitClear (page undated; data Jan 2020–Dec 2024).
https://www.gitclear.com/ai_assistant_code_quality_2025_research
From 211 million changed lines, copy-pasted lines rose from 8.3% to 12.3% (2021–2024), and moved (refactored) lines fell from 25% to under 10%. *Supports:* why continuous maintenance and quality gates matter more as AI output grows (topic 9). GitClear's causal reading is interpretation.

**Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity** — METR, 10 Jul 2025.
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
In a randomised controlled trial (16 experienced developers, 246 real issues in mature repositories they knew well), AI-allowed tasks took 19% longer, yet developers believed AI had made them 20% faster. *Supports:* measuring outcomes rather than perceived speed; caution on PR-count metrics.

## 9. Continuous automated maintenance and large-scale changes

**Software Engineering at Google, Chapter 22: Large-Scale Changes** — Hyrum Wright (ed. Lisa Carey), O'Reilly 2020, free online edition at abseil.io.
https://abseil.io/resources/swe-book/html/ch22.html
A large-scale change (LSC) is a set of related changes that cannot practically be committed atomically, and the largest feasible atomic change shrinks as a codebase grows. Google's Rosie tool splits an LSC into shards that are tested, reviewed and submitted independently. *Supports:* the canonical model behind agent-driven fleet migrations.

**OpenRewrite docs** — OpenRewrite by Moderne (current).
https://docs.openrewrite.org/
OpenRewrite refactors code automatically by editing Lossless Semantic Trees through visitors grouped into recipes, preserving the original formatting. Prepackaged recipes cover framework migrations, security fixes and style. *Supports:* the deterministic-tooling counterpart that agents complement or call.

**Piranha: Reducing Feature Flag Debt at Uber** — Murali Krishna Ramanathan, Lazaro Clapp, Rajkishore Barik and Manu Sridharan, ICSE-SEIP 2020.
https://2020.icse-conferences.org/details/icse-2020-Software-Engineering-in-Practice/16/Piranha-Reducing-Feature-Flag-Debt-at-Uber
Piranha generates diffs that remove code behind stale feature flags. From late 2017 to mid-2019 it produced cleanup diffs for 1,381 flags, and about two-thirds were merged unmodified. *Supports:* Uber's own pre-LLM history of automated maintenance.

**Introducing Piranha: An Open Source Tool to Automatically Delete Stale Code** — Manu Sridharan, Rajkishore Barik and Lazaro Clapp, Uber Blog, 17 Mar 2020.
https://www.uber.com/blog/piranha/
Piranha (Objective-C, Swift, Java) runs weekly on Uber's Android and iOS codebases and assigns each generated diff to the flag's author for review; about two thousand stale flags have been removed. *Supports:* the "assign the machine's diff to an accountable human" pattern.

(Spotify Honk Part 1, topic 5, is the AI-era continuation of the same idea.)

## 10. Platform engineering and paved roads

**Chapter 8 – Release Engineering** — Dinah McNutt (ed. Betsy Beyer, Tim Harvey), *Site Reliability Engineering*, Google / O'Reilly 2016, sre.google.
https://sre.google/sre-book/release-engineering/
The chapter sets four principles: self-service, high velocity (frequent, small releases), hermetic builds, and policy enforcement through gated operations. Reliable services depend on automated, repeatable release processes from source to deployment. *Supports:* the paved-road foundation that agents ride on.

**Team Topologies key concepts** — Team Topologies (Matthew Skelton, Manuel Pais), teamtopologies.com.
https://teamtopologies.com/key-concepts
Platform teams offer an internal product to speed up stream-aligned teams. The Thinnest Viable Platform keeps the platform minimal, and cognitive load is a hard limit to manage. *Supports:* framing Uber's AI infra as a platform product with internal customers.

(DORA platform-engineering capability, topic 8, gives the AI-specific evidence.)

## 11. Token-spend governance and FinOps for AI

**FinOps for AI Overview** — FinOps Foundation (contributors from Wayfair, Google, AWS and others), last updated 17 Feb 2026.
https://www.finops.org/wg/finops-for-ai-overview/
Token-based billing makes AI costs harder to track, because billed tokens can differ from what the user typed. The overview proposes cost per token as a metric and adds token-based units to unit economics, such as cost per call and value measures set against AI spend. *Supports:* the token-governance record's vocabulary and metrics.

(LiteLLM virtual keys and budgets and Kong's cost management, topic 1, show where those controls are enforced.)

## 12. The changing engineer role: context engineering, multitasking, verification

**How AI is transforming work at Anthropic** — Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern and Deep Ganguli, Anthropic Research, 2 Dec 2025.
https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
Employees report using Claude for about 60% of their work, with roughly a 50% productivity gain. Over half can fully delegate only 0–20% of tasks, because they supervise and validate the output. The authors call this the "paradox of supervision": good oversight needs the very skills that delegation may erode. *Supports:* verification as the core engineering skill.

**Building effective agents** — Erik Schluntz and Barry Zhang, Anthropic Engineering, 19 Dec 2024.
https://www.anthropic.com/engineering/building-effective-agents
The post distinguishes workflows (fixed, code-defined paths) from agents (which direct their own process) and catalogues patterns: prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimizer. It advises adding complexity only when it clearly pays off. *Supports:* a shared vocabulary for the role and harness records; it pairs with Stripe's blueprints.

**Codebase cognitive debt (Technology Radar blip)** — Thoughtworks, Techniques, ring **Caution**, Vol. 34, Apr 2026.
https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt
This is the growing gap between how a system is built and what the team understands of its design. AI-accelerated change, especially with agent swarms, widens it. *Supports:* the risk side of the role shift; why engineers must stay owners of intent.

**DX Core 4: Measuring developer productivity with the DX Core 4** — Abi Noda, Laura Tacho, Margaret-Anne Storey and Michaela Greiler, DX (page undated; © 2026).
https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/
The framework uses four dimensions (speed, effectiveness, quality and business impact) and unifies DORA, SPACE and DevEx. *Supports:* a balanced alternative to PR counts when measuring feature velocity (topic 8).

**The SPACE of Developer Productivity: There's more to it than you think** — Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck and Jenna Butler, *ACM Queue* 19(1), Feb 2021 (Microsoft Research listing).
https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/
The paper argues that productivity cannot be captured by one metric and needs several dimensions. The commonly cited five are Satisfaction, Performance, Activity, Communication and Efficiency; the listing page does not name them, so cite the paper for that. *Supports:* why "more PRs" alone is not velocity.

**DevEx: What Actually Drives Productivity** — Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler, DX research page, 3 May 2023 (full text in *ACM Queue* 21(2), 2023).
https://getdx.com/research/devex-what-actually-drives-productivity/
The abstract ties developer experience to productivity, efficiency, product quality and retention. The paper's framework centres on three dimensions (feedback loops, cognitive load, flow state); the landing page does not list them, so cite the paper. *Supports:* inner-loop speed and multitasking load as developer-experience concerns.

---

## Not verified (could not fetch; do not cite without a manual check)

- ACM Queue full texts of SPACE (`queue.acm.org/detail.cfm?id=3454124`) and DevEx (`queue.acm.org/detail.cfm?id=3595878`): Cloudflare 403. Use the Microsoft Research and DX landing pages above instead.
- OpenAI "Introducing Codex" (`openai.com/index/introducing-codex/`): 403. Use the Codex Cloud docs above.
- Lyft, "Scaling productivity on microservices at Lyft (Part 3): Extending our Envoy mesh with staging overrides" (eng.lyft.com, Medium): 403. This is the canonical request-isolation source and well worth a manual check. The URL found by search is https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f.
- Google Cloud DORA landing page (`cloud.google.com/devops/state-of-devops`): fetched, but only the title came back. The seven-capability "DORA AI Capabilities Model" could not be confirmed from the page, so confirm it in the PDF before citing.
- No Thoughtworks blip named "AI gateway" or "MCP gateway" was found; LiteLLM is the radar's gateway entry.
