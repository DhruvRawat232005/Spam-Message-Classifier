# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', names=['label', 'message'])

# Encode labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Create pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('nb', MultinomialNB())
])

# Train model
model.fit(df['message'], df['label'])

# Create model directory if not exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, 'model/spam_model.pkl')
print("Model trained and saved successfully.")
