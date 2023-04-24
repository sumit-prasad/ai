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