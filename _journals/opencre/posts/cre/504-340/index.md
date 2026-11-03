---
id: "CRE-504-340"
title: "Encrypt sensitive data with algorithms that provide both confidentiality and integrity"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-504-340
excerpt: "CRE 504-340 · in Technical application security controls › Secure data storage › Encrypt data at rest · 19 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [504-340](https://opencre.org/cre/504-340)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.3.7](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v83-sensitive-private-data) | Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [97](https://capec.mitre.org/data/definitions/97.html) | Cryptanalysis | automatic |
| [459](https://capec.mitre.org/data/definitions/459.html) | Creating a Rogue Certification Authority Certificate | automatic |
| [473](https://capec.mitre.org/data/definitions/473.html) | Signature Spoof | automatic |
| [475](https://capec.mitre.org/data/definitions/475.html) | Signature Spoofing by Improper Validation | automatic |
| [608](https://capec.mitre.org/data/definitions/608.html) | Cryptanalysis of Cellular Encryption | automatic |
| [614](https://capec.mitre.org/data/definitions/614.html) | Rooting SIM Cards | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [327](https://cwe.mitre.org/data/definitions/327.html) | Use of a Broken or Risky Cryptographic Algorithm | curated |
| [325](https://cwe.mitre.org/data/definitions/325.html) | Missing Cryptographic Step | automatic |
| [328](https://cwe.mitre.org/data/definitions/328.html) | Use of Weak Hash | automatic |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |
| [780](https://cwe.mitre.org/data/definitions/780.html) | Use of RSA Algorithm without OAEP | automatic |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | automatic |
| [1240](https://cwe.mitre.org/data/definitions/1240.html) | Use of a Cryptographic Primitive with a Risky Implementation | automatic |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C8](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c8-protect-data-everywhere.html) | curated |

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100010](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20Hashes.js) | Information Disclosure - Hash | automatic |
| [100021](https://github.com/zaproxy/community-scripts/blob/main/passive/Telerik%20Using%20Poor%20Crypto.js) | Telerik UI for ASP.NET AJAX Cryptographic Weakness (CVE-2017-9248) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [504-340](https://opencre.org/cre/504-340). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
