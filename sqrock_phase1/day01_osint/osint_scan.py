"""
Day 1 - OSINT & Passive Reconnaissance
Sqrock Cybersecurity Internship
Collects WHOIS, DNS/IP, and geolocation data for a domain using only
public, passive sources (no direct contact with the target's systems).
Run only against domains you own or are authorized to test.
"""
import socket
import json

try:
    import whois
except ImportError:
    whois = None

import urllib.request


def osint_scan(domain: str) -> dict:
    result = {"domain": domain}

    # WHOIS lookup (registrar, creation date, name servers)
    if whois:
        try:
            w = whois.whois(domain)
            result["registrar"] = w.registrar
            result["creation_date"] = str(w.creation_date)
            result["name_servers"] = w.name_servers
        except Exception as e:
            result["whois_error"] = str(e)
    else:
        result["whois_error"] = "python-whois not installed"

    # DNS resolution
    try:
        ip = socket.gethostbyname(domain)
        result["ip"] = ip
    except socket.gaierror as e:
        result["dns_error"] = str(e)
        return result

    # IP geolocation (public API, passive)
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}", timeout=5) as resp:
            geo = json.loads(resp.read().decode())
        result["city"] = geo.get("city")
        result["country"] = geo.get("country")
        result["isp"] = geo.get("isp")
    except Exception as e:
        result["geo_error"] = str(e)

    return result


if __name__ == "__main__":
    domain = "example.com"  # replace with your own authorized lab domain
    data = osint_scan(domain)
    print(json.dumps(data, indent=2))
