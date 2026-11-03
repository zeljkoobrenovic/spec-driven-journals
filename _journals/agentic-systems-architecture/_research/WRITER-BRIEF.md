# Writer Brief — chapter authoring

You are writing pages of **Architecting Agentic Systems**, a serious, technically deep architecture book for software architects, senior engineers and technical leaders who design and operate agentic systems. **Quality is the priority**: depth, accuracy, coherence, concrete examples, verifiable references, no hype and no shallow survey content.

Journal root: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/agentic-systems-architecture/` (ROOT).

## Read first (in this order)

1. `ROOT/_research/style-guide.md`: format, voice, evidence discipline (seven kinds of statement), the "Across Domains" rule, diagram rules, failure-pattern names and valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md`: the whole book plan. Find your contract(s) and skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/_research/scenario-ledger.md`: the canonical fictional Ostrell facts, including every line under "Additions by chapter". Your examples must agree with it. Then `ROOT/_research/consistency-issues.md`: canonical rulings on terminology and on which interview-design choices the book adopts or rejects. They win over the sources.
4. The research briefs named in your contract (`ROOT/_research/brief-*.md`) and the digests (`ROOT/_research/digest-*.md`). Read the relevant parts in full; skim the rest for anything your topic needs. The digests describe the author's interview designs: use them as **design examples** with their source path and step, never as deployed systems. Where digests note inconsistencies between sources, reconcile them in your chapter (say which design you adopt and why).
5. Model chapter for voice and density: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/posts/24-dms-integration/index.md` (read at least the first 200 lines; its figures are images now, but in this book you write mermaid diagrams).
6. If chapters already exist in `ROOT/posts/`, skim the ones your contract links to, so terminology and examples stay consistent.

## Research

The briefs are your primary factual base. When your chapter needs a fact the briefs do not cover, or a brief marks something as uncertain or ⚠ volatile, verify it yourself with WebSearch/WebFetch against primary sources and cite it with its publication date. Do not state unverified claims as fact; when you cannot verify, say that the public evidence stops there. arXiv abstracts (`https://arxiv.org/abs/<id>`) fetch reliably. The web-search quota is shared with other writers: search sparingly; fetch known URLs directly.

## Length cap

Keep the article (front matter to the start of "Sources and Evidence") **at or under 8,000 words including tables**; aim for 5,500–7,000. Cut repetition, not substance.

## Deliverables per page

- `ROOT/posts/<folder>/index.md`: the article, written to the style guide.
- `ROOT/posts/<folder>/spec.md`: the spec, written to the style guide. The template is at `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`.
- Optionally, append canonical new Ostrell facts to "Additions by chapter" in `scenario-ledger.md`. Append only: other writers work in parallel. Use one small append edit, and re-read the file's tail immediately before you edit it.

Write only in your own page folders, plus that one append. Do not edit `config.yaml`, other pages, or files outside ROOT.

## Verify before you finish

1. Run the build: `cd /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals && python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. "missing post" warnings for pages other writers have not finished are fine; your own files must not cause errors. A transient error from a parallel build can be ignored if a rerun passes.
2. Run the render check on your pages: `python3.11 ROOT/_research/tools/render_check.py <permalink> [<permalink> ...]`. Every page must print `OK`.
   - **`unresolved=[[x]]`** means the link points to a page that is not written yet. Acceptable only if `x` is a valid permalink from the style guide.
   - **`XJ:` entries** mean a link resolved to another journal outside the allowed sibling list, and must be fixed. Exception: keep links to this book's not-yet-written pages whose permalinks also exist in other books (`introduction`, `toolkit`, `glossary`, `bibliography`, `part-1` … `part-11`).
   - Fix every mermaid failure.
3. Re-read your article once as a demanding reviewer (a principal engineer who has run agents in production) and check that:
   - generic sentences and vendor-brochure paragraphs are cut;
   - every substantive claim has a nearby citation; research findings say what was measured and its limits; company claims are dated; illustrative numbers are labeled; interview material is labeled as design examples;
   - Ostrell numbers match the ledger;
   - the "Across Domains" comparison is specific, not symmetric filler;
   - failure scenarios name detection, containment and recovery;
   - the three KEY POINTS are sharp and the trade-offs are real.

## Report back

In under 150 words: files written, word count, the 3 key points, any facts you added to the ledger, and any uncertainty a reviewer should check.

## Privacy rule for web requests

Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies.
