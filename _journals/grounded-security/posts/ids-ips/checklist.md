---
timetoread: "5 min read"
---
*The working checklist behind this record — the full IDS/IPS reference from detection concepts through placement, tuning, and encrypted traffic, following the handbook's chapter. The Article tab carries the rationale and anti-patterns.*

## 1. IDS vs. IPS

- [ ] Remember: an **IDS detects, logs, and alerts** on suspicious activity
- [ ] Remember: an **IPS can detect and actively block or disrupt** suspicious traffic
- [ ] IDS = visibility and alerting; IPS = visibility plus prevention
- [ ] Use IDS/IPS tools to complement endpoint security such as antivirus and EDR
- [ ] Always review alerts in context before deciding whether activity is malicious
- [ ] Use threat intelligence feeds to help determine whether an IP address, domain, or behavior is suspicious

## 2. Network-Based IDS (NIDS)

- [ ] Remember: a **NIDS monitors network traffic** rather than activity on just one computer
- [ ] Place NIDS sensors where important traffic can be observed
- [ ] Use **promiscuous mode** to let a network interface listen to traffic passing across the network
- [ ] Consider **Snort** for signature-based network intrusion detection and prevention
- [ ] Note that Snort 3 supports multithreading for improved performance
- [ ] Consider **Suricata** — multithreaded and designed for high-speed network monitoring
- [ ] Use Suricata for file extraction, protocol analysis, and TLS-related inspection where needed
- [ ] Consider **Zeek** for network analysis, logging, and visibility
- [ ] Remember that Zeek can work alongside tools such as Snort and Suricata rather than replacing them
- [ ] Choose between Snort, Suricata, and Zeek based on the environment and monitoring goals

## 3. Host-Based IDS (HIDS)

- [ ] Remember: a **HIDS monitors activity on an individual host or endpoint**
- [ ] Use HIDS tools to watch files, processes, system changes, and network connections
- [ ] Consider **OSSEC** as an example of a host-based intrusion detection tool
- [ ] Use file integrity monitoring to compare current files with known-good values or hashes
- [ ] Treat unexpected changes to important files as a possible indicator of compromise
- [ ] Use **osquery** to query endpoint information with SQL-like commands
- [ ] Remember that HIDS and **EDR** can overlap, but EDR normally provides stronger response and remediation features
- [ ] Use endpoint monitoring especially where network monitoring cannot see everything happening on the device

## 4. Honeypots

- [ ] Remember: a **honeypot is a decoy system or service designed to attract attackers**
- [ ] Keep honeypots isolated and closely monitored
- [ ] Treat unexpected interaction with a honeypot as usually suspicious
- [ ] Expect honeypot alerts to have a high signal-to-noise ratio
- [ ] Consider examples such as **Cowrie, OpenCanary, MySQLpot, and NoPo**
- [ ] Use honeypots to supplement other security controls, not replace them

## 5. Intrusion Prevention Systems

- [ ] Place an IPS **inline** so traffic passes through it
- [ ] Use inline placement to stop malicious traffic before it reaches its destination
- [ ] Base IPS decisions on signatures, behaviors, anomalies, and other detection methods as appropriate
- [ ] Understand that some systems attempt to interrupt suspicious connections using **TCP reset packets**
- [ ] Remember that TCP reset techniques are generally less reliable than true inline blocking
- [ ] Note that Snort can be configured for active response or prevention
- [ ] Always consider the possibility of false positives before allowing automatic blocking

## 6. Next-Generation Firewalls

- [ ] Remember: an **NGFW combines traditional firewall functions with more advanced security features**
- [ ] Note that NGFWs often include built-in IDS/IPS capabilities
- [ ] Look for common features: application awareness, application control, identity tracking, and threat detection
- [ ] Note that some NGFWs can inspect encrypted traffic
- [ ] Consider NGFWs to reduce the need for separate security appliances in smaller environments
- [ ] Remember that an NGFW is not automatically the best choice for every organization
- [ ] Consider network size, architecture, security requirements, scalability, and budget before choosing a product
- [ ] Know the common vendors: Cisco, Check Point, Palo Alto Networks, Fortinet, SonicWall, and Sophos

## 7. IDS/IPS in the Cloud

- [ ] Adapt IDS/IPS monitoring as cloud environments change rapidly
- [ ] Expect traditional static monitoring to struggle with containers, microservices, and dynamically created workloads
- [ ] Integrate cloud IDS/IPS solutions with cloud-native platforms and orchestration tools where possible
- [ ] Use monitoring that understands container and workload lifecycle changes in Kubernetes environments
- [ ] Use virtual network taps or similar mechanisms to send cloud traffic to IDS/IPS systems

## 8. AWS Reminders

