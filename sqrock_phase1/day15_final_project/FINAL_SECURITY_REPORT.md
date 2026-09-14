# Final Security Report — SE Attack Chain Simulator
## Sqrock Cybersecurity Internship, Final Project (Day 15)

## Purpose
This project consolidates every technique studied across the 15-day
program into one CLI tool that walks through a full social engineering
attack chain, purely for red-team/awareness-training demonstration in
an authorized lab environment.

## The attack chain modeled
**OSINT → Profile Build → Phish Craft → Delivery → Exploit → Persist**

1. **OSINT** (Day 1, 5) — passive recon resolves a domain and would, in
   the full toolset, pull WHOIS/geolocation and public GitHub/LinkedIn
   data to build a target profile.
2. **Profile Build** (Day 5, 9) — aggregates the OSINT into a structured
   profile (role, company, tech stack) and screens social profiles for
   impersonation/bot signals.
3. **Phish Craft** (Day 3, 6) — scores candidate URLs for phishing
   indicators and generates a personalized spear-phishing training
   email using the built profile.
4. **Delivery** (Day 2, 4) — email harvesting plus vishing/smishing
   script generation model how the payload reaches the target across
   channels.
5. **Exploit/Persist** (Day 7, 8, 10) — credential attacks, USB-drop
   payload simulation, and honeypot/watering-hole tracking model what
   happens after the initial click.
6. **Detect & Respond** (Day 11, 12, 13, 14) — awareness training,
   ML-based phishing detection, SIEM log correlation, and automated
   incident response close the loop from attacker action to defender
   response.

## Key findings across the program
- Every stage of a real SE attack chain has a **corresponding,
  automatable defensive control** (OSINT minimization, DMARC/SPF,
  rate limiting, endpoint policy, awareness training, SIEM
  correlation, IR automation).
- The weakest link throughout is **human judgment under urgency/
  authority pressure** — technical controls reduce attack surface but
  training remains the primary defense against the initial click.
- Detection quality depends heavily on **log correlation** (Day 13):
  no single event (a failed login, a new mail rule) is conclusive on
  its own, but the combination is a strong account-takeover signal.

## Recommendations
1. Deploy DMARC at `p=reject` (Day 6) to eliminate the domain-spoofing
   vector used throughout the spear-phishing modules.
2. Roll out the Day 11 awareness quiz as a recurring (not one-time)
   training requirement.
3. Feed the Day 13 SIEM correlation rules and Day 14 IR automation
   into the organization's actual SOC tooling.
4. Periodically re-run OSINT exposure checks (Day 1, 5) on employees
   in privileged roles to catch newly exposed information.

*Deliverable: full integrated CLI tool (`se_chain.py`) + this final report.*
