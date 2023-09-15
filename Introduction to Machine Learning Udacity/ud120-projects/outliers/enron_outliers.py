#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit
import joblib
import matplotlib.pyplot as plt

# read in data dictionary, convert to numpy array
data_dict = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))
features = ["salary", "bonus"]

# Remove the outlier
data_dict.pop("TOTAL", 0)

data = featureFormat(data_dict, features)

# your code below
# print(data_dict)

# Visualize the data
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

# Find the outlier
for key, value in data_dict.items():
    if value["salary"] != "NaN" and value["salary"] > 2.5e7:
        print(key, value["salary"])


# This is the outlier
# 26,704,229