- [ ] Use **Amazon GuardDuty** for managed threat detection
- [ ] Remember that GuardDuty uses threat intelligence, anomaly detection, and machine learning
- [ ] Use **AWS CloudTrail** to record account and API activity
- [ ] Use **VPC Flow Logs** for information about network traffic
- [ ] Use **Amazon EventBridge** to help route security-related events
- [ ] Remember that third-party IDS/IPS products can also be deployed in AWS

## 9. Azure Reminders

- [ ] Use **Microsoft Defender for Cloud** for security monitoring and threat detection
- [ ] Use **Microsoft Sentinel** for SIEM and security analytics capabilities
- [ ] Use **KQL** to query Microsoft security and logging data
- [ ] Use **Azure Activity Logs** to record subscription-level activity
- [ ] Use **Azure Resource Logs** for information about individual resources
- [ ] Use **Azure Monitor Logs** to centralize and analyze logging data

## 10. GCP Reminders

- [ ] Use **Event Threat Detection (ETD)** to analyze Google Cloud logging data for suspicious activity
- [ ] Review ETD findings in **Security Command Center**
- [ ] Use **Cloud Audit Logs** to record administrative and access-related activity
- [ ] Use **Cloud Logging** to collect logs from Google Cloud services and workloads
- [ ] Review firewall, network, and security logs together for better context

## 11. Alert Management

- [ ] Remember that too many alerts cause **alert fatigue**
- [ ] Focus attention on alerts that provide useful and actionable information
- [ ] Remember: a **false positive** is an alert for activity that is not actually malicious
- [ ] Recognize that a legitimate event can still be noisy if it occurs too frequently
- [ ] Do not automatically disable a rule simply because it generates many alerts
- [ ] Adjust thresholds, IP ranges, ports, severity levels, or exclusions when appropriate
- [ ] Consider logging low-priority events instead of generating immediate alerts for all of them
- [ ] Treat IDS/IPS tuning as an **ongoing process**, not a one-time configuration task

## 12. Snort Rule Reminders

- [ ] Remember the basic structure: **action + protocol + source + destination + rule options**
- [ ] `msg` = message shown when the rule triggers
- [ ] `sid` = unique signature ID
- [ ] `rev` = rule revision number
- [ ] `content` = data the rule should search for
- [ ] `offset` = where the content search should begin in the packet
- [ ] `flow` = direction or state of the network connection
- [ ] Write more specific rules — they usually create fewer false positives
- [ ] Test custom rules before deploying them broadly
- [ ] Use **PCAP files** for testing and validating detection rules

## 13. IDS/IPS Placement

- [ ] Remember that IDS/IPS placement determines which traffic can actually be inspected
- [ ] Place sensors at important **network choke points**
- [ ] Monitor the internet connection for visibility into inbound and outbound traffic
- [ ] Remember that perimeter monitoring alone may miss traffic moving between internal systems
- [ ] Monitor the **DMZ** to improve visibility into public-facing systems
- [ ] Use internal monitoring to help detect lateral movement
- [ ] Recognize that large numbers of VLANs can make complete monitoring more difficult and expensive
- [ ] Choose placement based on the network topology and the threats you are most concerned about
- [ ] Use multiple monitoring points or other security technologies in microsegmented networks

## 14. Encrypted Traffic

- [ ] Remember that IDS/IPS tools cannot normally inspect encrypted payload contents without decryption
- [ ] Recognize that encryption can hide malicious activity from network monitoring tools
- [ ] Remember that some attacks can still be detected using visible connection information or unencrypted portions of traffic
- [ ] Consider **SSL/TLS inspection** for deeper visibility into encrypted traffic
- [ ] Account for the performance overhead TLS inspection introduces
- [ ] Weigh the privacy, compliance, and legal concerns of decrypting traffic
- [ ] Note that some NGFWs include built-in SSL/TLS inspection
- [ ] Note that Snort and Suricata can be used with proxies that decrypt traffic
- [ ] Use **JA3 fingerprints/hashes** to identify TLS clients or suspicious encrypted connections without reading the encrypted payload

## 15. Final Reminders

- [ ] **IDS = detect and alert**
- [ ] **IPS = detect and prevent**
- [ ] **NIDS = monitor the network**
- [ ] **HIDS = monitor the host**
- [ ] EDR adds endpoint detection plus response capabilities
- [ ] Honeypots provide decoy systems that help expose attacker behavior
- [ ] NGFWs combine firewalling with advanced security functions
- [ ] Cloud environments require adaptable monitoring
- [ ] Reduce false positives so important alerts are easier to recognize
- [ ] Put IDS/IPS sensors where they can see the traffic that matters
- [ ] Remember that encrypted traffic limits visibility unless additional inspection techniques are used
- [ ] Make IDS/IPS tools part of a **larger layered security strategy**
- [ ] Remember that logs and alerts only provide value when someone reviews them and knows how to respond

With the final reminders internalized, the detection layer has sensors where the threat model needs them, a tuned alert queue, and honest answers about encrypted traffic. The test running through the whole sequence: **logs and alerts only provide value when someone reviews them and knows how to respond.**
