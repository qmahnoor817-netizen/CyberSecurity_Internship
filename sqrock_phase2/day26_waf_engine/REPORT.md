# Day 26 — Custom WAF Engine Report

## What a WAF does
A Web Application Firewall sits in front of (or alongside) the
application and inspects every incoming request against a ruleset —
signature patterns (this exercise), behavioral anomalies, or rate
thresholds — dropping requests that match known-bad patterns before
they ever reach application code. It's a **complementary** layer to
secure coding (parameterized queries, output encoding), not a
replacement for it.

## Rules implemented
- XSS: `<script` tags and inline event handlers (`onerror=`, `onload=`, `onmouseover=`)
- SQLi: `UNION SELECT`, boolean-bypass patterns (`' OR '1'='1`), and destructive statements (`DROP TABLE`)
- Path traversal: `../../` sequences used to escape a web root and read arbitrary files

## Test results
Of 6 sample requests, the path-traversal, XSS, and both SQLi requests
are correctly **BLOCKED**, while the two legitimate requests (plain
search query, numeric product ID) are **ALLOWED**. See script output
for the exact rule that triggered each block.

## Inline vs. Reverse Proxy WAF deployment
| Model | How it works | Trade-offs |
|---|---|---|
| **Inline (embedded middleware)** | The WAF logic runs *inside* the application process itself (like this script would, as Flask/Django middleware) | Simple to deploy for a single app; but adds latency to every app instance and must be updated/redeployed with the app. |
| **Reverse Proxy (edge)** | A dedicated proxy (e.g., ModSecurity/Nginx, Cloudflare, AWS WAF) sits in front of *all* backend services and inspects traffic before it reaches any of them | Centralizes rule management across many services, can be updated independently of app deploys, and blocks malicious traffic before it consumes any backend compute — the standard choice for production. |

## Limitations
Signature-based rules can be evaded with encoding, case variation, or
novel payloads not yet in the ruleset — a WAF reduces risk but should
never be the *only* defense against injection or XSS.

*Deliverable: WAF script output against 6 test payloads + this Inline vs. Reverse Proxy comparison.*
