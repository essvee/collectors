from fuzzywuzzy import process
import numpy as np
from fuzzywuzzy import fuzz

cluster_list = []


def cluster_names(input_list):
    clusters = []

    for name in input_list:
        # Get best matches
        cluster = process.extractBests(name, input_list, score_cutoff=87)

        # Get just the names - we don't need the match values
        only_names = [name for name, value in cluster]
        clusters.append(only_names)

        # Remove touched name from input so we don't get duplicates
        for remove_name in only_names:
            names.remove(remove_name)

    return clusters


def token_set_clustering(input_list):
    checked = []

    for name in input_list:
        cluster = []
        # print("Currently looking at: " + name)

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


names = ["A Chavez", "A Hamon", "A Harvey", "A Mohyuddin CIBC leg", "A Polaszek", "A Postle", "A wogumi", "A, Mohyuddin CIBC leg.",
         "A. Aguias", "A. Broodbank", "A. Busck", "A. C. Jashi", "A. Garido", "A. Harvey", "A. K. Walker", "A. Lopez-Avila", "A. Michelmore",
         "A. Mohyuddin", "A. Mohyuddin CIBC", "A. Mohyuddin CIBC leg.", "A. Moore", "A. Polac. E", "A. Polac. E.", "A. Polarsek",
         "A. Polaszak", "A. Polaszek", "A. Polaszek et al.", "A. van Harten", "A.Aguiar"]

token_set_clustering(names)
for list in cluster_list:
    print(list)
