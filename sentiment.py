import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample input text
text = "I love this product. It works perfectly and I would recommend it to anyone."

# Analyze sentiment
sentiment_scores = sia.polarity_scores(text)

# Print the sentiment scores
print(sentiment_scores)