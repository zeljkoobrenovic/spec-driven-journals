---
name: probe-further
description: Research and add a "To Probe Further" section to a post's main article (index.md) — a short, verified list of external resources (books, papers, guides, talks, standards) with the linked title, a citation, and one sentence on why each one helps the reader go deeper on the post's subject. Use whenever the user asks for further reading, external resources, a reading list, links to go deeper, "probe further", "learn more", or to enrich a post with references in _journals/*/posts/*/ — including batch requests across a whole journal.
---

# To Probe Further (post enrichment with external resources)

## Goal

Append a `## To Probe Further` section to a post's `index.md`: a curated,
**verified** list of external resources that let a motivated reader go deeper
than the post itself. Each entry gives the title (linked), who published it and
when, and **one sentence on why it is relevant to this post** — what the
reader gets there that the post only touched on.

This is enrichment, not evidence. The post's argument must still stand on its
own; the section is the "where next" for a reader who wants more. It does not
replace a journal's bibliography, inline citations, or `Authoritative
References` section, and it never edits them.

## Contract rules

- **Edit only `index.md`.** Do not touch `spec.md`, `config.yaml`, other
  modality files (`summary.md`, `checklist.md`, `dialog.md`, `comics.md`), or a
  journal's bibliography/glossary posts. The section belongs to the article
  modality only.
- **Every link is verified before it is written.** Fetch each URL (WebFetch)
  and confirm that the page exists, is the resource you think it is, and that
  its content matches the description you are about to write. A plausible link
  that 404s or points at the wrong thing is worse than no link: readers lose
  trust in the whole list. Never write a URL from memory alone.
- **Preserve the post.** Do not rewrite prose, headings, or the opening
  highlight block. The only change is the new (or refreshed) section at the end.
- **Idempotent.** If `## To Probe Further` already exists, refresh it in place
  (drop dead links, add better resources, tighten descriptions) rather than
  appending a second one.
- Do not invent resources. If you cannot find a strong, verifiable resource for
  a theme, leave it out; four good entries beat six padded ones.

## Placement and shape

The section is always the **last `##` section** of the article, after whatever
the post currently ends with (`Questions to Consider`, `Authoritative
References`, a closing section, a figure). Keep one blank line before and after
the heading.

```markdown
## To Probe Further

- **[Title of the resource](https://verified.url/)** — Author or publisher, year.<br>*One sentence on why a reader of this post should open it.*
- **[Second resource](https://verified.url/)** — Author or publisher, year.<br>*One sentence on why it is relevant here.*
```

Each bullet is one line: the linked title, an em-dash, the citation ending
with a full stop, then `<br>` (no surrounding spaces) and the sentence in
italics (`*…*`, closing star after the full stop). The
`<br>` puts the relevance sentence on its own line under the citation when
rendered; the post renderer passes raw HTML through, so it works inside list
items.

Rules for entries:

- **4–6 entries** per post. Fewer for a narrow post, never more than 7.
- **Title is the link text**, in bold, so the list skims well. Use the
  resource's real title, not a paraphrase.
- **Attribution after the dash**: author or publishing organization and year
  (or "undated" when the page carries no date). For a book, name the author and
  publisher. For a paper, the authors and venue or series. For a standard or
  guide, the issuing body.
- **Exactly one sentence of description**, roughly 15–30 words, and it
  explains relevance to *this* post, not the resource in general. "Chapter 3
  works the same waterfall calculation this post sketches, with a full
  numerical example" beats "A classic text on private equity". One sentence
  means one full stop, no semicolons, no em-dash inside it. Where the resource
  comes from an interested party (a vendor, a fund, a lobby group) fold that
  into the sentence in a few words ("the sponsors' own account of…") so the
  reader knows what kind of evidence it is.
- **Match the post's register.** Plain language, declarative, no hype ("must
  read", "seminal"). Expand acronyms the post has not already expanded.
- Order entries from the most general or accessible to the most specialized,
  or follow the order of the post's own argument — pick one and keep it.

## Choosing resources

Start from the post: read `index.md` (and skim `spec.md` for Audience and
Sources) and write down the three to five ideas a reader would most want to
go deeper on. Then look for one strong resource per idea. Good candidates, in
rough order of preference:

1. **Primary or authoritative sources** — the original paper, standard,
   regulator page, model document, or official report behind an idea the post
   uses.
2. **Books or long-form guides** that treat the subject at chapter length,
   linked to the publisher's page or a stable catalogue page (not a retailer).
3. **Practitioner writing** — essays, well-known blog posts, talks — from people
   with direct experience, when the post's subject is practice rather than
   theory.
