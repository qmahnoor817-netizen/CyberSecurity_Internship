# Day 25 — File Upload / Magic Bytes Validation Report

## The vulnerability
Many upload handlers validate files only by their **extension** or
**declared MIME type** (both fully attacker-controlled). An attacker
can rename a PHP web shell to `shell.png`, and if the server only
checks the extension, it gets accepted and stored in a web-accessible
directory — if that directory also happens to execute PHP, the
attacker now has remote code execution.

## Magic bytes as the real signal
Every real file format starts with a fixed byte sequence (its "magic
number") written by the actual encoder — a genuine PNG always starts
with `89 50 4E 47 0D 0A 1A 0A`, regardless of filename. Checking this
raw binary header instead of trusting the extension makes the
filename irrelevant to the validation decision.

## Test results
Running the script generates two local demo files, then validates them:
- `sample_real.png` — starts with the correct PNG signature →
  **VALIDATION PASSED**.
- `sample_disguised.png` — plain text content given a `.png`
  extension → **SECURITY EXCEPTION**, correctly rejected despite the
  filename, proving the check relies on actual byte content rather
  than trusting the extension. (A real attacker payload would use
  something like renamed PHP/script source instead of plain text —
  the detection logic is identical either way, since it never looks
  at the content, only the header bytes.)

## Mitigation report for secure upload handling
1. **Validate magic bytes**, not extension/MIME type (this exercise).
2. **Re-encode images server-side** (e.g., open and re-save with an
   image library) — this destroys any non-image data appended to a
   polyglot file, even if the header check alone were bypassed.
3. **Store uploads outside the web root**, or in a bucket/service with
   no execute permission, so even a successfully uploaded malicious
   file can't be directly requested and executed.
4. **Rename uploaded files** to a generated, non-attacker-controlled
   name and strip the original extension where possible.
5. **Enforce a strict file-size limit** and, for images specifically,
   validate dimensions to catch malformed files early.

*Deliverable: validation output against a benign and a malicious sample + this mitigation report.*
