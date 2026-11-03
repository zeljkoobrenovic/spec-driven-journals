---
status: accepted
revised: 2026-10-22
---

# Spec: OpenCRE Atlas — Introduction

## Intent

Explain what the OpenCRE Atlas journal is: a generated, browsable copy of the OpenCRE Common Requirement Enumeration, with one page per CRE and one per mapped standard or tool. Tell the reader how the pages are organised and how to use them to move between standards.

## Audience

Engineers, architects and security leads who meet several security standards (ASVS, CWE, NIST, ISO 27001, PCI DSS …) and want one place that shows where those standards say the same thing.

## Success criteria

- A reader knows in the first screen what a CRE is and why the mapping matters.
- The page states the counts (CREs, roots, standards) that match the generated data.
- The reader knows the three ways in: the five top-level areas, the per-area sections, and the Standards and Tools section.
- The page says plainly that the content is generated from OpenCRE data and is not an independent analysis, and links to opencre.org for the live data.
- It explains the difference between *curated* and *automatic* links.

## Non-goals

- No commentary on the quality of individual standards or mappings.
- No hand-written prose on individual CRE pages — those are generated.

## Modalities

- `index.md` only.

## Open questions

- Should the journal later add hand-written guidance posts (for example, "using CREs in a security requirements backlog")?
- Icons and logos for 547 generated pages: generate per top-level area rather than per page?

## Decision log

- 2026-10-22 — One page per CRE, permalink `cre-<id>`, so CRE ids (stable in OpenCRE) drive URL stability.
- 2026-10-22 — The largest root (Technical application security controls, 361 CREs) is split into one index section per child; the other four roots get one section each.
- 2026-10-22 — The cached export was page 1 of 6; pages 2–6 were fetched from `https://opencre.org/rest/v1/all_cres?page=N&per_page=100` and cached beside it.

## Sources

- OpenCRE: https://opencre.org
- OpenCRE REST API, `/rest/v1/all_cres`
- Cached export: `_journals/opencre/_input/cres*.json`
- Generator: `_journals/opencre/_tools/generate_journal.py`

## Changelog

- 2026-10-22 — First version.
