#!/usr/bin/python3

import os
import joblib
import re
import sys
import os

sys.path.append(os.path.abspath("../tools/"))
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

# temp_counter is a way to speed up the development--there are
# thousands of emails from Sara and Chris, so running over all of them
# can take a long time
# temp_counter helps you only look at the first 200 emails in the list so you
# can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        # Only look at the first 200 emails when developing
        # Once everything is working, remove this line to run over the full dataset
        temp_counter += 1
        if temp_counter < 200:
            print(f"Before join path:{os.path}")
            path = os.path.join('..', path[:-1])
            print(f"Current Path:{path}")
            email = open(path, "r")

            # Use parseOutText to extract the text from the opened email
            text = parseOutText(email)

            # Use str.replace() to remove any instances of the words
            # ["sara", "shackleton", "chris", "germani"]
            text = text.replace("sara", "")
            text = text.replace("shackleton", "")
            text = text.replace("chris", "")
            text = text.replace("germani", "")

            # Append the text to word_data
            word_data.append(text)

            # Append a 0 to from_data if the email is from Sara, and 1 if it's from Chris
            if name == "sara":
                from_data.append(0)
            else:
                from_data.append(1)

            email.close()

print("Emails Processed")
from_sara.close()
from_chris.close()

joblib.dump(word_data, open("your_word_data.pkl", "wb"))
joblib.dump(from_data, open("your_email_authors.pkl", "wb"))


# in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
vectorizer.fit_transform(word_data)
print(f"Number of words in vocabulary: {len(vectorizer.get_feature_names())}")
print(f"Word number 34597 in vocabulary: {vectorizer.get_feature_names()[34597]}")


