---
id: "CRE-117-371"
title: "Use a centralized access control mechanism"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-117-371
excerpt: "CRE 117-371 · in Technical application security controls › Secure data storage › Data access control · 231 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [117-371](https://opencre.org/cre/117-371)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-538-770]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Related CREs

- [[cre-155-155]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.4.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v14-access-control-architecture) | Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [1](https://capec.mitre.org/data/definitions/1.html) | Accessing Functionality Not Properly Constrained by ACLs | automatic |
| [17](https://capec.mitre.org/data/definitions/17.html) | Using Malicious Files | automatic |
| [19](https://capec.mitre.org/data/definitions/19.html) | Embedding Scripts within Scripts | automatic |
| [35](https://capec.mitre.org/data/definitions/35.html) | Leverage Executable Code in Non-Executable Files | automatic |
| [58](https://capec.mitre.org/data/definitions/58.html) | Restful Privilege Elevation | automatic |
| [121](https://capec.mitre.org/data/definitions/121.html) | Exploit Non-Production Interfaces | automatic |
| [122](https://capec.mitre.org/data/definitions/122.html) | Privilege Abuse | automatic |
| [150](https://capec.mitre.org/data/definitions/150.html) | Collect Data from Common Resource Locations | automatic |
| [161](https://capec.mitre.org/data/definitions/161.html) | Infrastructure Manipulation | automatic |
| [167](https://capec.mitre.org/data/definitions/167.html) | White Box Reverse Engineering | automatic |
| [180](https://capec.mitre.org/data/definitions/180.html) | Exploiting Incorrectly Configured Access Control Security Levels | automatic |
| [233](https://capec.mitre.org/data/definitions/233.html) | Privilege Escalation | automatic |
| [441](https://capec.mitre.org/data/definitions/441.html) | Malicious Logic Insertion | automatic |
| [456](https://capec.mitre.org/data/definitions/456.html) | Infected Memory | automatic |
| [478](https://capec.mitre.org/data/definitions/478.html) | Modification of Windows Service Configuration | automatic |
| [479](https://capec.mitre.org/data/definitions/479.html) | Malicious Root Certificate | automatic |
| [481](https://capec.mitre.org/data/definitions/481.html) | Contradictory Destinations in Traffic Routing Schemes | automatic |
| [500](https://capec.mitre.org/data/definitions/500.html) | WebView Injection | automatic |
| [501](https://capec.mitre.org/data/definitions/501.html) | Android Activity Hijack | automatic |
| [502](https://capec.mitre.org/data/definitions/502.html) | Intent Spoof | automatic |
| [503](https://capec.mitre.org/data/definitions/503.html) | WebView Exposure | automatic |
| [536](https://capec.mitre.org/data/definitions/536.html) | Data Injected During Configuration | automatic |
| [545](https://capec.mitre.org/data/definitions/545.html) | Pull Data from System Resources | automatic |
| [546](https://capec.mitre.org/data/definitions/546.html) | Incomplete Data Deletion in a Multi-Tenant Environment | automatic |
| [550](https://capec.mitre.org/data/definitions/550.html) | Install New Service | automatic |
| [551](https://capec.mitre.org/data/definitions/551.html) | Modify Existing Service | automatic |
| [552](https://capec.mitre.org/data/definitions/552.html) | Install Rootkit | automatic |
| [556](https://capec.mitre.org/data/definitions/556.html) | Replace File Extension Handlers | automatic |
| [558](https://capec.mitre.org/data/definitions/558.html) | Replace Trusted Executable | automatic |
| [562](https://capec.mitre.org/data/definitions/562.html) | Modify Shared File | automatic |
| [563](https://capec.mitre.org/data/definitions/563.html) | Add Malicious File to Shared Webroot | automatic |
| [564](https://capec.mitre.org/data/definitions/564.html) | Run Software at Logon | automatic |
| [578](https://capec.mitre.org/data/definitions/578.html) | Disable Security Software | automatic |
| [624](https://capec.mitre.org/data/definitions/624.html) | Hardware Fault Injection | automatic |
| [625](https://capec.mitre.org/data/definitions/625.html) | Mobile Device Fault Injection | automatic |
| [679](https://capec.mitre.org/data/definitions/679.html) | Exploitation of Improperly Configured or Implemented Memory Protections | automatic |
| [680](https://capec.mitre.org/data/definitions/680.html) | Exploitation of Improperly Controlled Registers | automatic |
| [681](https://capec.mitre.org/data/definitions/681.html) | Exploitation of Improperly Controlled Hardware Security Identifiers | automatic |
| [697](https://capec.mitre.org/data/definitions/697.html) | DHCP Spoofing | automatic |
| [702](https://capec.mitre.org/data/definitions/702.html) | Exploiting Incorrect Chaining or Granularity of Hardware Debug Components | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | curated |
| [9](https://cwe.mitre.org/data/definitions/9.html) | J2EE Misconfiguration: Weak Access Permissions for EJB Methods | automatic |
| [13](https://cwe.mitre.org/data/definitions/13.html) | ASP.NET Misconfiguration: Password in Configuration File | automatic |
| [41](https://cwe.mitre.org/data/definitions/41.html) | Improper Resolution of Path Equivalence | automatic |
| [42](https://cwe.mitre.org/data/definitions/42.html) | Path Equivalence: 'filename.' (Trailing Dot) | automatic |
| [43](https://cwe.mitre.org/data/definitions/43.html) | Path Equivalence: 'filename....' (Multiple Trailing Dot) | automatic |
| [44](https://cwe.mitre.org/data/definitions/44.html) | Path Equivalence: 'file.name' (Internal Dot) | automatic |
| [45](https://cwe.mitre.org/data/definitions/45.html) | Path Equivalence: 'file...name' (Multiple Internal Dot) | automatic |
| [46](https://cwe.mitre.org/data/definitions/46.html) | Path Equivalence: 'filename ' (Trailing Space) | automatic |
| [47](https://cwe.mitre.org/data/definitions/47.html) | Path Equivalence: ' filename' (Leading Space) | automatic |
| [48](https://cwe.mitre.org/data/definitions/48.html) | Path Equivalence: 'file name' (Internal Whitespace) | automatic |
| [49](https://cwe.mitre.org/data/definitions/49.html) | Path Equivalence: 'filename/' (Trailing Slash) | automatic |
| [50](https://cwe.mitre.org/data/definitions/50.html) | Path Equivalence: '//multiple/leading/slash' | automatic |
| [51](https://cwe.mitre.org/data/definitions/51.html) | Path Equivalence: '/multiple//internal/slash' | automatic |
| [52](https://cwe.mitre.org/data/definitions/52.html) | Path Equivalence: '/multiple/trailing/slash//' | automatic |
| [53](https://cwe.mitre.org/data/definitions/53.html) | Path Equivalence: '\multiple\\internal\backslash' | automatic |
| [54](https://cwe.mitre.org/data/definitions/54.html) | Path Equivalence: 'filedir\' (Trailing Backslash) | automatic |
| [55](https://cwe.mitre.org/data/definitions/55.html) | Path Equivalence: '/./' (Single Dot Directory) | automatic |
| [56](https://cwe.mitre.org/data/definitions/56.html) | Path Equivalence: 'filedir*' (Wildcard) | automatic |
| [57](https://cwe.mitre.org/data/definitions/57.html) | Path Equivalence: 'fakedir/../realdir/filename' | automatic |
| [58](https://cwe.mitre.org/data/definitions/58.html) | Path Equivalence: Windows 8.3 Filename | automatic |
| [202](https://cwe.mitre.org/data/definitions/202.html) | Exposure of Sensitive Information Through Data Queries | automatic |
| [219](https://cwe.mitre.org/data/definitions/219.html) | Storage of File with Sensitive Data Under Web Root | automatic |
| [220](https://cwe.mitre.org/data/definitions/220.html) | Storage of File With Sensitive Data Under FTP Root | automatic |
| [250](https://cwe.mitre.org/data/definitions/250.html) | Execution with Unnecessary Privileges | automatic |
| [256](https://cwe.mitre.org/data/definitions/256.html) | Plaintext Storage of a Password | automatic |
| [257](https://cwe.mitre.org/data/definitions/257.html) | Storing Passwords in a Recoverable Format | automatic |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |
| [259](https://cwe.mitre.org/data/definitions/259.html) | Use of Hard-coded Password | automatic |
| [260](https://cwe.mitre.org/data/definitions/260.html) | Password in Configuration File | automatic |
| [261](https://cwe.mitre.org/data/definitions/261.html) | Weak Encoding for Password | automatic |
| [262](https://cwe.mitre.org/data/definitions/262.html) | Not Using Password Aging | automatic |
| [263](https://cwe.mitre.org/data/definitions/263.html) | Password Aging with Long Expiration | automatic |
| [266](https://cwe.mitre.org/data/definitions/266.html) | Incorrect Privilege Assignment | automatic |
| [267](https://cwe.mitre.org/data/definitions/267.html) | Privilege Defined With Unsafe Actions | automatic |
| [268](https://cwe.mitre.org/data/definitions/268.html) | Privilege Chaining | automatic |
| [269](https://cwe.mitre.org/data/definitions/269.html) | Improper Privilege Management | automatic |
| [270](https://cwe.mitre.org/data/definitions/270.html) | Privilege Context Switching Error | automatic |
| [271](https://cwe.mitre.org/data/definitions/271.html) | Privilege Dropping / Lowering Errors | automatic |
| [272](https://cwe.mitre.org/data/definitions/272.html) | Least Privilege Violation | automatic |
| [273](https://cwe.mitre.org/data/definitions/273.html) | Improper Check for Dropped Privileges | automatic |
| [274](https://cwe.mitre.org/data/definitions/274.html) | Improper Handling of Insufficient Privileges | automatic |
| [276](https://cwe.mitre.org/data/definitions/276.html) | Incorrect Default Permissions | automatic |
| [277](https://cwe.mitre.org/data/definitions/277.html) | Insecure Inherited Permissions | automatic |
| [278](https://cwe.mitre.org/data/definitions/278.html) | Insecure Preserved Inherited Permissions | automatic |
| [279](https://cwe.mitre.org/data/definitions/279.html) | Incorrect Execution-Assigned Permissions | automatic |
| [281](https://cwe.mitre.org/data/definitions/281.html) | Improper Preservation of Permissions | automatic |
| [282](https://cwe.mitre.org/data/definitions/282.html) | Improper Ownership Management | automatic |
| [283](https://cwe.mitre.org/data/definitions/283.html) | Unverified Ownership | automatic |
| [285](https://cwe.mitre.org/data/definitions/285.html) | Improper Authorization | automatic |
| [286](https://cwe.mitre.org/data/definitions/286.html) | Incorrect User Management | automatic |
| [287](https://cwe.mitre.org/data/definitions/287.html) | Improper Authentication | automatic |
| [288](https://cwe.mitre.org/data/definitions/288.html) | Authentication Bypass Using an Alternate Path or Channel | automatic |
| [289](https://cwe.mitre.org/data/definitions/289.html) | Authentication Bypass by Alternate Name | automatic |
| [290](https://cwe.mitre.org/data/definitions/290.html) | Authentication Bypass by Spoofing | automatic |
| [291](https://cwe.mitre.org/data/definitions/291.html) | Reliance on IP Address for Authentication | automatic |
| [293](https://cwe.mitre.org/data/definitions/293.html) | Using Referer Field for Authentication | automatic |
| [294](https://cwe.mitre.org/data/definitions/294.html) | Authentication Bypass by Capture-replay | automatic |
| [295](https://cwe.mitre.org/data/definitions/295.html) | Improper Certificate Validation | automatic |
| [296](https://cwe.mitre.org/data/definitions/296.html) | Improper Following of a Certificate's Chain of Trust | automatic |
| [297](https://cwe.mitre.org/data/definitions/297.html) | Improper Validation of Certificate with Host Mismatch | automatic |
| [298](https://cwe.mitre.org/data/definitions/298.html) | Improper Validation of Certificate Expiration | automatic |
| [299](https://cwe.mitre.org/data/definitions/299.html) | Improper Check for Certificate Revocation | automatic |
| [300](https://cwe.mitre.org/data/definitions/300.html) | Channel Accessible by Non-Endpoint | automatic |
| [301](https://cwe.mitre.org/data/definitions/301.html) | Reflection Attack in an Authentication Protocol | automatic |
| [302](https://cwe.mitre.org/data/definitions/302.html) | Authentication Bypass by Assumed-Immutable Data | automatic |
| [303](https://cwe.mitre.org/data/definitions/303.html) | Incorrect Implementation of Authentication Algorithm | automatic |
| [304](https://cwe.mitre.org/data/definitions/304.html) | Missing Critical Step in Authentication | automatic |
| [305](https://cwe.mitre.org/data/definitions/305.html) | Authentication Bypass by Primary Weakness | automatic |
| [306](https://cwe.mitre.org/data/definitions/306.html) | Missing Authentication for Critical Function | automatic |
| [307](https://cwe.mitre.org/data/definitions/307.html) | Improper Restriction of Excessive Authentication Attempts | automatic |
| [308](https://cwe.mitre.org/data/definitions/308.html) | Use of Single-factor Authentication | automatic |
| [309](https://cwe.mitre.org/data/definitions/309.html) | Use of Password System for Primary Authentication | automatic |
| [321](https://cwe.mitre.org/data/definitions/321.html) | Use of Hard-coded Cryptographic Key | automatic |
| [322](https://cwe.mitre.org/data/definitions/322.html) | Key Exchange without Entity Authentication | automatic |
| [346](https://cwe.mitre.org/data/definitions/346.html) | Origin Validation Error | automatic |
| [350](https://cwe.mitre.org/data/definitions/350.html) | Reliance on Reverse DNS Resolution for a Security-Critical Action | automatic |
| [370](https://cwe.mitre.org/data/definitions/370.html) | Missing Check for Certificate Revocation after Initial Check | automatic |
| [419](https://cwe.mitre.org/data/definitions/419.html) | Unprotected Primary Channel | automatic |
| [420](https://cwe.mitre.org/data/definitions/420.html) | Unprotected Alternate Channel | automatic |
| [421](https://cwe.mitre.org/data/definitions/421.html) | Race Condition During Access to Alternate Channel | automatic |
| [422](https://cwe.mitre.org/data/definitions/422.html) | Unprotected Windows Messaging Channel ('Shatter') | automatic |
| [424](https://cwe.mitre.org/data/definitions/424.html) | Improper Protection of Alternate Path | automatic |
| [425](https://cwe.mitre.org/data/definitions/425.html) | Direct Request ('Forced Browsing') | automatic |
| [433](https://cwe.mitre.org/data/definitions/433.html) | Unparsed Raw Web Content Delivery | automatic |
| [520](https://cwe.mitre.org/data/definitions/520.html) | .NET Misconfiguration: Use of Impersonation | automatic |
| [521](https://cwe.mitre.org/data/definitions/521.html) | Weak Password Requirements | automatic |
| [522](https://cwe.mitre.org/data/definitions/522.html) | Insufficiently Protected Credentials | automatic |
| [523](https://cwe.mitre.org/data/definitions/523.html) | Unprotected Transport of Credentials | automatic |
| [527](https://cwe.mitre.org/data/definitions/527.html) | Exposure of Version-Control Repository to an Unauthorized Control Sphere | automatic |
| [528](https://cwe.mitre.org/data/definitions/528.html) | Exposure of Core Dump File to an Unauthorized Control Sphere | automatic |
| [529](https://cwe.mitre.org/data/definitions/529.html) | Exposure of Access Control List Files to an Unauthorized Control Sphere | automatic |
| [530](https://cwe.mitre.org/data/definitions/530.html) | Exposure of Backup File to an Unauthorized Control Sphere | automatic |
| [539](https://cwe.mitre.org/data/definitions/539.html) | Use of Persistent Cookies Containing Sensitive Information | automatic |
| [549](https://cwe.mitre.org/data/definitions/549.html) | Missing Password Field Masking | automatic |
| [551](https://cwe.mitre.org/data/definitions/551.html) | Incorrect Behavior Order: Authorization Before Parsing and Canonicalization | automatic |
| [552](https://cwe.mitre.org/data/definitions/552.html) | Files or Directories Accessible to External Parties | automatic |
| [553](https://cwe.mitre.org/data/definitions/553.html) | Command Shell in Externally Accessible Directory | automatic |
| [555](https://cwe.mitre.org/data/definitions/555.html) | J2EE Misconfiguration: Plaintext Password in Configuration File | automatic |
| [556](https://cwe.mitre.org/data/definitions/556.html) | ASP.NET Misconfiguration: Use of Identity Impersonation | automatic |
| [566](https://cwe.mitre.org/data/definitions/566.html) | Authorization Bypass Through User-Controlled SQL Primary Key | automatic |
| [593](https://cwe.mitre.org/data/definitions/593.html) | Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created | automatic |
| [599](https://cwe.mitre.org/data/definitions/599.html) | Missing Validation of OpenSSL Certificate | automatic |
| [603](https://cwe.mitre.org/data/definitions/603.html) | Use of Client-Side Authentication | automatic |
| [612](https://cwe.mitre.org/data/definitions/612.html) | Improper Authorization of Index Containing Sensitive Information | automatic |
| [618](https://cwe.mitre.org/data/definitions/618.html) | Exposed Unsafe ActiveX Method | automatic |
| [620](https://cwe.mitre.org/data/definitions/620.html) | Unverified Password Change | automatic |
| [623](https://cwe.mitre.org/data/definitions/623.html) | Unsafe ActiveX Control Marked Safe For Scripting | automatic |
| [638](https://cwe.mitre.org/data/definitions/638.html) | Not Using Complete Mediation | automatic |
| [639](https://cwe.mitre.org/data/definitions/639.html) | Authorization Bypass Through User-Controlled Key | automatic |
| [640](https://cwe.mitre.org/data/definitions/640.html) | Weak Password Recovery Mechanism for Forgotten Password | automatic |
| [645](https://cwe.mitre.org/data/definitions/645.html) | Overly Restrictive Account Lockout Mechanism | automatic |
| [647](https://cwe.mitre.org/data/definitions/647.html) | Use of Non-Canonical URL Paths for Authorization Decisions | automatic |
| [648](https://cwe.mitre.org/data/definitions/648.html) | Incorrect Use of Privileged APIs | automatic |
| [708](https://cwe.mitre.org/data/definitions/708.html) | Incorrect Ownership Assignment | automatic |
| [732](https://cwe.mitre.org/data/definitions/732.html) | Incorrect Permission Assignment for Critical Resource | automatic |
| [749](https://cwe.mitre.org/data/definitions/749.html) | Exposed Dangerous Method or Function | automatic |
| [766](https://cwe.mitre.org/data/definitions/766.html) | Critical Data Element Declared Public | automatic |
| [782](https://cwe.mitre.org/data/definitions/782.html) | Exposed IOCTL with Insufficient Access Control | automatic |
| [798](https://cwe.mitre.org/data/definitions/798.html) | Use of Hard-coded Credentials | automatic |
| [804](https://cwe.mitre.org/data/definitions/804.html) | Guessable CAPTCHA | automatic |
| [836](https://cwe.mitre.org/data/definitions/836.html) | Use of Password Hash Instead of Password for Authentication | automatic |
| [842](https://cwe.mitre.org/data/definitions/842.html) | Placement of User into Incorrect Group | automatic |
| [862](https://cwe.mitre.org/data/definitions/862.html) | Missing Authorization | automatic |
| [863](https://cwe.mitre.org/data/definitions/863.html) | Incorrect Authorization | automatic |
| [923](https://cwe.mitre.org/data/definitions/923.html) | Improper Restriction of Communication Channel to Intended Endpoints | automatic |
| [925](https://cwe.mitre.org/data/definitions/925.html) | Improper Verification of Intent by Broadcast Receiver | automatic |
| [926](https://cwe.mitre.org/data/definitions/926.html) | Improper Export of Android Application Components | automatic |
| [927](https://cwe.mitre.org/data/definitions/927.html) | Use of Implicit Intent for Sensitive Communication | automatic |
| [939](https://cwe.mitre.org/data/definitions/939.html) | Improper Authorization in Handler for Custom URL Scheme | automatic |
| [940](https://cwe.mitre.org/data/definitions/940.html) | Improper Verification of Source of a Communication Channel | automatic |
| [941](https://cwe.mitre.org/data/definitions/941.html) | Incorrectly Specified Destination in a Communication Channel | automatic |
| [942](https://cwe.mitre.org/data/definitions/942.html) | Permissive Cross-domain Security Policy with Untrusted Domains | automatic |
| [1004](https://cwe.mitre.org/data/definitions/1004.html) | Sensitive Cookie Without 'HttpOnly' Flag | automatic |
| [1022](https://cwe.mitre.org/data/definitions/1022.html) | Use of Web Link to Untrusted Target with window.opener Access | automatic |
| [1191](https://cwe.mitre.org/data/definitions/1191.html) | On-Chip Debug and Test Interface With Improper Access Control | automatic |
| [1193](https://cwe.mitre.org/data/definitions/1193.html) | Power-On of Untrusted Execution Core Before Enabling Fabric Access Control | automatic |
| [1220](https://cwe.mitre.org/data/definitions/1220.html) | Insufficient Granularity of Access Control | automatic |
| [1222](https://cwe.mitre.org/data/definitions/1222.html) | Insufficient Granularity of Address Regions Protected by Register Locks | automatic |
| [1224](https://cwe.mitre.org/data/definitions/1224.html) | Improper Restriction of Write-Once Bit Fields | automatic |
| [1230](https://cwe.mitre.org/data/definitions/1230.html) | Exposure of Sensitive Information Through Metadata | automatic |
| [1231](https://cwe.mitre.org/data/definitions/1231.html) | Improper Prevention of Lock Bit Modification | automatic |
| [1233](https://cwe.mitre.org/data/definitions/1233.html) | Security-Sensitive Hardware Controls with Missing Lock Bit Protection | automatic |
| [1243](https://cwe.mitre.org/data/definitions/1243.html) | Sensitive Non-Volatile Information Not Protected During Debug | automatic |
| [1244](https://cwe.mitre.org/data/definitions/1244.html) | Internal Asset Exposed to Unsafe Debug Access Level or State | automatic |
| [1252](https://cwe.mitre.org/data/definitions/1252.html) | CPU Hardware Not Configured to Support Exclusivity of Write and Execute Operations | automatic |
| [1256](https://cwe.mitre.org/data/definitions/1256.html) | Improper Restriction of Software Interfaces to Hardware Features | automatic |
| [1257](https://cwe.mitre.org/data/definitions/1257.html) | Improper Access Control Applied to Mirrored or Aliased Memory Regions | automatic |
| [1259](https://cwe.mitre.org/data/definitions/1259.html) | Improper Restriction of Security Token Assignment | automatic |
| [1260](https://cwe.mitre.org/data/definitions/1260.html) | Improper Handling of Overlap Between Protected Memory Ranges | automatic |
| [1262](https://cwe.mitre.org/data/definitions/1262.html) | Improper Access Control for Register Interface | automatic |
| [1263](https://cwe.mitre.org/data/definitions/1263.html) | Improper Physical Access Control | automatic |
| [1267](https://cwe.mitre.org/data/definitions/1267.html) | Policy Uses Obsolete Encoding | automatic |
| [1268](https://cwe.mitre.org/data/definitions/1268.html) | Policy Privileges are not Assigned Consistently Between Control and Data Agents | automatic |
| [1270](https://cwe.mitre.org/data/definitions/1270.html) | Generation of Incorrect Security Tokens | automatic |
| [1274](https://cwe.mitre.org/data/definitions/1274.html) | Improper Access Control for Volatile Memory Containing Boot Code | automatic |
| [1275](https://cwe.mitre.org/data/definitions/1275.html) | Sensitive Cookie with Improper SameSite Attribute | automatic |
| [1276](https://cwe.mitre.org/data/definitions/1276.html) | Hardware Child Block Incorrectly Connected to Parent System | automatic |
| [1280](https://cwe.mitre.org/data/definitions/1280.html) | Access Control Check Implemented After Asset is Accessed | automatic |
| [1283](https://cwe.mitre.org/data/definitions/1283.html) | Mutable Attestation or Measurement Reporting Data | automatic |
| [1290](https://cwe.mitre.org/data/definitions/1290.html) | Incorrect Decoding of Security Identifiers | automatic |
| [1292](https://cwe.mitre.org/data/definitions/1292.html) | Incorrect Conversion of Security Identifiers | automatic |
| [1294](https://cwe.mitre.org/data/definitions/1294.html) | Insecure Security Identifier Mechanism | automatic |
| [1296](https://cwe.mitre.org/data/definitions/1296.html) | Incorrect Chaining or Granularity of Debug Components | automatic |
| [1297](https://cwe.mitre.org/data/definitions/1297.html) | Unprotected Confidential Information on Device is Accessible by OSAT Vendors | automatic |
| [1299](https://cwe.mitre.org/data/definitions/1299.html) | Missing Protection Mechanism for Alternate Hardware Interface | automatic |
| [1302](https://cwe.mitre.org/data/definitions/1302.html) | Missing Source Identifier in Entity Transactions on a System-On-Chip (SOC) | automatic |
| [1304](https://cwe.mitre.org/data/definitions/1304.html) | Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation | automatic |
| [1311](https://cwe.mitre.org/data/definitions/1311.html) | Improper Translation of Security Attributes by Fabric Bridge | automatic |
| [1312](https://cwe.mitre.org/data/definitions/1312.html) | Missing Protection for Mirrored Regions in On-Chip Fabric Firewall | automatic |
| [1313](https://cwe.mitre.org/data/definitions/1313.html) | Hardware Allows Activation of Test or Debug Logic at Runtime | automatic |
| [1314](https://cwe.mitre.org/data/definitions/1314.html) | Missing Write Protection for Parametric Data Values | automatic |
| [1315](https://cwe.mitre.org/data/definitions/1315.html) | Improper Setting of Bus Controlling Capability in Fabric End-point | automatic |
| [1316](https://cwe.mitre.org/data/definitions/1316.html) | Fabric-Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges | automatic |
| [1317](https://cwe.mitre.org/data/definitions/1317.html) | Improper Access Control in Fabric Bridge | automatic |
| [1320](https://cwe.mitre.org/data/definitions/1320.html) | Improper Protection for Outbound Error Messages and Alert Signals | automatic |
| [1323](https://cwe.mitre.org/data/definitions/1323.html) | Improper Management of Sensitive Trace Data | automatic |
| [1328](https://cwe.mitre.org/data/definitions/1328.html) | Security Version Number Mutable to Older Versions | automatic |
| [1334](https://cwe.mitre.org/data/definitions/1334.html) | Unauthorized Error Injection Can Degrade Hardware Redundancy | automatic |
| [1385](https://cwe.mitre.org/data/definitions/1385.html) | Missing Origin Validation in WebSockets | automatic |
| [1390](https://cwe.mitre.org/data/definitions/1390.html) | Weak Authentication | automatic |
| [1391](https://cwe.mitre.org/data/definitions/1391.html) | Use of Weak Credentials | automatic |
| [1392](https://cwe.mitre.org/data/definitions/1392.html) | Use of Default Credentials | automatic |
| [1393](https://cwe.mitre.org/data/definitions/1393.html) | Use of Default Password | automatic |
| [1394](https://cwe.mitre.org/data/definitions/1394.html) | Use of Default Cryptographic Key | automatic |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C7](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c7-enforce-access-controls.html) | curated |

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10057](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UsernameIdorScanRule.java) | Username Hash Found | automatic |
| [10110](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/JsFunctionScanRule.java) | Dangerous JS Functions | automatic |
| [90028](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java) | Insecure HTTP Method | automatic |
| [110007](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/Username%20Idor%20Scanner.js) | Username Hash Found in WebSocket message | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [117-371](https://opencre.org/cre/117-371). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
