from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

word = "running"
pos = pos_tag([word])[0][1][0].lower()  # Get the first character of the POS tag
lemma = lemmatizer.lemmatize(word, pos=pos)
print(f"Lemma of {word} is {lemma}")