---
id: "CRE-841-757"
title: "Use approved cryptographic algorithms in generation, seeding and verification of OTPs"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-841-757
excerpt: "CRE 841-757 · in Technical application security controls › Authentication › Authentication mechanism › MFA/OTP · 12 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, ZAP Rule
---
> **CRE**: [841-757](https://opencre.org/cre/841-757)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]] › [[cre-062-850]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-zap-rule]]

## Related CREs

- [[cre-170-772]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.8.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v28-one-time-verifier) | Verify that approved cryptographic algorithms are used in the generation, seeding, and verification of OTPs. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [192](https://capec.mitre.org/data/definitions/192.html) | Protocol Analysis | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [326](https://cwe.mitre.org/data/definitions/326.html) | Inadequate Encryption Strength | curated |
| [328](https://cwe.mitre.org/data/definitions/328.html) | Use of Weak Hash | automatic |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.4.2 | curated |
|  | 5.1.5.2 | curated |

More: [[standard-nist-800-63]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10105-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java) | Weak Authentication Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [841-757](https://opencre.org/cre/841-757). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
