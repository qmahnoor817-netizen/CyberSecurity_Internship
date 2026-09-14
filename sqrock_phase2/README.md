Sqrock IT Solutions — Cybersecurity Internship
Combined Submission Guide — Phase 1 (Days 1–15) & Phase 2 (Days 16–30)

This README covers both phases together. Each phase also has its own README inside its folder with phase-specific detail — this is the top-level index.

sqrock_internship/     <- Phase 1: Social Engineering Attack Simulations (Days 1-15)
sqrock_phase2/          <- Phase 2: Web App Security & Defensive Automation (Days 16-30)

Every day-folder in both phases follows the same layout:

One or more working .py scripts (the task's "PYTHON LAB IMPLEMENTATION")
REPORT.md — the written analysis/report deliverable
Any extra named deliverable (checklist, playbook, template, guide)
1. One-time environment setup

You need Python 3 and VS Code with the Python + Pylance extensions. (Full VS Code setup steps were covered earlier — see your chat history if you need the install walkthrough again.)

Install every package used across both phases in one go:

pip install python-whois requests flask scikit-learn
Package	Needed for
python-whois	Phase 1, Day 1
requests	Phase 1 Days 1, 2, 5, 7; Phase 2 Days 16, 20, 30
flask	Phase 1, Day 7 (local lab login server)
scikit-learn	Phase 1, Day 12

Everything else in both phases runs with the Python standard library only — no install needed.

2. Phase 1 — Social Engineering (Days 1–15)
Day	Topic
1	OSINT & Passive Reconnaissance
2	Email Harvesting & SE Prep
3	Phishing Page Anatomy & Detection
4	Vishing & Smishing Simulation Scripts
5	OSINT + SE: Target Profile
6	Spear Phishing Email Craft (Lab Only)
7	Password Attacks & Credential Stuffing
8	USB Drop Attack Simulation
9	Social Media Impersonation & Fake Profile Detection
10	Baiting & Watering Hole Attack Simulation
11	SE Awareness Training Module
12	Phishing Email Detection with ML
13	SIEM Log Analysis for SE Attack Detection
14	SE Incident Response Plan
15	Final Project: SE Attack Chain Simulator

Runs immediately (stdlib only): Days 3, 4, 6, 8, 9, 11, 13, 14, 15 Needs requests/python-whois + internet: Days 1, 2, 5 Needs Flask + two terminals: Day 7 (start lab_login_server.py, then run brute_force_sim.py) Needs scikit-learn: Day 12 Binds a local port, view in browser: Day 10 (localhost:8080)

3. Phase 2 — Web App Security & Defensive Automation (Days 16–30)
Day	Topic
16	HTTP Security Header Analysis
17	Local Network Port & Service Scanning
18	SQL Injection (SQLi) Log Detection Engine
19	Docker Container Misconfiguration Scanner
20	Web Directory Brute-Force Simulation
21	Cross-Site Scripting (XSS) Payload Sanitizer
22	API Rate Limiting — Token Bucket Logic
23	Postgres Database Credential Auditing
24	Automated Threat Intel IP Blocking Pipeline
25	File Upload Vulnerability & Magic Bytes Validator
26	Building a Custom Web Application Firewall (WAF) Engine
27	Automated Vulnerability Report Aggregator
28	SIEM Alert Trigger Automation via Webhooks
29	Incident Containment & Asset Isolation Scripting
30	Final Project: Automated Web Vulnerability Scanner

Runs immediately (stdlib only): Days 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29 Needs requests + a live local target: Days 16, 20, 30 (point at your own server, e.g. python -m http.server 8000, or a Flask app on port 5000)

Two days are intentionally "simulate only," by design:

Day 28 (webhook alerts) — the real requests.post() call is commented out, so it won't accidentally fire a message to a real Slack/Teams channel. Uncomment it and supply your own webhook URL to make it live.
Day 29 (host containment) — logs and simulates the containment steps; the TODO comments mark exactly where a real cloud/firewall API call would go. No real infrastructure is touched.
