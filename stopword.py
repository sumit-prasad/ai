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