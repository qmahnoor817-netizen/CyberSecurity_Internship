# Day 9 — Social Media Impersonation & Fake Profile Detection Report

## Why fake profiles matter in SE
Attackers build fake or cloned profiles to establish social proof and
trust *before* the actual attack — a fake "recruiter" connects on
LinkedIn, builds rapport over a few messages, then sends a malicious
"job description" attachment. A cloned profile (same photo, similar
name/handle to a real employee) is used for **impersonation** — asking
colleagues for a "quick favor" while posing as someone they already know.

## Heuristics used
- **Account age** — very new accounts (<30 days) are higher risk.
- **Following:follower ratio** — bots follow aggressively but attract
  few genuine followers.
- **Missing profile picture / default bio** — low-effort setup,
  common in mass-created bot/impersonation accounts.
- **Very low post count** — accounts created solely to message people,
  not to actually participate.

## Analysis of 5 sample profiles
| Profile | Score | Verdict |
|---|---|---|
| A | High | New, imbalanced ratio, no photo — likely fake |
| B | Low | Old, balanced, active — likely genuine |
| C | Medium | Newish + imbalanced ratio — worth a manual check |
| D | Low | Established, active, normal ratio — likely genuine |
| E | Very high | Brand-new, zero activity, default everything — almost certainly fake |

(Exact scores from `fake_profile_scorer.py` output.)

## Defender takeaway
No single heuristic is definitive — combine automated scoring with a
human review step, and train staff to verify new "colleague" or
"recruiter" connection requests through a second channel before
engaging.

*Deliverable: script + analysis of 5 anonymized profile samples.*
