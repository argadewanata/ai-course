import nltk
nltk.download("stopwords")  # Download the stopwords dataset

from nltk.corpus import stopwords

sw = stopwords.words("english")

print("Length of all stopwords ",len(sw))  # 179 stopwords in English
print("First stopwords in the list",sw[0])  # First stopword in the list
print("Last stopwords in the list", sw[178])  # Last stopword in the list
    