---
id: "CRE-586-842"
title: "Secure user management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-586-842
excerpt: "CRE 586-842 · in Technical application security controls · 7 sub-requirements · 3 mappings to 2 standards and tools."
tags: OWASP Top 10 2021, PCI DSS
---
> **CRE**: [586-842](https://opencre.org/cre/586-842)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-owasp-top-10-2021]], [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n586842["Secure user management"]
  n586842 --> n327505["Change password with presence of old and new…"]
  n586842 --> n065183["Disallow default credentials"]
  n586842 --> n813610["Do not use static secrets"]
  n586842 --> n138448["Inform users for authentication renewal"]
  n586842 --> n235658["Notify user about credential change"]
  n586842 --> n808425["Notify users about anomalies in their usage p…"]
  n586842 --> n751176["Offer password changing functionality"]
  style n586842 stroke-width:3px
---end mermaid---

## Contains

- [[cre-327-505]]
- [[cre-065-183]]
- [[cre-813-610]]
- [[cre-138-448]]
- [[cre-235-658]]
- [[cre-808-425]]
- [[cre-751-176]]

## Related CREs

- [[cre-673-736]]
- [[cre-123-124]]
- [[cre-724-770]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A07](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) | Identification and Authentication Failures | curated |

More: [[standard-owasp-top-10-2021]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.2 | User identification and related accounts for users and administrators are strictly managed throughout an account’s lifecycle. | automatic |
| 8.2.4 | Addition, deletion, and modification of user IDs, authentication factors, and other identifier objects are managed as follows: () Authorized with the appropriate approval. () Implemented with only the privileges specified on the documented approval. (CUSTOMIZED APPROACH OBJECTIVE): Lifecycle events for user IDs and authentication factors cannot occur without appropriate authorization. (APPLICABILITY NOTES): This requirement applies to all user accounts, including employees, contractors, consultants, temporary workers, and third-party vendors. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [586-842](https://opencre.org/cre/586-842). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
