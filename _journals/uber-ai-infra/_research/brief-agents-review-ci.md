# Research brief: Uber's agentic coding, code review, CI and productivity measurement (public record)

Compiled 2026-10-20 to back the journal built from the Pragmatic Engineer podcast "Uber's AI infra, from the inside" (14 Oct 2026, Uday Kiran Medisetty). Every URL in "Sources" was fetched on that date. Status tags:

- **CONFIRMED**: an Uber-authored source (blog, paper, talk by Uber staff) or independent reporting says the same thing.
- **PARTLY CONFIRMED**: the system or idea is public, but the podcast's specifics (numbers, mechanics) are not.
- **PODCAST-ONLY**: nothing public found. Attribute it to Medisetty in the podcast.

Several sources are third-party summaries of talks (Port, OpenClawDatabase, ZenML, rywalker.com). Their numbers are Uber's own claims passed on by someone else. Where possible, cite the Uber blog or the talk page instead.

---

## 1. Minion (background coding agent)

| Podcast claim | Status | Public evidence |
| --- | --- | --- |
| Minion is Uber's background/cloud coding agent | CONFIRMED | PE inside look (Mar 2026); Background Agents Summit talk (May 2026); AI Engineer World's Fair talk; Uber job posting ("Minions, our background agent orchestration system") |
| ~15% of production PRs | PARTLY CONFIRMED | Public figures are **11%** of PRs opened by agents (PE, Mar 2026), **11% of merged PRs** (Ramakrishnan, May 2026) and "about 10% of committed code built by autonomous agents" (Khosrowshahi on an earnings call, per Fortune, May 2026). 15% in October fits a rising trend but appears only in the podcast. |
| Runs on a "mega DevPod" holding all repos | CONFIRMED | AI Engineer talk (Medisetty & Huda): per-language DevPods replaced by one "mega DevPod" with all repositories. Agents claim pre-provisioned Kubernetes "balloon pods" from a warm pool, with repos snapshotted and search indexes pre-built, so they start in seconds. |
| Built on DevPods | CONFIRMED | Podcast show notes: Minion built in 2025 on DevPods, which Uber created in 2017. Ramakrishnan describes the path as container prototype → DevPod → Minion. |
| Triggered from web / Slack | PARTLY CONFIRMED | Secondary summaries list web, Slack, GitHub PR and code-review interfaces. No Uber-authored page fetched for this. |
| Plan mode; Minion v2 | PODCAST-ONLY | |
| Stops at a draft PR, does not push straight to CI | CONFIRMED (talk) | AI Engineer talk demo: inner-loop validation (static analysis, visual checks, integration checks) runs first. The reason given is that pushing straight to CI wasted shared CI capacity. |
| Autonomous PRs carry evidence | CONFIRMED (talk) | Autonomous PRs include a table of every check that ran, plus screenshots. |

Related public numbers (Uber, 2026):

- **More than 70% of PRs are attributed to local or cloud agents** (AI Engineer talk; Uber blog "Running a Software Factory Efficiently", 27 Aug 2026). This counts any PR an agent was involved in. The 11–15% figures count PRs a background agent authored. **Do not compare the two directly.**
- Lines of code per engineer roughly **doubled year over year** (talk). This is diff/LOC velocity, the metric the podcast says Uber is moving away from.
- Adoption (PE, Mar 2026): 84% of developers are "agentic coding users", 92% use agents monthly, Claude Code usage rose from 32% (Dec 2025) to 63% (Feb 2026), and AI costs are up 6x since 2024.
- Skills: 2,500 skills and 20K+ runs a day (talk, mid-2026), then **3,600+ skills and 30K+ executions a day** (Uber blog, Aug 2026). From Feb to Aug 2026, weekly active users of agentic tools grew 7x and weekly agentic requests grew 9.4x.

## 2. `aifx validate` and inner-loop validation

- **CONFIRMED.** The podcast show notes (spelled "afx validate") say agents run it before opening a PR, to clear simple CI checks such as lint and build rules.
- AIFX is the CLI that provisions AI clients, finds MCP servers, runs background tasks and updates tools (PE, Mar 2026). It wraps Claude Code, Codex and OpenCode and carries settings, skills and plugins across those harnesses (podcast show notes).
- Uber's MCP Gateway blog (1 Oct 2026) says Code Mode, served through aifx (`mcp list` / `mcp search` / `mcp call`), "is now the company default for MCP tool use in coding agents."
- The list of rules moved into the inner loop (coverage, templates) is PODCAST-ONLY. The talk confirms the general move: "validation moved into the agent's inner loop, static analysis failures auto-fixed."

