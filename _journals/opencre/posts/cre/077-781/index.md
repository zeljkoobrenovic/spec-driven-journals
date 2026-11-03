---
id: "CRE-077-781"
title: "Use separately stored secret salt (pepper)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-077-781
excerpt: "CRE 077-781 · in Technical application security controls › Secure data storage › Secret storage · 7 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Cheat Sheets
---
> **CRE**: [077-781](https://opencre.org/cre/077-781)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-223-780]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.4.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v24-credential-storage) | Verify that an additional iteration of a key derivation function is performed, using a salt value that is secret and known only to the verifier. Generate the salt value using an approved random bit generator (SP 800-90Ar1) and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | curated |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [077-781](https://opencre.org/cre/077-781). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
