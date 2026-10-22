# Writer Brief — chapter authoring

You are writing pages of **Architecting a Vehicle Data and Dealer SaaS Platform**, a serious, technically deep architecture book for chief architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors, portals, lessors and dealer groups. **Quality is the priority**: depth, accuracy, coherence, concrete examples, no shallow placeholder content.

Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/` (ROOT).

## Read first (in this order)

1. `ROOT/_research/style-guide.md`: format, voice, evidence discipline, the "Across Markets" rule, diagram rules, failure-pattern names and valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md`: the whole book plan. Find your contract(s) and skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/_research/scenario-ledger.md`: the canonical fictional Axleby facts, including every line under "Additions by chapter". Your examples must agree with it.
4. The research briefs named in your contract, in `ROOT/_research/brief-*.md`, and the parts of `ROOT/_research/productscape-digest.md` that cover your contract's bricks. Read the relevant parts in full and skim the others for anything your topic needs.
5. Model chapter for voice and density: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/posts/12-availability-engine/index.md` (read at least the first 220 lines; its figures are images now, but in this book you write mermaid diagrams).
6. If chapters already exist in `ROOT/posts/`, skim the ones your contract links to, so terminology and examples stay consistent.

## Research

The briefs are your primary factual base. When your chapter needs a fact the briefs do not cover, or a brief marks something as uncertain, verify it yourself with WebSearch/WebFetch against primary sources and cite it with its publication date. Do not state unverified company facts as fact; when you cannot verify, say that the public evidence stops there.

Research tips:
- Medium article pages often return 403. A publication's RSS feed returns the full post text: `https://medium.com/feed/<publication>`.
- EUR-Lex blocks fetches. The EU Publications Office serves the official texts: fetch `http://publications.europa.eu/resource/celex/<CELEX>` with an `Accept: application/xhtml+xml` header, using curl in Bash if WebFetch cannot set headers.
- The web-search quota is shared. When it runs out, fetch known URLs directly.

## Length cap

Keep the article (front matter to the start of "Sources and Evidence") **at or under 8,000 words including tables**; aim for 5,500–7,000. Cut repetition, not substance.

## Deliverables per page

- `ROOT/posts/<folder>/index.md`: the article, written to the style guide.
- `ROOT/posts/<folder>/spec.md`: the spec, written to the style guide. The template is at `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`.
- Optionally, append canonical new Axleby facts to "Additions by chapter" in `scenario-ledger.md`. Append only: other writers work in parallel. Use one small append edit, and re-read the file's tail immediately before you edit it.

Write only in your own page folders, plus that one append. Do not edit `config.yaml`, other pages, or files outside ROOT.

## Verify before you finish

1. Run the build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`.
   - "missing post" warnings for pages other writers have not finished are fine. Your own files must not cause errors.
   - A transient error from a parallel build can be ignored if a rerun passes.
2. Run the render check on your pages: `python3.11 ROOT/_research/tools/render_check.py <permalink> [<permalink> ...]`. Every page must print `OK`.
   - **`unresolved=[[x]]`** means the link points to a page that is not written yet. This is acceptable only if `x` is a valid permalink from the style guide; it will resolve once that page exists.
   - **`XJ:` entries** mean a link resolved to another journal outside the allowed sibling list, and must be fixed. Exception: keep links to this book's not-yet-written pages whose permalinks also exist in other books (`introduction`, `toolkit`, `glossary`, `bibliography`, `domain-coverage`, `part-1` … `part-10`). They resolve in-journal once the page exists, so do not remove them.
   - Fix every mermaid failure.
3. Re-read your article once as a demanding chief-architect reviewer and check that:
   - generic sentences are cut;
   - every company claim has a dated source and inferences are labeled; illustrative numbers are labeled;
   - Axleby numbers match the ledger;
   - the "Across Markets" comparison is specific and evidenced, not symmetric filler;
   - failure handling covers duplicates, conflicts, incomplete records, retries, partial failures and outages where relevant;
   - the three KEY POINTS are sharp and the trade-offs are real.

## Report back

In under 150 words: files written, word count, the 3 key points, any facts you added to the ledger, and any uncertainty a reviewer should check.

## Privacy rule for web requests

Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies. For SEC EDGAR (which requires a contact User-Agent), use `research-bot admin@example.com` or skip EDGAR.
