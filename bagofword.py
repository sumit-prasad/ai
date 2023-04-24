import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk."

tokens = word_tokenize(text)

# calculate word frequency
freq_dist = nltk.FreqDist(tokens)

print(freq_dist.most_common(10))