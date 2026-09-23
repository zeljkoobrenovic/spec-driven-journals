---
status: accepted
revised: 2026-09-23
---

# Spec: PART I — Understanding Financing and Ownership

## Intent

Introduce money, authority, valuation, returns and cash as tools for understanding the owner’s expectations and the company leader’s room to act. Establish comparison from the start.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the existing header logo. Give every configured chapter its own box, use short recognizable title labels without duplicating chapter numbers, and connect the chapters to the part's overall purpose.
- Group the six chapters into tracing money and control, interpreting value and returns, and confirming funding and cash; lead to the money a commitment can rely on.
- Generate the overview through the Gemini API, matching the book's ivory, navy, teal and ochre illustration style. Lay the six chapters out as a single stacked column, tall rather than wide, with explanatory lettering that renders at roughly 14 to 16 CSS pixels at a 375-pixel phone width (about 327 pixels of content width) so every label and the closing banner read without zooming; wrap explanations onto several short lines rather than shrinking them. Label each chapter in plain language a beginner can understand without opening it, and let the first card say what customers, lenders and investors each expect rather than only naming them. Publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export. Keep the linked chapter walkthrough as the full-title reading guide.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Keep the money's direction and conditions clear: describe the cash-flow chapter so that outgoing payments (taxes, loan payments) are distinguished from money customers still owe; describe the funding-choices chapter so that loans and the company's own cash fit without implying every funding source changes ownership; and say that spendable cash depends on actual cash, agreement terms and spending approvals together, never on an agreement or an investor label alone.
- Orient a beginner using ordinary language: explain lenders, investors, shares, shareholders, profit, funds, promised-but-unpaid money, valuation and payouts (distributions) in short sentences at first use, and describe each chapter's subject without finance jargon. Where the book's emphasis is fund-backed buyouts, say so without implying that every buyout involves a fund. Describe each chapter's subject accurately; the returns chapter follows one fictional fund through alternative sale prices, not three separate investors. Briefly recall what the previous part established, and explain the next learning step without assuming later vocabulary.
- Say why the part exists and what its chapters do together, in under 400 reader-visible words counted after the chapter links expand to their published titles (image alt text and markup excluded). Do not repeat in a chapter's description what its expanded title already says.
- Walk the chapters in order, one line each, showing why that order. Name each chapter by its linked title rather than a number, so the list survives renumbering.
- State what the reader should be able to do by the end — and, where it matters, what the part will not give them.
- Hand off to the next part in the closing line.

## Non-goals

Summarising the chapters' arguments, which would make the part introduction a substitute for reading them. No new claims, no evidence of its own, no worked examples.

## Modalities

Article with one chapter-overview diagram. These are short orientation pieces; a TL;DR of a 400-word introduction would duplicate it, and a comic would imply an argument the piece does not make.

## Open questions

None for the agreed part structure. Introductions remain unnumbered; chapter reading positions follow the configuration, and existing permalinks remain stable.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- **2026-09-13: Added as unnumbered part openers.** The author asked for an introduction chapter per part. Unnumbered was chosen over numbered so that no existing chapter renumbers and every cross-reference and reading route keeps working.
- Length capped at ~400 words so an introduction cannot start competing with the chapters it introduces.

## Sources

The journal's current config.yaml and the configured chapter introductions. These pieces describe the book's own structure and make no external factual claims.

## Changelog

- 2026-09-23: In-depth review round 3 (P1-006 to P1-008). Separate money customers still owe from outgoing payments in the cash-flow description; broaden the funding-choices description to costs, obligations and ownership effects; replace the agreements-only claim with actual cash, agreement terms and spending approvals. Wording only; artwork, permalink and chapter sequence unchanged.
- 2026-09-23: In-depth review round 2 (P1-002 to P1-005). Explain lenders, investors, profit and distributions at first use; scope the buyout sentence to fund-backed buyouts; describe the returns chapter as alternative outcomes for one fund; regenerate the overview taller with larger, wrapped lettering and a first card that explains the parties; cut duplicated chapter-description wording so the expanded body falls under 400 words. Permalink and chapter sequence unchanged.
- 2026-09-23: In-depth review round 1 (P1-001 to P1-004). Explain the opening's finance vocabulary in short plain sentences, replace specialist chapter descriptions with plain-language glosses, regenerate the chapter overview as a stacked single-column image with plain labels that stay readable on a phone, and cut the introduction to under 400 expanded words. Permalink and chapter sequence unchanged.
- 2026-09-22: Add one visual chapter framework at the author's request, showing the learning connections and the part's shared outcome. Generate an image through the Gemini API as explicitly requested, with alt text and a caption; retain the linked walkthrough and stable permalinks.
- 2026-09-15: Name the parties in the fund-commitment example (a fund’s investors commit capital; the manager calls it; neither step puts cash in the company’s budget). Conditional actual-agreement framing kept unchanged. Permalink unchanged.
- 2026-09-14: Reframe the opening as a contractual condition on funding (source and terms affect usable money, approvals and payment dates), remove the repeated funding claim, point experienced readers to the part as a refresher and link the optional fund-economics reference. Permalink unchanged.
- 2026-09-13: Align the specification heading with the current part-introduction title.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Chapter walkthroughs changed from "**Chapter N** does X" to linked titles. Numbers were duplicated state that would silently rot if a chapter moved; the build renders link text from the target's title, so this stays correct automatically.
- 2026-09-13: Created.
