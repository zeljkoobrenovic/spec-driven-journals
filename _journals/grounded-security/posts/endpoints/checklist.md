---
timetoread: "4 min read"
---
*The working checklist behind this record — endpoint security from patching to the final review, across laptops, desktops, mobile, and the nontraditional endpoints. The Article tab carries the rationale and anti-patterns.*

## 1. Keeping Endpoints Up to Date

- [ ] Enable regular operating system security updates
- [ ] Use centralized patch management where possible
- [ ] Verify that patches are successfully deployed
- [ ] Keep Windows endpoints updated through Windows Update for Business or an approved management platform
- [ ] Use MDM to manage and push updates to macOS devices
- [ ] Configure Unix/Linux desktops to receive regular package updates
- [ ] Automate updates with management tools or scheduled jobs where appropriate
- [ ] Establish a process for updating unmanaged/BYOD devices
- [ ] Keep third-party applications patched and current
- [ ] Monitor software without automatic updates for new releases
- [ ] Maintain an inventory of installed applications and versions

## 2. Harden Endpoints

- [ ] Establish a secure baseline configuration for each endpoint type
- [ ] Remove or disable unnecessary services
- [ ] Confirm what a service does before disabling it
- [ ] Regularly review running services and processes
- [ ] Remove unnecessary applications and components
- [ ] Limit unnecessary functionality to reduce the attack surface

## 3. Use Desktop Firewalls

- [ ] Enable the host-based firewall on every endpoint
- [ ] Configure inbound traffic restrictions
- [ ] Restrict outbound traffic where appropriate
- [ ] Review firewall rules periodically
- [ ] Apply firewall policies to devices used on home, public, or otherwise untrusted networks

## 4. Implement Full-Disk Encryption

- [ ] Enable full-disk encryption on laptops and desktops containing organizational data
- [ ] Use BitLocker on supported Windows systems
- [ ] Use FileVault on supported macOS systems
- [ ] Use an appropriate full-disk encryption solution on Linux/Unix systems
- [ ] Store or centrally manage recovery keys where required
- [ ] Confirm encryption is active before deploying devices
- [ ] Remember that a locked, sleeping, or hibernating device may still retain encryption keys in memory
- [ ] Shut down devices when stronger protection against physical attacks is required

## 5. Endpoint Protection

- [ ] Install approved antivirus/antimalware or endpoint protection software
- [ ] Keep endpoint protection software and signatures updated
- [ ] Confirm protection services are running correctly
- [ ] Regularly review alerts and detections
- [ ] Do not rely on endpoint protection as the only security control

## 6. Mobile Device Management

- [ ] Enroll supported mobile devices in an MDM platform
- [ ] Enforce PIN/password requirements
- [ ] Enforce VPN use where required
- [ ] Control or restrict application installation
- [ ] Apply approved configuration policies
- [ ] Enable remote erase/wipe capabilities
- [ ] Define which device types and platforms the organization will support
- [ ] Apply appropriate controls to BYOD devices

## 7. Endpoint Visibility and Monitoring

- [ ] Collect endpoint security telemetry
- [ ] Monitor open network connections
- [ ] Monitor running processes
- [ ] Monitor open files and other relevant system activity
- [ ] Centralize endpoint logs where possible
- [ ] Use endpoint data to support malware detection and incident investigation
- [ ] Consider tools such as osquery or Sysmon where appropriate
- [ ] Define employee privacy expectations before deploying extensive monitoring
- [ ] Coordinate monitoring policies with HR/legal requirements

## 8. Secure Other Endpoints

- [ ] Inventory nontraditional endpoints and IoT devices
- [ ] Change default passwords immediately
- [ ] Remove or disable unnecessary default accounts
- [ ] Keep device firmware and software updated
- [ ] Segment insecure or specialized devices from sensitive systems where appropriate
- [ ] Include printers in endpoint security reviews
- [ ] Include IP-enabled cameras
- [ ] Include IP-enabled thermostats/HVAC systems
- [ ] Include electronic door-locking systems
- [ ] Include IP telephony systems
- [ ] Include SCADA/industrial-control devices where applicable
- [ ] Document, secure, and test specialized devices before placing them into production

## 9. Centralize Endpoint Management

- [ ] Use centralized management consoles wherever practical
- [ ] Centralize authentication
- [ ] Centralize configuration and policy enforcement
- [ ] Centralize patch and software management
- [ ] Centralize security logging
- [ ] Centralize organizational file storage where appropriate
- [ ] Maintain consistent configurations across similar endpoint types
- [ ] Reduce unnecessary administrative overhead through automation

## Final Endpoint Security Review

- [ ] All operating systems are patched
- [ ] Third-party applications are patched
- [ ] Unnecessary services are disabled
- [ ] Host firewalls are enabled
- [ ] Full-disk encryption is enabled
- [ ] Endpoint protection is installed and current
- [ ] Mobile devices are appropriately managed
- [ ] Endpoint activity is sufficiently logged and monitored
- [ ] IoT and specialized endpoints are inventoried and secured
- [ ] Endpoint security controls are centrally managed where practical

With the final review green, the endpoint estate meets the bar — every device class covered, none exempt. The test running through the whole sequence: **does the review come back green for every device class, including the printer?**
