from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

print(stemmer.stem("responsiveness"))  # respons
print(stemmer.stem("responsivity"))  # respons
print(stemmer.stem("unresponsive"))  # unrespons
print(stemmer.stem("unresponsiveness"))  # unrespons