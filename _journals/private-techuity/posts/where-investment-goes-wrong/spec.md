---
status: accepted
revised: 2026-09-26
---

# Spec: Where Investment Can Go Wrong

## Intent

Give readers memorable names for company mistakes and missed opportunities around outside investment before they enter Part I. Organize the post around recognizable behavior, with distinct patterns for distinct problems or unused possibilities, and connect each to whichever parts help address it. Place the post immediately after the introduction as an unnumbered opening guide.

## Audience

Product and engineering leaders working with outside investors, including leaders who inherit the arrangement. Assume no finance training. Founders, finance colleagues and investor advisers can use the same questions to discuss a company situation.

## Success criteria

- Give the patterns short, memorable names in accessible everyday language. Use The Dusty Address Book for the unused investor network. Explain each name through concrete behavior; omit part names from the pattern headings.
- Match each name to its mechanism: committing before announced funds are available; invoking investor authority to close discussion; gradual expansion of an adviser's role; adding commitments without removing them; confusing increased scale with capability; and moving costs or risks elsewhere. Use the author's latest proposed names, choosing The Nodding Room for apparent consensus and retaining The Exit Halo for the final pattern. Keep the tone focused on observable behavior and avoid implying deliberate deception.
- Let the problems determine the number and order of patterns. Several patterns may draw on one part, and one pattern may draw on several parts. Cover the current eight parts without requiring a one-to-one mapping; link to part introductions rather than repeat chapter-level reading routes.
- Give each pattern an illustrative warning sign, the consequence for company work and a question that starts a useful response. Separate conflicting interests from borrowed investor authority, and intrusive support from unused support.
- Include missed opportunities explicitly: an available network left unexplored, confirmed funding and time that never address recurring constraints, and outside expertise that delivers work without transferring capability the company needs. Explain what could be gained and how to examine it. Keep gradual loss of decision authority separate from the missed opportunity to learn from an expert, and allow intentional continuing external support.
- Cover misunderstood money and ownership; unclear authority and conflicting incentives; unused or intrusive support; commitments without evidence or resources; changes in size without changes in work; apparent savings with hidden costs; obligations lost through ownership changes; and misleading lessons from success or failure stories.
- Explain how investment can expose or amplify existing company problems, while also creating opportunities and new demands. Keep company leaders' actions and investors' actions visible; do not imply that every investment causes these problems.
- Distinguish normal disagreement, uncertainty and transition costs from repeated behavior that leaves them unexamined or unmanaged. Explain that a problem can cross several parts.
- Use short, plain-language examples without invented historical claims, prevalence statistics or new financial calculations. Identify the examples as illustrative and define specialist terms locally.
- Follow the opening-guide style: IN THIS SECTION and three KEY POINTS, followed by a compact pattern-and-warning-sign table and the diagnostic discussion. Put the reading links with each pattern. Aim for roughly 1,900–2,300 words for the expanded set of twelve patterns.
- Give the article one header logo and each of its twelve patterns one explanatory illustration. Make the mechanism visible, including unused relationships, funded time and opportunities to learn. Use the book's ivory, navy, muted teal and ochre palette, short readable labels, descriptive alt text and numbered captions; preserve the prose and pattern names.
- Insert the post directly after `introduction/index.md` in configuration and link it from the introduction and book index. Keep existing permalinks and main-chapter numbers stable; include both opening guides as front matter in the manuscript export.

## Non-goals

A second reading guide, a catalogue of every chapter's anti-patterns, new case research, a judgment about all investors, or a universal score for company health. Detailed remedies belong in the linked parts.

## Modalities

Illustrated article: one header logo and twelve figures, one for each pattern. Place each figure after the paragraph that explains the mechanism. The pattern table provides the overview; the figures make individual mechanisms easier to recognize. Keep generation prompts in the journal's research directory. The numbered chapters retain their existing summaries and comics.

## Open questions

None for the initial scope. Revisit the examples as the author receives reader feedback.

## Decision log

