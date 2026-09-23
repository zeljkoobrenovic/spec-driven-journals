# Investor-network learning chapter — 22 September 2026

## Author request and placement

The author accepted a dedicated chapter about investor support through knowledge sharing, seminars, summits, conferences, peer communities and road trips, starting with the supplied Prosus China visit. During drafting, the author added CTO Starter Kit and supplied its public start page and GitHub repository.

The new chapter is `posts/18a-learn-through-investors-network/`, permalink `learn-through-investors-network`. It is displayed as Chapter 20, after operating-model blueprints and before sourcing help. The sourcing-to-engagement handoff stays intact. Existing source paths were retained because the workspace already contained substantial editorial work; configuration supplies reading order. The journal now has 34 main chapters and 45 configured pages.

## Editorial choices

- Give discovery and continuing relationships their own place alongside learning for a known decision. Avoid treating every event as an immediate delivery project or requiring invented financial returns.
- Use an independent fictional company, Northline, and new characters Mira and Tomas. Its €1,200 learning-budget limit and six person-days do not alter the Larkspur ledger. Two travel/visit days plus one preparation/follow-through day per person make six person-days. The visit changes a research question; it does not authorize a feature or establish a saving.
- Identify CTO Starter Kit as the author’s project. Describe the documented resources and distinguish a proposed application by an investor community from observed adoption.
- Register S101–S105 in the bibliography with their consultation limits. Investor descriptions establish activities or offers; the Wenger-Trayner source supplies a conceptual definition. The format comparison and learning brief are proposed methods.
- Add Tool 14 and contextual links from the support, AI and technology operating partner chapters. Update the Part IV guide, six-chapter overview, contents and companion specs before their related content changes.

## Reading formats and artwork

The article is approximately 2,875 words after excluding front matter and image alt text; the independent summary is 415 words by the same whitespace-based count. The comic contains five pages of three strips each, with captions and exact dialogue transcripts. Source metadata and prose distinguish it from the shared Larkspur example.

`render-investor-learning-20260922.py` authors the chapter’s SVG logo, icon, two explanatory figures, five comic pages and the Part IV overview. It uses the standard library (plus Pillow, when present under python3.11, to measure Arial line widths for the comic pages since round 2 of the in-depth review), fixed dialogue and the journal’s ivory/navy/teal/ochre palette. Every image was rendered and visually inspected. Text was checked against SVG bounds in Chromium. The previous Part IV overview remains available as a historical asset.

## Verification

- Full repository build succeeded, including `[built] private-techuity`; the final private-techuity build also succeeded after spec reconciliation.
- Checked 45 configured pages, correct insertion between operating-model blueprints and sourcing help, consecutive displayed numbers 1–34, source registrations, cross-links and new image paths.
- Chromium checks at 1280px and 390px: Article, TL;DR and Comic tabs work; the new images load; both CTO Starter Kit links are present; no page JavaScript errors or horizontal page overflow. The new chapter appears in the journal index and Part IV guide, and Tool 14 resolves.
- The local manuscript export uses JPEG quality 80 to stay inside the existing 40 MB budget. Source artwork remains unchanged. Final export: 45 articles, 34 main chapters, 131 resources, 37.28 MB total. `validate_manuscript.py manuscripts/owned --source _journals/private-techuity --max-manuscript-mb 40` returned `[valid]`, checking 565 anchors and 1,115 internal links.
- A broad whitespace check flags existing two-space Markdown line breaks produced by the exporter in the acquisition and recovery chapters; these are retained. Source and new-chapter whitespace checks pass.
- Shared files changed during validation. The new chapter was preserved separately, the current integration rechecked, and the final site/browser/manuscript checks rerun successfully. No unrelated source revisions were restored from the initial snapshot.

The local export was refreshed; no remote site deployment, publication or Leanpub PDF/EPUB preview was performed.

## Reproduction

