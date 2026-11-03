---
id: "CRE-366-835"
title: "Escape output against XSS"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-366-835
excerpt: "CRE 366-835 · in Technical application security controls › Input and output protection › Output encoding and injection prevention · 51 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [366-835](https://opencre.org/cre/366-835)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-161-451]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.3.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v53-output-encoding-and-injection-prevention) | Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [18](https://capec.mitre.org/data/definitions/18.html) | XSS Targeting Non-Script Elements | automatic |
| [32](https://capec.mitre.org/data/definitions/32.html) | XSS Through HTTP Query Strings | automatic |
| [63](https://capec.mitre.org/data/definitions/63.html) | Cross-Site Scripting (XSS) | automatic |
| [85](https://capec.mitre.org/data/definitions/85.html) | AJAX Footprinting | automatic |
| [86](https://capec.mitre.org/data/definitions/86.html) | XSS Through HTTP Headers | automatic |
| [193](https://capec.mitre.org/data/definitions/193.html) | PHP Remote File Inclusion | automatic |
| [199](https://capec.mitre.org/data/definitions/199.html) | XSS Using Alternate Syntax | automatic |
| [209](https://capec.mitre.org/data/definitions/209.html) | XSS Using MIME Type Mismatch | automatic |
| [243](https://capec.mitre.org/data/definitions/243.html) | XSS Targeting HTML Attributes | automatic |
| [244](https://capec.mitre.org/data/definitions/244.html) | XSS Targeting URI Placeholders | automatic |
| [588](https://capec.mitre.org/data/definitions/588.html) | DOM-Based XSS | automatic |
| [591](https://capec.mitre.org/data/definitions/591.html) | Reflected XSS | automatic |
| [592](https://capec.mitre.org/data/definitions/592.html) | Stored XSS | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [79](https://cwe.mitre.org/data/definitions/79.html) | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') | curated |
| [80](https://cwe.mitre.org/data/definitions/80.html) | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) | automatic |
| [81](https://cwe.mitre.org/data/definitions/81.html) | Improper Neutralization of Script in an Error Message Web Page | automatic |
| [82](https://cwe.mitre.org/data/definitions/82.html) | Improper Neutralization of Script in Attributes of IMG Tags in a Web Page | automatic |
| [83](https://cwe.mitre.org/data/definitions/83.html) | Improper Neutralization of Script in Attributes in a Web Page | automatic |
| [84](https://cwe.mitre.org/data/definitions/84.html) | Improper Neutralization of Encoded URI Schemes in a Web Page | automatic |
| [85](https://cwe.mitre.org/data/definitions/85.html) | Doubled Character XSS Manipulations | automatic |
| [86](https://cwe.mitre.org/data/definitions/86.html) | Improper Neutralization of Invalid Characters in Identifiers in Web Pages | automatic |
| [87](https://cwe.mitre.org/data/definitions/87.html) | Improper Neutralization of Alternate XSS Syntax | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) | curated |
|  | [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) | curated |
|  | [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C4](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c4-encode-escape-data.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [40012](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java) | Cross Site Scripting (Reflected) | automatic |
| [40014](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PersistentXssScanRule.java) | Cross Site Scripting (Persistent) | automatic |
| [40016](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PersistentXssPrimeScanRule.java) | Cross Site Scripting (Persistent) - Prime | automatic |
| [40017](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/PersistentXssSpiderScanRule.java) | Cross Site Scripting (Persistent) - Spider | automatic |
| [40026](https://github.com/zaproxy/zap-extensions/blob/main/addOns/domxss/src/main/java/org/zaproxy/zap/extension/domxss/DomXssScanRule.java) | Cross Site Scripting (DOM Based) | automatic |
| [40031](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/OutOfBandXssScanRule.java) | Out of Band XSS | automatic |
| [40101](https://github.com/zaproxy/zap-extensions/blob/main/addOns/foxhound/src/main/java/org/zaproxy/zap/extension/foxhound/ExtensionFoxhound.java) | Cross-site Scripting | automatic |
| [40102](https://github.com/zaproxy/zap-extensions/blob/main/addOns/foxhound/src/main/java/org/zaproxy/zap/extension/foxhound/ExtensionFoxhound.java) | Cross-site Scripting | automatic |
| [100014](https://github.com/zaproxy/community-scripts/blob/main/passive/find_reflected_params.py) | Reflected HTTP GET Parameter(s) | automatic |
| [210000-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via inline event handler | automatic |
| [210000-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via Element.innerHTML | automatic |
| [210000-3](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via Element.outerHTML | automatic |
| [210000-4](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via insertAdjacentHTML | automatic |
| [210000-5](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via document.write | automatic |
| [210000-6](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | DOM XSS via DOM mutations | automatic |
| [210003-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | javascript: URL assigned to href | automatic |
| [210003-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | javascript: URL navigated via location.href | automatic |
| [210003-3](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | javascript: URL assigned to iframe.src | automatic |
| [210003-4](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | data: URL assigned to script.src | automatic |
| [210006-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | javascript: URL assigned to form action | automatic |
| [210006-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | javascript: URL assigned to formAction | automatic |
| [210007-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Response field rendered via innerHTML | automatic |
| [210007-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Response field rendered via document.write | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [366-835](https://opencre.org/cre/366-835). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
