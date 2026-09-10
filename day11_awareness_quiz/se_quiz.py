"""
Day 11 - Social Engineering Awareness Training Quiz (CLI)
10-question scenario-based quiz with score tracking, saved to JSON.
"""
import json
import datetime

QUESTIONS = [
    {"q": "An email asks you to verify your password via a link. You should:",
     "opts": ["A) Click the link", "B) Call IT directly", "C) Reply with password"],
     "ans": "B", "exp": "Always verify via official channels, never click email links."},
    {"q": "You find a USB drive in the parking lot. You should:",
     "opts": ["A) Plug it in to check", "B) Hand it to security", "C) Keep it"],
     "ans": "B", "exp": "USB drops are a classic baiting attack vector."},
    {"q": "A caller claiming to be IT asks for your password to 'fix an issue'. You should:",
     "opts": ["A) Give it — they're IT", "B) Refuse and report it", "C) Give a fake password"],
     "ans": "B", "exp": "Legitimate IT never needs your password."},
    {"q": "A LinkedIn recruiter you've never met sends a job offer PDF. You should:",
     "opts": ["A) Open it immediately", "B) Verify their identity first", "C) Forward it to friends"],
     "ans": "B", "exp": "Unsolicited attachments from new contacts are a common malware vector."},
    {"q": "An SMS says your bank account is locked, with a short link to 'unlock' it. You should:",
     "opts": ["A) Tap the link fast", "B) Open the bank app directly instead", "C) Reply STOP"],
     "ans": "B", "exp": "Go to the official app/site, never a link in an unsolicited text."},
    {"q": "A colleague's email suddenly asks you to buy gift cards urgently. You should:",
     "opts": ["A) Buy them quickly", "B) Verify by calling them", "C) Ignore and delete"],
     "ans": "B", "exp": "Urgent gift-card requests are a classic Business Email Compromise pattern; verify via a known channel."},
    {"q": "A website's login form submits over plain HTTP with an odd domain. This is a sign of:",
     "opts": ["A) Normal behavior", "B) Possible phishing", "C) Nothing to worry about"],
     "ans": "B", "exp": "No HTTPS + unusual domain are classic phishing indicators."},
    {"q": "You receive an unexpected 'password reset' code by SMS you didn't request. You should:",
     "opts": ["A) Share it if asked", "B) Ignore and change your password", "C) Forward it to the requester"],
     "ans": "B", "exp": "An unrequested code often means someone else is trying to log in as you."},
    {"q": "The best defense against most social engineering is:",
     "opts": ["A) Antivirus software alone", "B) Ongoing awareness training", "C) A stronger firewall"],
     "ans": "B", "exp": "SE exploits people, not just systems, so training is the primary defense."},
    {"q": "A new 'colleague' asks to bypass badge check by tailgating you into the office. You should:",
     "opts": ["A) Let them in — seems fine", "B) Politely decline and direct them to reception", "C) Ignore them"],
     "ans": "B", "exp": "Tailgating is a physical social-engineering technique; always enforce badge policy."},
]


def run_quiz():
    score = 0
    responses = []
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}: {q['q']}")
        for o in q['opts']:
            print(f"  {o}")
        ans = input("Your answer (A/B/C): ").strip().upper()
        correct = ans == q['ans']
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. {q['exp']}")
        responses.append({"question": q['q'], "your_answer": ans, "correct": correct})

    print(f"\nFinal Score: {score}/{len(QUESTIONS)}")

    report = {
        "timestamp": str(datetime.datetime.now()),
        "score": score,
        "total": len(QUESTIONS),
        "responses": responses,
    }
    with open("quiz_score_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Score report saved to quiz_score_report.json")


if __name__ == "__main__":
    run_quiz()
