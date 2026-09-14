# Sqrock Cybersecurity Internship — Phase 2 Full Submission (Days 16–30)

Each `dayNN_*` folder contains:
- The working Python script(s) for that day's task
- `REPORT.md` — the written report/analysis deliverable
- Any extra deliverable named in the task brief (checklist, playbook, template, sample files)

## How to submit
1. Run each script and screenshot the output where the brief asks for
   "execution logs" — most Phase 2 scripts run fully offline with no
   setup (see table below).
2. Read and lightly rewrite each `REPORT.md` in your own words before
   submitting.
3. Zip/upload the whole folder, or submit day-by-day per your
   supervisor's format.

## What needs extra setup vs. runs immediately

| Runs immediately (stdlib only) | Needs `pip install requests` | Needs a real target/network to see full output |
|---|---|---|
| Day 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29 | Day 16 | Day 16 (needs a live server at the URL you point it to) |
| | Day 20 | Day 20 (needs a live server on localhost:5000) |
| | Day 30 (partial) | Day 30 (recon portion needs a live target) |

Install everything at once:
```
pip install requests
```

## Notes on specific days
- **Day 16 / 20 / 30**: point the script at your own local dev server
  (e.g., `python -m http.server 8000`, or a Flask app on port 5000) so
  there's something to actually audit — running against nothing just
  prints "Target Unreachable."
- **Day 17**: scans 127.0.0.1 by default — on a clean machine, expect
  "No open ports found," which is itself a valid (good) finding. Start
  a local server on one of the scanned ports to see a positive detection.
- **Day 19**: includes both a vulnerable and a hardened sample
  Dockerfile so you can show the scanner catching real issues *and*
  passing a clean config.
- **Day 25**: includes a real PNG-signature sample and a PHP-payload
  file disguised with a `.png` extension, so the magic-bytes check has
  something real to catch.
- **Day 28 / 29**: intentionally simulate the final network/API call
  rather than executing it for real (no live Slack webhook or cloud
  API call is made) — this keeps the exercise safe to run without
  needing real infrastructure credentials. The report explains exactly
  where a production integration would plug in.

## Reminder
Every task here is scoped to lab/localhost/your-own-infrastructure use
per the program's ethical guidelines — don't point any of these at
systems you don't own or have written authorization to test.
