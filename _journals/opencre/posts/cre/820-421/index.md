---
id: "CRE-820-421"
title: "Authenticate HTTP headers added by a trusted proxy or SSO device"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-820-421
excerpt: "CRE 820-421 · in Technical application security controls › Input and output protection › Validate HTTP request headers · 11 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [820-421](https://opencre.org/cre/820-421)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-541-441]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.5.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v145-http-request-header-validation) | Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [12](https://capec.mitre.org/data/definitions/12.html) | Choosing Message Identifier | automatic |
| [36](https://capec.mitre.org/data/definitions/36.html) | Using Unpublished Interfaces or Functionality | automatic |
| [62](https://capec.mitre.org/data/definitions/62.html) | Cross Site Request Forgery | automatic |
| [166](https://capec.mitre.org/data/definitions/166.html) | Force the System to Reset Values | automatic |
| [216](https://capec.mitre.org/data/definitions/216.html) | Communication Channel Manipulation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [306](https://cwe.mitre.org/data/definitions/306.html) | Missing Authentication for Critical Function | curated |
| [288](https://cwe.mitre.org/data/definitions/288.html) | Authentication Bypass Using an Alternate Path or Channel | automatic |
| [322](https://cwe.mitre.org/data/definitions/322.html) | Key Exchange without Entity Authentication | automatic |
| [425](https://cwe.mitre.org/data/definitions/425.html) | Direct Request ('Forced Browsing') | automatic |
| [1299](https://cwe.mitre.org/data/definitions/1299.html) | Missing Protection Mechanism for Alternate Hardware Interface | automatic |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [820-421](https://opencre.org/cre/820-421). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
