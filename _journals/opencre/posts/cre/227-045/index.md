---
id: "CRE-227-045"
title: "Identify sensitive data and subject it to a policy"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-227-045
excerpt: "CRE 227-045 · in Governance processes for security › Security Analysis and documentation › Asset management › Data classification and handling · 151 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, ISO 27001, NIST 800-53 v5, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [227-045](https://opencre.org/cre/227-045)
>
> **Part of**: [[cre-567-755]] › [[cre-766-162]] › [[cre-287-823]] › [[cre-074-873]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.3.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v83-sensitive-private-data) | Verify that all sensitive data created and processed by the application has been identified, and ensure that a policy is in place on how to deal with sensitive data. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [22](https://capec.mitre.org/data/definitions/22.html) | Exploiting Trust in Client | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [95](https://capec.mitre.org/data/definitions/95.html) | WSDL Scanning | automatic |
| [116](https://capec.mitre.org/data/definitions/116.html) | Excavation | automatic |
| [169](https://capec.mitre.org/data/definitions/169.html) | Footprinting | automatic |
| [170](https://capec.mitre.org/data/definitions/170.html) | Web Application Fingerprinting | automatic |
| [224](https://capec.mitre.org/data/definitions/224.html) | Fingerprinting | automatic |
| [285](https://capec.mitre.org/data/definitions/285.html) | ICMP Echo Request Ping | automatic |
| [287](https://capec.mitre.org/data/definitions/287.html) | TCP SYN Scan | automatic |
| [290](https://capec.mitre.org/data/definitions/290.html) | Enumerate Mail Exchange (MX) Records | automatic |
| [291](https://capec.mitre.org/data/definitions/291.html) | DNS Zone Transfers | automatic |
| [292](https://capec.mitre.org/data/definitions/292.html) | Host Discovery | automatic |
| [293](https://capec.mitre.org/data/definitions/293.html) | Traceroute Route Enumeration | automatic |
| [294](https://capec.mitre.org/data/definitions/294.html) | ICMP Address Mask Request | automatic |
| [295](https://capec.mitre.org/data/definitions/295.html) | Timestamp Request | automatic |
| [296](https://capec.mitre.org/data/definitions/296.html) | ICMP Information Request | automatic |
| [297](https://capec.mitre.org/data/definitions/297.html) | TCP ACK Ping | automatic |
| [298](https://capec.mitre.org/data/definitions/298.html) | UDP Ping | automatic |
| [299](https://capec.mitre.org/data/definitions/299.html) | TCP SYN Ping | automatic |
| [300](https://capec.mitre.org/data/definitions/300.html) | Port Scanning | automatic |
| [301](https://capec.mitre.org/data/definitions/301.html) | TCP Connect Scan | automatic |
| [302](https://capec.mitre.org/data/definitions/302.html) | TCP FIN Scan | automatic |
| [303](https://capec.mitre.org/data/definitions/303.html) | TCP Xmas Scan | automatic |
| [304](https://capec.mitre.org/data/definitions/304.html) | TCP Null Scan | automatic |
| [305](https://capec.mitre.org/data/definitions/305.html) | TCP ACK Scan | automatic |
| [306](https://capec.mitre.org/data/definitions/306.html) | TCP Window Scan | automatic |
| [307](https://capec.mitre.org/data/definitions/307.html) | TCP RPC Scan | automatic |
| [308](https://capec.mitre.org/data/definitions/308.html) | UDP Scan | automatic |
| [309](https://capec.mitre.org/data/definitions/309.html) | Network Topology Mapping | automatic |
| [310](https://capec.mitre.org/data/definitions/310.html) | Scanning for Vulnerable Software | automatic |
| [312](https://capec.mitre.org/data/definitions/312.html) | Active OS Fingerprinting | automatic |
| [313](https://capec.mitre.org/data/definitions/313.html) | Passive OS Fingerprinting | automatic |
| [317](https://capec.mitre.org/data/definitions/317.html) | IP ID Sequencing Probe | automatic |
| [318](https://capec.mitre.org/data/definitions/318.html) | IP 'ID' Echoed Byte-Order Probe | automatic |
| [319](https://capec.mitre.org/data/definitions/319.html) | IP (DF) 'Don't Fragment Bit' Echoing Probe | automatic |
| [320](https://capec.mitre.org/data/definitions/320.html) | TCP Timestamp Probe | automatic |
| [321](https://capec.mitre.org/data/definitions/321.html) | TCP Sequence Number Probe | automatic |
| [322](https://capec.mitre.org/data/definitions/322.html) | TCP (ISN) Greatest Common Divisor Probe | automatic |
| [323](https://capec.mitre.org/data/definitions/323.html) | TCP (ISN) Counter Rate Probe | automatic |
| [324](https://capec.mitre.org/data/definitions/324.html) | TCP (ISN) Sequence Predictability Probe | automatic |
| [325](https://capec.mitre.org/data/definitions/325.html) | TCP Congestion Control Flag (ECN) Probe | automatic |
| [326](https://capec.mitre.org/data/definitions/326.html) | TCP Initial Window Size Probe | automatic |
| [327](https://capec.mitre.org/data/definitions/327.html) | TCP Options Probe | automatic |
| [328](https://capec.mitre.org/data/definitions/328.html) | TCP 'RST' Flag Checksum Probe | automatic |
| [329](https://capec.mitre.org/data/definitions/329.html) | ICMP Error Message Quoting Probe | automatic |
| [330](https://capec.mitre.org/data/definitions/330.html) | ICMP Error Message Echoing Integrity Probe | automatic |
| [464](https://capec.mitre.org/data/definitions/464.html) | Evercookie | automatic |
| [467](https://capec.mitre.org/data/definitions/467.html) | Cross Site Identification | automatic |
| [472](https://capec.mitre.org/data/definitions/472.html) | Browser Fingerprinting | automatic |
| [497](https://capec.mitre.org/data/definitions/497.html) | File Discovery | automatic |
| [498](https://capec.mitre.org/data/definitions/498.html) | Probe iOS Screenshots | automatic |
| [508](https://capec.mitre.org/data/definitions/508.html) | Shoulder Surfing | automatic |
| [560](https://capec.mitre.org/data/definitions/560.html) | Use of Known Domain Credentials | automatic |
| [573](https://capec.mitre.org/data/definitions/573.html) | Process Footprinting | automatic |
| [574](https://capec.mitre.org/data/definitions/574.html) | Services Footprinting | automatic |
| [575](https://capec.mitre.org/data/definitions/575.html) | Account Footprinting | automatic |
| [576](https://capec.mitre.org/data/definitions/576.html) | Group Permission Footprinting | automatic |
| [577](https://capec.mitre.org/data/definitions/577.html) | Owner Footprinting | automatic |
| [616](https://capec.mitre.org/data/definitions/616.html) | Establish Rogue Location | automatic |
| [643](https://capec.mitre.org/data/definitions/643.html) | Identify Shared Files/Directories on System | automatic |
| [646](https://capec.mitre.org/data/definitions/646.html) | Peripheral Footprinting | automatic |
| [651](https://capec.mitre.org/data/definitions/651.html) | Eavesdropping | automatic |
| [694](https://capec.mitre.org/data/definitions/694.html) | System Location Discovery | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information to an Unauthorized Actor | curated |
| [201](https://cwe.mitre.org/data/definitions/201.html) | Insertion of Sensitive Information Into Sent Data | automatic |
| [203](https://cwe.mitre.org/data/definitions/203.html) | Observable Discrepancy | automatic |
| [204](https://cwe.mitre.org/data/definitions/204.html) | Observable Response Discrepancy | automatic |
| [205](https://cwe.mitre.org/data/definitions/205.html) | Observable Behavioral Discrepancy | automatic |
| [206](https://cwe.mitre.org/data/definitions/206.html) | Observable Internal Behavioral Discrepancy | automatic |
| [207](https://cwe.mitre.org/data/definitions/207.html) | Observable Behavioral Discrepancy With Equivalent Products | automatic |
| [208](https://cwe.mitre.org/data/definitions/208.html) | Observable Timing Discrepancy | automatic |
| [209](https://cwe.mitre.org/data/definitions/209.html) | Generation of Error Message Containing Sensitive Information | automatic |
| [210](https://cwe.mitre.org/data/definitions/210.html) | Self-generated Error Message Containing Sensitive Information | automatic |
| [211](https://cwe.mitre.org/data/definitions/211.html) | Externally-Generated Error Message Containing Sensitive Information | automatic |
| [213](https://cwe.mitre.org/data/definitions/213.html) | Exposure of Sensitive Information Due to Incompatible Policies | automatic |
| [214](https://cwe.mitre.org/data/definitions/214.html) | Invocation of Process Using Visible Sensitive Information | automatic |
| [215](https://cwe.mitre.org/data/definitions/215.html) | Insertion of Sensitive Information Into Debugging Code | automatic |
| [359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information to an Unauthorized Actor | automatic |
| [497](https://cwe.mitre.org/data/definitions/497.html) | Exposure of Sensitive System Information to an Unauthorized Control Sphere | automatic |
| [531](https://cwe.mitre.org/data/definitions/531.html) | Inclusion of Sensitive Information in Test Code | automatic |
| [532](https://cwe.mitre.org/data/definitions/532.html) | Insertion of Sensitive Information into Log File | automatic |
| [535](https://cwe.mitre.org/data/definitions/535.html) | Exposure of Information Through Shell Error Message | automatic |
| [536](https://cwe.mitre.org/data/definitions/536.html) | Servlet Runtime Error Message Containing Sensitive Information | automatic |
| [537](https://cwe.mitre.org/data/definitions/537.html) | Java Runtime Error Message Containing Sensitive Information | automatic |
| [538](https://cwe.mitre.org/data/definitions/538.html) | Insertion of Sensitive Information into Externally-Accessible File or Directory | automatic |
| [540](https://cwe.mitre.org/data/definitions/540.html) | Inclusion of Sensitive Information in Source Code | automatic |
| [541](https://cwe.mitre.org/data/definitions/541.html) | Inclusion of Sensitive Information in an Include File | automatic |
| [548](https://cwe.mitre.org/data/definitions/548.html) | Exposure of Information Through Directory Listing | automatic |
| [550](https://cwe.mitre.org/data/definitions/550.html) | Server-generated Error Message Containing Sensitive Information | automatic |
| [598](https://cwe.mitre.org/data/definitions/598.html) | Use of HTTP Request With Sensitive Query String | automatic |
| [615](https://cwe.mitre.org/data/definitions/615.html) | Inclusion of Sensitive Information in Source Code Comments | automatic |
| [651](https://cwe.mitre.org/data/definitions/651.html) | Exposure of WSDL File Containing Sensitive Information | automatic |
| [1254](https://cwe.mitre.org/data/definitions/1254.html) | Incorrect Comparison Logic Granularity | automatic |
| [1255](https://cwe.mitre.org/data/definitions/1255.html) | Comparison Logic is Vulnerable to Power Side-Channel Attacks | automatic |
| [1273](https://cwe.mitre.org/data/definitions/1273.html) | Device Unlock Credential Sharing | automatic |
| [1295](https://cwe.mitre.org/data/definitions/1295.html) | Debug Messages Revealing Unnecessary Information | automatic |
| [1300](https://cwe.mitre.org/data/definitions/1300.html) | Improper Protection of Physical Side Channels | automatic |
| [1303](https://cwe.mitre.org/data/definitions/1303.html) | Non-Transparent Sharing of Microarchitectural Resources | automatic |
| [1431](https://cwe.mitre.org/data/definitions/1431.html) | Driving Intermediate Cryptographic State/Results to Hardware Module Outputs | automatic |

More: [[standard-cwe]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 5.32 | Intellectual property rights | curated |
| 5.33 | Protection of records | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-12 Information Management and Retention](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-12) | curated |

More: [[standard-nist-800-53-v5]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C8](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c8-protect-data-everywhere.html) | curated |

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoPrivateAddressDisclosureScanRule.java) | Private IP Disclosure | automatic |
| [10009](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InPageBannerInfoLeakScanRule.java) | In Page Banner Information Leak | automatic |
| [10036-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java) | Server Leaks its Webserver Application via \Server\ HTTP Response Header Field | automatic |
| [10036-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java) | Server Leaks Version Information via \Server\ HTTP Response Header Field | automatic |
| [10037](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XPoweredByHeaderInfoLeakScanRule.java) | Server Leaks Information via \X-Powered-By\ HTTP Response Header Field(s) | automatic |
| [10039](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XBackendServerInformationLeakScanRule.java) | X-Backend-Server Header Information Leak | automatic |
| [10062](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PiiScanRule.java) | PII Disclosure | automatic |
| [10096](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/TimestampDisclosureScanRule.java) | Timestamp Disclosure - Unix | automatic |
| [10097-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - LanMan / DES | automatic |
| [10097-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - Kerberos AFS DES | automatic |
| [10097-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - OpenBSD Blowfish | automatic |
| [10097-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - MD5 Crypt | automatic |
| [10097-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-256 Crypt | automatic |
| [10097-6](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-512 Crypt | automatic |
| [10097-7](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - BCrypt | automatic |
| [10097-8](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - NTLM | automatic |
| [10097-9](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - Salted SHA-1 | automatic |
| [10097-10](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-512 | automatic |
| [10097-11](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-384 | automatic |
| [10097-12](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-256 | automatic |
| [10097-13](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-224 | automatic |
| [10097-14](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-1 | automatic |
| [10097-15](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - LanMan | automatic |
| [10097-16](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - MD4 / MD5 | automatic |
| [10103](https://github.com/zaproxy/zap-extensions/blob/main/addOns/imagelocationscanner/src/main/java/org/zaproxy/zap/extension/imagelocationscanner/ImageLocationScanRule.java) | Image Exposes Location or Privacy Data | automatic |
| [40029](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/TraceAxdScanRule.java) | Trace.axd Information Leak | automatic |
| [40034](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/EnvFileScanRule.java) | .env Information Leak | automatic |
| [40035](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/HiddenFilesScanRule.java) | Hidden File Found | automatic |
| [40042](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SpringActuatorScanRule.java) | Spring Actuator Information Leak | automatic |
| [100002](https://github.com/zaproxy/community-scripts/blob/main/passive/clacks.js) | Server is running on Clacks - GNU Terry Pratchett | automatic |
| [100004](https://github.com/zaproxy/community-scripts/blob/main/passive/detect_csp_notif_and_reportonly.js) | Content Security Policy Violations Reporting Enabled | automatic |
| [100012](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20IBANs.js) | Information Disclosure - IBAN Numbers | automatic |
| [100013](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20Internal%20IPs.js) | Information Disclosure - Private IP Address | automatic |
| [100019](https://github.com/zaproxy/community-scripts/blob/main/passive/Server%20Header%20Disclosure.js) | Information Disclosure - Server Header | automatic |
| [100023](https://github.com/zaproxy/community-scripts/blob/main/passive/X-Powered-By_header_checker.js) | Information Disclosure - X-Powered-By Header | automatic |
| [100034](https://github.com/zaproxy/community-scripts/blob/main/passive/google_api_keys_finder.js) | Information Disclosure - Google API Key | automatic |
| [100036](https://github.com/zaproxy/community-scripts/blob/main/passive/s3.js) | Information Disclosure - Amazon S3 Bucket URL | automatic |
| [110004](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/Email%20Disclosure.js) | Email address found in WebSocket message | automatic |
| [110005](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/PII%20Disclosure.js) | Personally Identifiable Information via WebSocket | automatic |
| [110008](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/XML%20Comments%20Disclosure.js) | Information Disclosure - Suspicious Comments in XML via WebSocket | automatic |
| [120000-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/InformationInStorageScanRule.java) | Information Disclosure - Information in Browser localStorage | automatic |
| [120000-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/InformationInStorageScanRule.java) | Information Disclosure - Information in Browser sessionStorage | automatic |
| [120001-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/SensitiveInfoInStorageScanRule.java) | Information Disclosure - Sensitive Information in Browser localStorage | automatic |
| [120001-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/SensitiveInfoInStorageScanRule.java) | Information Disclosure - Sensitive Information in Browser sessionStorage | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [227-045](https://opencre.org/cre/227-045). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
