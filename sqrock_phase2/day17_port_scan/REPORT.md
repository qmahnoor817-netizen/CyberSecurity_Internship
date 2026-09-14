# Day 17 — Local Port & Service Scanning Report

## Concept
A TCP connect scan attempts a full handshake on each target port; a
successful connect (`connect_ex` returns `0`) means something is
actively listening there. This is the simplest, most reliable scan
type (versus SYN/stealth scans, which need raw sockets and elevated
privileges) — appropriate for an authorized local audit.

## Why these ports matter
- **22 (SSH)** — remote administration; exposed + weak credentials =
  direct host compromise.
- **80/443 (HTTP/HTTPS)** — expected for web apps, but worth confirming
  nothing *unexpected* is bound there.
- **5432 (PostgreSQL)** — a database port should almost never be
  reachable from outside its own host/container network; exposure here
  is a direct path to Day 23's credential-auditing risks.
- **8080 (HTTP-Alt/Admin)** — commonly used by admin dashboards,
  dev servers, or container management UIs that are easy to forget
  running in the background.

## Findings
Script output lists every port from the target set that responded —
on a typical dev machine you'd expect to see 80/443 if a local server
is running, and ideally *not* see 5432 or 8080 open to anything beyond
localhost.

## Network mapping / topology notes
For a containerized dev environment, map: which services bind to
`0.0.0.0` (reachable from other containers/hosts) vs. `127.0.0.1`
(local-only). Any database or admin port bound to `0.0.0.0` without a
firewall rule in front of it should be flagged as an exposed
developer environment finding.

*Deliverable: scan output + short network mapping notes on exposed services.*
