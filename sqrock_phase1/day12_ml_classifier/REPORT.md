# Day 12 — Phishing Email Detection with ML Report

## Approach
A **Naive Bayes** text classifier (`MultinomialNB` on bag-of-words
`CountVectorizer` features) was trained on a synthetic 50-email dataset
(25 phishing, 25 legitimate) split 70/30 for train/test. Naive Bayes is
a standard baseline for spam/phishing classification: it's fast to
train, works well on relatively small text datasets, and is easy to
explain (probability driven by word frequency differences between
classes).

## Features used
- Raw word-frequency counts (bag-of-words) as the base feature set.
- In a production system this would be extended with: URL count,
  presence of urgency keywords, sender-domain reputation, and whether
  links point to a domain that doesn't match the display text.

## Results
See script output for the exact accuracy score, confusion matrix, and
per-class precision/recall on the held-out test split. On a small
synthetic dataset like this, accuracy is expected to be high because
the two classes use fairly distinct vocabulary (urgency/verification
language vs. routine internal-office language) — real-world phishing
is noisier and requires a much larger, continuously updated dataset.

## Limitations
- 50 samples is far too small for a production model; this is a
  learning exercise, not a deployable classifier.
- Bag-of-words ignores word order and context — modern phishing
  classifiers typically use richer features or transformer-based
  embeddings.
- The dataset is synthetic and doesn't capture the full diversity of
  real phishing campaigns (multilingual, image-based, QR-code phishing).

*Deliverable: trained model + confusion matrix + accuracy report on 50-sample dataset.*
