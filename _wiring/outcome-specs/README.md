# Outcome specs

Two hierarchical JSON specifications, written before any prose, that the prose
is generated from and checked against. The schemas are approved and the
pipeline is implemented (`_wiring/validate_spec.py`, `_wiring/check_draft.py`,
the `journal-spec`, `spec-creator`, `detailed-article` and `draft-check`
skills); no existing journal has been converted yet.

| File | What it is |
| --- | --- |
| `journal-spec.schema.json` | JSON Schema for the journal spec: journal → parts → posts |
| `post-spec.schema.json` | JSON Schema for the post spec: post → sections → paragraphs |
| `common.schema.json` | Definitions both share: intent, thesis, role, flow, transition, opening, closing, and the enums |
| `check-report.schema.json` | JSON Schema for the result of checking a draft against its spec |
| `RULES.md` | Each field and check, the guide it came from, the rule in one line; sources; the check catalogue |
| `PIPELINE.md` | The pipeline today, the proposed pipeline, what happens when a check fails, what the example exposed, open decisions |
| `examples/commerce-platform-architecture.journal-spec.json` | ORDERED as a journal spec: all 14 parts, Part I's posts in full, the other 62 posts at outline level |
| `examples/boundaries-and-systems-of-record.post-spec.json` | ORDERED chapter 4 as a post spec: 10 sections, 53 paragraphs |

Both examples were reconstructed from published text and are in `draft`. The post spec is the only spec file for a post: it replaces `spec.md`.
