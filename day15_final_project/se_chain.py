"""
Day 15 - Final Project: SE Attack Chain Simulator (CLI menu)
Ties together the components built across the internship:
OSINT -> Profile -> Phish Scoring -> Template -> IR Trigger.

This menu imports/re-implements lightweight versions of each module
so the whole chain can be demoed from one file. Lab/authorized use only.
"""
import json
import re
import socket
from urllib.parse import urlparse
import datetime


# ---- Module: OSINT (simplified, DNS-only to avoid extra deps) ----
def module_osint(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[OSINT] {domain} -> {ip}")
    except socket.gaierror as e:
        print(f"[OSINT] Lookup failed: {e}")


# ---- Module: Target profile (from Day 5 concept, offline demo data) ----
def module_profile():
    profile = {
        "name": "Riya Sharma", "company": "Sqrock", "location": "Bangalore, India",
        "top_langs": {"Python": 8, "JavaScript": 3},
    }
    print(json.dumps(profile, indent=2))


# ---- Module: Phishing URL scorer (from Day 3) ----
KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]


def module_phish(url):
    p = urlparse(url)
    score = 0
    if not url.startswith("https"):
        score += 30
    for kw in KEYWORDS:
        if kw in p.netloc.lower():
            score += 15
    if p.netloc.count('.') > 3:
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    score = min(score, 100)
    print(f"[PHISH] {url} -> Risk: {score}%")


# ---- Module: Spear-phish training template (from Day 6) ----
def module_template():
    target = {"name": "Riya Sharma", "email": "riya@company.com",
              "company": "Sqrock", "location": "Bangalore, India"}
    print(f"""
From    : it-support@{target['company'].lower()}.com
To      : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},
We noticed a login from {target['location']}. Verify within 24h.
[Verify Account] -> https://lab.internal/awareness-test
""")


# ---- Module: IR trigger (from Day 14) ----
def module_ir():
    incident = {"type": "phishing", "severity": "HIGH", "user": "riya@sqrock.com"}
    actions = ["LOCK user account", "Revoke active sessions",
               "Quarantine email", "Block sender domain"]
    print(f"[IR] Incident: {incident}")
    for a in actions:
        print(f"  [x] {a}")
    with open("final_ir_report.json", "w") as f:
        json.dump({"incident": incident, "actions": actions,
                    "timestamp": str(datetime.datetime.now())}, f, indent=2)


MODULES = {
    "osint": ("Run passive OSINT on a domain", lambda: module_osint(input("Domain: ").strip())),
    "profile": ("Build target profile from public data", module_profile),
    "phish": ("Score a URL for phishing indicators", lambda: module_phish(input("URL: ").strip())),
    "template": ("Generate spear-phishing training email", module_template),
    "ir": ("Trigger incident response workflow", module_ir),
}


def menu():
    while True:
        print("\n===== SE CHAIN SIMULATOR =====")
        print("== Sqrock Cybersecurity Internship — Final Project ==")
        for k, (desc, _) in MODULES.items():
            print(f"  [{k}] {desc}")
        print("  [quit] Exit")
        choice = input("\nSelect module: ").strip().lower()
        if choice == "quit":
            break
        if choice in MODULES:
            print(f"\n[+] Launching {choice} module...\n")
            MODULES[choice][1]()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