## 3. CI load, "code red", self-healing CI and SubmitQueue

| Podcast claim | Status | Evidence |
| --- | --- | --- |
| CI jobs more than doubled year over year, so a CI "code red" was declared in 2026 | PODCAST-ONLY (the "code red" itself) | The show notes repeat it. No Uber blog uses the phrase. The pressure was anticipated publicly: the June 2025 SubmitQueue post says AI-assisted development will deepen speculation trees and calls for new scheduling algorithms. The AI Engineer talk names CI capacity as a coming bottleneck. |
| Self-healing CI | CONFIRMED | The Uber blog (Aug 2026) lists "self-healing CI failures" as a managed-agent task. The AI Engineer talk says self-healing CI fixes a large share of failures. No public success rate. |
| Maintenance runs off-peak | CONFIRMED (talk summary) | Port's write-up of the talk: a maintenance loop runs on **Sundays**, when CI has spare capacity, and caps how many diffs reach an engineer on Monday. Incident reviews are mined monthly for new maintenance skills. This may be the public shadow of Fox (section 6). |

SubmitQueue background ("Slashing CI Costs at Uber", 23 Jun 2025):

- SubmitQueue is Uber's speculative merge queue. It keeps the mainline green across **six major monorepos and seven languages**, is used by more than 4,500 engineers and lands tens of thousands of changes a month.
- The old strategy cancelled in-progress builds when newer changes looked likelier to succeed, which affected **40–65% of builds**.
- The new strategy extends BLRD (Bypassing Large Diffs) with a probabilistic prioritiser and uses NGBoost to predict build times. It cut CI resource use by **53%** and wait times by **37%**. Android went from 5.43 to 1.96 builds per change. Go P95 wait time fell from 33.7 to 18.6 minutes.
- Earlier figure (Korlam, PE podcast, Mar 2025): roughly one commit per minute, with CI taking 10–30 minutes.

## 4. AI code review: uReview

"uReview: Scalable, Trustworthy GenAI for Code Review at Uber" (Uber blog, 12 Aug 2025):

- uReview is the **Commenter** half of the system. **Fixer** proposes code changes in response to human or AI comments and is not detailed.
- A prompt-chained pipeline: generate → filter (confidence grading, semantic deduplication, category suppression) → validate → deduplicate. Three assistants: Standard (bugs), Best Practices (from the style-rule registry) and AppSec.
- It analyses **over 90% of ~65,000 weekly diffs** and has a **4-minute median** latency in CI. **75%** of comments are rated useful and **over 65%** are addressed, against 51% for human comments.
- It claims ~1,500 hours saved a week (~39 developer-years a year), assuming 10 minutes saved per commit.
- Best configuration: Claude-4-Sonnet generates comments and o4-mini-high grades them. Runs across six monorepos (Go, Java, Android, iOS, TypeScript, Python).
- Lessons: developers rejected readability, style and logging nits. Correctness bugs and missing error handling scored well. Simple syntactic rules stay with linters.
- **Contradiction inside the post:** it gives "65,000 diffs per week" in one place and "per month" in another.
- **Open question:** the 2025 post says Uber reviews in **Phabricator**, while the 2026 material (podcast, talk) says "PRs". Check whether Uber has moved to GitHub before writing "PR" for 2025-era facts.

The AI Engineer talk adds a two-loop design: a smaller, faster model reviews in the inner loop, and a stronger reasoning model with a review skill does the outer-loop review.

The podcast says **all PRs are still human-reviewed**. Public sources agree; none describes auto-landing.

## 5. Code Inbox, risk score, blast radius, "green lane"

| Claim | Status | Evidence |
| --- | --- | --- |
| Code Inbox exists | CONFIRMED | PE (Mar 2026) calls it "smart PR routing". ZenML's summary of PE says it routes PRs to reviewers by expertise and availability, and was built because AI raises PR volume. Ramakrishnan describes "smarter review routing". |
| Inbox shows completed AI review, screenshots/videos, risk score, blast radius | PARTLY CONFIRMED | The show notes say each change gets a **risk score** before a human reviews it, alongside AI review and screenshots/videos. "Blast radius" and the risk-model details are PODCAST-ONLY. |
| "Green lane" auto-landing of low-risk PRs, backtested on historical data | PODCAST-ONLY | No Uber source. The closest public analogue is **Meta's RADAR** (section 9). |

