# Review: Strategy for Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the sharper records in the journal: the four-layer chain, the IT-hourglass diagnosis, and the ACED gate come through in every modality, and the Rationale's "I look for the mechanism sentences first" close makes the standard operational. The most useful improvement: the mapped-landscape / Wardley commitment is the only Statement commitment that gets no Rationale support — it is asserted in one bullet and never argued, which makes it feel bolted on next to the well-defended layers around it.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "A mapped landscape" / Rationale]** Every other Statement commitment gets a Rationale paragraph; the Wardley-style landscape mapping gets none — the classification (genesis/custom/product/commodity), commoditization candidates, and refresh-with-usage-data ideas appear once in the Statement and are never argued. *Add one or two Rationale sentences on why mapping earns its place, or fold it into the roadmap paragraph explicitly.*
- **[checklist.md · §8 "Strategy Communication"]** This section (state what is not included, simple conceptual models, concise document) has no echo in the article beyond ACED's Clarity letter. Acceptable as source reproduction, but it is the one checklist section a reader cannot map back to anything in the Article tab. *A half-sentence in the article's ACED paragraph ("Clarity also means saying what the strategy does not include") would close the gap.*

### Nits

- **[index.md · Figure 1 caption]** "the layers exist to force the middle of the argument — the mechanisms — to exist" — "exist … to exist" in one sentence; reword one of them.
- **[index.md · highlight]** "It describes transformation, meaning changed ways of working, not optimization, meaning new technology under old habits" — the double "meaning" gloss is clunky; an em-dash pair or parentheses would read better.
- **[checklist.md · §2 note]** "IT Hourglass" is capitalized here but "IT hourglass" everywhere else (article, anti-patterns, comic caption); pick one casing.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight |
| The four layers survive | met | index.md · Statement table + Figure 1 + Rationale ¶2; checklist.md §2; comics Panels 2–4 |
| Transformation vs optimization survives | met | index.md · Statement + Rationale ¶4; checklist.md §3; comics Panel 5 |
| Design and governance survive | met | index.md · Statement (design + governance bullets) + Figure 2 + Rationale ¶5; checklist.md §§4–5; comics Panel 7 |
| Landscape and roadmap survive | met | index.md · Statement ("mapped landscape", "point, path, terrain") + Figure 3; checklist.md §§6–7; comics Panel 6 — landscape half is Statement-only, see Minor |
| ACED survives | met | index.md · Statement + Rationale ¶6; checklist.md §9 + Final Go/No-Go; comics Panel 8 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no design mechanics beyond requiring trade-offs in the document, no execution mechanics, no strategy template.
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — the four layers, the hourglass, buzzword mechanisms, rate of change, point/path/terrain, relinquished control, and ACED are the same claims everywhere.
- **Terminology:** consistent — "IT hourglass", "IT pyramid", "point, path, and terrain", "ACED" used identically (one capitalization slip, see Nits).
- **Voice & tone:** consistent first-person approve-or-send-back register; the comic keeps Vera as the signer, matching "before I sign one".
- **Coverage parity:** the comic covers seven of the article's beats and skips landscape mapping — acceptable for the form. The checklist's §8 (communication) is the only checklist section with no article counterpart (see Minor).

## Layer-by-layer notes

### Spec

- Follows the template; success criteria are concrete and individually checkable; the Decision log explains the four-layer/ACED framing choice well.
- Non-goals cleanly fence off the three neighboring records plus "not a template", which is a useful fourth fence.
- No bloat, no dangling open questions.

### index.md

- House record shape complete and in conventional order; Title Case headings; `draft:gray` front matter matches the DRAFT highlight.
- The Rationale is the record's engine: "a strategy is a bet placed from a position", "executed by rumor", and "a document everyone agrees with instantly is usually a document that decided nothing" are all strong, quotable, and on-argument.
- The "Concretely" close (read the waist of the hourglass first; send back documents with no contestable decision) turns the standard into a repeatable review behavior — exactly what the spec's Audience needs.
- All three figures exist and are captioned; all five `[[…]]` cross-links resolve.

### checklist.md

- Nine sections plus Final Go/No-Go; runnable and internally consistent; the italic source notes under sections are a nice touch that keeps fidelity visible.
- Terminology matches the article throughout (hourglass, IT pyramid, ACED, point/path/terrain, happy path).
- §8 is the only section without an article anchor (see Minor).

### comics.md

- Eight panels, all image files present under `assets/images/platform-strategy/`; captions run Panel 1–8; alt text matches captions and scenes; VERA/KAI cast consistent with the shared cast/style block.
- The arc mirrors the article's argument order faithfully: copied strategy → hourglass → buzzwords → four-layer chain → optimization-as-transformation → roadmap → relinquished control → ACED gate.
- Panel 8 ("A strategy that decides nothing does not get signed") is a clean compression of the record's load-bearing line.

## Fixes applied (2026-08-13)

- index.md · Statement "A mapped landscape" / Rationale — fixed: folded landscape mapping into the rate-of-change Rationale paragraph with a sentence arguing why the map earns its place (genesis-to-commodity classification shows where harmonization pays next; usage data keeps the bets current).
- checklist.md · §8 "Strategy Communication" — fixed: closed the article gap per the reviewer's suggestion by extending the ACED paragraph's Clarity sentence with "clarity includes saying what the strategy does not include" (article edit, no spec change needed).
- index.md · Figure 1 caption — fixed: reworded to "the layers are there to force the middle of the argument — the mechanisms — to exist" (removed "exist … to exist").
- index.md · highlight — fixed: replaced the double "meaning" glosses with parentheses: "transformation (changed ways of working), not optimization (new technology under old habits)".
- checklist.md · §2 note — fixed: "IT Hourglass" recased to "IT hourglass" to match the rest of the post.
