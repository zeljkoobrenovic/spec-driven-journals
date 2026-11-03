---
id: "CRE-545-243"
title: "Block execution/output of uploaded files"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-545-243
excerpt: "CRE 545-243 · in Technical application security controls › Input and output protection › File handling · 5 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [545-243](https://opencre.org/cre/545-243)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.5.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v125-file-download) | Verify that direct requests to uploaded files will never be executed as HTML/JavaScript content. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [1](https://capec.mitre.org/data/definitions/1.html) | Accessing Functionality Not Properly Constrained by ACLs | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [434](https://cwe.mitre.org/data/definitions/434.html) | Unrestricted Upload of File with Dangerous Type | curated |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-09](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/09-Test_Upload_of_Malicious_Files.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100022](https://github.com/zaproxy/community-scripts/blob/main/passive/Upload%20form%20discovery.js) | Upload Form Discovered | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [545-243](https://opencre.org/cre/545-243). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