## 6. Large-scale change: Piranha → PolyglotPiranha → OpenRewrite/Shepherd; Fox

- **Piranha** (Uber blog, 17 Mar 2020; Sridharan, Barik, Clapp): deletes code behind stale feature flags in Java, Swift and Objective-C. About **2,000 stale flags** removed across Android and iOS. A diff takes under 3 minutes. A flag untouched for a configurable period (example: 8 weeks) counts as stale. Runs weekly and sends the diff to the flag's author. It is the precedent for the podcast's "opt-in weekly PRs".
- **PolyglotPiranha** (PLDI 2024 paper "A Lightweight Polyglot Code Transformation Language"; open source, `polyglot-piranha` on PyPI): graph-ordered match/replace rules. Per Gitar/Sonar (May 2024), Uber used it for three refactorings over six months on Java (7.5M LoC), Kotlin (2.5M) and Swift (7.5M), producing **nearly 5,000 PRs** and deleting **200k+ lines**. Gitar was co-founded by ex-Uber engineers (Gautam Korlam); treat it as close to Uber rather than independent.
- **Shepherd**: CONFIRMED by name and use. "How Uber Executed A JUnit Migration at Massive Scale" (Uber blog, 7 Apr 2026; Mishra & Vejju):
  - Starting point: 600K+ JUnit 4 tests across 15M lines of code. **75,000+ test classes** and **1.25M+ lines** migrated in **about 4 months**, through **5,000+ diffs**.
  - The changes are deterministic **OpenRewrite** recipes (`JUnit4to5Migration` plus custom ones). A custom Bazel aspect supplies the classpath. Precondition recipes skip targets that cannot be migrated.
  - **Shepherd generates a diff per migrated target**, and each diff goes through CI. This matches the podcast's "per-module PRs".
  - Bulk migration with generative AI was tried and failed. AI was kept for debugging test and build failures.
  - Planned next: Spring Boot 3, Guava → JDK, Joda-Time → java.time.
- The AI Engineer talk claims **250+ automated migrations covering ~9M lines**.
- **Fox** (opt-in weekly self-improving PRs: dead code, performance, noisy logs): PODCAST-ONLY under that name. The Sunday maintenance loop with a Monday diff cap (section 3) is the nearest public description.

## 7. Test generation: AutoCover (supporting context)

- ICSE-SEIP 2026 paper, Distinguished Paper Award (Rastenis, Chou, Roy Choudhary of Uber; Just of UW). AutoCover is a LangGraph pipeline (prepare → generate → execute → validate/repair) with CLI, Headless and IDE modes.
- It now produces **about 11% of all new tests** reviewed and added to the codebase. Its validation gates are coverage delta, mutation/branch checks where available, and multi-run flakiness checks.
- PE (Mar 2026) reports 5,000+ unit tests a month.

## 8. Productivity measurement

- **Eng Metrics Dashboard** (PE, 4 Oct 2022): Khosrowshahi showed it at an all-hands on 4 Aug 2022. It shows diff counts and focus time.
  - A first version from around 2017 showed org-level diff counts and was visible to director level and above.
  - In 2020 leadership showed weekly diffs per engineer.
  - One org encouraged **4–5 diffs per engineer per week**.
  - This is the "diff velocity" baseline that the podcast says Uber is moving off.
- **Developer NPS**: Korlam (PE podcast, Mar 2025) says tooling NPS rose from **−50 to +8**. Uber ran regular dev surveys, and Local Developer Analytics measured build times on laptops.
- **Measuring AI impact** (DX Annual, 16 Apr 2026, Ty Smith & Abhishek Tibrewal; DX newsletter recap 22 Jun 2026):
  - The approach moved through four phases: adoption → engagement → causality → agentic value. "There is no single metric that proves AI ROI."
  - "Developer-years saved" was tried and **failed**: it created replacement anxiety and needed constant recalibration.
  - PR counts break down with agents. **Feature velocity is the new North Star**, backed by flow efficiency, quality and capability expansion.
  - Uber **classifies PRs by type and complexity**. This CONFIRMS the podcast's PR tagging and the move from diff to feature velocity.
  - The type list (feature/bugfix/maintenance/testing/docs) and the trend of feature PRs up and maintenance PRs down appear in the podcast show notes. **P50 feature time** is PODCAST-ONLY.
