# Day 14 — SE Incident Response Plan Report

## IR phases
Preparation → Identification → Containment → Eradication → Recovery →
Lessons Learned (see `IR_PLAYBOOK.md` for the full breakdown as applied
to social engineering incidents specifically).

## Automation built
`ir_automation.py` takes an incident dict (type + severity) and:
1. Prints a triggered-response summary.
2. Selects containment actions based on incident type/severity
   (account lockout + session revocation for HIGH/CRITICAL; mail
   quarantine for phishing; mailbox-rule cleanup + forced reset for
   account takeover).
3. Writes a timestamped JSON report (`ir_report.json`) for the
   incident record.

## Sample run
Simulated an account-takeover incident (matching the Day 13 SIEM
alert: brute-force success + suspicious mail rule) at CRITICAL
severity — the script correctly selects account lockout, session
revocation, mailbox-rule removal, and forced MFA re-enrollment.

*Deliverable: IR script + JSON report sample + IR playbook document.*
