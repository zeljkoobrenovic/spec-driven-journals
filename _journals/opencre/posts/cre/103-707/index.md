---
id: "CRE-103-707"
title: "Allow unicode in passwords"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-103-707
excerpt: "CRE 103-707 · in Technical application security controls › Authentication › Credentials directives · 13 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63
---
> **CRE**: [103-707](https://opencre.org/cre/103-707)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-455-885]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.1.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v21-password-security) | Verify that any printable Unicode character, including language neutral characters such as spaces and Emojis are permitted in passwords. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [16](https://capec.mitre.org/data/definitions/16.html) | Dictionary-based Password Attack | automatic |
| [49](https://capec.mitre.org/data/definitions/49.html) | Password Brute Forcing | automatic |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |
| [70](https://capec.mitre.org/data/definitions/70.html) | Try Common or Default Usernames and Passwords | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [509](https://capec.mitre.org/data/definitions/509.html) | Kerberoasting | automatic |
| [555](https://capec.mitre.org/data/definitions/555.html) | Remote Services with Stolen Credentials | automatic |
| [561](https://capec.mitre.org/data/definitions/561.html) | Windows Admin Shares with Stolen Credentials | automatic |
| [565](https://capec.mitre.org/data/definitions/565.html) | Password Spraying | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [521](https://cwe.mitre.org/data/definitions/521.html) | Weak Password Requirements | curated |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |

More: [[standard-nist-800-63]]

## Source

Generated from the OpenCRE catalogue entry [103-707](https://opencre.org/cre/103-707). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
