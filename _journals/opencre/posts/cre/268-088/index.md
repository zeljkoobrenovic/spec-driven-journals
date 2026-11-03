---
id: "CRE-268-088"
title: "Limit query impact GraphQL/data layer expression DoS"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-268-088
excerpt: "CRE 268-088 · in Technical application security controls › Input and output protection › Sanitization and sandboxing · 25 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [268-088](https://opencre.org/cre/268-088)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-764-765]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Related CREs

- [[cre-623-550]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V13.4.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x21-V13-API.md#v134-graphql) | Verify that a query allow list or a combination of depth limiting and amount limiting is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries. For more advanced scenarios, query cost analysis should be used. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [125](https://capec.mitre.org/data/definitions/125.html) | Flooding | automatic |
| [130](https://capec.mitre.org/data/definitions/130.html) | Excessive Allocation | automatic |
| [147](https://capec.mitre.org/data/definitions/147.html) | XML Ping of the Death | automatic |
| [197](https://capec.mitre.org/data/definitions/197.html) | Exponential Data Expansion | automatic |
| [229](https://capec.mitre.org/data/definitions/229.html) | Serialized Data Parameter Blowup | automatic |
| [230](https://capec.mitre.org/data/definitions/230.html) | Serialized Data with Nested Payloads | automatic |
| [231](https://capec.mitre.org/data/definitions/231.html) | Oversized Serialized Data Payloads | automatic |
| [469](https://capec.mitre.org/data/definitions/469.html) | HTTP DoS | automatic |
| [482](https://capec.mitre.org/data/definitions/482.html) | TCP Flood | automatic |
| [486](https://capec.mitre.org/data/definitions/486.html) | UDP Flood | automatic |
| [487](https://capec.mitre.org/data/definitions/487.html) | ICMP Flood | automatic |
| [488](https://capec.mitre.org/data/definitions/488.html) | HTTP Flood | automatic |
| [489](https://capec.mitre.org/data/definitions/489.html) | SSL Flood | automatic |
| [490](https://capec.mitre.org/data/definitions/490.html) | Amplification | automatic |
| [491](https://capec.mitre.org/data/definitions/491.html) | Quadratic Data Expansion | automatic |
| [493](https://capec.mitre.org/data/definitions/493.html) | SOAP Array Blowup | automatic |
| [494](https://capec.mitre.org/data/definitions/494.html) | TCP Fragmentation | automatic |
| [495](https://capec.mitre.org/data/definitions/495.html) | UDP Fragmentation | automatic |
| [496](https://capec.mitre.org/data/definitions/496.html) | ICMP Fragmentation | automatic |
| [528](https://capec.mitre.org/data/definitions/528.html) | XML Flood | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [770](https://cwe.mitre.org/data/definitions/770.html) | Allocation of Resources Without Limits or Throttling | curated |
| [774](https://cwe.mitre.org/data/definitions/774.html) | Allocation of File Descriptors or Handles Without Limits or Throttling | automatic |
| [789](https://cwe.mitre.org/data/definitions/789.html) | Memory Allocation with Excessive Size Value | automatic |
| [1325](https://cwe.mitre.org/data/definitions/1325.html) | Improperly Controlled Sequential Memory Allocation | automatic |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [268-088](https://opencre.org/cre/268-088). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
