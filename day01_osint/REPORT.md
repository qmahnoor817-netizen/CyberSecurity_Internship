# Day 1 — OSINT & Passive Reconnaissance Report

## What passive OSINT means
Passive reconnaissance gathers information about a target using only
publicly available sources — WHOIS records, DNS entries, IP geolocation
databases, search engines, and public code repositories — without ever
sending traffic directly to the target's own infrastructure in a way
that could be logged as an intrusion attempt. This is contrasted with
**active** recon, which touches the target directly (port scans, banner
grabbing) and carries legal/detection risk if unauthorized.

## Tool used
`osint_scan.py` pulls three data points for a domain:
- **WHOIS**: registrar, creation date, name servers
- **DNS**: resolves the domain to an IP address
- **Geolocation**: maps that IP to an approximate city/country/ISP via a
  public geolocation API

## Findings on practice domain (example.com)
Running the script against `example.com` (a domain explicitly reserved
by IANA for documentation/testing) returns registrar and hosting
metadata without touching any production system. This demonstrates how
an attacker could build an initial footprint of an organization
(hosting provider, likely region, technical contacts) before any direct
contact — which is exactly why organizations should keep WHOIS privacy
enabled and monitor what DNS/hosting metadata is publicly exposed.

## Defender takeaway
- Enable WHOIS privacy/proxy registration where possible.
- Regularly audit what your public DNS records reveal (internal
  hostnames, mail servers, subdomains).
- Treat any OSINT footprint as the first step of a longer attack chain,
  and reduce it where feasible.

*Deliverable: script output (screenshot) + this report.*
