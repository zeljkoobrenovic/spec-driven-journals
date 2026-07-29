# Review: Internal Communication

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the tighter records in the journal. All spec success criteria are met, the checklist faithfully reproduces all seven source sections, and the article's "drip / kernel / packet" framing carries cleanly across modalities. The one item worth a look: the comic covers six of the article's beats but skips "extract the kernel" entirely — the only one of the spec's three named moves absent from the Comic tab.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 1

### Blockers
- None.

### Major
- None.

### Minor
- **[comics.md · whole strip]** "Extract the kernel" — one of the three named moves the spec's decision log organizes the principle around — has no panel. The comic covers drip, testing, packet, channels, and repetition, but the executive-feedback move is absent. *Consider whether the strip should trade one beat (e.g. merge panels 2–3) for a kernel panel, or accept the omission deliberately.*
- **[index.md · Rationale ¶1 vs. Anti-Patterns bullet 1]** The silence-then-siren point is made twice in close-to-parallel language: "teaches the organization to dread their messages" (Rationale) and "learns that a message from me means trouble" (Anti-Patterns). One of the two could be leaner since Figure 2's caption also carries it. *Trim one restatement.*

### Nits
- **[index.md · after Figures 1–3]** Double blank line after each figure caption block — consistent with sibling posts but still extra whitespace.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (drip-over-broadcast in one paragraph) | met | index.md · highlight blockquote |
| Rationale argued, not asserted | met | index.md · Rationale ("Consistency beats intensity", "The kernel matters more than the debate") |
| Checklist survives intact (7 PDF sections) | met | checklist.md · drip, kernel, test, packet, short, every channel, final audit — all present |
| Anti-patterns concrete (≥3, incl. named examples) | met | index.md · Anti-Patterns (5 items, incl. all three the spec names) |
| Credit explicit (Primer + lethain essay) | met | index.md · Authoritative References |

Non-goals respected: yes — no meeting-design content (deferred to [[meetings]]), no metrics-reporting content (deferred to [[measuring-engineering-organizations]]), no writing-course material beyond what the checklist demands.
Drift: none. Spec status `accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — drip cadence, reviewer questions, three-part packet, and "at least one person on every team" all match between article and checklist.
- **Terminology:** Consistent — "the drip," "the kernel," "the packet," "silence-then-siren," "repetition is delivery" used identically where they appear.
- **Voice & tone:** Consistent first-person declarative; checklist imperative as intended; comic keeps the VERA/LEO register.
- **Coverage parity:** Nearly even; the comic omits the "extract the kernel" beat (see Minor). Checklist and article are in full parity.

## Layer-by-layer notes

### Spec
- Template-complete, short, with genuinely checkable criteria (each names a verifiable artifact: the highlight, the seven checklist sections, three named anti-patterns, two references).
- Decision log usefully records the "three named moves, not channel-by-channel" structural choice — and the article honors it.

### index.md
- House record shape and Title Case headings correct; status highlight matches front matter.
- All three figures resolve and are captioned; all five `[[…]]` cross-links resolve.
- The "says / does not say" table is particularly strong here — each row pairs the commitment with its over-application, which preempts the obvious misreadings.
- "When I feel I am repeating myself is roughly when the organization is hearing it for the first time" (Rationale ¶4) is a good quotable line and is echoed well by comic Panel 7.

### checklist.md
- Excellent operational shape: grouped by the source's seven sections, nested sub-checklists for reviewer flags and packet summary fields, closes with the pre-send audit.
- Intro line correctly points the reader to the Article tab for rationale — good division of labor.

### comics.md
- Seven panels, all image files exist under `assets/images/internal-communication/`; alt text and captions agree.
- Clear arc (unreceived announcement → siren → single channel → drip → test → packet/channels → repetition-as-delivery); visual metaphors consistent.
- Missing kernel beat noted under Minor.
