# Day 2 — Email Harvesting & SE Prep Report

## Concept
Email harvesting scrapes publicly visible pages (staff directories,
"contact us" pages, PDFs, cached pages) for email address patterns using
regex. It's usually the first concrete step after OSINT — turning a
company name into a list of real accounts to target.

## Pretexting
Pretexting is the construction of a believable false identity/scenario
("I'm from IT, I need to verify your login") used to justify a request
for information or action. Effective pretexts rely on:
- Plausible authority (IT, HR, vendor, executive)
- Urgency or a stated deadline
- A small, "reasonable-sounding" ask (not "give me your password" but
  "confirm your employee ID")

## Ethics boundary
Only harvest from domains you own or have written authorization to
test. `testphp.vulnweb.com` is a purpose-built vulnerable test site
used here instead of a real company.

## How attackers use this
Harvested emails feed directly into spear-phishing (Day 6) — each
address becomes a target for a personalized, pretext-driven email.
Attackers often pair harvested emails with LinkedIn/GitHub data (Day 5)
to guess likely usernames and add personal detail that increases click
rates.

## Defender takeaway
- Avoid publishing direct personal emails where a role alias will do
  (`support@`, not `jane.doe@`).
- Monitor for your domain's emails appearing in breach dumps.
- Train staff that "how did they know my name/role" is not proof of
  legitimacy.

*Deliverable: script + list of found emails + this write-up.*
