# Day 21 — XSS Payload Sanitizer Report

## Sanitization approach
1. **HTML-escape** the input (`html.escape`) — converts `<`, `>`, `&`,
   `"`, `'` into their HTML entity equivalents (`&lt;`, `&gt;`, etc.),
   so any tags in the input are rendered as visible text instead of
   being parsed as markup by the browser.
2. **Strip known-dangerous tokens** (`script`, `onerror`, `onload`,
   `javascript:`) as an extra defense-in-depth layer, since some
   contexts (e.g., inserting into an existing `href` attribute) can
   still be dangerous even with entities escaped.

## 10 adversarial test results
Ran against `<script>` tags, event-handler-based payloads
(`onerror`, `onload`, `onmouseover`), `javascript:` URIs in both
`iframe` and `href` contexts, and a char-code-obfuscated variant. See
script output — all payload characters that enable execution
(`<`, `>`, quotes) are entity-encoded, and the keyword-based check
catches the `script`/`on*`/`javascript:` tokens as a second layer.

## Stored vs. Reflected vs. DOM-based XSS
| Type | Where the payload lives | Trigger |
|---|---|---|
| **Stored** | Saved in the backend database (e.g., a comment field) | Executes for *every* user who later views the page containing it — highest severity, since it doesn't require tricking a specific victim into clicking a link. |
| **Reflected** | Included in the request itself (e.g., a search query parameter) and echoed straight back into the response | Only executes if the victim is tricked into clicking a crafted URL containing the payload. |
| **DOM-based** | Never touches the server at all — a client-side script reads something attacker-controlled (like `location.hash`) and writes it into the page via `innerHTML` or similar | Executes purely in the browser; server-side sanitization alone won't catch this — the client-side JS itself must avoid unsafe sinks. |

## Defender takeaway
Output encoding must match the **context** it's inserted into (HTML
body vs. HTML attribute vs. JS string vs. URL) — a single generic
`html.escape()` handles HTML-body context well but isn't sufficient on
its own for JS or URL contexts, which need their own encoding rules.

*Deliverable: output for 10 adversarial payloads + this Stored/Reflected/DOM comparison.*
