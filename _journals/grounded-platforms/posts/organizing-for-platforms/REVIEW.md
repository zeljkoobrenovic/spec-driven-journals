# Review: Organizing for Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, internally consistent record that lands the spec's small-product-company framing cleanly across all three modalities. The article is well argued, the checklist reads as a faithful, runnable reproduction of the chapter checklist, and the comic covers the load-bearing beats with all eight panel images present. Publish-ready after minor polish; the single most important thing to address is the engagement-mode terminology wobble ("onboarding" vs "setup") between the Statement, the Rationale, and the checklist.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, bullet 5]** The engagement modes are listed as "self-service, onboarding, consulting, community, and co-creation", but the Rationale ("The engagement model is a portfolio…"), Figure 2's context, and checklist §10 all use "setup" for that mode. One term should win everywhere. *Suggest standardizing on "setup" (the checklist's and spec's term).*
- **[index.md · Statement, bullet 5]** The spec's customer-machinery criterion names four personas — developers, administrators, operators, end users — but the article compresses to "from developers to administrators to end users", dropping operators. Checklist §9 keeps "system administrators and operational users", so the criterion is only met across modalities, not in the article. *Suggest "developers, administrators, operators, and end users".*
- **[checklist.md · §14 Recruiting & Retention]** This section sits squarely in the hiring-and-growing-people territory the spec's first non-goal fences off to [[building-platform-teams]], and neither the spec's Intent nor the article acknowledges it exists in the checklist. Source fidelity explains its presence, but the spec and article act as if it isn't there. *Suggest a one-line acknowledgement (e.g. in the spec's Sources note or the article's "How to Read This") rather than removal.*

### Nits

- **[checklist.md · §6 and §7 headings]** "East-West" / "North-South" use hyphens where the article consistently uses en-dashes ("east–west", "north–south").
- **[index.md · front matter `excerpt`]** The excerpt near-duplicates the highlight's phrasing ("the org chart never ships in the platform experience… adoption is a relationship, not a rollout") — closer to copy than compression; harmless, but a lighter paraphrase would earn its place.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The roles survive | met | index.md · Statement b2, Rationale ¶1; checklist.md §2 |
| Both alignment axes survive | met | index.md · Statement b3–b4, Rationale ¶3–4, Figure 1; checklist.md §6–7 |
| The customer machinery survives | partial | index.md · Statement b5, Rationale ¶5 (operators persona missing; "onboarding"/"setup" wobble); checklist.md §8–10 complete |
| The restraint survives | met | index.md · Statement b6, Rationale ¶6, Figure 3; checklist.md §12–13 |
| Credit is explicit | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes, with one brush — checklist §14 (Recruiting & Retention) overlaps the [[building-platform-teams]] non-goal; source fidelity justifies it, but it goes unacknowledged (see Minor).
Drift: none — spec `accepted` stands; the post delivers what the spec contracts.

## Cross-modality alignment

- **Facts & framing:** consistent — the accountable leader plus five owned functions (strategy, roadmap, delivery, marketing, support), both alignment axes, and the do-we-need-it gate carry identically across article, checklist, and comic.
- **Terminology:** one wobble — "onboarding" (Statement) vs "setup" (Rationale, checklist §10). Otherwise load-bearing phrases ("ticket queue", "shipped org chart", "fix, wrap, or work around", "Thinnest Viable Platform") are used consistently.
- **Voice & tone:** consistent first-person declarative; the comic compresses without changing register.
- **Coverage parity:** even for the spec's beats. The checklist is deliberately broader (§3 Technology Strategy, §14 Recruiting & Retention have no article echo); §3 is anchored by the technology-strategy role in the Statement, §14 is not anchored anywhere (see Minor).

## Layer-by-layer notes

### Spec

- Clean template compliance; criteria are concrete and checkable, non-goals do real fencing work against three sibling records.
- The success criteria enumerate five content beats plus credit but stay silent on two checklist sections (§3, §14) — a deliberate compression, but it leaves the checklist's outer edges without a criterion to check against.

### index.md

- Well-structured: six Statement commitments, each picked up by exactly one Rationale paragraph — a tight, followable mapping.
- The contrast table and anti-patterns do their house job without contradicting each other; "professional-services drift" appears in Rationale, table, and anti-patterns, which is the house recap pattern rather than true repetition.
- All three figures exist on disk and are captioned; all five `[[…]]` cross-links resolve to existing posts.
- Highlight status DRAFT matches front-matter `status: draft:gray` and the Scope section.

### checklist.md

- Faithful in structure and register to a chapter checklist: 14 numbered sections plus a Final Platform Health Check, with italic source-note asides that stay descriptive.
- Terminology tracks the article except the hyphen/en-dash headings and the "setup" term the article's Statement renames.

### comics.md

- Eight panels, all image files present, captions run Panel 1–8, captions match their alt text and (spot-checked) the images; VERA/KAI cast consistent with the declared style.
- The narrative arc (hook → problem → wrong way → principle → two axes → cost → closer) mirrors the article's argument order — good parity with no invented beats.

## Fixes applied (2026-08-13)

- index.md · Statement, bullet 5 (engagement modes) — fixed: standardized on "setup" ("self-service, setup, consulting, community, and co-creation"), matching spec, Rationale, and checklist §10.
- index.md · Statement, bullet 5 (personas) — fixed: now "developers, administrators, operators, and end users", restoring the operators persona.
- checklist.md · §14 Recruiting & Retention — fixed: one-line acknowledgement added in the article's "How to Read This" (fenced to [[building-platform-teams]]) and a matching note in the spec's Sources bullet; spec `revised:` bumped and Changelog line added.
- checklist.md · §6/§7 headings — fixed: hyphens replaced with en-dashes ("East–West", "North–South") to match the article.
- index.md · front matter `excerpt` — fixed: lightly paraphrased the two near-verbatim highlight phrases ("infrastructure seams never reach the user", "adoption is earned continuously rather than announced once").
