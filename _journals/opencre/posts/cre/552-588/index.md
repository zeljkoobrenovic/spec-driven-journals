---
id: "CRE-552-588"
title: "Detect and prevent unusual activity"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-552-588
excerpt: "CRE 552-588 · in Technical application security controls › Robust business logic · 5 sub-requirements · 3 mappings to 1 standard and tool."
tags: PCI DSS
---
> **CRE**: [552-588](https://opencre.org/cre/552-588)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]]
>
> **Maps to**: [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n854643["Robust business logic"] --> n552588["Detect and prevent unusual activity"]
  n552588 --> n725682["Enable configurable alert against usage anoma…"]
  n552588 --> n534605["Enforce natural sequence of business flows to…"]
  n552588 --> n660867["Implement business logic limits against ident…"]
  n552588 --> n456535["Monitor for realistic 'human time' business l…"]
  n552588 --> n418853["Monitor unusual activities on system"]
  style n552588 stroke-width:3px
---end mermaid---

## Contains

- [[cre-725-682]]
- [[cre-534-605]]
- [[cre-660-867]]
- [[cre-456-535]]
- [[cre-418-853]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 9.5.1.2 | POI device surfaces are periodically inspected to detect tampering and unauthorized substitution. (CUSTOMIZED APPROACH OBJECTIVE): Point of Interaction Devices cannot be tampered with, substituted without authorization, or have skimming attachments installed without timely detection. | automatic |
| 10.4.3 | Exceptions and anomalies identified during the review process are addressed. (CUSTOMIZED APPROACH OBJECTIVE): Suspicious or anomalous activities are addressed. | automatic |
| A3.5.1 | A methodology is implemented for the prompt identification of attack patterns and undesirable behavior across systems that includes: () Identification of anomalies or suspicious activity as it occurs. () Issuance of prompt alerts upon detection of suspicious activity or anomaly to responsible personnel. () Response to alerts in accordance with documented response procedures. PCI DSS Reference: Requirements 10, 12 (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [552-588](https://opencre.org/cre/552-588). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
