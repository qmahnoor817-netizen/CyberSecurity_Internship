# Day 11 — SE Awareness Training Module Report

## Why training is the #1 defense
Technical controls (spam filters, DMARC, MFA) reduce the *volume* and
*success rate* of social engineering, but the final decision point is
almost always a human choosing whether to click, reply, or comply.
Effective training closes that gap by building recognition patterns
people can apply under real-world time pressure.

## What makes training effective
- **Realistic scenarios** rather than abstract rules — this quiz uses
  concrete situations (a caller, a text, a colleague's odd email).
- **Immediate feedback** — each wrong answer is followed by the
  specific reasoning, not just "incorrect."
- **Repetition** — periodic re-training and simulated phishing
  campaigns (tools like GoPhish/KnowBe4) reinforce the pattern over
  time; industry data commonly cited by these platforms shows
  organizations running regular simulated-phishing programs see
  substantially lower click-through rates than those that train once
  and stop.

## Tool built
`se_quiz.py` — a 10-question CLI quiz covering phishing, vishing,
smishing, BEC (gift-card fraud), physical tailgating, and credential
hygiene. Each attempt is scored and saved to `quiz_score_report.json`
for tracking over time.

*Deliverable: 10-question quiz + JSON score report (generated on run).*
