# Day 23 — Postgres Credential Auditing Report

## Why databases are high-value targets
A database typically holds the full "crown jewels" of an application —
user records, credentials, financial data — in one place. Compromising
the database directly often yields far more value to an attacker than
compromising a single application account, which is why default or
weak database credentials represent an outsized risk relative to how
common they still are in dev/staging environments.

## Checks implemented
1. **Known-default credential pairs** — `postgres:postgres`,
   blank passwords, `admin:admin` — these are the very first
   combinations automated scanning tools and worms try.
2. **Weak/short password heuristic** — flags any credential under 12
   characters as a baseline hygiene warning, even if not a known default.

## Sample findings
Against the sample credential set, `postgres:postgres` is flagged
**CRITICAL**, `dev:test123` is flagged **WARNING** (too short), and
`app_user` with a strong passphrase **passes**.

## Administrative blueprint (deliverable)
- **Authorization**: never use the `postgres` superuser for application
  connections — create least-privilege roles scoped to only the
  schemas/tables the app needs.
- **Connection limiting**: set `max_connections` appropriately and use
  connection pooling (e.g., PgBouncer) to prevent connection-exhaustion DoS.
- **Network exposure**: bind Postgres to `localhost`/internal network
  only (ties back to Day 17's port-scan finding for 5432); never expose
  5432 directly to the internet.
- **Encryption**: enforce `sslmode=require` (or stricter) for all
  connections, and evaluate row-level security policies for
  multi-tenant data separation.
- **Credential hygiene**: rotate credentials regularly, store them in a
  secrets manager (not `.env` files committed to source control, per
  Day 20's finding on exposed `.env`), and enforce a minimum password
  policy for all database roles.

*Deliverable: verification logging output + this administrative blueprint.*
