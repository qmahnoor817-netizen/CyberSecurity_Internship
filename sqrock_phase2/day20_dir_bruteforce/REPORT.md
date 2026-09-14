# Day 20 — Web Directory Brute-Force Report

## Concept
Directory/endpoint brute-forcing sends requests for a wordlist of
commonly-used paths (`/admin`, `/.git`, `/backup.sql`, `/.env`) against
a target, looking for anything that responds `200 OK` (exists and is
accessible) or `403 Forbidden` (exists but is access-controlled — still
useful info, since it confirms the path is real).

## Why these paths are risky if exposed
- **`/admin`, `/dashboard`** — administrative interfaces are high-value
  targets; if reachable without additional network restriction, they
  become a direct target for credential attacks (Day 7 in Phase 1,
  Day 23 here).
- **`/.env`** — commonly contains database credentials, API keys, and
  secret tokens in plaintext; an exposed `.env` is often a full
  compromise on its own.
- **`/.git`** — an exposed `.git` directory lets an attacker reconstruct
  the entire source history, potentially recovering old
  hardcoded secrets that were later "removed" but never rotated.
- **`/backup.sql`** — a database dump left in a web-accessible
  directory can leak the entire dataset, including hashed (or worse,
  plaintext) credentials.

## Findings
Running against a local dev server will typically show `.env`/`.git`/
`backup.sql` as **not found (404)** on a properly configured server —
any `200`/`403` result for these specific paths is a finding worth
escalating immediately.

## Remediation brief
- Serve static apps from a directory that contains *only* what's meant
  to be public — never the project root.
- Explicitly deny access to dotfiles and known-sensitive filenames at
  the web-server/reverse-proxy layer (e.g., Nginx `location ~ /\.` block).
- Keep secrets out of the web root entirely — use environment variables
  injected at runtime, not committed `.env` files.
- Add automated external scanning (or this exact type of script) to CI
  to catch accidental exposure before it reaches production.

*Deliverable: script execution log + this remediation brief.*
