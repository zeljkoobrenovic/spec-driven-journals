# Research brief: Security, identity and human oversight in agentic systems

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief is vendor-neutral. Anthropic, Microsoft, AWS, Google DeepMind and OpenAI get the most space because they have published dated, quantified material on agent security, not because the book endorses their products. Most of the measured numbers here are **vendor self-reports or academic benchmark results**, and the brief says which is which every time.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Undated documents say "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor explainer, conference summary, search-result digest), not from the primary document, or from a primary page that could not be fetched in full.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about the internals of a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Source types.** For each research result the brief says whether it is a **peer-reviewed paper**, an **arXiv preprint**, a **vendor engineering post** (describes a system and gives numbers, but is unreviewed and the vendor chose the test), **vendor marketing/product docs**, a **standard or spec**, or **regulation**. A vendor's attack-success number measures the vendor's own attacker against the vendor's own model on the vendor's own test set; such numbers are not comparable across vendors and rarely comparable across a vendor's own successive posts (see 2.4).

**Evidence age matters.** This field moves monthly. Benchmarks from mid-2024 (AgentDojo v1–v3) measured GPT-4o and Claude 3.x; the models behind today's agents are two or three generations later. The structural results (what an architecture can and cannot guarantee) age well; the per-model attack-success rates do not. Each section gives the date of its evidence. Sources older than about 18 months (before roughly April 2025) are marked **[old evidence]**.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: protocol versions, draft standards, product names and availability, regulatory dates, model names.

**Research limitation.** The shared web-search quota was used sparingly, and several primary pages could not be fetched:

- Aim Security's original EchoLeak write-up (HTTP 403), The Hacker News coverage (403) and Microsoft's MSRC advisory page (JavaScript-only) could not be read. EchoLeak facts come from the NVD API record and an arXiv case study.
- OpenAI's December 2025 post on hardening ChatGPT Atlas returned 403; only search-result digests were available.
- The full OWASP Top 10 for Agentic Applications document is behind a download link; the ten category names come from a secondary source (Promptfoo documentation).
- The PubMed web pages were behind a bot check; abstracts were read through the NCBI E-utilities API.
- Cedar's marketing site returned only a playground title; Cedar semantics come from its documentation and its arXiv paper.
- No independent (non-vendor) measurement of a production agent's prompt-injection rate was found. Every production number in this brief comes from the vendor that runs the system.

---

## PART 1: The threat — prompt injection as an architectural problem

### 1.1 Indirect prompt injection: the founding result

