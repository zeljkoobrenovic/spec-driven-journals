# RETROFITTED — Style Guide for Chapter Writers

Read this, `../PLAN.md` (your chapter contract and your neighbours'), `fact-ledger.md` (canonical facts, names, numbers and transcript corrections) and the research briefs named in your contract **before writing**. Model chapter for voice and density: `_journals/finance-systems-architecture/posts/20-payments-fundamentals/index.md` (read at least the first 150 lines). Keep its discipline: concrete, defined, evidenced, example-driven.

## What this book is

A case-study journal about **one real company's** internal AI developer infrastructure, starting from one podcast episode and widened by Uber's public engineering record and the industry context. Every chapter does three jobs:

1. **Explain what Uber built** — the system, its mechanism and its history, as far as the public record shows.
2. **Expose the foundation underneath** — the pre-AI investment the AI-era system depends on (the book's thesis: *the harness is the easy part*).
3. **Translate it for everyone else** — what a company that is not Uber should copy, in what minimal form, with what prerequisites, and what not to copy.

## Voice and audience

- The reader is an engineering leader, platform/DevEx lead, staff or principal engineer, or CTO. Do **not** explain what an API gateway, monorepo, CI, Kubernetes or a coding agent is. **Do** define Uber-specific system names and AI-tooling terms (MCP, skills, harness, background agent) on first use in each chapter (one clause), and link to the chapter that owns the term (PLAN "Owns").
- First person ("I", "my") is the author's judgement and recommendations, used sparingly ("The rule I would use…"). The author has **no inside knowledge of Uber** and never implies any. Never write as if speaking for Uber.
- American spelling. Plain, declarative sentences. No marketing language ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class", "revolutionize", "supercharge"). Exception: inside direct quotes.
- Explain **why the system exists, how it works, what it depends on, what it trades off** — not feature lists.
- People: Uday Kiran Medisetty (Uber Distinguished Engineer, the guest) — on second reference "Medisetty"; Gergely Orosz (host, *The Pragmatic Engineer*) — "Orosz". Use they/them for anyone whose pronouns you do not know, including both of them, or simply repeat the surname.

## Evidence discipline (non-negotiable)

Five kinds of statement; make the kind obvious from wording:

0. **First check the ledger's "Cross-source reconciliation" table.** Several AI-era systems are also described in written 2026 Uber sources (the Aug 2026 "Running a Software Factory Efficiently" blog, the Oct 2026 "Designing MCP Gateway" blog, the AI Engineer 2026 talk, the Apr 2026 JUnit/Shepherd blog). Where a written source exists, cite it with its date and treat the podcast as the complementary account; where podcast and written source disagree, follow the table.
1. **Uber's own account (podcast)** — most facts about the AI-era systems (AIFX, MCP Gateway, skills, context graph, Minion, Code Inbox, Slate-for-agents, Capri, Fox, Wisdom, DebugAssist, spend tiers) come only from the October 2026 episode. Attribute them: "Medisetty described…", "According to Medisetty…", "Uber says…", "in the October 2026 Pragmatic Engineer episode". Numbers from the podcast (15% of production PRs, ~30,000 skill executions a day, 100+ node types, ~50% token-cost reduction) are always attributed, never stated as independent fact.
2. **Documented fact** — Uber engineering blog posts, papers, open-source repositories, Pragmatic Engineer articles, standards. Give the **year of publication in the sentence** the first time ("In a 2024 engineering post, Uber described its GenAI Gateway…") and link inline. If the source is more than about three years old, say the system may have changed. Only use facts marked VERIFIED in the briefs or that you verify yourself with WebFetch.
3. **Industry practice / comparison** — other companies (Stripe, Spotify, Google, Lyft, Meta) with dated sources; general practice phrased as "commonly", "a typical pattern".
4. **Labeled inference** — how something at Uber is plausibly built when the record is silent. Label it: a callout `> **INFERENCE, NOT DOCUMENTED:** …` or the phrase "a plausible reading — not a documented description —". Never present invented internals (service names, schemas, volumes, team sizes) as fact. When the record is silent and an inference would not help, say "Uber has not described…" — honest gaps are a feature.
5. **Recommendation** — the author's view for the reader's organization, with reasoning and the conditions under which it does not hold.

Quotes: short direct quotes from the episode are welcome (≤ 40 words each, at most ~4 per chapter), attributed, lightly corrected for transcription errors (see ledger) — never fabricated. The transcript is auto-generated; quote the *meaning* accurately and use the corrected names. Do not reproduce long transcript passages. Do not reuse the Pragmatic Engineer screenshot (`_input/.../img.png`) — describe what it shows if needed.

Time: write "as of October 2026" for state-of-the-world claims. Today is 2026-10-20.

## Page format

Folder: `posts/<folder>/` (from PLAN) with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-20
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one or two sentences>

> **WHY IT MATTERS:** <one or two sentences, from an engineering leader's view>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **BUILT ON:** <one line naming the pre-AI foundations this system depends on, each linked with [[permalink]] where a chapter owns it — e.g. "DevPods (2017), the per-language monorepos and Bazel, Slack and web entry points">

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem concretely; bold 1–3 key phrases.>
```

Exactly three KEY POINTS. (Preface and Reference pages: use `IN THIS BOOK, YOU WILL:` / omit BUILT ON where it does not fit.)

Body (a guide, not a rigid template — name sections by content, not generic labels like "Concepts"):

1. **The problem Uber had** — what made the system necessary, in Uber's terms (scale, cities, PR volume, review load).
2. **What Uber built** — the system as described: components, entry points, behaviour, numbers (attributed). At least one mermaid diagram.
3. **The foundation underneath** — the pre-AI pieces it reuses and why it would be hard without them. Link Part I chapters.
4. **Design choices and trade-offs** — a table of the alternatives (e.g. MCP vs CLI, gateway vs direct vendor access, auto-land vs human review) and when each is right.
5. **Elsewhere in the industry** — 1–3 dated comparisons (Stripe, Spotify, Google, Lyft, GitHub, Anthropic/OpenAI docs) — similarities and differences.
6. **If you are not Uber** — the minimum viable version, prerequisites, buy/build/open-source options, sequencing, and what *not* to copy. A short table by company size (≈50, ≈500, ≈5,000 engineers) is ideal.
7. **Failure modes** — concrete ways this goes wrong (for Uber or for an imitator).
8. **What the record does not say** — open questions the public record leaves unanswered (honest gaps).
9. **Questions to ask** — 6–10 questions a reader can take into their own planning or design review.
10. A closing paragraph handing off to the next chapter in reading order with a `[[link]]`.
11. `## Sources and Evidence` — grouped: *The source episode*, *Uber engineering sources*, *Industry and research sources*; each entry: linked title, publisher/author, **year**, one clause on what it supports. End with: "Statements about Uber's AI-era systems are Uber's own account unless another source is cited; recommendations and labeled inferences are the author's judgement."

Length: **3,500–5,500 words** for Part I–IV chapters (depth over breadth; one well-worked example beats five mentions); Preface pages 2,500–4,500; System Catalog / Glossary / Bibliography as long as needed.

## Diagrams

Mermaid blocks (rendered client-side). Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Engineer in Slack"] -->|"@Minion follow this thread"| B["Minion on mega DevPod"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~25 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point>*`. Aim for 2–3 diagrams per chapter. Diagrams of Uber systems show the described flow, not invented internals; if a diagram includes an inferred piece, the caption says so.

Use GitHub tables generously: dependency maps, trade-offs, company-size adoption, before/after.

## Cross-links

Link chapters with `[[permalink]]`. Valid permalinks (this book only): `introduction`, `the-harness-is-the-easy-part`, `timeline`, `build-what-does-not-exist`, `monorepos-and-one-build`, `devpods`, `contracts-and-context-propagation`, `model-gateway`, `aifx-harness-layer`, `mcp-gateway`, `skills-monorepo`, `context-graph`, `token-spend-governance`, `plans-as-source-of-truth`, `minion`, `inner-loop-and-self-healing-ci`, `slate`, `capri`, `code-review-signals`, `shepherd-and-fox`, `wisdom-and-debug-assist`, `feature-velocity`, `the-engineer-as-context-builder`, `the-retrofit-playbook`, `system-catalog`, `glossary`, `bibliography`. Link where it helps (typically 6–12 per chapter); do not re-teach what another chapter owns — summarize in a sentence and link. Never invent a permalink: a typo can silently resolve to another journal's page. No links to other journals.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-10-20`. Intent, Audience, Success criteria (5–8 checkable boxes, ticked), Non-goals (what neighbouring chapters own), Modalities (article only for now; boxes unticked), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: `- **2026-10-20** — Initial spec and article. Status \`accepted\`. *(AI-mediated session)*`). Typically 400–800 words.

## Quality bar — check before finishing

- Every Uber AI-era claim is attributed to the episode or another dated source; no invented internals; inferences labeled; podcast numbers attributed.
- The BUILT ON line and "foundation underneath" section make the thesis concrete for this system.
- At least two mermaid diagrams; at least one trade-off table; an "If you are not Uber" section with sizes; failure modes; what the record does not say; questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure. No undefined jargon; every acronym expanded on first use in the chapter.
- Mermaid blocks follow the syntax rules; cross-links use only valid permalinks; names follow the ledger's corrected spellings.
