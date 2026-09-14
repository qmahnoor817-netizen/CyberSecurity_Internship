"""
Day 12 - Phishing Email Detection with ML
Naive Bayes text classifier trained on a small labeled dataset (50 samples).
Requires: pip install scikit-learn
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 50-sample labeled dataset (25 phishing, 25 legitimate) - synthetic examples for training
PHISHING = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Urgent: update your bank details to avoid closure",
    "Your PayPal account has been limited, verify now",
    "Action required: confirm your password within 24 hours",
    "Your package could not be delivered, click to reschedule",
    "Security alert: unusual sign-in detected, verify identity",
    "Your invoice is overdue, pay immediately to avoid penalty",
    "Congratulations, you have won a gift card, claim here",
    "Your Netflix subscription payment failed, update card now",
    "IT Support: your mailbox is full, click to increase storage",
    "Your Apple ID has been locked, verify your identity",
    "Final notice: your account will be closed today",
    "Confirm your identity to unlock your account",
    "We noticed suspicious activity, log in to secure your account",
    "Your Amazon order has an issue, verify payment details",
    "Reset your password immediately, suspicious login detected",
    "Your tax refund is ready, click to claim",
    "Your subscription has expired, renew now to avoid data loss",
    "Immediate action needed: unusual withdrawal on your account",
    "Your document is ready to view, sign in to access",
    "Your account access will be revoked unless verified today",
    "You have a pending secure message, click to view",
    "Your wire transfer requires urgent approval",
    "Your voicemail is ready, click here to listen",
]

LEGIT = [
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Meeting notes from yesterday's call",
    "Lunch order for the office party this Friday",
    "Reminder: submit your timesheet by end of week",
    "Project status update for the engineering team",
    "Here are the slides from today's presentation",
    "Can we reschedule our 1:1 to Thursday?",
    "Quarterly newsletter from the marketing team",
    "Your flight itinerary for next week's conference",
    "Draft budget for next quarter, feedback welcome",
    "New hire orientation schedule for next Monday",
    "Server maintenance window scheduled this weekend",
    "Notes from the design review meeting",
    "Happy birthday from the whole team!",
    "Please review the attached contract draft",
    "Weekly sales report for the regional team",
    "Reminder: office closed for the public holiday",
    "Updated onboarding checklist for new employees",
    "Thanks for your help on the release last night",
    "Can you send over the latest project timeline?",
    "Coffee chat next week to catch up?",
    "Your expense report has been approved",
    "Notes from the retrospective meeting",
    "Welcome to the team, looking forward to working together",
]

emails = PHISHING + LEGIT
labels = [1] * len(PHISHING) + [0] * len(LEGIT)  # 1 = phishing, 0 = legit

X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.3, random_state=42, stratify=labels
)

pipe = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB()),
])
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix (rows=true, cols=pred) [legit, phishing]:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["legit", "phishing"]))

# Quick manual test
new_samples = ["Please verify your PayPal login immediately", "Meeting notes from yesterday"]
for t in new_samples:
    pred = pipe.predict([t])[0]
    print(f"{'PHISHING' if pred else 'LEGIT'}: {t}")
