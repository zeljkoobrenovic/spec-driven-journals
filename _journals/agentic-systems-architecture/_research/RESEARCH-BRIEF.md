# Research Brief — Architecting Agentic Systems

You are preparing one verified research brief for **Architecting Agentic Systems**, a serious architecture book for software architects, senior engineers and technical leaders who design and operate agentic systems (LLM-driven systems that plan, call tools and act over multiple steps). It follows the format and evidence discipline of its sibling books in this repository: *Architecting a Vehicle Data and Dealer SaaS Platform* (`_journals/vehicle-data-dealer-saas-architecture/`), BOOKED (`_journals/stays-marketplace-architecture/`), LISTED (`_journals/listing-systems-architecture/`).

ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/agentic-systems-architecture/`

Research date: **28 October 2026**. Your knowledge may be older than this; anything that changes (protocol versions, SDK features, model names, prices, regulation application dates) must be verified against a current source, and anything you cannot verify must be flagged ⚠.

## The book's frame

The book argues that an agentic system is an ordinary distributed system with one unusual component — a model that proposes actions whose output varies — and that the architecture's job is to **bound that component**: decide where it may decide, what it may touch, what state it can see, how its actions are made durable, reversible or approved, and how evidence about its behavior decides how much autonomy it gets. It covers foundations (when agents are justified; workflows vs bounded loops vs autonomous execution), reference architecture, orchestration and multi-agent coordination, context/retrieval/memory/state, tools and execution boundaries, reliability and recovery, security and human oversight, evaluation and observability, performance and economics, and deployment and evolution. Contrast domains: coding agents, customer support, sales/marketing, finance operations, legal, HR, research, healthcare, public benefits.

## Format to match

Read the first 60 lines of `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/listing-systems-architecture/_research/brief-search-discovery.md` and copy its conventions exactly:

- Title `# Research brief: <topic>` and a "Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*" line.
- A "How to read this brief" section with the three tags: **[VERIFIED: url, published YYYY-MM(-DD)]** (you fetched the page in this session and it supports the claim; date = publication date, or "n.d., accessed 2026-10" for undated docs), **[WIDELY REPORTED: url, YYYY]** (reputable secondary source), **[ASSUMPTION/JUDGEMENT]** (industry knowledge or inference; every statement about a proprietary system a company has not described).
- Evidence-age warnings (this field moves fast: say when a source is older than ~18 months and may describe a superseded model, API or protocol version), ⚠ volatility flags, and an honest "Research limitation" paragraph naming what you could not verify.
- Numbered PARTs and sections; tables of contrasts; quote sparingly and accurately.
- For research papers, record **what was actually measured, on what benchmark/setting, and the limitations** — not just the headline. Distinguish peer-reviewed papers, preprints, vendor engineering posts and vendor marketing.
- **Per section, a short "Durable vs volatile" note**: which part is a durable architectural principle and which is tied to a framework, model, provider or version.
- **Per section, a short "Architecture implications" note**: what the evidence implies for system design (tagged ASSUMPTION/JUDGEMENT).
- End with: "Key numbers" table (each with source and date and what it measured), "Where sources disagree", "Open questions / not verifiable", and "Source list" (title, author/publisher, year, URL, type: paper / spec / docs / engineering post / incident report / regulation / press).

## Research rules

- Prefer primary sources: original papers (arXiv, ACL/NeurIPS/ICLR/USENIX proceedings), official specifications (MCP, A2A, OpenTelemetry semantic conventions, JSON Schema, OAuth RFCs), official vendor documentation (Anthropic, OpenAI, Google, Microsoft, AWS), engineering writeups from teams that built and operated systems, incident analyses and court/regulator decisions, standards bodies (NIST, OWASP, ISO/IEC, EU AI Act text).
- arXiv abstract pages (`https://arxiv.org/abs/<id>`) fetch reliably; the HTML full text is at `https://arxiv.org/html/<id>`. Medium pages often return 403: try `https://medium.com/feed/<publication>`. EUR-Lex blocks fetches; use `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: application/xhtml+xml` via curl.
- The web-search quota is shared with other researchers running in parallel; search efficiently, then fetch known URLs directly.
- Never invent results, benchmark numbers, deployment experience or claims of production readiness. Never invent internals of a real company's system. If something is only plausible, tag it ASSUMPTION/JUDGEMENT.
- Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies.
- Record every source with its publication date. Aim for **50–100 tagged claims** and **400–800 lines**. Depth and accuracy beat breadth.

## Deliverable

Write only `ROOT/_research/brief-<your-topic>.md` (the name is given in your task). Do not edit any other file.

## Report back

Under 200 words: file written, line count, the five most important findings for the book's architecture, where sources disagree, and the biggest gaps you could not verify.
