#!/usr/bin/python3

""" 
    Skeleton code for k-means clustering mini-project usign feature scaling.
"""
import os
import joblib
import numpy
import matplotlib.pyplot as plt
import sys

sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color=colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii]
                            [1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

# load in the dict of dicts containing all the data on each person in the dataset
data_dict = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))
# there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

# the input features we want to use can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi = "poi"

# For 2 features
features_list = [poi, feature_1, feature_2]

# For 3 features
# features_list = [poi, feature_1, feature_2, feature_3]

data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)

# Querying the min and max values of exercised_stock_options
exercised_stock_options = []
for person in data_dict:
    if data_dict[person]["exercised_stock_options"] != "NaN":
        exercised_stock_options.append(
            data_dict[person]["exercised_stock_options"])

print(f"Minimum exercised_stock_options: {min(exercised_stock_options)}")
print(f"Maximum exercised_stock_options: {max(exercised_stock_options)}")

# Querying the min and max values of salary
salary = []
for person in data_dict:
    if data_dict[person]["salary"] != "NaN":
        salary.append(data_dict[person]["salary"])

print(f"Minimum salary: {min(salary)}")
print(f"Maximum salary: {max(salary)}")

# Show 2 features
for f1, f2 in finance_features:
    plt.scatter(f1, f2)
plt.show()

# Show 3 features
# for f1, f2, _ in finance_features:
#     plt.scatter(f1, f2)
# plt.show()

# Rescale salary and exercised_stock_options
scaler = MinMaxScaler()
rescaled_salary = scaler.fit_transform(numpy.array(salary).reshape(-1, 1))
rescaled_exercised_stock_options = scaler.fit_transform(numpy.array(exercised_stock_options).reshape(-1, 1))

# Convert numpy arrays to regular Python float values
rescaled_salary = [item[0] for item in rescaled_salary]
rescaled_exercised_stock_options = [item[0] for item in rescaled_exercised_stock_options]

# Combine the rescaled features into a single list of lists
rescaled_finance_features = [[s, e] for s, e in zip(rescaled_salary, rescaled_exercised_stock_options)]

# cluster here; create predictions of the cluster labels
# for the data and store them to a list called pred
from sklearn.cluster import KMeans

n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(rescaled_finance_features)
pred = kmeans.predict(rescaled_finance_features)

# rename the "name" parameter when you change the number of features so that the figure gets saved to a different file
try:
    Draw(pred, rescaled_finance_features, poi, mark_poi=False,
         name="clusters_2features_scaled.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("No predictions object named pred found, no clusters to plot")