- Greshake et al. introduced **indirect prompt injection**: an attacker plants instructions in data an LLM-integrated application is likely to retrieve, so the attacker needs no direct access to the model. The paper argues that such applications "blur the line between data and instructions" [VERIFIED: https://arxiv.org/abs/2302.12173, published 2023-02-23, v2 2023-05-05]. **[old evidence]** — arXiv preprint; the abstract names no venue (it was later presented at ACM AISec 2023 [ASSUMPTION/JUDGEMENT — not confirmed in this session]).
- What was demonstrated: attacks against **Bing's GPT-4-powered Chat**, code-completion engines and synthetic applications on GPT-4. The authors claim that processing retrieved prompts can act like **arbitrary code execution**, manipulate application behavior and control whether and how other APIs are called. Their impact taxonomy includes data theft, "worming" and contamination of information ecosystems [VERIFIED: https://arxiv.org/abs/2302.12173, published 2023-02-23].
- The authors stated that effective mitigations were lacking at the time of writing [VERIFIED: same].
- NIST's Generative AI Profile adopts the concept: indirect prompt injection occurs when adversaries remotely exploit LLM-integrated applications by injecting prompts into data likely to be retrieved, and security researchers "have already demonstrated" such exploits [VERIFIED: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, published 2024-07-26].

**Durable vs volatile.** Durable: an LLM cannot reliably separate instructions from data in its context window, so any content it reads is a potential control channel. Volatile: the specific demonstration targets (Bing Chat in 2023) no longer exist in that form.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat every tool result, retrieved document, email, web page, file, issue comment and tool *description* as attacker-controllable input to the planner. The trust boundary in an agentic system is not the network edge; it runs through the context window.

### 1.2 The lethal trifecta and the Agents Rule of Two

- Simon Willison's **lethal trifecta** (16 June 2025): an agent is exploitable for data theft if it combines (1) access to **private data**, (2) exposure to **untrusted content**, and (3) the ability to **communicate externally** in a way that can exfiltrate data [VERIFIED: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/, published 2025-06-16]. Type: practitioner blog, highly influential, not peer-reviewed.
- Willison's stance on guardrail products: vendors advertising that they catch "95% of attacks" are, by web-security standards, offering a failing grade; "we still don't know how to 100% reliably prevent this from happening" [VERIFIED: same].
- He argues **MCP** makes the trifecta easy to assemble, because users mix tools from different sources and many tools both read private data and expose untrusted content; once users combine tools themselves, vendors cannot protect them [VERIFIED: same].
- The post lists products with documented exfiltration bugs, most since fixed: Microsoft 365 Copilot, GitHub's official MCP server, GitHub Copilot Chat, GitLab Duo, ChatGPT (incl. plugins and Operator), Google Bard/NotebookLM/AI Studio, Writer.com, Amazon Q, Slack, Mistral Le Chat, xAI Grok, and Anthropic's Claude iOS app [VERIFIED: same]. This is a curated list of public disclosures, not a measured incidence rate.
- Meta's **Agents Rule of Two** (31 October 2025), explicitly inspired by the trifecta and by a Chromium policy of the same name: within one session an agent should satisfy **no more than two** of [A] processes untrustworthy inputs, [B] accesses sensitive systems or private data, [C] changes state or communicates externally. If a task needs all three, the agent should not run autonomously; it needs supervision such as human approval, or a fresh context [VERIFIED: https://ai.meta.com/blog/practical-ai-agent-security/, published 2025-10-31]. Type: vendor engineering post.
- Meta's stated limits: the rule does not address other threats (agent mistakes, hallucination, excessive privilege, spam, lower-consequence injection outcomes such as misleading answers), and a compliant design still fails if a user blindly confirms a warning [VERIFIED: same].

| | Lethal trifecta (Willison) | Agents Rule of Two (Meta) |
| --- | --- | --- |
| Third leg | Ability to exfiltrate / communicate externally | Change state **or** communicate externally |
| Scope | Data theft | Data theft **and** unwanted actions |
| Resolution | Remove one leg | Remove one leg, or add human approval / fresh context |
| Evidence | Catalogue of disclosed incidents | Design rule; no measurement published |

**Durable vs volatile.** Durable: a capability-combination rule is model-independent and survives model upgrades. Volatile: Meta frames the rule as provisional, to hold until injection can be reliably detected.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Make the trifecta a design-review check per *session*, not per agent. The practical move is usually to split the agent: one context reads untrusted content without private data or egress; another holds private data but never sees raw untrusted content. Egress control (an allow-listed proxy, no auto-rendered images or links) is often the cheapest leg to remove.

### 1.3 OWASP: LLM Top 10 (2025) and Agentic Top 10 (2026)

- The **OWASP Top 10 for LLM Applications 2025**: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption [VERIFIED: https://genai.owasp.org/llm-top-10/, n.d., accessed 2026-10]. The English release date is not shown on the page; translations are dated 12 March 2025, which places the English edition before then (generally reported as November 2024) [ASSUMPTION/JUDGEMENT].
- **LLM06 Excessive Agency** names three root causes — excessive **functionality**, excessive **permissions**, excessive **autonomy** — and prescribes: run extensions **in the user's context** with the narrowest OAuth scope; require **human approval** for high-impact actions; and **complete mediation**: "Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not." Logging, monitoring and rate limiting limit damage but do not prevent excessive agency [VERIFIED: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/, n.d., accessed 2026-10].
- The **OWASP Top 10 for Agentic Applications for 2026** was published by the OWASP GenAI Security Project on **9 December 2025** [VERIFIED: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/, published 2025-12-09], announced at Black Hat Europe 2025 [WIDELY REPORTED: https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/, 2026].
- Its ten categories [WIDELY REPORTED: https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/, 2026]: ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution; ASI06 Memory and Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents. Secondary sources differ slightly on exact titles (e.g. "Identity Abuse" vs "Identity & Privilege Abuse") ⚠ — cite the OWASP PDF for wording.

**Durable vs volatile.** Durable: the categories map onto classic security concepts (confused deputy, supply chain, least privilege, input handling). Volatile: ranks and names are revised every one to two years; the "2026" label on a December 2025 document already causes citation confusion.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Use OWASP as a review checklist and a shared vocabulary with security teams, not as a design method. LLM06's "complete mediation" sentence is the single most useful line for this book: the authorization decision belongs in the system the agent calls, not in the model.

---

## PART 2: Defenses — what is measured, what is proposed

### 2.1 AgentDojo: the reference benchmark

- **AgentDojo** (Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, Tramèr; ETH Zurich and Invariant Labs) is an extensible environment for prompt-injection attacks and defenses on tool-using agents: **97 user tasks** (email client, e-banking, travel booking, workspace) and **629 security test cases** [VERIFIED: https://arxiv.org/abs/2406.13352, v1 2024-06-19, v3 2024-11-24]. **[old evidence]** arXiv preprint; it is generally reported as a NeurIPS 2024 Datasets and Benchmarks paper, but the arXiv page does not say so [ASSUMPTION/JUDGEMENT].
- What it measures: **benign utility** (task success with no attack), **utility under attack**, and **targeted attack success rate (ASR)** — the share of cases in which the agent performs the attacker's injected task [VERIFIED: https://arxiv.org/html/2406.13352v3, 2024-11-24].
- Results with the baseline "important message" attack (Table 3, v3): GPT-4o 69.0% benign utility, 50.1% utility under attack, **47.7% targeted ASR**; Claude 3.5 Sonnet 78.2% / 51.2% / 33.9%; Claude 3 Opus 66.6% / 52.5% / 11.3%; Gemini 1.5 Pro 45.6% / 28.9% / 25.6% [VERIFIED: https://arxiv.org/html/2406.13352v3, 2024-11-24].
- Defenses on GPT-4o (Table 5, v3): no defense 57.7% targeted ASR; **data delimiting** (spotlighting-style) 41.7%; **repeat user prompt** (sandwiching) 27.8%; **BERT prompt-injection detector** 8.0% but benign utility falls from 69.0% to 41.5%; **tool filter** (the LLM picks the tools it needs before seeing untrusted data) **6.8%** with utility 73.1% [VERIFIED: same]. The text rounds the tool-filter figure to 7.5%.
- **Internal inconsistency** in v3: the no-defense GPT-4o ASR is 47.69% in Table 3 and 57.69% in Table 5; the introduction says LLMs solve "less than 66%" of tasks and that attacks succeed in "less than 25%" of cases against the best agents, both of which conflict with the tables [VERIFIED: same]. Chapter writers should cite table numbers with the table and version.
- Stated limitations: attacks and defenses are simple and stronger adaptive attacks are expected; the tool filter fails when tools cannot be planned in advance or when the task's own tools suffice for the attack (about **17%** of test cases); the detector has too many false positives; repeating the prompt is unlikely to withstand adaptive attacks; multimodal agents are not covered [VERIFIED: same].

**Durable vs volatile.** Durable: the three-metric framing (benign utility, utility under attack, ASR) and the finding that isolation-style defenses beat prompt-style defenses. Volatile: every per-model number; the models tested are retired or superseded.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Even the weakest structural defense in the benchmark (deciding the tool set before reading untrusted data) outperformed every prompt-level defense. Report utility *and* ASR for any defense you adopt; a detector that cuts ASR by halving utility is a product decision, not a free win.

### 2.2 Spotlighting and prompt-level defenses

- Microsoft's **spotlighting** (Hines et al.) marks untrusted input by delimiting, datamarking or encoding it so the model can tell its provenance. In the authors' experiments with "GPT-family models", ASR dropped from **above 50% to below 2%** with "minimal impact on task efficacy" [VERIFIED: https://arxiv.org/abs/2403.14720, published 2024-03-20]. **[old evidence]** — arXiv preprint; the abstract names no model versions and the attacks were static.
- In AgentDojo, a spotlighting-style delimiter defense only reduced GPT-4o ASR from 57.7% to 41.7% (2.1) — an example of a defense whose headline number did not transfer to an agentic benchmark [VERIFIED: https://arxiv.org/html/2406.13352v3, 2024-11-24].

### 2.3 Adaptive attacks break published defenses

- **"The Attacker Moves Second"** (Nasr, Carlini, Sitawarin, Tramèr and 10 others; OpenAI, Anthropic, Google DeepMind and academic authors) evaluated **12 recent defenses** against jailbreaks and prompt injection with adaptive attacks (gradient descent, reinforcement learning, random search, human-guided exploration) and reports ASR "**above 90% for most**", although most of those defenses originally reported near-zero ASR [VERIFIED: https://arxiv.org/abs/2510.09023, published 2025-10-10]. Type: arXiv preprint.
- The authors' conclusion: evaluations with static attack strings or weak optimization are flawed, and "future defense work must consider stronger attacks" [VERIFIED: same].

**Durable vs volatile.** Durable: a defense evaluated only against fixed attack strings tells you little. Volatile: which specific defenses were broken.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat model-level and classifier-level defenses as probability reducers, never as boundaries. Any vendor ASR figure should be read with three questions: which attacker (static or adaptive), how many attempts, and whose test set.

### 2.4 Vendor-reported defense measurements (self-reported, non-comparable)

All numbers in this section are **vendor engineering posts or product posts**: unreviewed, on vendor-chosen test sets, with vendor-built attackers.

| Source | Date | Setting | Reported ASR |
| --- | --- | --- | --- |
| Anthropic, Claude for Chrome | 2025-08-25 | 123 test cases, 29 attack scenarios, autonomous mode | 23.6% → **11.2%** with mitigations; browser-specific set 35.7% → 0% |
| Anthropic, "Mitigating the risk of prompt injections in browser use" | 2025-11-24 | Internal adaptive Best-of-N attacker, 100 attempts per environment, ~2,200–3,200 attempts per bar | Opus 4.5: 8.0% model only → **1.4%** with improved safeguards; Sonnet 4.5 13.8% → 1.9% |
| Anthropic, "Claude in Chrome is generally available" | 2026-08-26 | Newer evaluation with attacks from professional red-teamers; counts only attacks that reached the model | Opus 4.5 **17.6%** without added safeguards; Opus 5 3.8%; Opus 5 / Sonnet 5 / Mythos 5 **0%** with probes + classifier; Fable 5 0.3% |

Sources: [VERIFIED: https://claude.com/blog/claude-for-chrome, published 2025-08-25, updated 2025-11-24 and 2025-12-18]; [VERIFIED: https://www.anthropic.com/research/prompt-injection-defenses, published 2025-11-24]; [VERIFIED: https://claude.com/blog/claude-in-chrome-generally-available, published 2026-08-26] ⚠ (model names and rates will change with the next release).

- The same model (Opus 4.5) appears at roughly 1–8% in November 2025 and 17.6% in August 2026 because the **evaluation got harder**, not because the model got worse. Anthropic retired its earlier evaluation as "saturated" [VERIFIED: https://claude.com/blog/claude-in-chrome-generally-available, published 2026-08-26]. This is the clearest illustration in the brief of why vendor ASRs cannot be compared across posts.
- Anthropic's stated caveats: a 1% ASR "still represents meaningful risk" and no browser agent is "immune to prompt injection" [VERIFIED: https://www.anthropic.com/research/prompt-injection-defenses, published 2025-11-24].
- Defenses described: RL training on simulated web content with embedded injections; classifiers scanning all untrusted content entering context (hidden text, manipulated images, deceptive UI); continuous internal red-teaming plus external arena challenges [VERIFIED: same]. Product mitigations in Chrome: site-level permissions, confirmations before high-risk actions (publishing, purchasing, sharing personal data), and blocked site categories (financial services, adult, pirated content) [VERIFIED: https://claude.com/blog/claude-for-chrome, published 2025-08-25].
- OpenAI (22 December 2025) describes hardening ChatGPT Atlas's agent mode with an adversarially trained model and an automated RL-based red-teaming attacker that found a new class of attacks, and frames prompt injection as a long-term challenge it expects to work on for years [WIDELY REPORTED: https://openai.com/index/hardening-atlas-against-prompt-injection/, 2025] — the English page returned 403 in this session; no numbers were verified.

**Durable vs volatile.** Durable: layered model training + input classifiers + action confirmation is the shared vendor pattern. Volatile: every number and model name.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A model's injection robustness is an input to how much autonomy you grant, measured in *your* harness against *your* tools. It does not remove the need for the structural controls in 2.5–2.7 and Part 4.

### 2.5 The Dual LLM pattern

- Willison's **Dual LLM pattern** (25 April 2023): a **privileged LLM** takes instructions only from trusted sources and can call tools; a **quarantined LLM** processes untrusted content and has no tools; a non-LLM **controller** runs both, stores quarantined outputs in variables (`$VAR1`, `$VAR2`) and lets the privileged LLM manipulate only the variable names, never the content [VERIFIED: https://simonwillison.net/2023/Apr/25/dual-llm-pattern/, published 2023-04-25]. **[old evidence]** — a design proposal, no measurement.
- His own caveats: it is "pretty bad" for complexity and user experience; future features can accidentally leak untrusted text into the privileged context; social engineering of the user remains; quarantined output must be treated as "potentially radioactive" and never fed back to the privileged LLM [VERIFIED: same].
- A 2025 update notes that the CaMeL paper found a flaw in the proposal and introduced a more complete system [VERIFIED: same].

### 2.6 CaMeL: capabilities and information flow (measured)

- **CaMeL** (Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis, Tramèr; Google DeepMind and ETH Zurich), "Defeating Prompt Injections by Design" [VERIFIED: https://arxiv.org/abs/2503.18813, v1 2025-03-24, v2 2025-06-24]. Type: arXiv preprint with released code (github.com/google-research/camel-prompt-injection).
- Mechanism: a **privileged LLM** sees only the user's query and writes a Python-like program; a **quarantined LLM** with no tools parses untrusted data into a fixed schema; a custom **interpreter** runs the program, tracks a data-flow graph, attaches **capabilities** (provenance and allowed readers) to every value, and checks **security policies** (Python functions returning Allowed/Denied) before each tool call [VERIFIED: https://arxiv.org/html/2503.18813v2, 2025-06-24].
- Measured on AgentDojo: **77% of tasks solved "with provable security"** vs **84% undefended** [VERIFIED: https://arxiv.org/abs/2503.18813, 2025-06-24]. Without any policies, CaMeL cut successful attacks for every model tested (Gemini 2.5 Pro from 300 to 0); against baselines with Claude 3.5 Sonnet over 949 attacks, CaMeL had **0** successful attacks versus 8 for the tool filter [VERIFIED: https://arxiv.org/html/2503.18813v2, 2025-06-24].
- Cost: median task uses about **2.82×** input tokens and **2.73×** output tokens vs native tool calling — the highest of the defenses analysed; a cheaper quarantined model cost ~1% utility for an estimated 12% cost saving [VERIFIED: same].
- Stated limits: vulnerable to **side channels** (partly mitigated by a STRICT mode); "cannot defend against text-to-text attacks" that do not change data flow, such as injection-induced phishing text; users must write and maintain policies; restrictive policies trigger approvals that may cause **user fatigue**; "prompt injection attacks are not fully solved"; return-oriented-programming-style attacks may be possible [VERIFIED: same]. Travel-suite utility is weak, attributed to poorly documented APIs [VERIFIED: same].

**Durable vs volatile.** Durable: separating control flow (from trusted input) from data flow (from untrusted input), with provenance labels checked by deterministic code at the tool boundary. Volatile: the specific interpreter, models and AgentDojo version.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] CaMeL is the strongest measured evidence that a *system-level* defense can give guarantees a model cannot. It is a research prototype, not a product: the price is a ~2.8× token bill, a policy-authoring burden, and loss of tasks whose plan depends on reading the data. Its ideas (provenance tags, a policy check at every tool call) are adoptable without adopting its interpreter.

### 2.7 Design patterns for securing agents (proposal, unmeasured)

- Beurer-Kellner, Buesser, Creţu, Debenedetti, Dobos, Fabian, Fischer, Froelicher, Grosse, Naeff, Ozoani, Paverd, Tramèr, Volhejn (IBM, Invariant Labs, ETH Zurich, Google, Microsoft and others), "Design Patterns for Securing LLM Agents against Prompt Injections" [VERIFIED: https://arxiv.org/abs/2506.08837, v1 2025-06-10, v3 2025-06-27]. Type: arXiv preprint.
- Guiding principle: once an agent has ingested untrusted input, "it must be constrained so that it is impossible for that input to trigger any consequential actions" [VERIFIED: https://arxiv.org/html/2506.08837v3, 2025-06-27].
- **No empirical evaluation**: the case studies (OS assistant, SQL agent, email/calendar assistant, customer-service bot, booking assistant, product recommender, resume screener, medication leaflet bot, medical-diagnosis intermediary, software-engineering agent) are qualitative threat-model analyses; the patterns are "intentionally simple, making them easier to analyze and reason about" [VERIFIED: same]. Only the first 100,000 characters were read; an appendix with measurements cannot be ruled out ⚠.

| Pattern | Mechanism | Residual risk the authors state |
| --- | --- | --- |
| Action-selector | LLM maps a request to one of a fixed set of actions; tool output never returns to the LLM | Utility limited to predefined actions |
| Plan-then-execute | Fix the action list before reading untrusted data | Injected data can still change *arguments* |
| LLM map-reduce | Isolated LLM per untrusted item; reducer sees only constrained output | Each mapper can be injected; reducer must not be an LLM or must get Booleans/numbers |
| Dual LLM | Privileged LLM never sees untrusted data; quarantined LLM has no tools; values by reference | Quarantined LLM can still produce attacker-controlled output |
| Code-then-execute | LLM writes a program that calls tools and quarantined LLMs (CaMeL-style) | Injected content can still set parameters (e.g. an email body) |
| Context-minimization | Remove the user's prompt from context once the action is chosen | Retrieval can still be manipulated; utility loss |

[VERIFIED: https://arxiv.org/html/2506.08837v3, 2025-06-27]

**Durable vs volatile.** Durable: all six patterns are model-independent and trade utility for structural security. Volatile: nothing much; this is the most durable source in the brief.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] These patterns map directly onto the book's "bound the component" frame: each one restricts *where* the model may decide. Present them in the book as a menu ordered by how much the model is allowed to decide, and be honest that only the code-then-execute family has a measured implementation (CaMeL).

### 2.8 Summary: evidence grade of each defense

| Defense | Kind | Evidence | Best measured result |
| --- | --- | --- | --- |
| Delimiters / spotlighting | Prompt-level | Preprint + benchmark | <2% (static, 2024); 41.7% on AgentDojo GPT-4o |
| Prompt sandwiching | Prompt-level | Benchmark | 27.8% on AgentDojo GPT-4o |
| Injection detector (classifier) | Filter | Benchmark; vendor posts | 8.0% on AgentDojo at large utility cost |
| Adversarial training + classifiers | Model-level | Vendor self-reports only | 0–17.6% depending on model and evaluation (Anthropic) |
| Tool filter / plan-then-execute | Structural | Benchmark | 6.8% on AgentDojo GPT-4o |
| CaMeL (capabilities + policies) | Structural | Preprint + code | 0 successful attacks; 77% vs 84% utility |
| Dual LLM, map-reduce, action-selector, context-minimization | Structural | Proposals | None measured |
| Rule of Two / trifecta removal | Design rule | Incident catalogue | None measured |
| Human confirmation | Oversight | Vendor data on approval rates (Part 5) | Users approve ~93% of prompts |

[ASSUMPTION/JUDGEMENT] The table compiles 2.1–2.7 and 5.3; the numbers are not comparable across rows.

---

## PART 3: Documented exploits

### 3.1 EchoLeak (CVE-2025-32711), Microsoft 365 Copilot

- NVD record: published **11 June 2025**; description "AI command injection in M365 Copilot allows an unauthorized attacker to disclose information over a network"; CWE-74 (injection); Microsoft (CNA) score **CVSS 3.1 9.3 Critical** (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N); NVD's own score **7.5 High** (scope unchanged, no integrity impact); CISA SSVC: exploitation "none", automatable "yes" [VERIFIED: https://nvd.nist.gov/vuln/detail/CVE-2025-32711 via services.nvd.nist.gov API, published 2025-06-11].
- Discovered by Aim Security (Aim Labs) and disclosed in June 2025 as a zero-click exploit triggered by a single crafted email; Microsoft fixed it server-side with no customer action required [WIDELY REPORTED: https://www.techrepublic.com/article/news-microsoft-365-copilot-flaw-echoleak/, 2025]. Aim's original post returned 403.
- Attack chain per an arXiv case study (Reddy and Gujral): (1) evade Microsoft's **XPIA** (cross-prompt injection attempt) classifier; (2) bypass link redaction with **reference-style Markdown**; (3) exploit **auto-fetched images**; (4) abuse a **Microsoft Teams proxy allowed by the content security policy** — together a privilege escalation across LLM trust boundaries without user interaction [VERIFIED: https://arxiv.org/abs/2509.10540, published 2025-09-06]. Type: arXiv case study by authors not affiliated with Aim or Microsoft as far as the page shows ⚠.
- Proposed mitigations in that paper: prompt partitioning, stronger input/output filtering, provenance-based access control, strict CSP [VERIFIED: same].
- No in-the-wild exploitation is recorded (CISA SSVC "none") [VERIFIED: NVD record above]. One secondary source's claim of a "May 2026" patch is inconsistent with the June 2025 record and should be ignored [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] EchoLeak is the canonical trifecta case: private data (the user's M365 graph), untrusted content (inbound email retrieved by RAG), and an exfiltration channel (an auto-loaded image URL through an allow-listed domain). The input classifier was bypassed; the **egress** controls (link redaction, CSP) were what had to be fixed. Rendering is an egress channel.

### 3.2 GitHub MCP "toxic agent flow" (Invariant Labs)

- Invariant Labs (26 May 2025): a prompt injection in an **issue on a public repository** causes an agent, asked to review open issues, to pull data from the user's **private repositories** and leak it in a **pull request on the public repository**. Demonstrated with **Claude 4 Opus in Claude Desktop** with the official GitHub MCP server; the authors say it is not model-specific and requires no compromised tool [VERIFIED: https://invariantlabs.ai/blog/mcp-github-vulnerability, published 2025-05-26]. Type: security-vendor research post (Invariant sells guardrail products — note the commercial interest).
- They call it "a fundamental architectural issue that must be addressed at the agent system level", not a GitHub server bug, and note that many users choose "Always Allow" confirmations. Mitigations: per-session least privilege (e.g. restrict a session to one repository) and runtime monitoring [VERIFIED: same].
- GitHub's response (10 December 2025): a **lockdown mode** (`X-MCP-Lockdown` header on the remote server) that surfaces public-repository content only from users with **push access**, and default **content sanitization** of issue and PR text (invisible Unicode, unsafe HTML, hidden text in code fences) [VERIFIED: https://github.blog/changelog/2025-12-10-the-github-mcp-server-adds-support-for-tool-specific-configuration-and-more, published 2025-12-10] ⚠. Third-party guides call lockdown best-effort, and a 2026 CVE (CVE-2026-48529) concerns cross-user confusion in the lockdown implementation in HTTP mode [WIDELY REPORTED: https://cvefeed.io/vuln/detail/CVE-2026-48529, 2026] — not verified against NVD.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A broadly scoped token (all of the user's repositories) plus a public input surface makes the confused deputy inevitable. The fix pattern is **provenance filtering at the tool** (only trusted authors' content enters context) and **session-scoped credentials**, not better prompting.

### 3.3 Slack AI exfiltration (PromptArmor)

- PromptArmor showed that an attacker who posts an instruction in a **public channel** (even one only they belong to) can make Slack AI, when another user asks about an API key in **their private channel**, render a "click here to reauthenticate" link with the key as a URL parameter; the attacker's message is not cited as a source. A second chain rendered phishing links [VERIFIED: https://www.promptarmor.com/resources/data-exfiltration-from-slack-ai-via-indirect-prompt-injection, n.d.; disclosure 2024-08-14]. **[old evidence]**
- Slack's initial reply (19 August 2024) called public-channel search results "intended behavior" [VERIFIED: same]. On 14 August 2024 Slack AI began ingesting uploaded files and connected sources (e.g. Google Drive), widening the surface so an attacker might not need to be in Slack at all; PromptArmor did not test that path [VERIFIED: same].

### 3.4 MCP tool poisoning, shadowing and rug pulls (Invariant Labs)

- **Tool poisoning** (1 April 2025): malicious instructions in an MCP tool's **description**, visible to the model but not shown in full to the user. Demonstrated in **Cursor**: an innocent `add` tool instructed the model to read `~/.cursor/mcp.json` and `~/.ssh/id_rsa` and pass them in a hidden parameter; Cursor's confirmation dialog did not show the full input [VERIFIED: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks, published 2025-04-01].
- **Shadowing**: one server's tool description changes how the agent uses *another* server's trusted tool (e.g. redirecting all `send_email` calls to the attacker), without the attacker's tool ever being called [VERIFIED: same].
- **Rug pull**: a server changes a tool description after the user approved it [VERIFIED: same].
- Proposed mitigations: show full tool descriptions; **pin** server and tool versions by hash; cross-server data-flow boundaries [VERIFIED: same]. These are proposals; no measured effect.
- The MCP spec's own security guidance covers a different class — authorization flaws: **confused-deputy** attacks on MCP proxy servers with static client IDs (mitigation: MCP proxies MUST implement per-client consent), **token passthrough** (MCP servers MUST NOT accept tokens not issued for them), SSRF during OAuth discovery, state-handle hijacking, and local server compromise (one-click local server installs MUST show the exact command and require approval) [VERIFIED: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices, n.d., accessed 2026-10, for protocol version 2026-07-28] ⚠.

**Durable vs volatile.** Durable: tool metadata is code-equivalent input and is part of the supply chain (OWASP ASI04). Volatile: specific clients' dialog behavior; MCP spec revisions.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat tool registration as dependency management: an allow-list of servers, pinned descriptions, diff-on-change, review before re-approval. A gateway between agents and tools is the natural place to enforce this (Part 6).

---

## PART 4: Identity, delegated authorization and least privilege

### 4.1 OAuth 2.1 and token exchange

- **OAuth 2.1** is still an **Internet-Draft**, not an RFC: draft-ietf-oauth-v2-1-16, 3 September 2026, expiring 7 March 2027. It consolidates RFC 6749/6750 with RFC 8252 and RFC 9700, **requires PKCE**, removes the implicit grant and the password grant, and requires exact redirect-URI matching [VERIFIED: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/, published 2026-09-03] ⚠. Book text should say "the OAuth 2.1 draft".
- **RFC 8693 OAuth 2.0 Token Exchange** (January 2020, Standards Track) distinguishes **impersonation** ("A is given all the rights that B has") from **delegation** (A "still has its own identity separate from B"). Requests carry a `subject_token` and optionally an `actor_token`; issued tokens can carry an `act` claim, nested to record a delegation chain ("The outermost act claim represents the current actor"), and a `may_act` claim stating who is allowed to act for the subject. Only the top-level claims and the current actor should drive access decisions; nested actors are informational [VERIFIED: https://www.rfc-editor.org/rfc/rfc8693.html, published 2020-01].
- **On-behalf-of** is the general name for a service exchanging a user's token for a downstream token in that user's context; Microsoft Entra exposes it as "delegated access" for agent identities (4.3) [VERIFIED: https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id, updated 2026-06-15].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Prefer **delegation** (`act` claim: agent X acting for user U) over impersonation (agent holds U's token). Delegation lets the downstream system and the audit log see that an agent acted, apply agent-specific policy, and revoke the agent without revoking the user.

### 4.2 MCP authorization (protocol version 2026-07-28) ⚠

- Authorization is **optional** in MCP; HTTP transports SHOULD follow the spec, stdio transports SHOULD NOT and take credentials from the environment [VERIFIED: https://modelcontextprotocol.io/specification/latest/basic/authorization, version 2026-07-28].
- A protected MCP server is an **OAuth 2.1 resource server**; MCP servers MUST implement **Protected Resource Metadata (RFC 9728)**; clients MUST send **Resource Indicators (RFC 8707)** naming the MCP server; servers MUST validate that tokens were issued for them as audience, and "MUST NOT accept or transit any other tokens" [VERIFIED: same].
- Client registration: **Client ID Metadata Documents** SHOULD be supported; **Dynamic Client Registration is now deprecated**, retained for backwards compatibility [VERIFIED: same]. Clients MUST validate the `iss` parameter (RFC 9207) to stop mix-up attacks [VERIFIED: same].
- Least privilege is built in: servers SHOULD send the scopes needed for an operation in `WWW-Authenticate`; clients start minimal and **step up** on `insufficient_scope` [VERIFIED: same]. The security guide lists "publishing all possible scopes" and wildcard scopes as common mistakes [VERIFIED: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices, accessed 2026-10].

**Durable vs volatile.** Durable: audience-bound tokens, no passthrough, step-up scopes. Volatile: the MCP revision (2026-07-28), the CIMD draft (-00), deprecation of DCR.

### 4.3 Workload and agent identity

- **SPIFFE** issues workloads short-lived cryptographic identity documents (**SVIDs**, X.509 or JWT) through a Workload API; **SPIRE** is its reference implementation with attestation-based issuance and federation [VERIFIED: https://spiffe.io/docs/latest/spiffe-about/overview/, n.d., accessed 2026-10]. Its CNCF graduated status was not confirmed on the page fetched [ASSUMPTION/JUDGEMENT: graduated in 2022].
- IETF: the individual draft **draft-klrc-aiagent-auth** ("AI Agent Authentication and Authorization"; Kasselman, Lombardo, Rosomakho, Campbell, Steele, Parecki) proposed best practices built on the **WIMSE** architecture and the OAuth 2.0 family, with no new protocols, and was **replaced by draft-ietf-wimse-aims-00**, "AI Identity Management System", a WIMSE working-group document dated **15 September 2026**, intended Informational, expiring 19 March 2027 [VERIFIED: https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/ and https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/, published 2026-09-15] ⚠.
- Other individual drafts (e.g. an "On-Behalf-Of User Authorization for AI Agents" OAuth extension, transaction tokens for agents) exist with no working-group standing as of mid-2026 [WIDELY REPORTED: https://labs.cloudsecurityalliance.org/research/csa-research-note-ietf-agent-identity-standards-20260902-csa/, 2026] ⚠.
- **NIST CAISI AI Agent Standards Initiative** (17 February 2026): three pillars (industry-led standards, community open-source protocols, research on agent security and identity); an RFI on AI agent security (due 9 March 2026); an NCCoE concept paper "Accelerating the Adoption of Software and AI Agent Identity and Authorization" (comments due 2 April 2026). As of the page's 14 August 2026 update, no outputs were listed [VERIFIED: https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative, updated 2026-08-14; https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure, published 2026-02-17].
- **Microsoft Entra Agent ID**: a distinct identity type for agents, separate from service principals and user accounts, designed for ephemerality ("created and destroyed thousands of times per day"); supports **autonomous access** (rights granted to the agent) and **delegated access** (acting for a user, who controls what is delegated); an optional one-to-one **agent user account** when a system requires a user identity; Copilot Studio agents get an agent identity with the creating user recorded as **sponsor**, and agent authentications are logged as AI agents [VERIFIED: https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id, created 2025-11-06, updated 2026-06-15] ⚠ (licensing via Microsoft Agent 365 is product-specific).

| Question | Human user | Workload | Agent (emerging practice) |
| --- | --- | --- | --- |
| Identity | Account + MFA | SPIFFE ID / service principal | Agent identity, distinct type, with a sponsor/owner |
| Lifetime | Years | Months | Minutes to months |
| Acting for a user | — | Rare | Common: delegation (`act`) preferred over impersonation |
| Audit | "U did X" | "Service S did X" | "Agent A did X for U, under policy P" |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of 4.1–4.3.

**Durable vs volatile.** Durable: agents need their own identity, short-lived credentials, and an explicit delegation link to a human. Volatile: every draft name, product name and NIST deliverable.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Give each agent (or each agent run, for high-risk work) its own identity; issue tokens per task, audience-bound, short-lived, down-scoped by token exchange; record the human principal in the token; never let the model see raw long-lived credentials (keep them in a broker or gateway the model calls). This turns LLM06 "excessive permissions" into an IAM question with existing tools.

### 4.4 Least privilege and data exposure

- OWASP LLM06 prescribes executing extensions in the user's context with minimum privileges and minimizing extensions, functions and permissions [VERIFIED: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/, accessed 2026-10].
- Anthropic's Claude Code sandbox combines **filesystem isolation** (writes limited to the working directory) and **network isolation** (egress only through a proxy with domain restrictions), arguing each covers the other's gap: without network isolation a compromised agent can exfiltrate SSH keys; without filesystem isolation it can escape the sandbox and reach the network [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20]. Type: vendor engineering post.
- In the GitHub MCP case, Invariant's recommended control was a per-session restriction to one repository [VERIFIED: https://invariantlabs.ai/blog/mcp-github-vulnerability, published 2025-05-26].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Least privilege for agents has three axes: which **tools** are reachable (tool filtering), which **data** a token can reach (scope and audience), and which **egress** destinations exist (network policy). The third is the one most often missing and the one that breaks the trifecta.

---

## PART 5: Human oversight

### 5.1 EU AI Act Article 14 (text) and related obligations

- **Article 14(1)**: high-risk AI systems "shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use" [VERIFIED: http://publications.europa.eu/resource/celex/32024R1689, Regulation (EU) 2024/1689, published 2024-07-12].
- **14(3)**: oversight measures "shall be commensurate with the risks, level of autonomy and context of use", built in by the provider and/or implemented by the deployer [VERIFIED: same].
- **14(4)**: overseers must be enabled to (a) understand capacities and limitations and monitor operation; (b) "remain aware of the possible tendency of automatically relying or over-relying on the output ... (automation bias)"; (c) correctly interpret output; (d) decide not to use, or "disregard, override or reverse" the output; (e) "intervene ... or interrupt the system through a 'stop' button or a similar procedure that allows the system to come to a halt in a safe state" [VERIFIED: same].
- **14(5)**: for remote biometric identification (Annex III point 1(a)), no action on an identification unless separately verified by **at least two natural persons** (with law-enforcement/migration exceptions) [VERIFIED: same].
- **Article 26(2)**: deployers "shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support" [VERIFIED: same].
- **Article 12**: high-risk systems "shall technically allow for the automatic recording of events (logs) over the lifetime of the system"; **Article 26(6)**: deployers keep those logs for "at least six months" unless other law says otherwise [VERIFIED: same].
- The Digital Omnibus on AI does **not** amend Article 14 (no "human oversight" text appears in the amending regulation) [VERIFIED: http://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24].

### 5.2 Application dates, as amended by the Digital Omnibus ⚠

- Original Article 113: general application **2 August 2026**; prohibitions and AI literacy (Chapters I–II) from 2 February 2025; GPAI and governance from 2 August 2025; Article 6(1) (Annex I product-embedded high-risk) from 2 August 2027 [VERIFIED: http://publications.europa.eu/resource/celex/32024R1689, published 2024-07-12].
- **Regulation (EU) 2026/1744** ("Digital Omnibus on AI"), adopted **8 July 2026**, published in the Official Journal **24 July 2026**, in force on the third day after publication (27 July 2026). It moves the high-risk requirements of Chapter III Sections 1–3 — which include Article 14 — to **2 December 2027** for **Annex III** (standalone) high-risk systems and **2 August 2028** for **Annex I** (product-embedded) systems, citing delayed standards and authorities [VERIFIED: http://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24].
- It also replaces Article 4 (AI literacy), softening the obligation into one to "take measures to support" literacy [VERIFIED: same], and sets 2 August 2030 for public-authority high-risk systems placed on the market before the application date [VERIFIED: same].
- Article 50 transparency duties and AI Office GPAI enforcement were reported as applying from 2 August 2026 as scheduled [WIDELY REPORTED: https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo, 2026] — not checked clause by clause.

**Durable vs volatile.** Durable: the content of Article 14 — understand, monitor, resist automation bias, override, stop. Volatile: dates; the omnibus shows they move.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Article 14 is written as design requirements on the system, not only on staff: an override path, a safe-state stop, interpretable output, and interface support against automation bias. For an agent in an Annex III domain (employment, credit, essential public services — the book's HR, finance and public-benefits examples), these are engineering requirements due by 2 December 2027. Article 12/26 logging is an audit-trail requirement the agent's trace store must meet.

### 5.3 Approval fatigue: what vendors have measured

- Anthropic: constant prompts cause "**approval fatigue**"; in internal usage, sandboxing reduced permission prompts by **84%** (measurement method not described) [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20].
- Anthropic's auto-mode post (25 March 2026): users **accept 93%** of manual permission prompts [VERIFIED: https://www.anthropic.com/engineering/claude-code-auto-mode, published 2026-03-25]. Later coverage of an August 2026 announcement cites 97% [WIDELY REPORTED: https://thenewstack.io/claude-code-auto-mode/, 2026] — not verified against a primary source.
- Auto mode replaces prompts with a **transcript classifier** (Sonnet 4.6) that sees only user messages and tool calls ("reasoning-blind": assistant text and tool outputs stripped), in two stages, plus a server-side injection probe on tool outputs. Measured: false-positive rate **0.4%** on 10,000 real internal actions; false-negative rate **17%** on **52** real overeager actions; **5.7%** on 1,000 synthetic exfiltration attempts. The authors: "The 17% false-negative rate on real overeager actions is the honest number"; auto mode is "not a drop-in replacement for careful human review on high-stakes infrastructure"; after 3 consecutive or 20 total denials the session escalates to the human [VERIFIED: same]. Type: vendor engineering post; small n for the key metric.
- A secondary claim that manual approval caught only ~14% of planted dangerous commands in Anthropic's testing [WIDELY REPORTED: search digest, 2026] could not be traced to the primary post ⚠ — do not use without verification.
- Auto mode became the default for new Claude Code sessions on several plans from 14 August 2026 [WIDELY REPORTED: https://cryptobriefing.com/anthropic-claude-code-auto-mode-default/, 2026] ⚠.
- Invariant's GitHub MCP write-up notes users commonly choose "Always Allow" [VERIFIED: https://invariantlabs.ai/blog/mcp-github-vulnerability, published 2025-05-26]; CaMeL's authors warn restrictive policies may cause desensitization through approval requests [VERIFIED: https://arxiv.org/html/2503.18813v2, 2025-06-24]; Meta notes a compliant Rule-of-Two design still fails if a user blindly confirms [VERIFIED: https://ai.meta.com/blog/practical-ai-agent-security/, published 2025-10-31].

### 5.4 Automation bias and habituation: the human-factors evidence

- Parasuraman & Manzey, *Human Factors* 52(3), 2010 (peer-reviewed review): automation **complacency** arises under multi-task load and is found in naive and expert participants and "cannot be overcome with simple practice"; automation **bias** produces omission and commission errors with imperfect aids, occurs in naive and expert participants, "cannot be prevented by training or instructions", and affects teams as well as individuals [VERIFIED: https://pubmed.ncbi.nlm.nih.gov/21077562/ via NCBI E-utilities, published 2010-06]. **[old evidence]** — but foundational and not model-dependent.
- Goddard, Roudsari & Wyatt, *JAMIA* 19(1), 2012 (systematic review, 74 of 13,821 papers): automation bias is mediated by experience, trust and confidence, workload, task complexity and time pressure; **mitigators** include training, **emphasizing user accountability**, the on-screen position of advice, updated confidence levels, and giving **information rather than recommendations** [VERIFIED: https://pubmed.ncbi.nlm.nih.gov/21685142/ via NCBI E-utilities, published 2011-06-16].
- Bansal et al., CHI 2021: with AI accuracy comparable to humans, AI explanations made people more likely to accept the AI's recommendation "regardless of its correctness" and did not improve complementary team performance [VERIFIED: https://arxiv.org/abs/2006.14779, v3 2021-01-12].
- Perry, Srivastava, Kumar & Boneh, CCS 2023: participants with an AI code assistant (codex-davinci-002) "wrote significantly less secure code" and were **more likely to believe it was secure**; those who trusted the AI less and engaged more wrote fewer vulnerabilities [VERIFIED: https://arxiv.org/abs/2211.03622, CCS '23, revised 2023-12-18]. **[old evidence]** — older model; the overconfidence finding is the durable part.
- Security-warning **habituation**: an fMRI and mouse-tracking study (Anderson, Vance, Kirwan et al., CHI 2015) found warnings that change appearance (polymorphic) resist habituation better than static ones; a longitudinal MIS Quarterly 2018 study found attention partially recovers between workdays [WIDELY REPORTED: https://misq.org/tuning-out-security-warnings-a-longitudinal-examination-of-habituation-through-fmri-eye-tracking-and-field-experiments.html, 2018] — abstracts not fetched.

**Durable vs volatile.** Durable: humans rubber-stamp frequent, mostly-benign approvals; explanations can increase over-reliance; training alone is weak. Volatile: the specific approval-rate numbers, which are one vendor's internal telemetry.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A human approval gate is a control only if approvals are **rare, consequential and informative**. Design implications: (1) remove most prompts structurally (sandbox, scoped tools) so the remaining ones matter; (2) show the concrete effect (diff, recipient, amount), not the model's justification; (3) vary or escalate presentation for high-risk actions; (4) measure the approval rate and time-to-approve as health metrics — a 93%+ approval rate means the gate is mostly ritual; (5) record approver identity, what they were shown, and the decision in the audit trail (Art. 14(4)(d)/(e), Art. 12).

---

## PART 6: Policy enforcement points for tool calls and audit trails

### 6.1 OPA and Cedar

- **Open Policy Agent**: a general-purpose policy engine, a **graduated CNCF project**, that decouples decision from enforcement — software sends JSON input and receives a decision computed from **Rego** policies and data; decisions can be arbitrary structured data, not only allow/deny [VERIFIED: https://www.openpolicyagent.org/docs/latest/, n.d., accessed 2026-10].
- **Cedar** semantics: **default deny** ("no request is authorized ... unless there is a specific permit policy"), **forbid overrides permit**, and policies that error are skipped (reported in diagnostics) [VERIFIED: https://docs.cedarpolicy.com/auth/authorization.html, n.d., accessed 2026-10].
- Cedar paper (Cutler et al., AWS): RBAC/ABAC/ReBAC expressiveness, an optional-typing validator, a **sound and complete logical encoding** for analysis (e.g. prove a refactor does not change permissions), properties proved in **Lean**, implemented in Rust; the authors report Cedar is "substantially" faster than OpenFGA and Rego in their benchmarks [VERIFIED: https://arxiv.org/abs/2403.04651, published 2024-03-07]. arXiv extended version; the conference venue (generally reported as OOPSLA 2024) was not confirmed [ASSUMPTION/JUDGEMENT]. The performance comparison is authored by Cedar's builders.

### 6.2 Policy at the tool gateway: a shipped example ⚠

- **Policy in Amazon Bedrock AgentCore** intercepts all agent traffic through AgentCore Gateway and evaluates each request against Cedar policies "before allowing tool access", enforced "at the boundary outside of agent's code"; supports natural-language authoring translated to Cedar and checked with automated reasoning for over-permissive, over-restrictive or unsatisfiable policies; logs every decision to CloudWatch [VERIFIED: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html, n.d., accessed 2026-10]. Generally available **3 March 2026** in 13 regions [VERIFIED: https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/, published 2026-03-03].
- The docs also describe **temporal (session-aware) policies** — e.g. require an approval before a transfer, cap the number of times an action runs, keep a running budget — and policy conditions on signals from Guardrails such as a prompt-attack score, authored in an open-source language called **Dogwood** [VERIFIED: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html, accessed 2026-10] ⚠ (Dogwood was not independently researched).
- [ASSUMPTION/JUDGEMENT] This is vendor documentation, not evidence of effectiveness. No measured reduction in attack success for gateway policy was found. Natural-language-to-policy translation is itself a model output and needs review.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The policy enforcement point (PEP) for an agent is the **tool-call boundary**: a gateway or interpreter that sees principal (agent + delegating user), action (tool), resource and arguments, and asks a policy decision point (OPA, Cedar) before execution. This is the deterministic analogue of CaMeL's per-call policy check and the concrete form of OWASP LLM06's "complete mediation". Session-aware policies (counts, budgets, "approval seen") are what distinguish agent policy from ordinary API authorization. Keep the PEP outside the agent process so a manipulated model cannot skip it.

### 6.3 Audit trails

- **OpenTelemetry GenAI semantic conventions** now live in a separate repository (open-telemetry/semantic-conventions-genai) and cover client spans, metrics, events, MCP, A2A and provider-specific conventions; agent spans (`invoke_agent`, `execute_tool`) are **status: Development** [VERIFIED: https://github.com/open-telemetry/semantic-conventions-genai, accessed 2026-10] ⚠.
- The MCP security guide lists audit damage as a reason token passthrough is forbidden: the MCP server cannot tell clients apart, and downstream logs show the wrong identity [VERIFIED: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices, accessed 2026-10].
- EU AI Act Articles 12 and 26(6): automatic event logging over the system lifetime and deployer retention of at least six months [VERIFIED: 5.1].
- RFC 8693 nested `act` claims record the delegation chain in the token itself [VERIFIED: 4.1].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] An agent audit record needs more than an API log: agent identity and version, delegating human, the policy decision and policy version, the provenance of the arguments (which inputs were untrusted), any approval (who, what they were shown, when), and the outcome. Traces built on draft OTel conventions should be versioned, because attribute names will change.

### 6.4 NIST frameworks ⚠

- **AI RMF 1.0** released 26 January 2023, functions Govern, Map, Measure, Manage; NIST says it "is being revised as part of the White House AI Action Plan" [VERIFIED: https://www.nist.gov/itl/ai-risk-management-framework, accessed 2026-10]. **[old evidence]** for the 1.0 text.
- **NIST AI 600-1** (Generative AI Profile), 26 July 2024, a cross-sectoral profile of AI RMF 1.0, voluntary, issued under EO 14110 [VERIFIED: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence, published 2024-07-26]. Its 12 risks: CBRN information; confabulation; dangerous, violent or hateful content; data privacy; environmental impacts; harmful bias or homogenization; **human-AI configuration** (explicitly including automation bias and over-reliance); information integrity; **information security** (including indirect prompt injection); intellectual property; obscene/degrading/abusive content; **value chain and component integration** [VERIFIED: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, published 2024-07-26]. **[old evidence]**; EO 14110 was rescinded in January 2025 [ASSUMPTION/JUDGEMENT], so the document's policy footing has changed though the text stands.
- NIST's SP 800-53 control-overlay project for AI (**COSAiS**) planned overlays for "Single Agent" and "Multi-Agent" systems; concept paper 14 August 2025; first discussion draft (predictive AI) 8 January 2026; no agent overlay draft is listed. On **20 October 2026** the project was renamed **COSIS — "Control Overlays for Super Intelligence Systems"** — per a 29 September 2026 Executive Order, with "SI" replacing "AI" in titles and earlier documents left unaltered [VERIFIED: https://csrc.nist.gov/projects/cosais, accessed 2026-10-28] ⚠⚠ (very recent; terminology may cause citation confusion).

**Durable vs volatile.** Durable: NIST's risk vocabulary (human-AI configuration, value chain) and the Govern/Map/Measure/Manage cycle. Volatile: everything about NIST's agent-specific deliverables, which as of October 2026 are still RFIs, concept papers and planned overlays.

---

## Key numbers

| Number | What it measured | Source | Date |
| --- | --- | --- | --- |
| 97 tasks / 629 security cases | AgentDojo benchmark size | arXiv 2406.13352 | 2024-11 |
| 47.7% (Table 3) / 57.7% (Table 5) | GPT-4o targeted ASR, no defense, AgentDojo "important message" attack — inconsistent within paper | arXiv 2406.13352v3 | 2024-11 |
| 6.8% (text: 7.5%) | GPT-4o ASR with tool-filter defense, utility 73.1% | same | 2024-11 |
| 8.0% with utility 41.5% | GPT-4o ASR with BERT injection detector | same | 2024-11 |
| ~17% | AgentDojo cases where task tools suffice for the attack (tool filter cannot help) | same | 2024-11 |
| >50% → <2% | Spotlighting ASR, GPT-family, static attacks | arXiv 2403.14720 | 2024-03 |
| >90% for most of 12 | Adaptive-attack ASR vs published defenses | arXiv 2510.09023 | 2025-10 |
| 77% vs 84% | CaMeL task success with provable security vs undefended, AgentDojo | arXiv 2503.18813 | 2025-06 |
| 0 of 949 | Successful attacks on CaMeL (Claude 3.5 Sonnet) vs 8 for tool filter | same | 2025-06 |
| 2.82× / 2.73× | CaMeL median input / output token overhead | same | 2025-06 |
| 23.6% → 11.2% | Claude for Chrome ASR, 123 cases, before/after mitigations (vendor) | claude.com | 2025-08 |
| 1.4% | Opus 4.5 ASR with improved safeguards, Best-of-N 100 attempts (vendor) | anthropic.com | 2025-11 |
| 17.6% → 0% | Opus 4.5 unguarded vs Opus 5 with probes+classifier, harder eval (vendor) | claude.com | 2026-08 |
| 93% | Share of manual permission prompts users accept (vendor telemetry) | anthropic.com | 2026-03 |
| 84% | Reduction in permission prompts from sandboxing, internal use (vendor, method undisclosed) | anthropic.com | 2025-10 |
| 0.4% / 17% / 5.7% | Auto-mode classifier FPR (n=10,000) / FNR on real overeager actions (n=52) / FNR on synthetic exfiltration (n=1,000) | anthropic.com | 2026-03 |
| 9.3 vs 7.5 | EchoLeak CVSS: Microsoft vs NVD | NVD | 2025-06 |
| 74 of 13,821 | Papers in Goddard automation-bias systematic review | JAMIA | 2011 |
| ≥ 6 months | AI Act deployer log retention (Art. 26(6)) | Reg. 2024/1689 | 2024-07 |
| 2 Dec 2027 / 2 Aug 2028 | New application dates for Annex III / Annex I high-risk requirements incl. Art. 14 | Reg. 2026/1744 | 2026-07 |

## Where sources disagree

- **AgentDojo's own numbers.** Table 3 (47.69%) and Table 5 (57.69%) give different no-defense GPT-4o ASRs, and the introduction's "<66% utility / <25% ASR" contradicts both. Cite the table and version.
- **Can training fix automation bias?** Parasuraman & Manzey (2010): it "cannot be prevented by training or instructions". Goddard et al. (2012) list training among mitigators, alongside accountability and interface design. Reconcilable: training helps a little, design and accountability help more [ASSUMPTION/JUDGEMENT].
- **Is prompt injection being solved by models?** Anthropic reports 0% ASR for its 2026 models with probes and classifiers on its current evaluation; Nasr et al. (2025) show most published defenses fall to adaptive attackers; Willison says 95% is a failing grade and nobody can prevent it 100%; Anthropic itself says no browser agent is immune and retired an evaluation as saturated. The positions are compatible only if vendor 0% means "0% against today's test set", not "solved".
- **Are explanations helpful to overseers?** The AI Act (Art. 14(4)(c)) requires that overseers can correctly interpret output; Bansal et al. found explanations increased acceptance regardless of correctness. Interpretation support must not mean persuasive justification [ASSUMPTION/JUDGEMENT].
- **EchoLeak severity.** Microsoft scores 9.3 (scope changed, integrity low); NVD scores 7.5.
- **Is the GitHub MCP exploit a vendor bug?** Invariant: architectural, not fixable server-side. GitHub shipped server-side mitigations (lockdown, sanitization) anyway; these reduce exposure but third parties call them best-effort.
- **Slack AI.** PromptArmor framed the public-channel injection as a vulnerability; Slack's first response called retrieval of public-channel content intended behavior.
- **Human approval as a control.** OWASP LLM06, Meta's Rule of Two and Article 14 all rely on human approval; Anthropic's telemetry (93% acceptance) and the automation-bias literature say frequent approvals are weak controls. Anthropic chose to replace most prompts with a classifier that misses 17% of real overeager actions.

## Open questions / not verifiable

- Independent measurement of prompt-injection success in **production** agents (not benchmarks, not vendor self-reports): none found.
- Whether any shipped product implements CaMeL-style capability tracking end to end: none confirmed [ASSUMPTION/JUDGEMENT: some vendors describe provenance-aware controls, but no internals were verified].
- Measured effectiveness of policy gateways (AgentCore Policy, OPA/Cedar at tool boundaries) against injection: none found. The structural argument is strong; the data is absent.
- The full OWASP Agentic Top 10 text, exact category titles and mitigations (download not read).
- OpenAI Atlas hardening numbers (page blocked); Aim Security's original EchoLeak disclosure timeline (page blocked).
- The source of the "manual approval caught ~14% of dangerous commands" claim attributed to Anthropic.
- Whether NIST will publish agent overlays (now under the COSIS name) or an agent profile of the AI RMF, and when.
- Final shape of IETF agent-identity work: draft-ietf-wimse-aims is -00 and Informational; OAuth 2.1 remains a draft after five years.
- Empirical studies of approval fatigue specific to LLM agents, beyond vendor telemetry: none found; the habituation evidence comes from browser security warnings.
- CVE-2026-48529 (GitHub MCP lockdown) details were not checked against NVD.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz | 2023 | https://arxiv.org/abs/2302.12173 | paper (preprint) |
| The lethal trifecta for AI agents | Simon Willison | 2025 | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | engineering post (blog) |
| The Dual LLM pattern for building AI assistants that can resist prompt injection | Simon Willison | 2023 | https://simonwillison.net/2023/Apr/25/dual-llm-pattern/ | engineering post (blog) |
| Agents Rule of Two: A Practical Approach to AI Agent Security | Meta AI | 2025 | https://ai.meta.com/blog/practical-ai-agent-security/ | engineering post |
| Defeating Prompt Injections by Design (CaMeL) | Debenedetti et al., Google DeepMind / ETH Zurich | 2025 | https://arxiv.org/abs/2503.18813 | paper (preprint) |
| Design Patterns for Securing LLM Agents against Prompt Injections | Beurer-Kellner et al. | 2025 | https://arxiv.org/abs/2506.08837 | paper (preprint) |
| AgentDojo | Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, Tramèr | 2024 | https://arxiv.org/abs/2406.13352 | paper (preprint/benchmark) |
| Defending Against Indirect Prompt Injection Attacks With Spotlighting | Hines et al., Microsoft | 2024 | https://arxiv.org/abs/2403.14720 | paper (preprint) |
| The Attacker Moves Second | Nasr, Carlini, Sitawarin, Tramèr et al. | 2025 | https://arxiv.org/abs/2510.09023 | paper (preprint) |
| Claude for Chrome (launch post) | Anthropic | 2025 | https://claude.com/blog/claude-for-chrome | vendor post |
| Mitigating the risk of prompt injections in browser use | Anthropic | 2025 | https://www.anthropic.com/research/prompt-injection-defenses | engineering post |
| Claude in Chrome is generally available | Anthropic | 2026 | https://claude.com/blog/claude-in-chrome-generally-available | vendor post |
| Continuously hardening ChatGPT Atlas against prompt injection | OpenAI | 2025 | https://openai.com/index/hardening-atlas-against-prompt-injection/ | engineering post (not read) |
| Beyond permission prompts: making Claude Code more secure and autonomous | Anthropic | 2025 | https://www.anthropic.com/engineering/claude-code-sandboxing | engineering post |
| How we built Claude Code auto mode | Anthropic (J. Hughes) | 2026 | https://www.anthropic.com/engineering/claude-code-auto-mode | engineering post |
| CVE-2025-32711 | NIST NVD / Microsoft | 2025 | https://nvd.nist.gov/vuln/detail/CVE-2025-32711 | incident report |
| EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System | Reddy, Gujral | 2025 | https://arxiv.org/abs/2509.10540 | paper (case study) |
| First Known Zero-Click AI Exploit: Microsoft 365 Copilot's EchoLeak Flaw | TechRepublic | 2025 | https://www.techrepublic.com/article/news-microsoft-365-copilot-flaw-echoleak/ | press |
| GitHub MCP Exploited: Accessing private repositories via MCP | Invariant Labs | 2025 | https://invariantlabs.ai/blog/mcp-github-vulnerability | incident report (vendor) |
| MCP Security Notification: Tool Poisoning Attacks | Invariant Labs | 2025 | https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks | incident report (vendor) |
| The GitHub MCP Server adds support for tool-specific configuration and more | GitHub | 2025 | https://github.blog/changelog/2025-12-10-the-github-mcp-server-adds-support-for-tool-specific-configuration-and-more | docs (changelog) |
| Data Exfiltration from Slack AI via Indirect Prompt Injection | PromptArmor | 2024 | https://www.promptarmor.com/resources/data-exfiltration-from-slack-ai-via-indirect-prompt-injection | incident report |
| OWASP Top 10 for LLM Applications 2025 | OWASP GenAI Security Project | 2024–25 | https://genai.owasp.org/llm-top-10/ | standard (community) |
| LLM06:2025 Excessive Agency | OWASP | 2025 | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | standard (community) |
| OWASP Top 10 for Agentic Applications for 2026 | OWASP GenAI Security Project | 2025 | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | standard (community) |
| OWASP Agentic AI red-team mapping | Promptfoo | 2026 | https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/ | docs (secondary) |
| AI Risk Management Framework | NIST | 2023 (page 2026) | https://www.nist.gov/itl/ai-risk-management-framework | standard |
| NIST AI 600-1 Generative AI Profile | NIST | 2024 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | standard |
| AI Agent Standards Initiative | NIST CAISI | 2026 | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative | standard (programme page) |
| Control Overlays for Super Intelligence Systems (formerly COSAiS) | NIST CSRC | 2025–26 | https://csrc.nist.gov/projects/cosais | standard (project page) |
| The OAuth 2.1 Authorization Framework (draft-ietf-oauth-v2-1-16) | IETF OAuth WG | 2026 | https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ | spec (draft) |
| RFC 8693 OAuth 2.0 Token Exchange | Jones, Nadalin, Campbell, Bradley, Mortimore | 2020 | https://www.rfc-editor.org/rfc/rfc8693.html | spec |
| MCP Authorization (2026-07-28) | Model Context Protocol | 2026 | https://modelcontextprotocol.io/specification/latest/basic/authorization | spec |
| MCP Security Best Practices | Model Context Protocol | 2026 | https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices | spec (guidance) |
| SPIFFE overview | SPIFFE project | n.d. | https://spiffe.io/docs/latest/spiffe-about/overview/ | docs |
| draft-klrc-aiagent-auth (replaced) | Kasselman et al. | 2026 | https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/ | spec (draft) |
| draft-ietf-wimse-aims-00 AI Identity Management System | IETF WIMSE WG | 2026 | https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/ | spec (draft) |
| IETF's Race to Standardize AI Agent Identity | Cloud Security Alliance | 2026 | https://labs.cloudsecurityalliance.org/research/csa-research-note-ietf-agent-identity-standards-20260902-csa/ | press / analysis |
| What are agent identities? (Microsoft Entra Agent ID) | Microsoft | 2025–26 | https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id | docs |
| Open Policy Agent documentation | OPA / CNCF | n.d. | https://www.openpolicyagent.org/docs/latest/ | docs |
| Cedar authorization semantics | Cedar project | n.d. | https://docs.cedarpolicy.com/auth/authorization.html | docs |
| Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization | Cutler et al., AWS | 2024 | https://arxiv.org/abs/2403.04651 | paper (preprint) |
| Policy in Amazon Bedrock AgentCore | AWS | 2026 | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html | docs |
| Policy in Amazon Bedrock AgentCore generally available | AWS | 2026 | https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/ | vendor announcement |
| OpenTelemetry GenAI semantic conventions | OpenTelemetry | 2026 | https://github.com/open-telemetry/semantic-conventions-genai | spec (development) |
| Regulation (EU) 2024/1689 (AI Act) | European Parliament and Council | 2024 | http://publications.europa.eu/resource/celex/32024R1689 | regulation |
| Regulation (EU) 2026/1744 (Digital Omnibus on AI) | European Parliament and Council | 2026 | http://publications.europa.eu/resource/celex/32026R1744 | regulation |
| The Digital Omnibus on AI enters into force today | Lewis Silkin | 2026 | https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo | press (law firm) |
| Complacency and bias in human use of automation: an attentional integration | Parasuraman, Manzey (Human Factors) | 2010 | https://pubmed.ncbi.nlm.nih.gov/21077562/ | paper (peer-reviewed) |
| Automation bias: a systematic review of frequency, effect mediators, and mitigators | Goddard, Roudsari, Wyatt (JAMIA) | 2012 | https://pubmed.ncbi.nlm.nih.gov/21685142/ | paper (peer-reviewed) |
| Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance | Bansal et al. (CHI '21) | 2021 | https://arxiv.org/abs/2006.14779 | paper (peer-reviewed) |
| Do Users Write More Insecure Code with AI Assistants? | Perry, Srivastava, Kumar, Boneh (CCS '23) | 2023 | https://arxiv.org/abs/2211.03622 | paper (peer-reviewed) |
| Tuning Out Security Warnings: A Longitudinal Examination of Habituation | Vance et al. (MIS Quarterly) | 2018 | https://misq.org/tuning-out-security-warnings-a-longitudinal-examination-of-habituation-through-fmri-eye-tracking-and-field-experiments.html | paper (peer-reviewed, not read) |
