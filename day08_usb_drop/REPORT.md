# Day 8 — USB Drop Attack Simulation Report

## Attack concept
A **USB drop attack** leaves infected drives in places the target is
likely to pick them up (parking lot, lobby, conference badge table).
Curiosity or a helpful instinct ("I should find the owner") leads the
victim to plug it in. On Windows, historic **AutoRun** functionality
could execute a payload the instant the drive was inserted, with no
further user action needed; modern Windows disables AutoRun for
executables by default, so contemporary variants rely on disguised
files (e.g., `Resume.pdf.exe`) or `HID emulation` drives (BadUSB) that
type malicious commands as if from a keyboard.

## What this simulation does (and doesn't do)
`usb_payload_sim.py` only writes local system metadata (hostname, OS,
username, current directory) to a local text file — a stand-in for the
kind of initial recon a real payload would perform before deciding on
a next stage. It has **no network component, no persistence, and no
destructive behavior** — it exists purely to make the "what happens
when you plug it in" moment concrete for a training audience.

## Prevention policy recommendations
- Disable AutoRun/AutoPlay via Group Policy on all managed endpoints.
- Deploy endpoint DLP/EDR that flags unrecognized USB mass-storage and
  HID devices.
- Physically label and control company-issued USB media; treat any
  found drive as untrusted.
- Run periodic USB-drop awareness drills (leave clean, monitored
  decoy drives) as part of the security-awareness program.

*Deliverable: simulated output file (`recon_log.txt`) + this write-up.*