- **2026-09-26 (illustrations)** — The author requested a logo and one illustration for each pattern. Use a shared editorial illustration style and distinct concrete metaphors, with brief captions that explain what went wrong or what opportunity was missed. Keep The Dusty Address Book and the existing article icon.
- **2026-09-26 (concrete names)** — Apply the author's new set: Spending the Press Release, The Nodding Room, The Ghost Veto, The Accidental Gatekeeper, The Dusty Rolodex, Never Fixing the Roof, Borrowed Brains, The Ratchet Roadmap, All Bulk, No Muscle, Squeezing the Balloon, Year Zero and The Exit Halo. Choose The Nodding Room for its concrete picture of apparent agreement; retain The Exit Halo because the pattern concerns an inference from success and need not involve deliberate deception.
- **2026-09-26 (missed opportunities)** — The author also requested patterns of missed opportunities. Make the existing Unopened Address Book explicit as one, and add The Unused Breathing Room and The Expertise That Leaves. Keep the twelve patterns in one guide with flexible part links.
- **2026-09-26 (mechanism refinement)** — Adopt the author's alternatives Spending the Announcement, The Invisible Veto, Advisor Creep, The One-Way Roadmap, Scale Mistaken for Strength and The Squeezed Balloon. Retain the other four names. Adjust examples and explanations to match timing, gradual drift and displaced costs; favor a precise name over forcing every title into the same grammatical form.
- **2026-09-26 (naming revision)** — The author requested catchier pattern names and relaxed the one-pattern-per-part organization. Use ten distinct patterns with supporting links across parts; retain the practical warning signs, consequences and questions.
- **2026-09-26** — The author requested a post immediately after the introduction about investment-related company challenges, anti-patterns and dysfunctions, preferably aligned with the book's parts. Use one principal pattern per part, with overlaps explained, to connect recognizable problems to the book's purpose.
- **2026-09-26** — Use an unnumbered opening guide so the diagnostic overview precedes the teaching sequence. Describe observable behavior and consequences instead of attributing motives to investors or management.

## Sources

- [[introduction]] — company-leader perspective, ownership distinctions and existing reading routes.
- [[part-1]], [[part-2]], [[part-3]], [[part-4]], [[part-5]], [[part-6]], [[part-7]], [[part-8]] — current scope and learning purpose of each part, together with their configured chapters.
- This post synthesizes the book's own arguments. Its short examples illustrate patterns; they are not additional historical evidence.

## Changelog

- **2026-09-26 (illustrations)** — Extend the specification before adding a header logo and twelve explanatory figures. Preserve the article's current wording, title, reading links and opening-guide position.
- **2026-09-26 (sentence review, WIGW-004)** — No change of intent. The Exit Halo's closing sentence drops the nested "ownership model: every company…" definition and now reads "one company's failure becomes a verdict on every company owned and controlled in the same way", keeping the warning against generalizing from one failure. Article, site page and manuscript chapter refreshed. Fixed.
- **2026-09-26 (follow-up review)** — No new findings; the follow-up confirmed WIGW-001–003 fixed in the article, site page and manuscript. No change to intent or article. The published book PDF and EPUB predate this chapter and do not contain it yet; they need a new book build to include it.
- **2026-09-26 (plain-language review, WIGW-001–003)** — No change of intent; the existing "assume no finance training" and "define specialist terms locally" criteria now apply more strictly. The opening explains what investors do with their money, including buying existing owners' shares; purchases of other businesses, funding rounds, how the investor's purchase was paid for and ownership models are explained where they first matter. Workplace terms are made concrete: product and engineering teams, the person responsible for an improvement (distinct from company owners), an improvement with a defined scope and finish point, the roadmap as the plan for upcoming work, the bill for running servers and software, and outages. The spec heading now matches the published title, and the manuscript export was refreshed so its heading reads "Where Investment Can Go Wrong". Pattern names, permalink and part links unchanged. All three findings fixed.
- **2026-09-26 (accessible wording)** — Replace The Dusty Rolodex with the author's refinement The Dusty Address Book. Preserve the image of a neglected network using familiar words that include professional contacts. Update the overview, heading, excerpt, introduction and export.
- **2026-09-26 (concrete names)** — Update the naming contract before synchronizing the overview, headings, examples, excerpt, closing passage and introduction. Preserve all twelve mechanisms, the missed opportunities and the flexible part links.
- **2026-09-26 (missed opportunities)** — Extend the contract before the article to cover unused relationships, funded time and knowledge transfer. Update the opening, overview, explanations, closing questions and introductory references while retaining the refined names.
- **2026-09-26 (mechanism refinement)** — Update the specification before refining six names and their explanations. Synchronize the overview, excerpt, closing example, introduction and manuscript export; retain ten patterns and the existing reading links.
- **2026-09-26 (naming revision)** — Update the contract before the article: lead with memorable pattern names, split distinct behaviors and use flexible links to the book's parts. Supersedes the initial one-pattern-per-part structure.
- **2026-09-26** — Initial specification written before the article, then accepted after the draft matched the eight-part diagnostic scope and configured placement. Article and spec agree; the book remains a working draft.
