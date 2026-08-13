---
status: accepted
revised: 2026-08-13
---

# Spec: Building Great Platform Teams

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I staff and shape platform teams. The post turns the platform-team
chapter of Camille Fournier and Ian Nowland's *Platform Engineering* into an
operating rule: a great platform team is a deliberately mixed team — people
who can write substantial production code alongside people with broad systems
and operational expertise, treated as equally valuable — guarded against both
the "too much systems" culture that automates instead of engineering problems
away and the "too much development" culture that chases new architecture while
production burns. Specialist and product roles earn their place when the need
is demonstrated; interviews, ladders, and recognition are aligned to the
actual work; and customer empathy is a hiring bar, because internal users are
customers of the platform.

## Audience

Engineering leaders staffing or restructuring platform teams; hiring managers
and interviewers building platform hiring loops; platform engineering
managers calibrating culture and recognition; peer executives comparing
operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the mixed-team rule, the
      two cultural failure modes staffed against, roles earned by demonstrated
      need, and customer empathy as a hiring bar.
- [x] **The composition guidance survives** — mixed software and systems
      expertise treated as equally valuable, reliability expertise where the
      need is real, specialists limited and kept close to their systems, and
      both "too much systems" and "too much development" cultures named with
      their symptoms.
- [x] **The role expectations survive** — software engineers curious about
      systems and willing to operate what they build; broad systems
      generalists who solve problems in code and keep a career path without
      forced specialization; reliability engineering as a specialized role
      with mandate and reach, not a catch-all label.
- [x] **The hiring and career machinery survives** — interviews customized to
      platform work (platform design, inverted design, operational behavioral,
      customer empathy), title/level/interview decisions separated, shared
      ladders where practical, and promotion evidence that counts operational,
      support, and customer impact rather than lines of code.
- [x] **The leadership and culture guidance survives** — managers who
      understand operational complexity and deliberate delivery pace; product
      management added at scale with platform-aware PMs; TPMs and supporting
      roles only when genuinely required; balanced culture and recognition as
      an explicit leadership responsibility.
- [x] **Credit is explicit** — References name Camille Fournier and Ian
      Nowland's *Platform Engineering* and the platform-team chapter.

## Non-goals

- Not [[getting-started]] — that record covers when the first platform team
  is justified and what it does first; this one covers who the team is made
  of and how it stays healthy.
- Not [[operating-platforms]] — that record covers the operational discipline
  itself; this one covers staffing so the team can carry that discipline.
- Not [[platform-as-a-product]] — that record is the product operating mode;
  this one only covers the product roles and product-minded staffing that
  support it.
- Not a compensation or leveling policy — ladders and pay bands stay with the
  wider organization; this record constrains only how platform work is
  evaluated within them.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Grounded in the platform-team chapter of Camille Fournier
  and Ian Nowland, *Platform Engineering: A Guide for Technical, Product, and
  People Leaders* (O'Reilly, 2024), via its chapter checklist — read through
  a practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed around balance as the load-bearing idea: the
  chapter's distinctive claim is that platform teams fail from cultural
  imbalance ("too much systems" or "too much development") more often than
  from lack of talent, so the record commits to staffing against both failure
  modes explicitly.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Building Great Team.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the chapter on
    building great platform teams.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
