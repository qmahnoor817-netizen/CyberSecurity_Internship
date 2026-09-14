# Day 7 — Password Attacks & Credential Stuffing Report

## Concepts
- **Brute force**: systematically try passwords (from a full keyspace
  or a wordlist) against one account.
- **Dictionary attack**: brute force restricted to a curated wordlist
  of likely/common passwords — much faster than exhaustive search.
- **Credential stuffing**: reuse username:password pairs leaked from
  *other* breaches against a new target, exploiting password reuse
  rather than guessing.

## Lab setup
1. `lab_login_server.py` — a toy Flask login endpoint (localhost only).
2. `brute_force_sim.py` — sends a small wordlist against it and reports
   which attempt (if any) succeeds.

Run order: start the server (`python lab_login_server.py`), then in a
second terminal run the simulator against `http://localhost:5000/login`.

## Defense implemented
`rate_limiter_defense.py` locks an IP out for 60 seconds after 3 failed
attempts (HTTP 429), demonstrating the standard mitigation stack:
- **Account lockout / rate limiting** (implemented here)
- **CAPTCHA** after N failures
- **MFA** so a correct password alone isn't sufficient
- **Breach-monitoring** (e.g., Have I Been Pwned API) to force resets
  on credential-stuffing-exposed accounts

*Deliverable: script demo on local lab + rate-limiter implementation.*
