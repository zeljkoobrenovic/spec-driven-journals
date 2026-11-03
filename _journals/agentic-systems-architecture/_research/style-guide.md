# Style Guide for Chapter Writers — Architecting Agentic Systems

Read this, `../PLAN.md` (your chapter contract), `scenario-ledger.md` (the shared fictional facts), the research briefs and digests named in your contract **before writing**. The reference books for voice, density and structure are *Architecting a Vehicle Data and Dealer SaaS Platform* (`_journals/vehicle-data-dealer-saas-architecture/`; read `posts/24-dms-integration/index.md` as the model chapter), BOOKED (`_journals/stays-marketplace-architecture/`, `posts/12-availability-engine/index.md`) and LISTED (`_journals/listing-systems-architecture/`). Keep their discipline: concrete, defined, evidenced, example-driven.

## Voice and audience

- The reader is an experienced software architect, senior engineer or technical leader. Do **not** explain what an API, a queue, a container, OAuth or a vector database is. **Do** define agent-specific, ML and regulatory terms on first use in each chapter (one clause), and link to the chapter that owns the term (see PLAN "Owns"). Expand every acronym on first use in each chapter (LLM, MCP, A2A, RAG, OTel, SoD, ERP, HRIS, CRM, PEP, OPA, SLO, TTFT…).
- First person ("I", "my") is the author speaking as a Chief Architect who has to make and defend these decisions: judgement and recommendations ("I would…", "The rule I use…"). Use it sparingly. Never claim specific real employers, real incidents or inside knowledge of any company.
- American spelling (organization, behavior, modeling, canceled). Plain, declarative sentences. No hype or buzzwords ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "revolutionize", "supercharge", "paradigm shift", "AI-native", "agentic future"). Do not anthropomorphize beyond what the mechanism supports: the model *proposes*, *selects*, *generates*; say "the model's output" rather than "the agent thinks" unless quoting.
- Explain **why components exist, where they belong, how they interact, when to use them, and what trade-offs they introduce** — not feature lists. Tie each choice to a consequence of failure, a requirement or a cost.
- **Durable vs volatile.** Separate durable principles from implementation details tied to a framework, model, provider or protocol version. Date every volatile fact ("as of October 2026", "the 2025-11-25 revision of the MCP specification"). Never name a specific model version as a recommendation.

## Evidence discipline (non-negotiable)

Seven kinds of statement; make the kind obvious from wording and source:

1. **Research finding** — from a paper or preprint. Say what was measured, on what benchmark or setting, and the main limitation, in a clause ("On τ-bench's retail tasks, the best 2024 agent's pass^8 fell below 25% (Yao et al., 2024) — a simulated-user benchmark, so treat it as an indicator, not a rate"). Say "preprint" when it is not peer reviewed.
2. **Documented experience** — an engineering writeup, incident report, postmortem, court or regulator decision. Give the organization and year in the sentence ("In its June 2025 engineering post, Anthropic reported…").
3. **Specification or documentation** — a standard, protocol spec, official docs, regulation. Give version or date and link the official text.
4. **Recommendation / judgement** — the author's architectural view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Ostrell. Always fictional; say so the first time in each chapter ("Ostrell, the fictional company this book follows").
6. **Assumption** — illustrative volumes, latency targets and costs that are neither Ostrell ledger facts nor documented: label them ("Assume…", "an illustrative target of…") or with `*(assumption)*` in table cells.
7. **Design example from the interview project** — material adapted from the author's system-design interview designs. Label it ("The author's agentic-support-platform interview design (step 4) adds…") and cite in Sources as: *Obrenović, Ž., "Agentic Support Platform", system-design interview design, `system-design-interviews/data/book/agentic-support-platform/interview.json`, 2026.* Never present it as a deployed system or as evidence of production behavior.

Link the source inline the first time it matters. Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself with WebFetch. Never invent results, benchmark numbers, deployment experience, production-readiness claims or internals of real companies; when the evidence runs out, **say so explicitly** ("No published evaluation compares … ; the following is the author's judgement"). Where sources disagree, present both and say what the disagreement implies for the decision. Vendor marketing is not evidence of effectiveness; a vendor's engineering post is documented experience about its own system only.

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-28
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one or two sentences>

> **WHY THE BUSINESS CARES:** <one or two sentences, from the product owner's, risk owner's or CFO's view>

> **WHY ARCHITECTS SHOULD CARE:** <one or two sentences>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-agentic-systems-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases. End the lead by naming the terms the chapter owns and the neighbouring chapters it builds on and hands to.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection. Part intros use "IN THIS PART, YOU WILL" and "FAILURE PATTERNS THIS PART ADDRESSES" and end with a `## Chapters in this part` list.

Body (a guide, not a rigid template — name sections by content, not generic labels):

