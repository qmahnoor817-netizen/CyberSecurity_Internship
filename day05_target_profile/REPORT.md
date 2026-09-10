# Day 5 — Target Profile (Attacker Perspective) Report

## What a real attacker builds
Combining LinkedIn (role, employer, colleagues), GitHub (tech stack,
commit times → likely working hours/timezone, email in commit
metadata), and Twitter/X (interests, travel, complaints about their
own company) lets an attacker assemble a profile like:

- Name, role, employer, location
- Technologies they work with (used to craft a believable fake
  "urgent bug" or "tool update" pretext)
- Working hours / timezone (best time to call/email so the target is
  rushed, not idle)
- Personal interests (used to build fake rapport)

## Tool used
`github_profile.py` pulls public GitHub profile + top languages from a
user's repos — the kind of tech-stack fingerprinting an attacker would
use to tailor a spear-phish (e.g., "urgent security patch for your
Python dependency" if the target's repos are mostly Python).

## Sample output
Running against a public account returns name, company, location, and
inferred top languages — all from data the platform makes public by
default.

## Defender takeaway
- Review what your public commit history, bio, and "company" field
  reveal — trim anything not necessary.
- Assume any employee's public profile is the starting point for a
  targeted attack, not just a resume.
- Security awareness training should explicitly cover "OSINT
  minimization," not just phishing recognition.

*Deliverable: profile JSON + this attacker-perspective analysis.*
