"""
Day 23 - Postgres Database Credential Auditing
Flags dangerous default/weak credential pairs against a known-bad list.
This is a CONFIGURATION AUDIT, not a live brute-force against a real DB -
it checks credential pairs you provide against known-default patterns.
"""

KNOWN_DEFAULTS = {("postgres", "postgres"), ("postgres", ""), ("admin", "admin"), ("postgres", "admin")}


def evaluate_db_credentials(target_ip: str, credential_dictionary: dict):
    print(f"[*] Evaluating DB Authentication Resilience on: {target_ip}")
    findings = []
    for username, secret in credential_dictionary.items():
        if (username, secret) in KNOWN_DEFAULTS:
            print(f"[CRITICAL] Default/known-weak credential pair active: {username}:{secret}")
            findings.append((username, "CRITICAL - default credential"))
        elif len(secret) < 12:
            print(f"[WARNING] Weak (short) password for user: {username}")
            findings.append((username, "WARNING - short password"))
        else:
            print(f"[-] Passed baseline check -> {username}:{secret[:3]}***")
            findings.append((username, "PASS"))
    return findings


if __name__ == "__main__":
    evaluate_db_credentials("127.0.0.1", {
        "postgres": "postgres",
        "app_user": "SecureP@ss2026!",
        "dev": "test123",
    })
