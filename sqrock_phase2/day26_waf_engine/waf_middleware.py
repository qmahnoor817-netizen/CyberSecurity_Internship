"""
Day 26 - Custom Web Application Firewall (WAF) Engine
Middleware-style payload inspector that blocks common attack patterns
before they'd reach an application backend.
"""
import re


class WAFMiddleware:
    def __init__(self):
        self.rules = [
            (re.compile(r"(?i)<script"), "XSS Attempt"),
            (re.compile(r"(?i)on(error|load|mouseover)\s*="), "XSS Attempt (event handler)"),
            (re.compile(r"(?i)union\s+select"), "SQLi Attempt"),
            (re.compile(r"(?i)'\s+or\s+'?\d*'?\s*=\s*'?\d*"), "SQLi Attempt (boolean bypass)"),
            (re.compile(r"\.\./\.\./"), "Path Traversal"),
            (re.compile(r"(?i)drop\s+table"), "SQLi Attempt (destructive)"),
        ]

    def inspect_payload(self, request_data: str) -> bool:
        for pattern, rule_name in self.rules:
            if pattern.search(request_data):
                print(f"[WAF BLOCK] Dropped request. Triggered Rule: {rule_name} -> {request_data}")
                return False
        print(f"[WAF ALLOW] Payload is clean. -> {request_data}")
        return True


TEST_REQUESTS = [
    "GET /image?file=../../etc/passwd HTTP/1.1",
    "GET /search?q=hello+world HTTP/1.1",
    "POST /comment?body=<script>alert(1)</script> HTTP/1.1",
    "GET /login?user=admin' OR '1'='1 HTTP/1.1",
    "GET /product?id=42 HTTP/1.1",
    "GET /report?q=UNION SELECT null,password FROM users HTTP/1.1",
]

if __name__ == "__main__":
    waf = WAFMiddleware()
    for req in TEST_REQUESTS:
        waf.inspect_payload(req)
