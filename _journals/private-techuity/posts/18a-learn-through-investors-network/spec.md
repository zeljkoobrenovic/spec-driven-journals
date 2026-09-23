---
status: accepted
revised: 2026-09-23
---

# Spec: Learn Through Your Investor’s Network: Knowledge, Peers and New Perspectives

## Intent

Help product and engineering leaders use investor-organized knowledge sharing, seminars, summits, conferences, peer communities and study visits to improve understanding, relationships and company practice. Give exploratory learning its own place alongside support for a known capability gap. Begin with the author-supplied Prosus China example and follow the learning into a concrete company decision without inventing measured returns.

## Audience

Company product and engineering leaders, including people inheriting an investor relationship. Assume no investment background. Explain in plain words, at first meaningful use and independently in each reading format, what an investor is and why it connects businesses, what artificial intelligence (AI) and a chief technology officer (CTO) are, and the fictional example’s trade (inventory software, wholesalers, reorder suggestions, product records). Name the cited organizers as investors at first mention and avoid unexpanded abbreviations such as FAQ. Investor-side organizers are secondary readers.

## Success criteria

- Place the chapter after [[operating-model-blueprints]] and before [[help-that-changes-capability]], preserving the latter’s direct handoff to [[useful-engagement]].
- Distinguish solving a known problem, exploring unfamiliar possibilities and developing continuing peer relationships. Allow useful questions and relationships to mature without requiring every event to justify immediate financial returns.
- Cover all six requested formats, their distinct uses and the company effort needed. Explain the investor’s contribution to access, convening, continuity and learning across companies without promising exclusive access or universal availability.
- Attribute the Prosus trip and reported reflections to Prosus; use Balderton and Insight Partners as complementary examples of described practices. Keep claims within the consulted primary sources and register S101–S104.
- Explain how ongoing peer communities work: shared practice, reciprocity, context, voluntary participation, candid discussion and agreed information boundaries. Define portfolio and community of practice locally.
- Include the author’s CTO Starter Kit, linking both the public start page and GitHub repository, as an example of reusable shared resources and routes to peers. Attribute ownership explicitly. Distinguish documented project features from the proposed use by investor communities; make no claim that an investor uses it or that it has demonstrated outcomes. In every format, give the kit’s purpose, the CTO role definition, the public files and the proposed use their own short sentences, with each definition beside the term it explains.
- Follow a clearly labelled independent Northline example from a choice of learning opportunity through time and spending approval to observations, contextual interpretation, team discussion and a next enquiry. Preserve the existing Larkspur ledger by using a separate company and cast. Keep one chronology across formats: the visit, the return discussion, the added customer-interview question and one learning review a month after the visit. The unresolved local condition is the varying product records of Northline’s customers, never Northline’s own records; figures and comic labels say so.
- End with a small reusable learning brief, practical review questions and a handoff to sourcing support. Add Tool 14 without changing existing tool numbers.
- Use the journal’s learning/why-investors-care/why-you-should-care opening, exactly three key points, restrained bold emphasis and plain language. Keep the article around 2,500–3,300 words, including the author-requested shared-resource example and the plain-language explanations required in Audience, with depth where the distinction between exploration and delivery matters.
- Provide an independently readable 300–500-word summary and a short illustrated comic of generated pages with captions and per-strip transcripts rendered from the page blocks. Illustrate the article with three Gemini-generated figures in the journal’s ivory, navy, teal and ochre palette: investor-supported learning, the relationship between shared resources and peer conversations, and bringing observations home with their context. Keep labels brief and accurate, distinguish the fictional example from evidence, and provide descriptive alt text and captions. Reuse the learning overview in the summary. Preserve the companion comic and navigation artwork. Update the Part IV overview to six chapters.
- Update the reading guides, chapter numbering, neighboring handoffs, relevant cross-links, bibliography and companion specs. Preserve existing public permalinks and asset namespaces. Build and inspect the rendered article and reading formats; check local links and assets.

## Non-goals

An assessment of China’s entire AI industry, a provider ranking, evidence of investment returns, a prescribed event calendar, or a requirement to convert curiosity into an immediate project. The fictional illustration is reasoning, not observed performance.

## Modalities

- `index.md`: article with three explanatory figures generated through the article-illustrator skill and Gemini API.
- `summary.md`: 300–500-word independent summary with a learning overview.
- `comics.md`: five illustrated comic pages of three strips each, with the same independent Northline decision. Each page is one Gemini-generated image with the dialogue, labels and amounts lettered in the artwork, generated from the `comic-page` blocks in `comics.md` (which are also the source of the captions and transcripts) with a Northline-only cast block (Mira, Tomas) and no Larkspur reference sheet; images live under `assets/images/18a-learn-through-investors-network/`, and every page is inspected against its script. The earlier vector pages remain reproducible from `_research/render-investor-learning-20260922.py` and are archived under `_research/comic-pages-pilot/18a-svg-pages/`.

## Open questions

The consulted investor accounts do not establish subsequent company outcomes. Observed follow-through could be added later with permission and evidence.

## Decision log

