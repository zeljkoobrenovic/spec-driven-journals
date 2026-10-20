# Writer Brief — LISTED chapter authoring

You are writing pages of **LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms**, a serious, technically deep architecture book for chief architects, principal engineers and engineering leaders of listing marketplaces. **Quality is the priority**: depth, accuracy, coherence, concrete examples, no shallow placeholder content.

Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/listing-systems-architecture/` (ROOT).

## Read first (in this order)

1. `ROOT/_research/style-guide.md` — format, voice, evidence discipline, diagram rules, failure-pattern names, valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md` — the whole book plan; find your contract(s) and skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/_research/scenario-ledger.md` — canonical fictional Veldmark facts. Your examples must agree with it.
4. The research briefs named in your contract, in `ROOT/_research/brief-*.md`, and `ROOT/_research/productscape-digest.md` (generalized domain model: customers, capabilities, data assets, streams, stressors). Read the relevant parts in full; skim the others for anything your topic needs.
5. Model chapter for voice and density: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/finance-systems-architecture/posts/20-payments-fundamentals/index.md` (read at least the first 150 lines).
6. If chapters already exist in `ROOT/posts/`, skim those your contract links to, so terminology and examples stay consistent.

## Research

The briefs are your primary factual base. Where your chapter needs a fact the briefs do not cover, or a brief marks something as uncertain, verify it yourself with WebSearch/WebFetch against primary sources and cite it with its publication date. Do not state unverified company facts as fact.

Research tips (from the briefing phase): Medium article pages often return 403, but a publication's RSS feed returns full post text — fetch `https://medium.com/feed/<publication>` (e.g. `adevinta-tech-blog`) and read on with `offset`. Adevinta also mirrors its tech blog at `https://adevinta.com/techblog/`. EUR-Lex blocks fetches, but the EU Publications Office serves the official Official Journal texts: fetch `http://publications.europa.eu/resource/celex/<CELEX>` (e.g. 32022R2065 for the DSA) with an `Accept: application/xhtml+xml` header (via curl in Bash if WebFetch cannot set headers). The web-search quota is shared and may run out; when it does, fetch known URLs directly. The ledger's "Sunday-evening peak" is a Veldmark illustration; the documented public example is Rightmove's (see brief-platform-data-ml) — never state the Sunday peak as an industry fact. Do not invent proprietary internals of real companies; when an inference helps, label it as described in the style guide.

## Deliverables per page

- `ROOT/posts/<folder>/index.md` — the article, per the style guide.
- `ROOT/posts/<folder>/spec.md` — the spec, per the style guide (template at `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`).
- Optionally append canonical new Veldmark facts to "Additions by chapter" in `scenario-ledger.md` (append only — other writers work in parallel; use one small append edit, re-reading the file's tail immediately before editing).

Write only in your own page folders (plus that append). Do not edit `config.yaml`, other pages, or files outside ROOT.

## Verify before you finish

1. Run `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "listing-systems|error|Traceback" | head` — missing files for pages other writers have not finished are fine; your files must not cause errors. (A transient error from a parallel build in another journal can be ignored if a rerun passes.)
2. Run the render check on your pages: `python3.11 /private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-spec-driven-journals/fae6a289-cfa0-449a-8385-7b4381f86340/scratchpad/render_check.py <permalink> [<permalink> ...]`. Every page must print `OK`. `unresolved=[[x]]` means a link to a page not yet written — acceptable only if `x` is a valid permalink from the style guide (it will resolve once that page exists); `XJ:` entries mean a link resolved to another journal and must be fixed — **except** links to this book's not-yet-written pages whose permalinks also exist in the finance book (`toolkit`, `glossary`, `bibliography`, `introduction`, `long-term-evolution`, `part-1`…`part-9`): keep those links; they resolve in-journal once the page exists. Do not remove them. Fix every mermaid failure.
3. Re-read your article once as a demanding chief-architect reviewer: cut generic sentences; every company claim has a dated source; inferences are labeled; Veldmark numbers match the ledger; the three KEY POINTS are sharp; the trade-offs are real.

## Report back

In under 150 words: files written, word count, the 3 key points, any facts you added to the ledger, and any uncertainty a reviewer should check.
