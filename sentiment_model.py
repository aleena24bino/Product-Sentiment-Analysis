import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Ranges from -1 to 1

    if polarity > 0.2:  # Adjust threshold for positive
        return "Positive"
    elif polarity < -0.2:  # Adjust threshold for negative
        return "Negative"
    else:
        return "Neutral"


def analyze_csv(file_path):
    """Processes a CSV file and applies sentiment analysis."""
    df = pd.read_csv(file_path)
    if 'review' not in df.columns:
        return "CSV must have a 'review' column!"
    
    df['sentiment'] = df['review'].apply(analyze_sentiment)
    return df
