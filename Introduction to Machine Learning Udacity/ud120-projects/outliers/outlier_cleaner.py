#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # your code goes here
    import numpy as np

    errors = np.abs(predictions - net_worths)
    cleaned_data = list(zip(ages, net_worths, errors))

    # Sort the data by error in ascending order
    cleaned_data.sort(key=lambda x: x[2])

    # Calculate the index where 90% of the data remains
    num_points_to_keep = int(0.9 * len(cleaned_data))

    # Keep the 90% of the data with the smallest errors
    cleaned_data = cleaned_data[:num_points_to_keep]

    print("[==== Data has been cleaned ====] \n")

    return cleaned_data
