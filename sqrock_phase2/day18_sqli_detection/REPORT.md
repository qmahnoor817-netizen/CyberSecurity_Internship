# Day 18 — SQLi Log Detection Report

## How SQL injection works
SQL injection happens when user-supplied input is concatenated
directly into a SQL query string instead of being passed as a bound
parameter. If a query is built like:

```
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
```

an attacker can submit `admin' OR '1'='1` as `user_input`, turning the
query into `... WHERE username = 'admin' OR '1'='1'` — a condition
that's always true, bypassing the intended login check entirely.
`UNION SELECT` variants go further, appending a second query to pull
data (like password hashes) from a completely different table.

## Detection approach
The log parser flags entries containing classic SQLi meta-characters
and keywords: stray single quotes (`'`), comment sequences (`--`, `#`),
`UNION SELECT`, always-true conditions (`OR 1=1`), and destructive
statements (`DROP TABLE`). This is a **signature-based** detection —
fast and low-overhead, but it can be evaded by encoding or obfuscating
the payload (which is why production WAFs, Day 26, combine multiple
detection layers).

## Unparameterized code vs. Prepared Statements
- **Unparameterized (vulnerable)**: the query string and the
  user-controlled data are the same string — the database can't tell
  where "code" ends and "data" begins, so injected SQL syntax gets
  executed as part of the query structure.
- **Prepared Statements (secure)**: the query structure is sent to the
  database *first*, compiled, and only then are user values bound into
  fixed parameter slots. The database engine never treats the bound
  values as executable SQL syntax, regardless of what characters they
  contain — this structurally eliminates SQLi, rather than relying on
  filtering "bad" characters after the fact.

## Findings
The script flags 2 of 5 mock log entries as malicious (the `OR '1'='1`
login bypass attempt and the `UNION SELECT`/`DROP TABLE` entries),
while normal numeric ID lookups pass through clean.

*Deliverable: log inspection output + this analysis of unparameterized queries vs. prepared statements.*
