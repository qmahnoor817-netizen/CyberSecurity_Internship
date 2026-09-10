# DMARC / SPF / DKIM Setup Guide (Defender Reference)

**SPF (Sender Policy Framework)**
Publish a DNS TXT record listing which mail servers are allowed to
send email for your domain, e.g.:
`v=spf1 include:_spf.google.com ~all`
Receiving servers check the sending server's IP against this list.

**DKIM (DomainKeys Identified Mail)**
Your mail server cryptographically signs outgoing messages; a public
key published in DNS lets receivers verify the signature wasn't
tampered with in transit.

**DMARC (Domain-based Message Authentication, Reporting & Conformance)**
Ties SPF + DKIM together and tells receivers what to do when a message
fails both, e.g.:
`v=DMARC1; p=reject; rua=mailto:dmarc-reports@yourcompany.com`
`p=reject` blocks spoofed mail claiming to be from your domain
outright — this is what stops attackers from sending
`it-support@yourcompany.com` emails that aren't really from you.

**Rollout order:** SPF → DKIM → DMARC at `p=none` (monitor only) → tighten
to `p=quarantine` → `p=reject` once reports show no legitimate mail breaking.
