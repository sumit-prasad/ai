#NLTK

# *************************************************************************************************************

# tokenization

import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk."

tokens = word_tokenize(text)
print(tokens)

# *************************************************************************************************************

# Stopword removal

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

text = "This is an example of text that contains stopwords like the, and, of, etc."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Remove stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print(filtered_tokens)

# *************************************************************************************************************

#stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

text = "I am running in the park and saw a runner passing by"

tokens = word_tokenize(text)

stemmed_words = []

for token in tokens:
    stemmed_word = stemmer.stem(token)
    stemmed_words.append(stemmed_word)

print(stemmed_words)

# *************************************************************************************************************

# lemmetization

from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

word = "running"
pos = pos_tag([word])[0][1][0].lower()  # Get the first character of the POS tag
lemma = lemmatizer.lemmatize(word, pos=pos)
print(f"Lemma of {word} is {lemma}")

# *************************************************************************************************************

# sentence tokenization

import nltk
from nltk.tokenize import sent_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk. My name is Sahil Raj."

tokens = sent_tokenize(text)
print(tokens)

# *************************************************************************************************************

# word frequency count

import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk."

tokens = word_tokenize(text)

# calculate word frequency
freq_dist = nltk.FreqDist(tokens)

# print the frequency of each word
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")

# *************************************************************************************************************

# bag of words

import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk."

tokens = word_tokenize(text)

# calculate word frequency
freq_dist = nltk.FreqDist(tokens)

print(freq_dist.most_common(10))

# *************************************************************************************************************

# Sentiment analysis

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

# *************************************************************************************************************

# Language detection

from langdetect import detect

text = "hello how are you"
language = detect(text)

print(language) # Output: fr

# *************************************************************************************************************