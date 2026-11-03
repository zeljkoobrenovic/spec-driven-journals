---
id: "CRE-481-710"
title: "AI model poisoning"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-481-710
excerpt: "CRE 481-710 · in Cross-cutting concerns › Protection against AI-Specfic Threats › AI model behaviour integrity threats · 4 sub-requirements · 3 mappings to 3 standards and tools."
tags: ENISA, MITRE ATLAS, OWASP Top10 for LLM
---
> **CRE**: [481-710](https://opencre.org/cre/481-710)
>
> **Part of**: [[cre-546-564]] › [[cre-803-457]] › [[cre-061-753]]
>
> **Maps to**: [[standard-enisa]], [[standard-mitre-atlas]], [[standard-owasp-top10-for-llm]]

## Where It Sits

---begin mermaid---
graph LR
  n061753["AI model behaviour integrity threats"] --> n481710["AI model poisoning"]
  n481710 --> n615663["Data poisoning of train/finetune/augmentation…"]
  n481710 --> n867642["Direct development-time model poisoning"]
  n481710 --> n020540["Direct runtime model poisoning"]
  n481710 --> n701654["Supply-chain model poisoning"]
  style n481710 stroke-width:3px
---end mermaid---

## Contains

- [[cre-615-663]]
- [[cre-867-642]]
- [[cre-020-540]]
- [[cre-701-654]]

## Related CREs

- [[cre-641-760]]
- [[cre-041-188]]
- [[cre-146-871]]
- [[cre-234-123]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ENISA

| ID | Section | Link |
| --- | --- | --- |
| [Table 3:](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms) | Poisoning | curated |

More: [[standard-enisa]]

### MITRE ATLAS

| ID | Section | Link |
| --- | --- | --- |
| [AML.T0020](https://atlas.mitre.org/techniques/AML.T0020) | Poison Training Data | curated |

More: [[standard-mitre-atlas]]

### OWASP Top10 for LLM

| ID | Section | Link |
| --- | --- | --- |
| [LLM04:2025](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/) | Data and Model Poisoning: Parent threat node | curated |

More: [[standard-owasp-top10-for-llm]]

## Source

Generated from the OpenCRE catalogue entry [481-710](https://opencre.org/cre/481-710). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