- 2026-09-22: The author accepted a dedicated Part IV chapter. Separating it from the sourcing chapter leaves room for discovery before a known capability gap exists.
- 2026-09-22: Use a separate fictional company to avoid changing the shared Larkspur budget or calendar. Compare a study visit with a cheaper option while acknowledging that broad exploration may justify a larger commitment.
- 2026-09-22: Use editable vector illustrations for exact, legible labels and the short comic’s decision sequence.
- 2026-09-22: At the author’s request, replace the article’s two vector diagrams with Gemini illustrations and add a figure explaining how resources such as CTO Starter Kit support continuing peer conversations. Generate from recorded prompts, inspect each image, and verify the rendered article before accepting the revision.

- 2026-09-23: Keep the vector comic rather than regenerating the five pages with the Gemini comic-page generator. The decision log already chose editable vectors for exact labels, the cast is independent of the shared Larkspur cast sheet, and the render script is the recorded source; restoring the SVGs from it is faithful and reproducible. Fix the page 5 chronology by making the caption describe planning the one-month review after the visit, which matches the dialogue and the article’s later review.
- 2026-09-23 (author request, later the same day): The author asked for this post's comic to follow the journal's comic-pages format like every other Owned chapter, so the vector comic is replaced by five generated pages. This supersedes the earlier same-day decision to keep the vector comic; the reasons for that decision (exact labels, an independent cast) are met by lettering the labels in the page scripts and by a Northline-only cast block generated without the Larkspur reference sheet.

## Sources

- [S101: Prosus, A Window on China. A Mirror on Ourselves.](https://www.prosus.com/news-insights/2026/a-window-on-china-a-mirror-on-ourselves): the author’s starting example; organizer’s account.
- [S102: Balderton, Collective CTO Summit](https://www.balderton.com/news/the-balderton-collective-cto-summit-bringing-100-ctos-together-online/): 2020 forum-to-summit example.
- [S103: Insight Partners, Onsite Hour](https://info.insightpartners.com/onsitehour.html): recurring learning offer and participant access, as described in its FAQ.
- [S104: Etienne and Beverly Wenger-Trayner, Communities of practice: a brief introduction](https://www.wenger-trayner.com/wp-content/uploads/2022/01/07-Brief-introduction-to-communities-of-practice.pdf): domain, community and practice; sustained interaction. Selected definition passages consulted.
- [S105: Željko Obrenović, CTO Starter Kit](https://ctostarter.com/start/index.html) and [repository](https://github.com/zeljkoobrenovic/cto-starter-kit): author-supplied project, public start page and repository README consulted; durable resources and discovery of peers.
- [[operating-model-blueprints]], [[help-that-changes-capability]], [[useful-engagement]], [[investors-adviser]], [[tech-operating-partner]] and [[ai-strategy-three-questions]]: boundaries and connections.

## Changelog

- 2026-09-23 (comic pages): The five SVG pages replaced by five generated comic pages of three strips each, keeping the same Northline chronology (choice of format, approval of €1,200 and six person-days, the visit with observation kept apart from the host's explanation, the return discussion and reframed question, the one-month learning review) and drawing the amounts and labels into the artwork. Captions and transcripts are rendered from the page blocks; the SVG comic and its markdown are archived under `_research/comic-pages-pilot/`. No figure or decision in the example changed; permalink unchanged.
- 2026-09-23: Round 3 of the in-depth review (INVNET-008). The CTO Starter Kit passages in the article, summary and comic note are split into short sentences: purpose, CTO definition, public files and proposed use each stand alone, and dashboards and controls have their own sentences in the article. Links, ownership attribution and the proposed-use qualification are unchanged; spec remains accepted.
- 2026-09-23: Round 2 of the in-depth review (INVNET-001, INVNET-007). The comic pages are relaid for phone reading: 600-unit-wide pages with stacked speakers and 24-unit dialogue replace the 960-unit side-by-side pages whose dialogue shrank to about 8 px on a phone; text is wrapped by measured width with a fallback-font allowance. The built site carries all five pages. Modalities updated accordingly; spec remains accepted.
- 2026-09-23: Round 1 of the in-depth review (INVNET-001 to INVNET-006). Title corrected to “Learn Through Your Investor’s Network”; permalink unchanged. Audience now requires plain first-use explanations of investor, AI, CTO and the example’s trade in every format. The five comic SVGs, missing from the source tree, are restored from the render script with the page 5 caption and several bubbles reworded for lay readers. Figure 3’s third panel is relabelled “Customers’ records vary”. Spec accepted.
- 2026-09-22: Complete the author-requested Gemini illustration pass: three explanatory JPEGs, captions and alt text, with the learning overview reused in the summary. Preserve the article’s prose and current front matter. Inspect all images, verify source and built assets, build all journals, and check Article and TL;DR at 1280px and 390px with no broken images, page overflow or JavaScript errors. Record prompts and image hashes in `_research/investor-learning-gemini-illustrations-20260922.json`; spec accepted.
- 2026-09-22: Complete the article, 415-word summary, five vector comic pages, figures, logo and icon. Add Tool 14, register S101–S105 and integrate the six-chapter Part IV route. Preserve existing source paths with an `18a` insertion and existing public URLs. Build, link/asset checks and desktop/mobile browser checks pass; spec accepted as matching the chapter.
- 2026-09-22: Add the author-requested CTO Starter Kit example and S105 before drafting its treatment.
- 2026-09-22: Initial spec, written before the chapter; status draft.