- **Cost pressure** is the backdrop for measuring value:
  - Reports say Uber used its whole 2026 AI-tools budget within four months (Fortune, 26 May 2026). COO Andrew Macdonald said of the link to consumer features: "That link is not there yet."
  - Bloomberg (via Gigazine, 5 Jun 2026) reports a **$1,500 per employee per month cap per tool**.
  - The Uber blog (Aug 2026) reports cost per session down 52% from its June peak, cost per 1K requests down ~34%, and total spend "relatively stable since April". It describes spend tiers, Slack alerts at 50/80/100%, manager sign-off for upgrades and a live cost counter.
  - The podcast's "~50% token cost reduction" is consistent with these figures.

---

## 9. Industry comparisons

- **Stripe Minions** (stripe.dev, Alistair Gray, Part 1 9 Feb 2026, Part 2 19 Feb 2026):
  - One-shot, unattended agents on a fork of Block's goose, usually started from a Slack thread.
  - They run on pre-warmed devboxes (EC2, ready in about 10 s) isolated from production and the internet.
  - "Blueprints" mix deterministic nodes (lint, push) with agent nodes (implement, fix CI).
  - **At most two CI rounds**, then the branch goes to a human.
  - Over 1,000 merged PRs a week (Part 1), then 1,300+ (Part 2). All are human-reviewed and contain no human-written code.
  - Toolshed MCP has ~500 tools, and 3M+ tests give the agents feedback.
  - Closest analogue to Minion, including the same name. The two-CI-round cap parallels Uber's choice to stop at a draft PR to protect CI.
- **Spotify Honk** (Spotify Engineering, 6 Nov 2025, Charas & Bruggmann):
  - Built on Fleet Management, which runs containerised source-to-source transformations. Since mid-2024 about **half of Spotify's PRs** have been automated by Fleet Management.
  - Honk swaps the deterministic scripts for agents. One Maven updater script had grown past 20K lines.
  - 1,500+ agent PRs merged, with 60–90% time savings and LLM-judge verification.
  - Analogue to Shepherd + Fox: deterministic fleet changes first, agents layered on top.
- **Google Rosie** (*Software Engineering at Google*, ch. 22 "Large-Scale Changes", Hyrum Wright):
  - Shards an LSC by ownership into atomically submittable changes, each with its own test-mail-submit pipeline in TAP.
  - Global approvers auto-approve expected patterns.
  - Rosie caps outstanding shards and runs at low priority **to protect shared test infrastructure**.
  - Thousands of changes a day; the `scoped_ptr` migration ran at 700+ changes a day.
  - The reference design that Shepherd's per-target diffs resemble. Its throttling is the same answer to the CI-load problem.
- **Meta Diff Risk Score + RADAR**:
  - DRS (Engineering at Meta, 6 Aug 2025): a fine-tuned Llama predicts the chance that a diff causes a SEV. It let **10,000+ changes land during a 2024 freeze** and has 19 risk use cases (test selection, reviewer selection and others).
  - RADAR (arXiv 2605.30208, May/Jun 2026): risk-aware auto-review. It has reviewed 535K+ diffs and landed 331K+. Moving the DRS threshold from p25 to p50 raised the approve rate to 60.31%. RADAR diffs revert at one-third the rate and cause production incidents at one-fiftieth the rate of other diffs.
  - The same paper reports lines per human-landed diff up 105.9% YoY and per-developer diff volume up 51%, with agentic AI behind more than 80% of that growth.
  - This is **the public precedent for Uber's "green lane"**: a calibrated risk score gating auto-approval, validated on historical outcomes.
- **Meta TestGen-LLM** (arXiv 2402.09171, FSE 2024): extends Kotlin tests behind build, pass-reliably and coverage filters. Of its tests, 75% built, 57% passed reliably and 25% raised coverage. It improved 11.5% of the classes it was applied to, and engineers accepted 73% of its recommendations. Analogue to AutoCover.
- **DORA 2025 State of AI-assisted Software Development** (Google Cloud, 23 Sep 2025, Harvey & DeBellis):
  - ~5,000 respondents. 90% use AI at work, and over 80% believe AI raised their productivity. 30% have little or no trust in AI code.
  - AI now correlates positively with throughput but **still negatively with delivery stability**.
  - "AI doesn't fix a team; it amplifies what's already there." 90% of organisations have an internal platform.
  - Supports the podcast's framing that Uber's prior platform investments (DevPods, SubmitQueue, Bazel) are what made agents pay off, and that CI load and stability are the bill.
