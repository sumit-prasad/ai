# sentence tokenization

import nltk
from nltk.tokenize import sent_tokenize

text = "This is a sample sentence, showing off the tokenization using nltk. My name is Sahil Raj."

tokens = sent_tokenize(text)
print(tokens)