4. **Datasets, surveys, or reports** a reader could use to test the post's
   claims against numbers.

Prefer resources the post does **not** already cite inline. Inline citations
and a journal bibliography already point the reader at the evidence; the point
of this section is to widen the map. A source the post cites may reappear only
when it is genuinely the best next read (for example, the full book behind a
paper the post quotes), and then say what more the reader will find there.

Mix formats when you can (a book, a paper, a practical guide, a talk) and
lean toward resources that are freely readable; when a resource is paywalled or
a book, say so implicitly through the attribution and link to a page that at
least shows the abstract or table of contents.

If a URL contains parentheses (some DOIs do, e.g. `10.1016/0749-5978(85)90049-4`),
percent-encode them as `%28` and `%29`: the post renderer ends a markdown link
at the first `)`, so a raw parenthesis truncates the link.

Prefer stable URLs: DOIs, publisher pages, organization sites, arXiv, SSRN,
NBER, government and regulator pages, established conference or journal sites.
Avoid link shorteners, search-result URLs, PDF mirrors of uncertain provenance,
and retailer pages.

When enriching several posts in one journal, keep the sets **distinct**: a
resource should appear in at most one or two posts, in the post where it fits
best. Duplicated lists across chapters signal that the research was generic
rather than tied to each post's argument.

## Workflow

1. **Read** `index.md` fully. Note the post's core claims, its named concepts,
   and any resources it already cites. Skim `spec.md` (Audience, Sources) and
   the journal's bibliography post if one exists, so you know what is already
   covered.
2. **List** the 3–5 themes worth deepening. For each, note the kind of
   resource that would serve the post's audience best (an executive reader
   wants a guide or a book chapter; an engineer may want a paper or a standard).
3. **Search** (WebSearch) per theme. Collect 2–3 candidates per theme; favor
   authoritative and stable sources as described above.
4. **Verify** each candidate you intend to use with WebFetch: confirm the page
   resolves, the title and author are as you will write them, and the content
   supports the relevance sentence. Drop anything you cannot confirm. If a
   fetch is blocked (bot protection) but the URL is a canonical publisher or
   DOI page, you may keep it only if a second source (search result snippet,
   the DOI resolver) confirms title and author.
5. **Write** the section in the shape above. Read each description once more
   and ask: does it say why *this* post's reader should open *this* link?
6. **Append** it as the last section of `index.md` (or replace the existing
   one). Keep the front matter, highlight block, and every other section
   byte-for-byte unchanged.
7. **Build**: run `python3 _wiring/build.py`, confirm `[built] <journal>`, and
   check that `docs/<journal>/<permalink>.html` contains the new heading and
   the link URLs (`grep -c "To Probe Further" docs/<journal>/<permalink>.html`).
8. **Report**: list the resources added per post and state that every URL was
   fetched and verified. Mention any theme for which no good resource was
   found so the author can supply one.

## Example

For a post arguing that adjusted earnings figures need their exact definitions
before a technology leader can rely on them:

```markdown
## To Probe Further

- **[Non-GAAP Financial Measures: Compliance and Disclosure Interpretations](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)** — U.S. Securities and Exchange Commission, living page.<br>*The regulator's own worked interpretations of which earnings adjustments are acceptable, so you can check what "adjusted" is allowed to mean.*
- **[Financial Statement Analysis and Security Valuation](https://www.mheducation.com/highered/product/financial-statement-analysis-security-valuation-penman/M9780078025310.html)** — Stephen Penman, McGraw-Hill, 5th edition.<br>*Chapters 9 to 11 walk the reconciliation from reported profit to cash that this post only sketches.*
- **[International Private Equity and Venture Capital Valuation Guidelines](https://www.privateequityvaluation.com/)** — IPEV Board, 2022 edition.<br>*The industry body's own description of the valuation practice most funds say they follow, which is where your investor's report definitions probably come from.*
```

## Anti-patterns

- Writing a link without fetching it, or keeping a link that fetched to a
  different page than expected.
- Descriptions that summarize the resource but never say why it matters to
  this post, or that run past one sentence.
- Dropping the `<br>` or the italics, so the sentence runs on from the citation
  or reads as a second heavy line rather than a light note under it.
- Generic lists ("the classic books on private equity") reused across several
  posts.
- Retailer or search-result links; link shorteners; PDF mirrors.
- Editing anything other than the new section: the spec, the bibliography,
  the post's prose, other modalities.
- Padding to reach a count. Four verified, relevant entries are the target;
  six is the ceiling in ordinary cases.
- Skipping the build check.
