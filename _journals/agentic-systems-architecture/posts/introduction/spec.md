---
status: accepted
revised: 2026-10-28
---

# Spec: Introduction: Bounding the Component That Decides

## Intent

Tell the reader, in one page, what the book argues and how to use it. The central idea is that an agentic system is an ordinary distributed system with one unusual component, a model whose proposals vary, and that the architecture's job is to bound that component. Three consequences follow and run through every chapter: autonomy is a budget per action class earned with evidence; the rest of the system must be more reliable than usual; evaluation is part of the architecture. The page says what the book is not (a framework tutorial, a model comparison, a case for or against agents), lays out the eleven parts as a learning path, routes a reader with a decision already waiting to the right chapters, explains the seven kinds of statement and the dating rule for volatile facts, introduces Ostrell and the interview designs, and states the limits of the evidence honestly.

## Audience

Software architects, principal and staff engineers, and engineering, platform and security leaders who design, review, operate or fund systems in which a model plans and acts. They know distributed systems; they need a way to make and defend decisions about agents.

## Success criteria

- [x] Preface callouts ("IN THIS SECTION, YOU WILL", WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE) and exactly three KEY POINTS.
- [x] The central idea and its three consequences are stated once, clearly, and labeled as the author's recommendations rather than findings.
- [x] A parts table with each part linked as `[[part-N]]` and its argument in one line, plus one mermaid map of the book with a caption.
- [x] A "Start with the decision in front of you" table of 12–18 rows, each linking only valid permalinks.
- [x] The seven kinds of statement in a table, each with an example sentence; cited examples copy wording and links from the chapters exactly.
- [x] The dating rule: research date October 2026, with dated examples for protocol versions, prices and regulation dates.
- [x] Ostrell in one paragraph, labeled fictional, linking [[meet-ostrell]]; the interview designs presented as design examples, not deployed systems, linking [[source-coverage]].
- [x] An honest limits section: fast-moving field, thin and largely vendor-reported production evidence, recommendations that are judgement. 3,000–5,000 words.

## Non-goals

- The sixteen failure patterns in depth — [[where-agentic-systems-go-wrong]].
- Ostrell's agents, platform, cast and incidents in depth — [[meet-ostrell]].
- The definition of an agentic system and its four new properties — [[what-makes-a-system-agentic]].
- The tier register — [[autonomy-and-consequence]]; promotion and demotion — [[evidence-for-autonomy]].
- The interview-design map — [[source-coverage]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[where-agentic-systems-go-wrong]], [[source-coverage]] and [[glossary]] were not yet written when this page was; once they exist, check that the pattern names and the description of the twelve designs here still match.
- The routing table should be re-checked after the review pass in case chapter scopes move.

## Decision log

- **2026-10-28** — Opened with the Double Credit rather than an abstract statement, because it shows in one paragraph that the failure was the system around the model, not the model, which is the book's argument.
- **2026-10-28** — Followed the vehicle book's introduction, but added a seven-row evidence table with a real example sentence per kind (copied from the chapters) and a separate "limits of the evidence" section, because agent evidence is thinner and more vendor-reported than that book's.
- **2026-10-28** — Kept new citations to four sources already cited across the chapters (τ-bench, Anthropic's 2025 multi-agent post, the MCP 2026-07-28 changelog, the AI Act and the Digital Omnibus).

## Sources

- **Internal**
  - `PLAN.md` — Positioning, Provenance, Structure and the introduction contract.
  - `_research/style-guide.md` — the seven kinds of statement, the dating rule, the failure-pattern names.
  - `config.yaml`, the part intros and the KEY POINTS of chapters 1–44.
  - [[meet-ostrell]] — Ostrell facts and the Double Credit numbers.
- **Interview sources**
  - `system-design-interviews/data/book/` — the twelve designs, cited collectively.
- **External**
  - [τ-bench](https://arxiv.org/abs/2406.12045), Yao et al., 2024 (preprint).
  - [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), Anthropic, 2025.
  - [MCP Specification 2026-07-28: Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog), MCP project, 2026.
  - [Regulation (EU) 2024/1689](http://publications.europa.eu/resource/celex/32024R1689) and [Regulation (EU) 2026/1744](http://publications.europa.eu/resource/celex/32026R1744).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
