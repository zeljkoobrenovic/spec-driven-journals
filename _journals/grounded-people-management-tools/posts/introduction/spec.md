---
status: accepted
revised: 2026-07-28
---

# Spec: Introduction

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Orient the reader to the grounded-people-management-tools journal: what it is
(Željko's people-management toolkit written down as 20 tool-shaped records),
why an executive writes down a toolkit (management quality at scale is a
systems property; principles without tools decay into vibes), where the
material comes from (the companion workbooks to Claire Hughes Johnson's
*Scaling People*, credits preserved), the record anatomy (principle blockquote,
ADR-shaped body, the runnable tool in the Checklist tab, View spec link), and
a map of the five sections with reading paths per audience.

## Audience

Managers in Željko's organization (the toolkit is the standard); peer
executives and his own manager (the blockquotes are the fifteen-minute
version); practitioners building their own toolkit (take the checklists).
First-person, essay-shaped.

## Success criteria

- [x] **KEY POINTS block** — exactly three bullets: what the journal is,
      that every record ships the runnable tool, how to read it.
- [x] **The toolkit framing lands** — tools vs. principles distinction made
      explicitly; this journal is the mechanics layer beneath the sibling
      journals.
- [x] **The map is complete** — all five sections listed with all 19
      tool-record `[[slug]]` links, plus workflow chains across records.
- [x] **Credit is explicit** — Claire Hughes Johnson / Stripe Press named,
      with the workbook-internal credits (Stan Slap, David Singleton,
      Kailey Stockenbojer) carried.
- [x] **Sibling journals linked** — relative links to the
      engineering-executive and product-management introductions.

## Non-goals

- Not a summary of any individual tool — each record carries its own.
- Not a review of the *Scaling People* book itself — only the workbooks
  ground this journal.
- No checklist modality — the introduction is essay-shaped, like the
  sibling journals' introductions.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — Grounded the journal in *Scaling People: The Workbooks*
  (the free companion PDF), not the book's prose: this journal is about
  runnable tools, and the workbooks are the tool layer.
- **2026-07-28** — Five sections following the workbooks' five-chapter arc
  (foundations, operating system, hiring, team development, performance)
  rather than the book's chapter titles, so the section names describe the
  reader's problem, not the source's structure.
- **2026-07-28** — Kept `permalink: introduction` for consistency with the
  sibling journals; `[[introduction]]` remains a banned cross-link target
  journal-wide because the slug is duplicated across journals.

## Sources

- **Internal**
  - `sources/Scaling-People-Workbooks_PDF_23_03_05.pdf` — the companion
    workbooks that ground every record in this journal.
- **External**
  - Claire Hughes Johnson, *Scaling People: Tactics for Management and
    Company Building* (Stripe Press, 2023) — the parent book.

## Changelog

- **2026-07-28** — Comics modality staged (comics.md, Comic tab, shared VERA/NOA cast) with pending panel blocks; 3 inline illustration placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-28** — Initial spec and introduction written together with the
  journal's 19 tool records. Status `accepted`. *(Željko, AI-mediated
  session)*
