---
id: "CRE-555-048"
title: "Log events sufficiently to recreate their order"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-555-048
excerpt: "CRE 555-048 · in Technical application security controls › Logging and error handling › Log relevant · 5 mappings to 4 standards and tools."
tags: ASVS, CWE, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [555-048](https://opencre.org/cre/555-048)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-402-706]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.1.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v71-log-content) | Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [778](https://cwe.mitre.org/data/definitions/778.html) | Insufficient Logging | curated |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C9](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c9-implement-security-logging-monitoring.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 10.2.2 | Audit logs record the following details for each auditable event: () User identification. () Type of event. () Date and time. () Success and failure indication. () Origination of event. () Identity or name of affected data, system component, resource, or service (for example, name and protocol). (CUSTOMIZED APPROACH OBJECTIVE): Sufficient data to be able to identify successful and failed attempts and who, what, when, where, and how for each event listed in requirement 10.2.1 are captured. | automatic |
| 10.5.1 | Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis. (CUSTOMIZED APPROACH OBJECTIVE): Historical records of activity are available immediately to support incident response and are retained for at least 12 months. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [555-048](https://opencre.org/cre/555-048). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
