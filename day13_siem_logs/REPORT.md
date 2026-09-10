# Day 13 — SIEM Log Analysis Report

## What SIEM is
Security Information and Event Management (SIEM) tools centralize logs
from many sources (auth systems, mail gateways, VPN, endpoints) and
apply correlation rules to surface anomalies analysts would otherwise
miss in the noise of routine activity.

## SE-related log signals covered
- **Repeated failed logins followed by success** — classic brute-force
  or credential-stuffing pattern, especially from a single external IP.
- **Mailbox rule creation** — attackers who compromise an account
  often create a hidden forwarding/deletion rule (e.g.,
  `forward_all`, `delete_and_forward`) to silently exfiltrate future
  mail or hide their tracks; this is one of the highest-value SE
  post-compromise indicators.
- **Off-hours successful logins** — a login at 2–4 AM local time from
  an account that normally logs in during business hours is a strong
  anomaly signal, especially paired with a foreign/unfamiliar IP.

## Parser output
`siem_log_parser.py` flags: a brute-force pattern on two accounts
(`admin`, `jsmith`), a suspicious `forward_all` rule tied to the
brute-forced `admin` account, and an off-hours login. See script
output for the full alert list.

## Alert report / recommended response
Any account showing **brute-force success + new forwarding rule** should
trigger immediate credential reset, session revocation, and a mailbox
rule audit (see Day 14's IR workflow) — this combination is a strong
indicator of a successful account-takeover following a social
engineering or credential-stuffing attack.

*Deliverable: parser demo + alert report on the sample logs.*