1. **Setting the scene at Ostrell** — a concrete 2027 situation that poses the chapter's question (one section, early).
2. **Concepts** — the foundations, defined precisely: entities, states, boundaries, invariants.
3. **Architecture** — components, responsibilities, interfaces, boundaries, data ownership; requirements per interaction (consistency, latency, durability, who may act) in a small table; at least one diagram. Code or pseudocode where it clarifies a mechanism (short, typed, language-neutral or Python/TypeScript; never a full framework tutorial).
4. **Evidence** — what research and documented experience say, dated and sourced, with limitations and disagreements.
5. **Worked example at Ostrell** — with numbers from the ledger, end to end.
6. **Failure modes and recovery** — concrete failure scenarios relevant to the topic: what happens, how it is detected, what contains it, how the system recovers.
7. **Trade-offs** — alternatives compared in a table; when each is right; tie the recommendation to explicit requirements and assumptions.
8. **Across Domains: How the Stakes Change the Design** — required in Parts II–X (exact heading): comparison table (Coding agents · Customer operations · Back office · High-stakes decisions) and a judgement on what is platform-common and what is domain policy. Where domains are the same for this topic, say so briefly.
9. **The Chief Architect's view** — the decisions, governance and long-term considerations; what to decide, who decides, what to watch; what is durable and what will change with model capabilities.
10. **Questions to ask** — 6–10 questions the reader can take into a design review.
11. A closing paragraph that hands off to the next page in reading order with a `[[link]]`.
12. `## Sources and Evidence` — grouped: *Research papers*, *Specifications, standards and regulation*, *Vendor documentation and engineering reports*, *Incidents, cases and decisions*, *Design examples from the author's interview project*; each entry: linked title, author/publisher, **publication year (or "n.d., accessed 2026-10")**, one clause on what it supports. End with: "Ostrell is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement."

Length: **5,000–7,000 words** for chapters (may go to 8,000 if the depth is earned); DOMAINS chapters 6,000–8,000; part intros 500–900. Depth beats breadth: one well-worked example beats five mentions. Do not re-teach what another chapter owns — define in one clause and link.

## Diagrams