- **METR** (10 Jul 2025, Becker, Rush, Barnes, Rein): an RCT with 16 experienced OSS developers and 246 tasks. With AI allowed they were **19% slower**, yet they expected a 24% speedup and afterwards believed in a 20% one. The page is now marked out of date by a Feb 2026 follow-up on late-2025 tools. Use it as the caution behind measuring feature velocity rather than self-reported speedup or diff counts.
- **"Capability overhang"**: an older AI-safety term (cf. Andy Jones's 2020 "AI overhang") for latent model ability beyond what is being elicited. In coding-agent usage, Thariq Shihipar (Anthropic, AI Engineer talk "Field Guide to Fable") uses it for the gap between what a model can do with the right harness, environment and code execution and what users actually get. LessWrong's "Are We In A Coding Overhang?" applies it to user skill. Cite it as a term in circulation, not a formal definition.

## 10. Contradictions and cautions

1. **Agent share of PRs:** 10% (CEO, earnings call), 11% (PE Mar; summit May), ~15% (podcast Oct), 70%+ "attributed to agents" (talk/blog Aug). The first three count autonomous authorship; the last counts any agent involvement. No source defines "agent PR" once a human edits it.
2. **uReview volume:** 65K diffs per week vs per month in the same post.
3. **Headcount:** "almost 3,000 in tech function" (PE) vs "~5,000 engineers" (press on the AI budget) vs "a few thousand engineers across twelve sites" (talk).
4. **Context graph:** "40M entries, 150 node/edge types" (talk) vs "24M nodes, 80M edges from 30+ systems" (Aug blog). Probably growth or a different count; cite the blog.
5. **Skills executions:** OpenClawDatabase's summary says 20K+ "cumulative"; the talk page and Port say 20K+ **per day**. Use per day.
6. **Review platform:** Phabricator (2025 uReview post) vs "PRs" in 2026 material.
7. **AI in migrations:** the JUnit post says generative AI **failed** for bulk migration (deterministic OpenRewrite won). The podcast frames Shepherd/Fox within the agentic story. Keep the distinction: Shepherd's changes are deterministic, and AI is used for repair and for Fox-style work.

---

## Sources

| # | Title | URL | Date | Author / speaker |
| --- | --- | --- | --- | --- |
| 1 | Uber's AI infra, from the inside (podcast page + show notes) | https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside | 2026-10-14 | Gergely Orosz with Uday Kiran Medisetty |
| 2 | Podwise episode summary | https://podwise.ai/episodes/9124006 | 2026-10-14 | — |
| 3 | How Uber uses AI for development: inside look | https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development | 2026-03-10 | Gergely Orosz (Ty Smith, Anshu Chada); paywalled after §3 |
| 4 | Inside Uber's agent-ready platform behind 11% of merged PRs | https://background-agents.com/summit/sessions/nikhil-ramakrishnan/ | 2026-05-07 | Nikhil Ramakrishnan (Uber) |
| 5 | Agentic SDLC at Uber: Building Blocks for Uber's Software Factory | https://ai.engineer/talks/17-YSUHo6Lk-agentic-sdlc-at-uber-building-blocks-ubers | 2026 (World's Fair) | Uday Kiran Medisetty, Adam Huda |
| 6 | Inside Uber's Agentic SDLC (talk summary) | https://openclawdatabase.com/news/videos/2026-08-21-uber-agentic-sdlc-software-factory/ | 2026-08-21 | third-party summary |
| 7 | How Uber built an AI software factory | https://newsletter.port.io/p/how-uber-built-a-software-factory | 2026-08-24 | Zohar Einy (Port) |
| 8 | Inside the Software Factory: Uber (aggregated sources) | https://software-factories.port.io/uber | 2026 | Port |
| 9 | Running a Software Factory Efficiently at Uber Scale | https://www.uber.com/us/en/blog/efficient-software-factory/ | 2026-08-27 | Uday Kiran Medisetty |
| 10 | Designing MCP Gateway: Uber's MCP Management Platform | https://www.uber.com/gb/en/blog/designing-mcp-gateway/ | 2026-10-01 | Srivastava, Mehndiratta, Gill |
| 11 | uReview: Scalable, Trustworthy GenAI for Code Review at Uber | https://www.uber.com/blog/ureview/ | 2025-08-12 | Mahajan, Roy Choudhary, Bond et al. |
| 12 | Slashing CI Costs at Uber | https://www.uber.com/us/en/blog/slashing-ci-costs-at-uber/ | 2025-06-23 | Lin, Juloori, Williams |
| 13 | How Uber Executed A JUnit Migration at Massive Scale | https://www.uber.com/blog/junit-migration/ | 2026-04-07 | Anshuman Mishra, Kaushik Vejju |
| 14 | Introducing Piranha | https://www.uber.com/blog/piranha/ | 2020-03-17 | Sridharan, Barik, Clapp |
| 15 | Automated Refactoring at Scale (PolyglotPiranha at Uber) | https://www.sonarsource.com/blog/automated-refactoring-at-scale/ | 2024-05-15 | Gitar / Sonar |
| 16 | AutoCover, ICSE-SEIP 2026 | https://conf.researchr.org/details/icse-2026/icse-2026-software-engineering-in-practice/58/Automated-Software-Test-Generation-at-Industry-Scale-Using-a-Multi-Agent-Architecture | 2026-04 | Rastenis, Chou, Roy Choudhary, Just |
| 17 | Building internal AI agent infrastructure (ZenML summary of #3) | https://www.zenml.io/llmops-database/building-internal-ai-agent-infrastructure-for-software-development-at-scale | 2026 | ZenML |
| 18 | Uber coding agents research notes | https://rywalker.com/research/uber-coding-agents | 2026 | Ry Walker (secondary) |
| 19 | How Uber is Measuring Engineering Productivity | https://newsletter.pragmaticengineer.com/p/uber-eng-productivity | 2022-10-04 | Gergely Orosz (paywalled) |
| 20 | Developer Experience at Uber with Gautam Korlam | https://newsletter.pragmaticengineer.com/p/developer-experience-at-uber | 2025-03-12 | Gergely Orosz |
| 21 | Uber's Journey of Measuring AI Impact on Developer Productivity (DX Annual) | https://getdx.com/dxannual/2026/sessions/measuring-ai-impact/ | 2026-04-16 | Ty Smith, Abhishek Tibrewal |
| 22 | Uber's journey of measuring AI impact (DX newsletter recap) | https://newsletter.getdx.com/p/ubers-journey-of-measuring-ai-impact | 2026-06-22 | Engineering Enablement (DX) |
| 23 | Uber's COO says it's getting harder to justify AI spend | https://www.fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ | 2026-05-26 | Jake Angelo |
| 24 | Uber caps AI tool spending (via Bloomberg) | https://gigazine.net/gsc_news/en/20260605-uber-caps-ai | 2026-06-05 | GIGAZINE |
| 25 | Minions: Stripe's one-shot, end-to-end coding agents | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | 2026-02-09 | Alistair Gray |
| 26 | Minions … Part 2 | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 | 2026-02-19 | Alistair Gray |
| 27 | 1,500+ PRs Later: Spotify's background coding agent (Honk, Part 1) | https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1 | 2025-11-06 | Max Charas, Marc Bruggmann |
| 28 | Software Engineering at Google, ch. 22 Large-Scale Changes | https://abseil.io/resources/swe-book/html/ch22.html | 2020 | Hyrum Wright |
| 29 | Diff Risk Score: AI-driven risk-aware software development | https://engineering.fb.com/2025/08/06/developer-tools/diff-risk-score-drs-ai-risk-aware-software-development-meta/ | 2025-08-06 | Engineering at Meta |
| 30 | Automating Low-Risk Code Review at Meta: RADAR | https://arxiv.org/abs/2605.30208 | 2026-05-28 (v2 06-12) | Chris Adams et al. (31 authors) |
| 31 | Automated Unit Test Improvement using LLMs at Meta (TestGen-LLM) | https://arxiv.org/abs/2402.09171 | 2024-02-14 | Alshahwan, Harman et al. |
| 32 | Announcing the 2025 DORA Report | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | 2025-09-23 | Nathen Harvey, Derek DeBellis |
| 33 | Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | 2025-07-10 | Becker, Rush, Barnes, Rein |
| 34 | Field Guide to Fable (capability overhang) | https://www.ai.engineer/talks/9fubhllmsBU-field-guide-to-fable | 2026 | Thariq Shihipar (Anthropic), from search summary only |
| 35 | Are We In A Coding Overhang? | https://www.greaterwrong.com/posts/vtgRghz3wvPGjkoCN/are-we-in-a-coding-overhang-1 | — | LessWrong, from search summary only |

Not fetched directly (search snippets only): sources 34 and 35, the Bloomberg original behind #24, and the Uber Minion job posting. Fetch these before quoting them.
