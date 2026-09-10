# Day 3 — Phishing Page Anatomy & Detection Report

## Phishing page anatomy
- **Visual cloning**: copies the real site's CSS/logo/layout so it looks
  legitimate at a glance.
- **Urgency triggers**: "your account will be suspended," countdown
  timers, warnings — designed to short-circuit careful reading.
- **URL tricks**: homograph attacks (lookalike Unicode characters),
  subdomain abuse (`paypal.login.evil.com` — the *real* domain is
  `evil.com`, `paypal.login` is just a subdomain), typosquatting.

## Scoring factors used
| Factor | Why it matters |
|---|---|
| No HTTPS | Legit login pages virtually always use TLS |
| Suspicious keyword in domain | "login/verify/secure" in the domain (not path) is a red flag |
| Excess subdomains (`.` count) | Common trick to bury the real domain |
| Raw IP address as host | Real brands don't link to bare IPs |
| Hyphenated domain | Cheap lookalike domains often use hyphens |
| Unusually long subdomain label | Used to push the real domain out of the visible URL bar on mobile |

## Results on 10 sample URLs
Ran `phish_scorer.py` against 10 URLs (legit sites like GitHub/Wikipedia
score near 0%; lookalike domains like `paypal-login.evil.com` and IP-based
login links score 70–100%). See script output for exact numbers.

## Defender takeaway
No single signal is proof of phishing — this is a **triage heuristic**,
not a verdict. Combine it with domain-age checks, certificate transparency
logs, and brand-monitoring tools for production use.

*Deliverable: script + test results on 10 URLs + this explanation.*
