---
timetoread: 2 min
---

AI-authored product architecture becomes reviewable when grounding explicitly connects the intended product model to explored reality, evidence is separated from assumptions, source files pass deterministic validation, and generated documentation is treated as output — never as the source of truth.

This closes the loop opened in [[what-is-spec-driven-product-architecture]]: dreaming defines the intended product architecture, exploring reads reality through source code, cloud activity, delivery logs, finance, incidents, ownership, and analytics, and grounding is the evidence join between the two. The first job of the model is not to be impressive; it is to be reviewable.

**What changes**

- The model separates sourced facts, explicit assumptions, informed inferences, and open questions — an agent may infer a plausible capability or product brick, but it must not present that inference as a sourced fact, and reported metrics keep their original scope.
- Every important concept either connects to evidence or is marked as an assumption: capabilities to customer evidence or analytics, product bricks to repositories, services, and cloud assets, team ownership to activity and incident signals. That exposes aspirational concepts, keeps the model current, and reveals trends and drift.
- Authoring standards rise: agents leave behind structured JSON with stable lowercase IDs and consistent references that scoped validators can parse and check — duplicate IDs, brick ownership, team dependencies, staffing consistency.
- The review loop is fixed: author source, validate, generate documentation, review rendered pages, return fixes to source. Editing generated docs directly breaks the loop.
- A first modeling session follows a practical ten-step sequence — from choosing a domain slug to recording assumptions and gaps for the next session. The first version only needs to be coherent enough to improve.

**What it costs**

- Evidence discipline and validation gates are extra authoring work; the payoff is that later review is possible at all.
- Deterministic validation is only the floor: humans still judge domain boundaries, KPI quality, brick ownership, team realism, and roadmap sequencing. The model makes that review easier, not unnecessary.

**What we are not doing**

- Not full validator documentation, and not instructions for running every generator group.
- Not an external evidence-source taxonomy.

A draft domain is good when it supports informed disagreement — when reviewers can say "this KPI is not measurable" or "this brick is too broad for one team." The Article tab covers the grounding loop, the validation scope, the publishing discipline, and the full first-session sequence; [[modeling-diverse-domains]] supplies the pattern library to start from.
