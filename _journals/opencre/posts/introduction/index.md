---
id: "OPENCRE-INTRODUCTION"
title: "About the OpenCRE Atlas"
date: 2026-10-22
author: Željko Obrenović
permalink: introduction
timetoread: 4 min
excerpt: "What OpenCRE is, how this journal is generated from its data, and how to use the 522 common requirements to move between ASVS, CWE, NIST, ISO 27001, PCI DSS and two dozen other standards and tools."
tags: opencre, security requirements, standards mapping, asvs, cwe, nist
---
> **KEY POINTS:**
>
> * **Security standards overlap but do not share a vocabulary** — ASVS, CWE, NIST 800-53, ISO 27001 and PCI DSS each describe the same controls in their own words and numbering.
> * **OpenCRE is the shared index** — each Common Requirement (CRE) is one topic, such as *Secret storage*, linked to every section of every standard that covers it.
> * **This journal is that index as pages** — 522 CRE pages in one tree plus 25 standard and tool pages, generated from the OpenCRE export so you can browse it next to the other journals.

<br>

[OpenCRE](https://opencre.org) (Open Common Requirement Enumeration) is an open project, started in OWASP, that links security standards to each other through a shared set of requirements. A *CRE* is one requirement topic with a stable identifier, for example [[cre-223-780]] (`223-780`). OpenCRE links each CRE to the sections of the standards that cover it: an ASVS requirement, a CWE weakness, a NIST control, a cheat sheet, a ZAP rule.

If you know one standard, a CRE takes you to the matching parts of the others. If you are writing a requirement, it gives you the standard references to cite.

## What Is in the Journal

The pages are generated from the OpenCRE export cached in `_journals/opencre/_input/`. Nothing on a CRE or standard page is written by hand.

| Part | Pages | What a page shows |
| --- | --- | --- |
| CRE pages | 522 | The CRE's place in the tree, the CREs it contains, related CREs, and a table per standard of the sections mapped to it |
| Standard and tool pages | 25 | The standard's sections, the CREs each one maps to, and where the standard lands in the tree |
| This introduction | 1 | How to read the rest |

The CREs form a single tree with five top-level areas:

- [[cre-636-660]] — the technical controls in the application itself: authentication, session management, access control, input and output protection, secure data storage, secure communication, logging, and AI security controls. With 361 CREs it is the largest area, so the index splits it into one section per child.
- [[cre-546-564]] — concerns that cut across all controls, such as architecture, configuration, cryptography and injection protection.
- [[cre-616-305]] — the development lifecycle: design and threat modelling, build and deployment, supply chain, verification and training.
- [[cre-567-755]] — governance: assurance, risk assessment, security requirements, policies and people.
- [[cre-862-452]] — operations: access control processes, detection and response, facilities management and improvement management.

## How to Use It

- **Start from a topic.** Open a top-level area, follow *Contains* down to the requirement you care about, and read its *Mapped Standards and Tools* table.
- **Start from a standard.** Open the standard's page in *Standards and Tools*, find your section (for example ASVS `V2.1.1`), and follow it to the CREs it maps to — and from there to the other standards.
- **Search.** The search box on the index filters by title, excerpt and tags; every CRE page is tagged with the standards it maps to, so typing `PCI DSS` lists the requirements PCI DSS touches.

Two kinds of mapping appear on every page:

- **Curated** links were set by OpenCRE editors.
- **Automatic** links were derived by OpenCRE, mostly through CWE and CAPEC. Treat them as leads to check, not as an authoritative equivalence.

## Coverage by Standard

The bubbles show how many CREs each standard or tool is linked to in this export.

---begin bubble-chart---
nodes:
  ASVS: 277
  CWE: 249
  CAPEC: 194
  OWASP Cheat Sheets: 180
  ZAP Rule: 118
  WSTG: 112
  PCI DSS: 103
  Proactive Controls: 73
  NIST 800-63: 70
  NIST 800-53 v5: 66
  OWASP AI Exchange: 64
  MITRE ATLAS: 57
  ENISA: 56
  ISO 27001: 47
  NIST AI 100-2: 44
  ETSI: 29
  NIST SSDF: 28
  Cloud Controls Matrix: 27
  DSOMM: 24
  SAMM: 22
  OWASP Top 10 2021: 16
  OWASP Top 10 for LLM: 12
  BIML: 11
  OWASP Top 10 for ML: 9
---end bubble-chart---

## Scope and Revisiting

This is a snapshot, not the live catalogue. OpenCRE changes as standards are added and mappings are reviewed, so check [opencre.org](https://opencre.org) before you rely on a mapping for an audit or a compliance claim.

To refresh the journal, replace the cached pages in `_journals/opencre/_input/` with a new export from `https://opencre.org/rest/v1/all_cres?page=N&per_page=100`, then run:

```bash
python3 _journals/opencre/_tools/generate_journal.py
python3 _wiring/build.py
```

The generator rewrites the CRE and standard pages and `config.yaml`; it leaves this introduction alone. CRE ids are stable in OpenCRE, and page URLs (`cre-<id>.html`) are built from them, so links into the journal survive a refresh.

## Authoritative References

- [OpenCRE](https://opencre.org) — the live catalogue, search and map.
- [OpenCRE on GitHub](https://github.com/OWASP/OpenCRE) — source code, data and the REST API.
