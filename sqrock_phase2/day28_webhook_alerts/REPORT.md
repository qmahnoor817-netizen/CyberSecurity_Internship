# Day 28 — SIEM Webhook Alert Automation Report

## Why real-time webhook alerting matters
Mean Time to Respond (MTTR) directly depends on how fast a detection
reaches a human who can act on it. Webhooks push structured alert data
directly into a team's existing chat-ops tool (Slack, MS Teams) the
moment an event fires, rather than requiring analysts to poll a
dashboard — this is what turns a detection (Phase 1 Day 13 / Day 18
here) into an actual, timely response.

## Implementation notes
`webhook_alerter.py` builds the alert payload and prints it for
verification, with the actual `requests.post()` call commented out by
default — this keeps the script safe to run in a lab/demo context
without accidentally spamming a real channel. To wire it up for real,
uncomment the `requests.post` line and supply your own Slack/Teams
incoming-webhook URL.

## Architecture: SIEM → webhook → response channel
```
[Detection source: SIEM correlation rule / log parser / WAF]
        |
        v
 [Alert formatter] --builds structured payload-->
        |
        v
 [Webhook dispatch] --HTTPS POST-->
        |
        v
 [Slack / MS Teams / PagerDuty channel] --human sees it, responds-->
        |
        v
 [Incident response workflow triggered] (ties into Phase 1 Day 14 / Day 29 here)
```

## Defender takeaway
Keep webhook payloads structured and consistent (type, source,
severity, timestamp) so downstream automation (or the on-call human)
can act quickly without needing to parse free-text; route different
severities to different channels (e.g., CRITICAL → paging tool,
LOW → logging channel only) to avoid alert fatigue.

*Deliverable: alert dispatch script output + this architecture diagram description.*
