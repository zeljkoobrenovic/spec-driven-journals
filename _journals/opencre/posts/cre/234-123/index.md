---
id: "CRE-234-123"
title: "Weakening training set backdoors"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-234-123
excerpt: "CRE 234-123 · in Technical application security controls › Technical AI security controls › AI engineering controls · 4 sub-requirements · 2 mappings to 2 standards and tools."
tags: ENISA, ETSI
---
> **CRE**: [234-123](https://opencre.org/cre/234-123)
>
> **Part of**: [[cre-636-660]] › [[cre-663-200]] › [[cre-041-173]]
>
> **Maps to**: [[standard-enisa]], [[standard-etsi]]

## Where It Sits

---begin mermaid---
graph LR
  n041173["AI engineering controls"] --> n234123["Weakening training set backdoors"]
  n234123 --> n854183["Benign fine-tuning and pruning"]
  n234123 --> n444058["Benign train data increase"]
  n234123 --> n788323["Model size reduction"]
  n234123 --> n567025["Train data distortion"]
  style n234123 stroke-width:3px
---end mermaid---

## Contains

- [[cre-854-183]]
- [[cre-444-058]]
- [[cre-788-323]]
- [[cre-567-025]]

## Related CREs

- [[cre-481-710]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ENISA

| ID | Section | Link |
| --- | --- | --- |
| [Table 5:](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms) | Integrate poisoning control after the "model evaluation" phase | curated |

More: [[standard-enisa]]

### ETSI

| ID | Section | Link |
| --- | --- | --- |
| [5.3](https://www.etsi.org/deliver/etsi_gr/SAI/001_099/005/01.01.01_60/gr_SAI005v010101p.pdf) | Mitigating backdoor attacks | curated |

More: [[standard-etsi]]

## Source

Generated from the OpenCRE catalogue entry [234-123](https://opencre.org/cre/234-123). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
