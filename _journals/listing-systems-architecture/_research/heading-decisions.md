# Heading Decisions

Heading conventions the author has settled for LISTED. The cross-chapter
consistency check (`sharpen_journal.sh -c`) reads this file and does not
report what it covers. Add a line when a finding is resolved, including when
the resolution is "leave as is".

## Fixed headings (keep the exact wording)

- `## Setting the Scene at Veldmark: <scene>` opens every chapter in Parts I–VIII.
- `## Trade-offs`, `## Failure Modes`, `## The Chief Architect's View`, `## Questions to Ask` and `## Sources and Evidence`, in that order near the end of every chapter. Chapter variants such as `## Trade-offs: <topic>` are fine.
- `## From <X> to <Y>` is the hand-off heading, one per chapter, kept short.
- `## Sources and Evidence` has three subheadings: `### Company engineering and investor sources`, `### Standards, regulation and documentation`, `### Research and practitioner sources`.
- Part IX cases share: `## How to Read This Case` (or `Cases`), `## Trade-offs the Case Illustrates` (or `Cases Illustrate`), `## Vertical Differences in the Record`, `## Where the Public Evidence Stops`.
- `## Architecture: <the design>` names the design, not just the chapter topic.
- H2 headings use title case; H3 headings use sentence case, lowercase after a colon.

## Intentional variation (do not report)

- **Public-evidence and Veldmark worked-example sections** are named by content, as the style guide asks ("a guide, not a rigid template — name sections by content"). Their varied prefixes ("What the Public Record Shows", "Public Examples", "Veldmark Worked Example: …", "Back to Barcelona", "In Practice: …") are deliberate.
- **06-vertical-requirements**: "Vertical Differences in Who Decides", because the whole chapter is about verticals.
- **16-publication-pipeline**: "Freshness SLAs by Vertical" replaces Vertical Differences and sits before Trade-offs.
- **43-modernization-and-migration**: "Wave 2" and "Wave 3" come from the chapter's own six-wave plan table; they are not chapter 03's industry waves.
- **13-listing-ingestion**: the "doors" metaphor is defined in the chapter; its subheading uses the glossary's "ingestion channel".
- **toolkit, Tool 10**: "Listing Event Specification" is a template for one event in the listing event contract, so it keeps "specification".
- **introduction and 45-long-term-evolution**: both use "The Argument: A Liquidity Machine" on purpose; the last chapter returns to the first.
- **39 and 42**: both have "The phishing rule, replayed"; the shared incident is deliberate.
- **part-9-intro**: its two extra sections ("How to read the cases", "The cases side by side") suit the cases part.
- **Running-example names in headings** may be shortened ("The bike, replayed…") when the section already named the full example.
