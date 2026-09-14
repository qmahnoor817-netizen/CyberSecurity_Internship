# Sqrock Cybersecurity Internship — Full 15-Day Submission

Each `dayNN_*` folder contains:
- The working Python script(s) for that day's task
- `REPORT.md` — the written report/analysis deliverable
- Any extra deliverable named in the task brief (e.g. DMARC guide, IR playbook)

## How to submit
1. Run each script (see "how to run" notes below) and take a screenshot
   of the output — several days explicitly want a screenshot.
2. Read/adjust each `REPORT.md` in your own words before submitting —
   these are starting drafts, not meant to be copy-pasted verbatim.
3. Zip or upload the whole folder, or submit day-by-day per your
   supervisor's format.

## Notes on running things
- **Day 1, 2, 5** need internet access and (Day 1) `pip install python-whois requests`.
- **Day 7** needs `pip install flask requests` — start `lab_login_server.py`
  in one terminal, then run `brute_force_sim.py` in another.
- **Day 10** binds to `localhost:8080` — run it, visit the URL in a
  browser, then Ctrl+C to save the log.
- **Day 12** needs `pip install scikit-learn`.
- Everything else runs with just the Python standard library.

## Reminder
Every task here is scoped to lab/localhost/your-own-domain use per the
program's ethical guidelines — don't point any of these at systems you
don't own or have written authorization to test.
