# Writer Brief — RECONCILED chapter authoring

You are writing chapters of **RECONCILED: Enterprise Architecture for Financial Systems**, a serious, technically deep architecture book for Chief Architects, finance-systems architects, integration architects and finance-transformation leaders. The user has asked that **quality is the priority**: depth, accuracy, coherence, concrete examples, no shallow placeholder content.

Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/finance-systems-architecture/` (call it ROOT).

## Read first (in this order)

1. `ROOT/_research/style-guide.md` — format, voice, evidence discipline, diagram rules, failure-pattern names, valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md` — the whole book plan; find your chapter contract(s) and also skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/_research/scenario-ledger.md` — the canonical fictional Northmere facts. Your examples must agree with it.
4. The research briefs named in your contract, in `ROOT/_research/brief-*.md` (ea-integration-ledger, sap, workday, oracle, blackline-onestream, payments, accounting-controls-regulation, satellites-ai), and `ROOT/_research/productscape-digest.md` (generalized domain model: capability bricks, data assets, streams, tutorial concepts, stressors). Use the digest's substance but never its source company's name.
5. Model chapter for voice and density: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/private-techuity/posts/27-manage-technical-debt/index.md` (read at least the first 150 lines).
6. If any chapters already exist in `ROOT/posts/`, skim the ones your contract links to, so terminology and examples stay consistent.

## Research

The briefs are your primary factual base. Where your chapter needs a fact the briefs do not cover, or a brief marks something as uncertain, verify it yourself with WebSearch/WebFetch against official documentation, and cite it. Do not state unverified vendor capabilities or dates as fact. Do not invent proprietary internals.

## Deliverables per chapter

- `ROOT/posts/<folder>/index.md` — the article, per the style guide.
- `ROOT/posts/<folder>/spec.md` — the spec, per the style guide (template at `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`).
- Optionally append canonical new Northmere facts to "Additions by chapter" in `scenario-ledger.md` (append only — other writers work in parallel; use a single small append edit).

Write only in your own chapter folders (plus that append). Do not edit config.yaml, other chapters, or files outside ROOT.

## Verify before you finish

1. Run `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -i -E "enterprise-applications|error|Traceback" | head` — the build may report missing files for chapters other writers have not finished; that is fine, but your files must not cause errors.
2. Check your `[[links]]` use only permalinks listed in the style guide.
3. Check there are no mermaid blocks: diagrams are generated illustrations (see the style guide's Diagrams section).
4. Re-read your article once as a demanding Chief Architect reviewer: cut generic sentences, fix any vendor claim without a source, make sure the Northmere numbers match the ledger, the three KEY POINTS are sharp, and the trade-offs are real.

## Report back

In under 150 words: files written, word count, the 3 key points, any facts you added to the ledger, and any uncertainty a reviewer should check.
