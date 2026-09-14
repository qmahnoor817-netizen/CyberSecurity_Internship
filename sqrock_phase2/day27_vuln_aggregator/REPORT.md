# Day 27 — Vulnerability Report Aggregator Report

## The problem this solves
Security teams commonly run several tools against the same codebase —
static analysis (Bandit for Python), dependency scanning (npm audit,
Trivy for containers), secrets scanning, etc. Each produces its own
output format and severity scale, so without aggregation, triaging
requires manually cross-referencing multiple dashboards — a major
contributor to **alert fatigue** in SOCs.

## Aggregation logic
`aggregate_reports()` merges findings from multiple mock tool outputs
into one list, filters by a minimum severity threshold (default
`HIGH`), sorts by severity (Critical first), and writes a single
unified JSON file — this is the shape a downstream ticketing/reporting
system would consume.

## Sample run
Of 5 mock findings across 3 tools, filtering at `HIGH+` correctly
surfaces the `CRITICAL` libcurl CVE and the two `HIGH` findings
(hardcoded password, prototype pollution), while the `MEDIUM`/`LOW`
findings are excluded from this summary (still available in the full
mock dataset for a lower-priority follow-up pass).

## Executive summary template
See `EXECUTIVE_SUMMARY_TEMPLATE.md` — designed for non-technical
stakeholders: leads with plain-language impact, a severity-count table,
the top 3 issues in business terms, and an explicit "no action needed"
section so the summary doesn't create unnecessary alarm outside the
security/engineering team.

*Deliverable: unified findings JSON + executive summary template.*
