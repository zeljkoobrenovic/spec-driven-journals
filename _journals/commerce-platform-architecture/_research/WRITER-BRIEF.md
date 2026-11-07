# Writer Brief — chapter authoring

You are writing pages of **ORDERED: Architecting Commerce Platforms**, a serious, technically accurate architecture book written for readers who are **new to commerce architecture**. **Quality is the priority**: depth, accuracy, coherence, concrete examples, plain language, no shallow placeholder content and no undefined jargon.

Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/commerce-platform-architecture/` (ROOT).

## Read first (in this order)

1. `ROOT/_research/style-guide.md`: audience, voice, evidence discipline, the three take-away tiers, page format, the "Across Scale Stages" rule, diagram rules, failure-pattern names and valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md`: positioning, the teaching discipline, and the chapter contracts. Find your contract(s) and skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/_research/scenario-ledger.md`: the canonical fictional Kestrel & Pine facts, including every line under "Additions by chapter". Your examples must agree with it.
4. The research briefs named in your contract, in `ROOT/_research/brief-*.md`. Read the relevant parts in full and skim the others for anything your topic needs.
5. Model chapter for density and evidence handling: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/posts/12-valuation-engine/index.md` (read at least the first 200 lines). It is written for experts; keep its rigor but write at a newcomer's altitude, as the style guide says.
6. If chapters already exist in `ROOT/posts/`, skim the ones your contract links to (and `meet-kestrel-and-pine` if present), so terminology and examples stay consistent.

## Research

The briefs are your primary factual base. When your chapter needs a fact the briefs do not cover, or a brief marks something as uncertain, verify it yourself with WebSearch/WebFetch against primary sources and cite it with its publication date. Do not state unverified company facts as fact; when you cannot verify, say that the public evidence stops there. Never cite the private journal FEDERATED, a "supplied brief" or a Productscape file.

Research tips: Medium pages often return 403 (use `https://medium.com/feed/<publication>`); EUR-Lex blocks fetches (use `http://publications.europa.eu/resource/celex/<CELEX>` with `Accept: application/xhtml+xml` via curl); the web-search quota is shared, so fetch known URLs directly.

## Length cap

Keep the article (front matter to the start of "Sources and Evidence") **at or under 6,500 words including tables**; aim for 4,000–5,500. Cut repetition, not substance.

## Deliverables per page

- `ROOT/posts/<folder>/index.md`: the article, written to the style guide.
- `ROOT/posts/<folder>/spec.md`: the spec, written to the style guide. The template is at `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`.
- Optionally, append canonical new Kestrel & Pine facts to "Additions by chapter" in `scenario-ledger.md`. Append only: other writers work in parallel. Use one small append edit, and re-read the file's tail immediately before you edit it.

Write only in your own page folders, plus that one append. Do not edit `config.yaml`, other pages, or files outside ROOT.

## Verify before you finish

1. Run the build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`.
   - "missing post" warnings for pages other writers have not finished are fine. Your own files must not cause errors.
   - A transient error from a parallel build can be ignored if a rerun passes.
2. Run the render check on your pages: `python3.11 ROOT/_research/tools/render_check.py <permalink> [<permalink> ...]`. Every page must print `OK`.
   - **`unresolved=[[x]]`** means the link points to a page that is not written yet. This is acceptable only if `x` is a valid permalink from the style guide; it will resolve once that page exists.
   - **`XJ:` entries** mean a link resolved to another journal outside the allowed sibling list, and must be fixed. Exception: keep links to this book's not-yet-written pages whose permalinks also exist in other books (`introduction`, `toolkit`, `glossary`, `bibliography`, `domain-coverage`, `part-1` … `part-11`). They resolve in-journal once the page exists, so do not remove them.
   - Fix every mermaid failure.
3. Re-read your article once as two reviewers: a demanding architect (every claim sourced, inferences labeled, trade-offs real, Kestrel & Pine numbers match the ledger) and a newcomer (every term defined before use, business problem first, no sentence that stacks three new terms, the "Across Scale Stages" table specific rather than symmetric filler, the three take-away tiers present and honest).

## Report back

In under 150 words: files written, word count, the 3 key points, any facts you added to the ledger, and any uncertainty a reviewer should check.

## Privacy rule for web requests

Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies. For SEC EDGAR (which requires a contact User-Agent), use `research-bot admin@example.com` or skip EDGAR.
