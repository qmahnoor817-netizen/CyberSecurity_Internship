# Automated Quarantine — Incident Response Playbook Overview

## Trigger conditions
Host isolation should trigger automatically (or with one-click analyst
approval) when a detection reaches CRITICAL confidence, e.g.:
- Confirmed malware execution (EDR alert)
- SIEM correlation showing brute-force success + suspicious mail rule
  (Phase 1 Day 13/14 pattern) tied to a specific host/account
- Data exfiltration volume anomaly from a single asset

## Containment sequence (this script's scope)
1. **Revoke active sessions** — invalidate auth tokens/cookies so the
   attacker's existing access is cut immediately, even before network
   changes propagate.
2. **Apply quarantine network policy** — move the host into a
   restricted Security Group / VLAN with no lateral access to other
   internal assets, preventing spread.
3. **Null-route external egress** — block the host from reaching the
   internet, cutting off C2 communication and exfiltration channels.

## After containment (next phases, not automated here)
- **Preserve evidence**: snapshot disk/memory before any remediation
  that would overwrite forensic artifacts.
- **Eradicate**: remove malware/persistence mechanisms once analyzed.
- **Recover**: restore the host to the network only after verification.
- **Lessons learned**: feed findings back into detection rules and
  training content.

## Human-in-the-loop consideration
Fully automated containment is powerful but risky if a detection rule
has false positives — many organizations gate CRITICAL auto-containment
behind a single analyst confirmation click (a "break glass" override
for extremely high-confidence signals only) to balance speed against
the cost of accidentally isolating a legitimate production host.
