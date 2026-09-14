"""
Day 14 - SE Incident Response Automation
Triggers a containment action list and writes a JSON IR report
based on an incoming alert (e.g., from the Day 13 SIEM parser).
"""
import datetime
import json


def ir_response(incident: dict) -> dict:
    print("\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")

    actions = []
    if incident['severity'] in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions",
                    "Notify SOC team", "Preserve mail/auth logs"]
    if incident['type'] == 'phishing':
        actions += ["Quarantine email", "Block sender domain",
                     "Scan attachments in sandbox"]
    if incident['type'] == 'account_takeover':
        actions += ["Remove suspicious mailbox rules", "Force password reset",
                     "Require MFA re-enrollment"]

    print("\nActions Taken:")
    for a in actions:
        print(f"  [x] {a}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now()),
    }
    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nIR report saved: ir_report.json")
    return report


if __name__ == "__main__":
    ir_response({
        "type": "account_takeover",
        "severity": "CRITICAL",
        "user": "jsmith@sqrock.com",
        "trigger": "brute force success + suspicious mail rule (Day 13 SIEM alert)",
    })