**No mermaid (28 Oct 2026).** Since the visual pass, every diagram in the book is a generated illustration. To draw a new diagram, write an `illustration-placeholder` block (the `article-illustrator` skill's format) whose prompt gives each element's position and quoted 1–3 word label and names every arrow; generate it, inspect it against the caption, and replace the placeholder with `![alt](assets/images/<folder>/<id>.jpeg)` followed by `**Figure N:** *<caption>*`. Procedure and tools: `ILLUSTRATOR-BRIEF.md`; the original mermaid sources are archived in `mermaid-figures.json` and their layout screenshots in `diagram-illustrations/refs/`. The mermaid rules below describe the text phase only.

During text writing, diagrams were **mermaid blocks** (rendered client-side). A later visual pass may convert them into generated illustrations, keeping the captions, so write each diagram so it would also make a clear 5–9-element illustration: a clear subject, few boxes, every arrow meaningful. Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Agent runtime"] -->|"tool call"| B["Tool broker"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~16 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias; message text after the colon must avoid semicolons, `#` and the word `end` alone), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point>*`. Aim for 2–4 diagrams per chapter; DOMAINS chapters must have a sequence diagram of the end-to-end flow.

Use GitHub tables generously: contrasts, decision criteria, responsibility matrices, state tables, requirement tables, domain comparisons, failure-scenario tables (scenario · detection · containment · recovery).

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `where-agentic-systems-go-wrong`, `meet-ostrell`, `part-1` … `part-11`, `what-makes-a-system-agentic`, `when-agents-are-justified`, `autonomy-and-consequence`, `workflows-loops-and-autonomous-agents`, `agentic-reference-architecture`, `models-and-the-model-gateway`, `agent-runtime`, `agents-in-the-enterprise`, `agent-interaction-design`, `planning-and-decomposition`, `routing-and-delegation`, `single-and-multi-agent-designs`, `coordination-and-handoffs`, `context-engineering`, `retrieval-and-grounding`, `agent-memory`, `task-state-and-checkpoints`, `provenance-and-freshness`, `tool-contracts`, `tool-ecosystems-and-mcp`, `sandboxes-and-execution-environments`, `side-effects-and-external-actions`, `durable-agent-execution`, `retries-idempotency-and-concurrency`, `partial-failure-and-compensation`, `agent-threat-model`, `prompt-injection-defense`, `agent-identity-and-least-privilege`, `human-oversight-and-bounded-autonomy`, `policy-enforcement-and-audit`, `evaluating-agentic-systems`, `building-agent-eval-suites`, `agent-observability`, `evidence-for-autonomy`, `agent-latency-and-throughput`, `agent-cost-and-model-routing`, `caching-and-context-budgets`, `versioning-agent-systems`, `staged-rollout-and-rollback`, `owning-agentic-systems`, `domain-coding-agents`, `domain-customer-operations`, `domain-back-office`, `domain-high-stakes-decisions`, `source-coverage`, `toolkit`, `glossary`, `bibliography`.

Allowed links to sibling books (for depth the reader can follow; do not re-teach them): RECONCILED (finance) `designing-financial-ledgers`; the vehicle book `events-webhooks-and-sync`, `provenance-and-data-quality`, `ingestion-and-entity-resolution`. Link where it helps (typically 8–15 per chapter). Never invent a permalink: a typo can silently resolve to another journal's page.

## Failure patterns (the opening guide `where-agentic-systems-go-wrong`)

Use these exact names:

| Pattern | Warning sign | Part that addresses it |
| --- | --- | --- |
| **The Agent-Shaped Hammer** | An agent loop is used where a fixed workflow, a single model call or plain code would do; nobody can state what the model decides that code could not. | I |
| **Autonomy by Default** | The agent may take every action its tools allow; autonomy was never sized to consequence and reversibility, nor earned with evidence. | I, VII, VIII |
| **The Compounding Error** | Long chains of model steps with no checks between them; a 95%-reliable step becomes a coin flip over a dozen steps. | I, III |
| **The Agent Committee** | Several agents talk to each other where one would do; tokens, latency and lost accountability rise and nobody can say which agent decided. | III |
| **The Lost Handoff** | Work passes between agents or to humans as free text; identifiers, constraints and commitments fall out on the way. | III |
| **Context Soup** | Everything is stuffed into the context window; relevant facts are drowned, stale or unmarked as untrusted. | IV |
| **Amnesiac Execution** | Task state lives only in the conversation; a crash, deploy or timeout restarts the task from scratch or repeats its side effects. | IV, VI |
| **Memory Without Expiry** | Long-term memory accumulates without provenance, review or expiry; stale and poisoned facts keep coming back. | IV |
| **The Fire-and-Forget Action** | Tools change external systems without idempotency keys, receipts or verification; nobody knows whether the action happened once, twice or not at all. | V, VI |
| **The Different Second Answer** | A retry re-asks the model, which proposes a different action; the system executes both, or neither, or the wrong one. | VI |
| **Ambient Authority** | The agent acts with a service account or the user's full credentials; any tool call can reach anything that identity can. | VII |
| **The Lethal Trifecta** | One agent combines private data, untrusted content and a way to send data out; a single injected instruction can exfiltrate. | VII |
| **The Rubber Stamp** | Human approval exists on paper, but approvers see too little, approve too fast and are never measured. | VII |
| **Vibe Evals** | Changes ship on demos and spot checks; there is no regression suite, no trajectory evaluation and no link from evidence to autonomy. | VIII |
| **The Token Bonfire** | No budgets per run, tenant or agent; loops, fan-out and retries turn into an invoice. | IX |
| **The Silent Upgrade** | Models, prompts, tools or policies change without versioning, evaluation or staged rollout; behavior drifts and nobody can say when or why. | X |

## Ostrell usage

- Use the cast, agents, platform components and numbers in `scenario-ledger.md`. Reuse the recurring worked examples (the Double Credit, the Poisoned Ticket, the Stale Price Book, the Weekend Fan-out, the Alias Drift, the Half-Posted Accrual, the Rubber Stamp, the Lost Handoff, the Fixture Purge) when relevant — amounts and dates must match.
- Time: chapters are set in 2027 unless the contract says otherwise.
- Do not name real model versions as Ostrell's models; use the ledger's tiers (Large, Mid, Small, Embed). Ostrell's providers are "two commercial model providers" and "an open-weight model in Ostrell's cloud account" — unnamed.
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- Ostrell must never resemble a specific real company closely enough to be read as a disguised description of it.
- The cast's pronouns are in the ledger. For real people (authors, cited engineers) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-10-28`. Intent, Audience, Success criteria (5–8 checkable boxes), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]`, the interview sources used, and key external sources), Changelog (one entry: `- **2026-10-28** — Initial spec and article. *(AI-mediated session)*`). Typically 500–900 words.

## Quality bar — check before finishing

- Every substantive technical claim has a nearby citation; research findings say what was measured and its limits; vendor/company claims are dated; inferences labeled; illustrative numbers labeled as assumptions or as Ostrell; interview material labeled as design examples.
- At least one Ostrell worked example with numbers; at least one trade-off table; at least one requirements table where flows are discussed; at least one failure-scenario table; the "Across Domains" section with its table (Parts II–X); at least two diagram figures; a Chief Architect's view; Questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure or in another chapter.
- No undefined jargon; every acronym expanded on first use in the chapter.
- Cross-links use only valid permalinks.
