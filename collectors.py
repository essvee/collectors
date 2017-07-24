import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

cluster_list = []
names = set()

names = pd.read_csv("coll_names.csv", sep=',', usecols=['Collector1'], squeeze=True)
print(names)

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


# names = ["A Chavez", "A Hamon", "A Harvey", "A Mohyuddin CIBC leg", "A Polaszek", "A Postle", "A wogumi", "A, Mohyuddin CIBC leg.",
#          "A. Aguias", "A. Broodbank", "A. Busck", "A. C. Jashi", "A. Garido", "A. Harvey", "A. K. Walker", "A. Lopez-Avila", "A. Michelmore",
#          "A. Mohyuddin", "A. Mohyuddin CIBC", "A. Mohyuddin CIBC leg.", "A. Moore", "A. Polac. E", "A. Polac. E.", "A. Polarsek",
#          "A. Polaszak", "A. Polaszek", "A. Polaszek et al.", "A. van Harten", "A.Aguiar"]

# token_set_clustering(names)
# for name_list in cluster_list:
#     print(name_list)
