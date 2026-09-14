# Day 29 — Incident Containment & Asset Isolation Report

## Why fast containment matters
Once an attacker has a foothold, the clock starts on **lateral
movement** — using the compromised host as a pivot point to reach
other internal systems. The faster a compromised asset is isolated
(sessions revoked, network access cut), the smaller the blast radius,
which is why containment automation is prioritized as one of the
highest-value SOC investments.

## What the script does
`isolate_compromised_host()` walks through the three standard
containment actions (revoke sessions, apply quarantine network policy,
null-route egress), logs each step, and writes a timestamped
`containment_log.json` record — this record is exactly the audit trail
a real IR process needs for the "lessons learned" and compliance phases.

## Important scope note
This script **simulates and logs** the containment workflow; it does
not call a real hypervisor, cloud provider, or firewall API. The
`TODO` comments mark exactly where a real deployment would plug in
actual infrastructure calls (e.g., AWS `modify-instance-attribute` for
Security Groups, a firewall controller's REST API for the null-route
step) — building that integration is an infrastructure-specific task
beyond what a lab exercise can safely demonstrate.

## Sample run
Isolating `192.168.1.150` produces the 3-step console log plus a
`containment_log.json` file recording the host, steps taken, timestamp,
and final `ISOLATED` status.

*Deliverable: containment script execution log + `IR_CONTAINMENT_PLAYBOOK.md`.*
