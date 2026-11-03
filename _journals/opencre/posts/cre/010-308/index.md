---
id: "CRE-010-308"
title: "Input validation"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-010-308
excerpt: "CRE 010-308 · in Technical application security controls › Input and output protection · 8 sub-requirements · 1 mapping to 1 standard and tool."
tags: OWASP Cheat Sheets
---
> **CRE**: [010-308](https://opencre.org/cre/010-308)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]]
>
> **Maps to**: [[standard-owasp-cheat-sheets]]

## Where It Sits

---begin mermaid---
graph LR
  n503455["Input and output protection"] --> n010308["Input validation"]
  n010308 --> n848711["Enforce input validation on a trusted service…"]
  n010308 --> n146706["Enforce JSON schema before processing"]
  n010308 --> n653242["Enforce schema on type/contents of structured…"]
  n010308 --> n176154["Monitor expectation of usage intensity (e.g.…"]
  n010308 --> n042550["Protect against mass parameter assignment attack"]
  n010308 --> n743237["Validatie/enforce HTTP inputs (against HTTP p…"]
  n010308 --> n031447["Whitelist all external (HTTP) input"]
  n010308 --> n232217["Whitelist redirected/forwarded URLs"]
  style n010308 stroke-width:3px
---end mermaid---

## Contains

- [[cre-848-711]]
- [[cre-146-706]]
- [[cre-653-242]]
- [[cre-176-154]]
- [[cre-042-550]]
- [[cre-743-237]]
- [[cre-031-447]]
- [[cre-232-217]]

## Related CREs

- [[cre-760-764]]
- [[cre-760-765]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [010-308](https://opencre.org/cre/010-308). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
