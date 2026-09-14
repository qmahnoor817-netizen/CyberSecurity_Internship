"""
Day 6 - Spear Phishing Email Craft (LAB / AWARENESS-TRAINING USE ONLY)
Generates training email drafts to be sent by an authorized
awareness-training platform (e.g., GoPhish) to consenting internal
staff - never to real, non-consenting recipients.
"""


def spear_phish_template(target: dict) -> str:
    return f"""
From    : it-support@{target['company'].lower()}.com
To      : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""


TARGETS = [
    {"name": "Riya Sharma", "email": "riya@company.com", "company": "Sqrock", "location": "Bangalore, India"},
    {"name": "Ahmed Khan", "email": "ahmed@company.com", "company": "Sqrock", "location": "Karachi, Pakistan"},
    {"name": "Lina Chen", "email": "lina@company.com", "company": "Sqrock", "location": "Singapore"},
]

if __name__ == "__main__":
    for t in TARGETS:
        print(spear_phish_template(t))
