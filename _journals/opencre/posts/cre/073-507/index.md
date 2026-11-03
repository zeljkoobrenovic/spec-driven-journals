---
id: "CRE-073-507"
title: "AI model behaviour integrity threats through inference"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-073-507
excerpt: "CRE 073-507 · in Cross-cutting concerns › Protection against AI-Specfic Threats › AI model behaviour integrity threats · 3 sub-requirements · 2 mappings to 1 standard and tool."
tags: ENISA
---
> **CRE**: [073-507](https://opencre.org/cre/073-507)
>
> **Part of**: [[cre-546-564]] › [[cre-803-457]] › [[cre-061-753]]
>
> **Maps to**: [[standard-enisa]]

## Where It Sits

---begin mermaid---
graph LR
  n061753["AI model behaviour integrity threats"] --> n073507["AI model behaviour integrity threats through…"]
  n073507 --> n686110["Direct prompt injection"]
  n073507 --> n370877["Evasion (e.g. adversarial examples)"]
  n073507 --> n012625["Indirect prompt injection"]
  style n073507 stroke-width:3px
---end mermaid---

## Contains

- [[cre-686-110]]
- [[cre-370-877]]
- [[cre-012-625]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ENISA

| ID | Section | Link |
| --- | --- | --- |
| [Table 3:](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms) | Evasion | curated |
|  | Use of adversarial examples crafted in white or grey box conditions (e.g. FGSM...) | curated |

More: [[standard-enisa]]

## Source

Generated from the OpenCRE catalogue entry [073-507](https://opencre.org/cre/073-507). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
