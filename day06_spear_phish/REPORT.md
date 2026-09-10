# Day 6 — Spear Phishing Craft (Lab) Report

## Spear phishing vs. generic phishing
Spear phishing targets one specific individual using OSINT gathered
about them (name, role, company, location) to make the pretext far
more convincing than a mass "Dear Customer" email.

## Key elements demonstrated
- **Spoofed sender**: `it-support@{company}.com` — looks internal.
- **Personal hook**: uses the target's real name and location to build
  false authenticity.
- **Urgency**: 24-hour deadline before "suspension."
- **Single call-to-action link**: routes to a controlled lab/training
  URL (`lab.internal/awareness-test`) — never a real external site.

## 3 drafts generated
See script output — three personalized drafts for different (fictional
lab) employees, each customized with name/company/location.

## Defense: DMARC/SPF/DKIM
See `DMARC_SPF_GUIDE.md` — these three DNS-based email-authentication
standards are the primary technical control against sender spoofing,
which is the mechanism spear phishing relies on to look "internal."

*Deliverable: 3 personalized drafts + DMARC/SPF setup guide.*
