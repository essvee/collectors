from fuzzywuzzy import process
from fuzzywuzzy import fuzz


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

names = ["A Chavez", "A Hamon", "A Harvey", "A Mohyuddin CIBC leg", "A Polaszek", "A Postle", "A wogumi", "A, Mohyuddin CIBC leg.",
         "A. Aguias", "A. Broodbank", "A. Busck", "A. C. Jashi", "A. Garido", "A. Harvey", "A. K. Walker", "A. Lopez-Avila", "A. Michelmore",
         "A. Mohyuddin", "A. Mohyuddin CIBC", "A. Mohyuddin CIBC leg.", "A. Moore", "A. Polac. E", "A. Polac. E.", "A. Polarsek",
         "A. Polaszak", "A. Polaszek", "A. Polaszek et al.", "A. van Harten", "A.Aguiar"]


clean_cluster = cluster_names(names)
print(names)
for clean_names in clean_cluster:
    print(clean_names)

