#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))

# How many data points (people) are in the dataset?
print("[1] Number of people in the dataset: ", len(enron_data))

# For each person, how many features are available?
print("[2] Number of features for each person: ",len(enron_data["SKILLING JEFFREY K"]))

# How many POIs are there in the E+F dataset?
count = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        count = count + 1
print("[3] Number of POIs in the E+F dataset: ", count)

# How many POIs exist?
poi_names = open("../final_project/poi_names.txt", "r")
poi_names.readline()
poi_names.readline()
count = 0
for line in poi_names:
    count += 1
print("[4] Number of POIs in total: ", count)

# What is all the features in the dataset?
print("[5] All the features in the dataset: ", enron_data["SKILLING JEFFREY K"].keys())

# What is the total value of the stock belonging to James Prentice?
print(f"[6] Total value of the stock belonging to James Prentice:{enron_data['PRENTICE JAMES']['total_stock_value']}")

# How many email messages do we have from Wesley Colwell to persons of interest?
print(f"[7] Number of email messages from Wesley Colwell to persons of interest: {enron_data['COLWELL WESLEY']['from_this_person_to_poi']}")

# What’s the value of stock options exercised by Jeffrey K Skilling?
print(f"[8] Value of stock options exercised by Jeffrey K Skilling: {enron_data['SKILLING JEFFREY K']['exercised_stock_options']}")

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?
total_payments_skilling = enron_data["SKILLING JEFFREY K"]["total_payments"]
total_payments_lay = enron_data["LAY KENNETH L"]["total_payments"]
total_payments_fastow = enron_data["FASTOW ANDREW S"]["total_payments"]
if total_payments_skilling > total_payments_lay and total_payments_skilling > total_payments_fastow:
    print(f"[9] Jeffrey K Skilling took home the most money: {total_payments_skilling}")
elif total_payments_lay > total_payments_skilling and total_payments_lay > total_payments_fastow:
    print(f"[9] Kenneth Lay took home the most money: {total_payments_lay}")
else:
    print(f"[9] Andrew Fastow took home the most money: {total_payments_fastow}")









