# Day 22 — API Rate Limiting (Token Bucket) Report

## How the token bucket algorithm works
Each client gets a virtual "bucket" that starts full (`capacity`
tokens). Every request consumes 1 token; if the bucket is empty, the
request is rejected (HTTP 429). Tokens refill continuously over time
at `refill_rate_per_sec`, calculated from elapsed time on each check
rather than a fixed timer — this makes it stateless-friendly (no
background thread needed) and naturally smooths out bursts: a client
can burst up to `capacity` requests instantly, then is limited to the
steady refill rate afterward.

## Simulation results
With `capacity=3` and `refill_rate=0.5/sec`, sending 6 rapid requests:
the first 3 are `ALLOWED` (draining the full bucket), and requests 4–6
are `BLOCKED` (bucket empty, refill hasn't caught up yet). After
waiting 4 seconds (≈2 tokens refilled at 0.5/sec), the next couple of
requests succeed again before the bucket drains once more — see script
output for the exact allow/block sequence.

## Why this defends against credential testing / DoS
- **Credential stuffing/brute force**: capping requests per client
  drastically slows down automated password-guessing scripts (Phase 1,
  Day 7), turning what could be thousands of attempts per minute into
  a handful.
- **Denial of Service**: prevents a single client from monopolizing
  server resources, protecting availability for legitimate users.

## Edge/gateway integration (architectural note)
In production, this logic typically sits at the **API gateway or edge
proxy layer** (e.g., Kong, Nginx `limit_req`, AWS API Gateway usage
plans, Cloudflare), not inside the application code itself — this lets
rate limiting apply uniformly across all backend services, scale
independently of app servers, and reject abusive traffic *before* it
consumes backend compute. The per-client ledger (keyed by IP, API key,
or user ID) would typically live in a shared store like Redis rather
than a local Python dict, so limits are enforced correctly across
multiple gateway instances.

*Deliverable: execution loop output showing allow/block transitions + this architectural note.*
