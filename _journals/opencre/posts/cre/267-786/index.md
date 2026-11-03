---
id: "CRE-267-786"
title: "Model confidentiality threats"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-267-786
excerpt: "CRE 267-786 · in Cross-cutting concerns › Protection against AI-Specfic Threats · 3 sub-requirements · 2 mappings to 2 standards and tools."
tags: ENISA, MITRE ATLAS
---
> **CRE**: [267-786](https://opencre.org/cre/267-786)
>
> **Part of**: [[cre-546-564]] › [[cre-803-457]]
>
> **Maps to**: [[standard-enisa]], [[standard-mitre-atlas]]

## Where It Sits

---begin mermaid---
graph LR
  n803457["Protection against AI-Specfic Threats"] --> n267786["Model confidentiality threats"]
  n267786 --> n342781["Direct development-time model leak"]
  n267786 --> n182732["Direct runtime model leak"]
  n267786 --> n141385["Model exfiltration"]
  style n267786 stroke-width:3px
---end mermaid---

## Contains

- [[cre-342-781]]
- [[cre-182-732]]
- [[cre-141-385]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ENISA

| ID | Section | Link |
| --- | --- | --- |
| [Table 3:](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms) | Model disclosure | curated |

More: [[standard-enisa]]

### MITRE ATLAS

| ID | Section | Link |
| --- | --- | --- |
| [AML.T0024.002](https://atlas.mitre.org/techniques/AML.T0024.002) | Exfiltration via AI Inference API: Extract AI Model | curated |

More: [[standard-mitre-atlas]]

## Source

Generated from the OpenCRE catalogue entry [267-786](https://opencre.org/cre/267-786). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
