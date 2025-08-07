# Task 3: NLP with spaCy - Named Entity Recognition + Sentiment

import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

review = "I recently bought the Samsung Galaxy S21 and I absolutely love it. The camera is amazing!"

doc = nlp(review)
print("Named Entities Found:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")

blob = TextBlob(review)
sentiment = blob.sentiment.polarity

print("\nSentiment Analysis:")
print("Polarity Score:", sentiment)
if sentiment > 0:
    print("Sentiment: Positive")
elif sentiment < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
