"""
Day 3 - Phishing Page Anatomy & Detection
Detector only - does not build/host any phishing page.
"""
import re
from urllib.parse import urlparse

KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal", "signin"]


def phish_score(url: str) -> int:
    p = urlparse(url)
    score = 0
    if not url.startswith("https"):
        score += 30
    for kw in KEYWORDS:
        if kw in p.netloc.lower():
            score += 15
    if p.netloc.count('.') > 3:
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    if '-' in p.netloc:
        score += 10
    if p.netloc.count('.') >= 1 and len(p.netloc.split('.')[0]) > 20:
        score += 10
    return min(score, 100)


TEST_URLS = [
    "https://paypal-login.evil.com/verify",
    "https://github.com",
    "http://192.168.1.5/bank-verify-account",
    "https://accounts.google.com/signin",
    "https://secure-update.account-verify.info/login",
    "https://amazon.co.uk",
    "https://microsoft365.login-secure-portal.xyz",
    "https://www.wikipedia.org",
    "http://appleid.apple.com.verify-account.top",
    "https://mybank.com/login",
]

if __name__ == "__main__":
    for u in TEST_URLS:
        print(f"{u:55s} -> Risk: {phish_score(u)}%")
