# Social Engineering Incident Response Playbook

## Phase 1 — Preparation
- Maintain an up-to-date contact list for SOC/IT/legal/comms.
- Pre-stage account-lock, session-revocation, and mail-rule-audit
  scripts so response time isn't spent writing tooling mid-incident.

## Phase 2 — Identification
- Confirm the alert (e.g., SIEM brute-force + mail-rule signal from
  Day 13) with a manual log review to rule out false positives.
- Classify severity (LOW/MEDIUM/HIGH/CRITICAL) based on account
  privilege level and data exposure.

## Phase 3 — Containment
- Lock the affected account and revoke active sessions/tokens.
- Remove any suspicious mailbox forwarding/deletion rules.
- Block the sender domain / IP at the mail gateway or firewall.

## Phase 4 — Eradication
- Force a password reset and MFA re-enrollment for the account.
- Scan any delivered attachments/links in a sandboxed environment.
- Check for lateral movement (other accounts touched from the same IP).

## Phase 5 — Recovery
- Restore normal account access only after verification.
- Monitor the account closely for a defined period post-incident.

## Phase 6 — Lessons Learned
- Document the full timeline, root cause, and what training/technical
  gap allowed the incident.
- Update awareness training content (Day 11 quiz bank) with the
  real-world pattern observed.

## Why documentation matters
Every step must be timestamped and logged — this record is required
for legal, regulatory (e.g., breach-notification law), and cyber
insurance purposes, and is what makes the "lessons learned" phase
possible.
