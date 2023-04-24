from langdetect import detect

text = "hello how are you"
language = detect(text)

print(language) # Output: fr