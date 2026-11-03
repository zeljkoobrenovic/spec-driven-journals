---
id: "CRE-675-168"
title: "Sanitize filename metadata from untrusted origin if processing is required"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-675-168
excerpt: "CRE 675-168 · in Technical application security controls › Input and output protection › File handling › File execution · 31 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [675-168](https://opencre.org/cre/675-168)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-451-082]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v123-file-execution) | Verify that user-submitted filename metadata is not used directly by system or framework filesystems and that a URL API is used to protect against path traversal. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [64](https://capec.mitre.org/data/definitions/64.html) | Using Slashes and URL Encoding Combined to Bypass Validation Logic | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [78](https://capec.mitre.org/data/definitions/78.html) | Using Escaped Slashes in Alternate Encoding | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [126](https://capec.mitre.org/data/definitions/126.html) | Path Traversal | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [22](https://cwe.mitre.org/data/definitions/22.html) | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') | curated |
| [23](https://cwe.mitre.org/data/definitions/23.html) | Relative Path Traversal | automatic |
| [24](https://cwe.mitre.org/data/definitions/24.html) | Path Traversal: '../filedir' | automatic |
| [25](https://cwe.mitre.org/data/definitions/25.html) | Path Traversal: '/../filedir' | automatic |
| [26](https://cwe.mitre.org/data/definitions/26.html) | Path Traversal: '/dir/../filename' | automatic |
| [27](https://cwe.mitre.org/data/definitions/27.html) | Path Traversal: 'dir/../../filename' | automatic |
| [28](https://cwe.mitre.org/data/definitions/28.html) | Path Traversal: '..\filedir' | automatic |
| [29](https://cwe.mitre.org/data/definitions/29.html) | Path Traversal: '\..\filename' | automatic |
| [30](https://cwe.mitre.org/data/definitions/30.html) | Path Traversal: '\dir\..\filename' | automatic |
| [31](https://cwe.mitre.org/data/definitions/31.html) | Path Traversal: 'dir\..\..\filename' | automatic |
| [32](https://cwe.mitre.org/data/definitions/32.html) | Path Traversal: '...' (Triple Dot) | automatic |
| [33](https://cwe.mitre.org/data/definitions/33.html) | Path Traversal: '....' (Multiple Dot) | automatic |
| [34](https://cwe.mitre.org/data/definitions/34.html) | Path Traversal: '....//' | automatic |
| [35](https://cwe.mitre.org/data/definitions/35.html) | Path Traversal: '.../...//' | automatic |
| [36](https://cwe.mitre.org/data/definitions/36.html) | Absolute Path Traversal | automatic |
| [37](https://cwe.mitre.org/data/definitions/37.html) | Path Traversal: '/absolute/pathname/here' | automatic |
| [38](https://cwe.mitre.org/data/definitions/38.html) | Path Traversal: '\absolute\pathname\here' | automatic |
| [39](https://cwe.mitre.org/data/definitions/39.html) | Path Traversal: 'C:dirname' | automatic |
| [40](https://cwe.mitre.org/data/definitions/40.html) | Path Traversal: '\\UNC\share\name\' (Windows UNC Share) | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHZ-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [6-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PathTraversalScanRule.java) | Path Traversal | automatic |
| [6-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PathTraversalScanRule.java) | Path Traversal | automatic |
| [6-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PathTraversalScanRule.java) | Path Traversal | automatic |
| [6-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PathTraversalScanRule.java) | Path Traversal | automatic |
| [6-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PathTraversalScanRule.java) | Path Traversal | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [675-168](https://opencre.org/cre/675-168). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
