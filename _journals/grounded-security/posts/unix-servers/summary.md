---
timetoread: "2 min read"
---

Every Unix application server in my organization **earns its place on the network**: fully patched on a small-step cadence, running only the services it exists to run, with a least-privilege filesystem, a host firewall permitting only required traffic, file-integrity monitoring against a trusted baseline, restrictive mount options, applications isolated and non-root, and mandatory access control enabled where the platform supports it — with every restriction verified against required functionality and the review repeated, not archived. The test each server is held to: only what the application requires is running, reachable, writable, and privileged — and the server still does its job.

**What changes**

* **Patching becomes a cadence, not a campaign.** OS and third-party software stay current through the package manager, important patches are tested, major upgrades carry rollback plans, update intervals stay small — and software installed outside the package manager is tracked separately with advisory subscriptions, so the hand-installed orphan stops being invisible.
* **The surface shrinks and stays shrunk.** Services are inventoried, each has a known purpose, the unneeded are disabled and blocked from restarting, and the server is periodically rechecked — because services come back.
* **The filesystem becomes the blast-radius control.** World-readable/writable and execute permissions pruned, restrictive `umask`, application accounts unable to read data they do not require, SUID/SGID binaries justified or stripped, and unexpected permission changes searched for regularly.
* **The host defends and watches itself.** A host firewall permits only required traffic with admin services restricted to trusted networks; file-integrity monitoring alerts on unexpected change to OS files, configs, and application directories — and unexplained alerts are investigated, not muted.
* **Applications get contained.** Restrictive mount options (`nodev`, `nosuid`, `noexec`, `ro`) where they fit; isolation via `chroot`, containers, or jails — never treated as a complete boundary alone; dedicated non-root accounts with `sudo` restricted; and SELinux/AppArmor-class MAC enabled where practical, permissive mode first, enforcement after.
* **Verification closes every thread.** The application still works, the server reboots clean, ports are scanned, restrictions tested, changes documented, exceptions approved and recorded — and the whole review repeats after major changes.

**What it costs**

* Testing every restriction against required functionality takes time — accepted deliberately, because an unverified control gets rolled back at 2 a.m. and never reinstated.
* The periodic recheck (services, permissions, firewall rules, MAC policies) is standing work per server, not a commissioning gate.
* MAC policies demand real effort as applications evolve; permissive-then-enforce is the sanctioned path, `setenforce 0` is not.

**What we are not doing**

* Not hardening until the application breaks — a recorded exception beats a silent regression.
* Not relying on the network firewall — the host defends itself even when the layers in [[network-security]] fail.
* Not covering the estate-wide scanning cadence or the data layer — those live in [[vulnerability-management]] and [[databases]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full hardening sequence and final security review. Grounded in the Unix Application Server Security chapter of the* Defensive Security Handbook*.*
