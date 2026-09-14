"""
Day 16 - HTTP Security Header Analysis
Audits a target's response headers against key browser-security controls.
Run against your own local server/lab environment only.
"""
import requests

TARGET_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def verify_headers(url: str):
    print(f"[*] Auditing Target Headers: {url}")
    try:
        res = requests.get(url, timeout=5)
        for header in TARGET_HEADERS:
            if header in res.headers:
                print(f"[+] CONFIGURED: {header} -> {res.headers[header][:40]}...")
            else:
                print(f"[-] VULNERABLE: Missing Security Header -> {header}")
    except requests.RequestException as e:
        print(f"[!] Target Unreachable: {e}")


if __name__ == "__main__":
    verify_headers("http://localhost:8000")  # point at your own local lab server