```bash
python3 -B _journals/private-techuity/_research/render-investor-learning-20260922.py
python3 -B _wiring/build.py
python3 -B manuscripts/_scripts/export_journal.py --journal _journals/private-techuity --output manuscripts/owned --author "Željko Obrenović" --frontmatter-post introduction --backmatter-section "Reference Material" --jpeg-quality 80 --max-manuscript-mb 40
python3 -B manuscripts/_scripts/validate_manuscript.py manuscripts/owned --source _journals/private-techuity --max-manuscript-mb 40
```

## In-depth review, round 1 — 23 September 2026

Findings INVNET-001 to INVNET-006 (`.in-depth-reviews/20260923-130030.MkVB7L/`). Dispositions are recorded in `posts/REVISION_LOG.md`; the essentials:

- The five comic SVGs referenced by `comics.md` were missing from the source tree and the built site (the `assets/images/learn-through-investors-network/` folder had been removed when the vector figures, logo and icon were replaced on 22 September). They were regenerated by running only `comics()` from `render-investor-learning-20260922.py`, whose `PAGES` table and intro were first revised for lay readers and for the page 5 chronology. The SVG root now sets `width` and `height`; without them Chromium rendered each page as a dot inside the post template’s `<img>`.
- Figure 3’s third scene was relettered “Customers’ records vary” (`retext-figure-investor-learning-20260923.py`, a Gemini image edit), inspected, downscaled to 1376×768 and re-recorded in `investor-learning-gemini-illustrations-20260922.json`; the previous image is archived under `discarded-illustration-variants/`.
- Article, summary and comic now explain investor, AI, CTO, inventory software, wholesaler, reorder suggestion and product records at first use; the title is “Learn Through Your Investor’s Network…”; permalink unchanged. Article ≈3,250 words, summary 497 words.
- Build, link and Playwright checks at 1280 px and 390 px pass for all three reading formats. The manuscript chapter and its four figures were refreshed from a temporary full export (`--jpeg-quality 80 --max-manuscript-mb 45`; the whole book now exceeds 40 MB because of chapters added by other sessions), but `Book.txt`, the manifest and `toolkit.md` still await the coordinated export noted on 20 September.

## 23 September 2026 — in-depth review round 2 (INVNET-001, INVNET-007)

- The five comic pages were relaid for phone reading. Each page is now 600 units wide (previously 960) with Mira’s bubble stacked above Tomas’s in every strip, dialogue at 24 units (previously 22), strip headings at 20 and labels at 20/18. On the Comic tab at a 390 px viewport the page shows 340 px wide, so dialogue renders at about 13.6 px instead of 7.8 px. Pages are 1,346 units tall (page 3, whose title wraps to two lines, 1,380).
- Dialogue, titles, headings and labels are wrapped by measured Arial widths (Pillow under python3.11) with a 12% allowance for the widest font in the declared stack (`Arial, 'Liberation Sans', Helvetica, 'DejaVu Sans', sans-serif`). A Chromium check of all 163 text elements across the five pages found none outside its bubble, label or card, both with the declared fonts and with every font forced to Verdana as a wide fallback.
- Wording of every bubble, label, caption and transcript is unchanged from round 1; only the geometry changed. `comics.md` was regenerated from the script, so its JSON records, transcripts and `aspect_ratio` values (300:673; page 3 10:23) match the SVGs.
- The built site’s copies of the five SVGs are byte-identical to the sources after `python3 _wiring/build.py`.

## 23 September 2026 — in-depth review round 3 (INVNET-008)

- The CTO Starter Kit passages were split into short sentences in the article, summary and the comic’s closing note (purpose, CTO definition, public files, proposed use; dashboards and controls each get a sentence in the article). The comic note lives in `render-investor-learning-20260922.py`; comics.md was regenerated from it and the five SVGs are unchanged (hashes verified).
- Summary 495 words. Build, link and Playwright checks at 1280 px and 390 px pass; the manuscript chapter was reinstalled from a temporary full export (only the edited paragraph differed). `Book.txt` and the manifest still omit the chapter.
