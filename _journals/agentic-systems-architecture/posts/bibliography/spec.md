---
status: accepted
revised: 2026-10-28
---

# Spec: Bibliography

## Intent

Give readers one register of the public sources the pages cite, findable by topic and by chapter. Each entry states the year the citing chapter gave, which of the book's five source groups it belongs to, whether it is a living page, and which pages rely on it, so a reader can weigh a claim by the kind and age of the source behind it. Agent evidence ages fast (preprints, vendor documentation, dated protocol revisions), so the page explains dates and volatility once, and states that the author's interview designs are design examples, not deployed systems. The page is generated, not hand-written, so it can be regenerated as other sessions finish chapters.

## Audience

Software architects, senior engineers and technical leaders who want to check a research finding, a vendor claim, a protocol detail or an incident against its source. Reviewers and later writing sessions use it to see which sources each chapter rests on.

## Success criteria

- [x] Front matter (permalink `bibliography`, date 2026-10-28), then IN THIS SECTION, YOU WILL; KEY POINTS with exactly three bullets; two failure patterns from the style guide (Vibe Evals, The Silent Upgrade); `<br>`; a short intro.
- [x] Every entry was harvested from a `## Sources and Evidence` section of a page in `config.yaml`; pages that are missing or still being written are skipped; URLs are copied exactly; notes such as "No public incident report…" are not entries.
- [x] Entries are deduplicated by normalized URL, RFC number, EU CELEX number and explicit equivalences, and carry identifiers R1, R2, … that never change; new sources append (registry: `_research/bib-tools/ids.json`).
- [x] Each entry has identifier, linked title, author or publisher, year (or "n.d., accessed …"), one clause on what it supports, an evidence type taken from the group heading it was cited under, a living-page mark where it applies, and a Cited in line of `[[permalink]]` links.
- [x] "How to Read This Register" explains evidence types, dates, volatility, and that interview designs are not deployed systems.
- [x] Topic sections with a Topic Index (identifier range, part link); Sources by Chapter in reading order.
- [x] Suspicious entries (missing years, year conflicts, implausible arXiv identifiers, dead links, secondary or tertiary sources) are listed in `_research/bib-tools/review.txt`, never dropped.
- [x] Ends with the Ostrell sentence; the build passes and every `[[…]]` link resolves.

## Non-goals

- Further reading or annotated reading lists (chapters own their sources).
- Judging whether each source supports its claim; the review list flags candidates for a human.
- The research briefs and digests in `_research/`, which are working notes, not public evidence.

## Modalities

Article only.

## Open questions

- Chapters 43 and 44, the preface, the part introductions and the reference pages are still being written; rerun the pipeline when they land (new sources append from the next free R-number).
- Some chapters list framework documentation (Temporal, LangGraph, OPA) under *Specifications, standards and regulation*; the register follows the majority heading. Decide whether to normalize the chapters.

## Decision log

- **2026-10-28** — Adapted the vehicle-data book's four-step pipeline (gen → classify → fix → render) instead of hand-writing the page, so the register can be regenerated as chapters land.
- **2026-10-28** — Evidence type comes from the chapter's group heading (majority, first-cited on a tie), with URL rules only as fallback; topics follow the parts, split where a part has two distinct subjects (sandboxes; observability; oversight and regulation).
- **2026-10-28** — Interview designs get one entry per design keyed by repository path, with every step any chapter cites, and their own topic.
- **2026-10-28** — An optional link check (`run.sh --links`) fetches every URL and compares arXiv page titles with the cited titles.

## Sources

- The opening guide (`where-agentic-systems-go-wrong`) for the failure patterns; `_research/style-guide.md` for the source groups and the opening callouts.
- Pipeline: `_research/bib-tools/` (`run.sh`, `gen.py`, `classify.py`, `fix.py`, `render.py`, `check_links.py`, `ids.json`, `review.txt`), adapted from `_journals/vehicle-data-dealer-saas-architecture/_research/bib-tools/`.

## Changelog

- **2026-10-28** — Initial spec and generated page. *(AI-mediated session)*
