"""
Day 2 - Email Harvesting & Social Engineering Prep
Only run against a domain/site you own or have explicit written
permission to test.
"""
import re
import urllib.request

EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}')


def harvest_emails(url: str) -> set:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode(errors="ignore")
    return set(EMAIL_RE.findall(html))


if __name__ == "__main__":
    # Use a lab/own domain or a site explicitly built for security testing practice.
    target_url = "http://testphp.vulnweb.com"  # known intentionally-vulnerable test site
    found = harvest_emails(target_url)
    print(f"Found {len(found)} email(s):")
    for e in sorted(found):
        print(" -", e)
