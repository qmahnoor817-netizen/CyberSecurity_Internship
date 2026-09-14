# Day 10 — Baiting & Watering Hole Report

## Concepts
- **Baiting**: leaving something enticing (a "Salary_2026.xlsx" link,
  a labeled USB drive) that the victim opens/clicks voluntarily.
- **Watering hole**: instead of attacking the target directly, the
  attacker compromises a *third-party site the target regularly
  visits* (an industry forum, a vendor portal) and waits for the
  target to visit it.

## Tool used
`honeypot_tracker.py` runs a minimal local HTTP server that logs every
visitor's IP, request path, timestamp, and User-Agent — the same
mechanism a real "bait" tracking link (bit.ly-style redirector, or a
tracking pixel) uses to tell an attacker whether/when a target clicked.

## Demo & log analysis
Running the server and visiting `http://localhost:8080/bait-link` from
a browser produces a log entry with the visitor's IP, path, and browser
fingerprint (User-Agent) — this is exactly the telemetry a phishing
awareness platform (or a real attacker) uses to know who clicked, from
where, and with what device.

## Mitigation report
- **Web filtering / DNS filtering** to block known-bad or newly
  registered domains before the browser loads them.
- **Script blocking (NoScript-style policies)** on endpoints that
  visit high-risk external sites.
- **Patch management** — watering-hole attacks often chain a compromised
  site with a browser/plugin exploit; unpatched clients are what turns
  a visit into a compromise.
- **Network segmentation** so a single compromised endpoint can't reach
  everything else.

*Deliverable: server demo + captured log analysis + this mitigation report.*
