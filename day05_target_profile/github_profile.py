"""
Day 5 - OSINT + SE: Build a Target Profile
Aggregates PUBLIC GitHub data into a profile JSON for threat-modeling
purposes. Only run against your own account or public accounts you are
authorized to study for this exercise.
"""
import json
import urllib.request


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "sqrock-intern-lab"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def github_profile(username: str) -> dict:
    base = "https://api.github.com"
    u = _get(f"{base}/users/{username}")
    repos = _get(f"{base}/users/{username}/repos")

    langs = {}
    for r in repos[:10]:
        lang = r.get("language")
        if lang:
            langs[lang] = langs.get(lang, 0) + 1

    return {
        "name": u.get("name"),
        "company": u.get("company"),
        "location": u.get("location"),
        "public_repos": u.get("public_repos"),
        "top_langs": langs,
        "bio": u.get("bio"),
    }


if __name__ == "__main__":
    profile = github_profile("torvalds")  # public figure, used for demo only
    print(json.dumps(profile, indent=2))
