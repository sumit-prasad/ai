import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk."

tokens = word_tokenize(text)

# calculate word frequency
freq_dist = nltk.FreqDist(tokens)

# print the frequency of each word
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")