"""
Day 9 - Social Media Impersonation & Fake Profile Detection
Behavioral heuristic scorer for suspicious/bot-like account signals.
"""


def fake_profile_score(profile: dict) -> int:
    score = 0
    age_days = profile.get("account_age_days", 365)
    if age_days < 30:
        score += 30
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    ratio = following / max(followers, 1)
    if ratio > 10:
        score += 25
    if profile.get("no_profile_pic"):
        score += 20
    if profile.get("posts", 100) < 5:
        score += 15
    if profile.get("default_bio"):
        score += 10
    return min(score, 100)


# 5 anonymized sample profiles for analysis
PROFILES = [
    {"label": "Sample A", "account_age_days": 7, "followers": 2, "following": 900,
     "no_profile_pic": True, "posts": 1, "default_bio": True},
    {"label": "Sample B", "account_age_days": 1200, "followers": 4500, "following": 320,
     "no_profile_pic": False, "posts": 870, "default_bio": False},
    {"label": "Sample C", "account_age_days": 45, "followers": 30, "following": 600,
     "no_profile_pic": True, "posts": 8, "default_bio": False},
    {"label": "Sample D", "account_age_days": 600, "followers": 220, "following": 180,
     "no_profile_pic": False, "posts": 340, "default_bio": False},
    {"label": "Sample E", "account_age_days": 2, "followers": 0, "following": 50,
     "no_profile_pic": True, "posts": 0, "default_bio": True},
]

if __name__ == "__main__":
    for p in PROFILES:
        print(f"{p['label']:10s} -> Fake Score: {fake_profile_score(p)}%")
