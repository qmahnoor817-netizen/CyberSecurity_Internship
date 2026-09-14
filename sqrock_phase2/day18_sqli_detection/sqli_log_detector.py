"""
Day 18 - SQL Injection (SQLi) Log Detection Engine
Parses mock web-server access logs for SQLi-pattern indicators.
"""
import re

MOCK_ACCESS_LOGS = [
    '192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200',
    "10.0.4.12 - \"POST /auth/login?user=admin' OR '1'='1 HTTP/1.1\" 401",
    '172.16.5.9 - "GET /search?q=UNION SELECT null,password FROM users-- HTTP/1.1" 500',
    '203.0.113.7 - "GET /product?id=17 HTTP/1.1" 200',
    "198.51.100.20 - \"GET /item?id=1; DROP TABLE orders;-- HTTP/1.1\" 500",
]

SQLI_REGEX = re.compile(r"(?i)('|--|#|UNION\s+SELECT|OR\s+\d+=\d+|DROP\s+TABLE)")


def analyze_sqli_signatures(logs: list):
    alerts = []
    for entry in logs:
        if SQLI_REGEX.search(entry):
            source_ip = entry.split(' ')[0]
            print(f"[CRITICAL MALICIOUS PATTERN] Source: {source_ip} -> {entry}")
            alerts.append(entry)
    if not alerts:
        print("[*] No SQLi signatures detected.")
    return alerts


if __name__ == "__main__":
    analyze_sqli_signatures(MOCK_ACCESS_LOGS)
