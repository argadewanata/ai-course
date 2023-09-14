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
poi_ef_count = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        poi_ef_count = poi_ef_count + 1
print("[3] Number of POIs in the E+F dataset: ", poi_ef_count)

# How many POIs exist?
poi_names = open("../final_project/poi_names.txt", "r")
poi_names.readline()
poi_names.readline()
poi_count = 0
for line in poi_names:
    poi_count += 1
print("[4] Number of POIs in total: ", poi_count)

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

# How many folks in this dataset have a quantified salary? What about a known email address?
count_salary = 0
count_email = 0
for person in enron_data:
    if enron_data[person]["salary"] != "NaN":
        count_salary += 1
    if enron_data[person]["email_address"] != "NaN":
        count_email += 1
print(f"[10] Number of folks in this dataset have a quantified salary: {count_salary}")
print(f"[10] Number of folks in this dataset have a known email address: {count_email}")

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
count_nan_total_payments = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == "NaN":
        count_nan_total_payments += 1
print(f"[11] Percentage of people in the dataset have “NaN” for their total payments: {count_nan_total_payments/len(enron_data)*100}%")

# How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
count_total_payments_poi = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1 and enron_data[person]["total_payments"] == "NaN":
        count_total_payments_poi += 1
print(f"[12] Percentage of POIs in the dataset have “NaN” for their total payments: {count_total_payments_poi/poi_count*100}%")

# If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.
# What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?
print(f"[13] New number of people of the dataset: {len(enron_data)+10}")
print(f"[14] New number of folks with “NaN” for total payments: {count_nan_total_payments+10}")

# What is the new number of POI’s in the dataset? What is the new number of POI’s with NaN for total_payments?
print(f"[15] New number of POIs in the dataset: {poi_ef_count+10}")
print(f"[16] New number of POIs with NaN for total_payments: {count_total_payments_poi+10}")




















