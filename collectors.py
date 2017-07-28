import numpy as np
from fuzzywuzzy import fuzz
import csv

cluster_list = []

# Find and cluster matching names
def token_set_clustering(input_list):
    checked = []

    for name in input_list:
        cluster = []

        # Create a new list of names we haven't encountered so far + turn into a list
        unchecked_list = np.setdiff1d(input_list, checked, assume_unique=True).tolist()

        # Go through each 'new' name and check for similarity against current name
        for unchecked_name in unchecked_list:
            # Only consider if similar enough and new to this iteration
            if (fuzz.token_set_ratio(name, unchecked_name) >= 80) and (unchecked_name not in checked):
                checked.append(unchecked_name)
                cluster.append(unchecked_name)

        if len(cluster) != 0:
            cluster_list.append(cluster)

# Get names from csv - should be unique
with open('coll_names.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    names = []
    for row in readCSV:
        names.append(row[0])

token_set_clustering(names)
for name_list in cluster_list:
    print(name_list)

print(len(cluster_list))
