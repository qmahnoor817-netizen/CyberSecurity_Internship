# Day 24 — Threat Intel IP Blocking Pipeline Report

## What threat intelligence feeds provide
Threat intel feeds aggregate Indicators of Compromise (IoCs) —
malicious IPs, domains, file hashes — observed across many
organizations' sensors, effectively crowdsourcing "known-bad"
infrastructure so a single defender doesn't have to discover every
threat independently. Common feed types: C2 (command & control)
infrastructure, botnet nodes, known brute-forcing sources, and
scanning hosts.

## Pipeline logic
The script ingests a feed, and any entry above a configurable
`risk_threshold` (90 by default) is written to `blocklist.json` as an
"action" item; lower-risk entries are logged for monitoring rather
than blocked outright — this two-tier approach avoids over-blocking on
lower-confidence indicators while still acting decisively on
high-confidence ones.

## Sample run
Of 4 mock feed entries, the `malware_c2` (98) and `brute_forcer` (92)
entries exceed the threshold and are blocked; `botnet_node` (85) and
`port_scanner` (60) are logged only. See `blocklist.json` for the
exact output.

## Operational diagram (described)
```
[Threat Intel Provider API]
        |
        v
 [Ingestion Script] --(score > threshold?)--> [Block List / Firewall API]
        |                                            |
        v                                            v
 [Monitoring Log]                          [Edge Firewall / WAF Rule Update]
```
In production, "Deploying block rule" would call a real firewall or
cloud security-group API (this script only writes to a local JSON
file to keep the exercise safe and side-effect-free) — the pipeline
would typically run on a schedule (e.g., every 15 minutes) to keep the
blocklist current as the feed updates.

*Deliverable: pipeline execution log + this operational diagram description.*
