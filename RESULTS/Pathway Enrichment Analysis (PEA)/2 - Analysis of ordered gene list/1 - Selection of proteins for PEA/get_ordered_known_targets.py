"""
This code selects the proteins that are known to be interacting with the drugs 
of all the .csv files within the same folder.
It only keeps the known targets of the hits.
It creates a .txt file that is suited for g:Profiler.
Here the proteins are ordered by the number of occurences in the list.
"""

import os
import csv

list_files = []
for file in os.listdir():
    if file.endswith(".csv"):
        list_files.append(os.path.join(file))

threshold = 0.9

list_genes = []
for file_name in list_files:
    file = open(file_name)
    doc = csv.reader(file)
    var = True
    for line in doc:
        if var == False:
            if line[-1] == "False":
                    list_genes.append([line[2], float(line[4])])
        var = False

list_genes.sort()
list_genes_int = []
list_occur = []
for i in range(len(list_genes) - 1):
    if list_genes[i][0] not in list_genes_int:
        compteur = 1
        proba = list_genes[i][1]
        k = i
        while list_genes[k][0] == list_genes[k + 1][0]:
            proba += list_genes[k + 1][1]
            compteur += 1
            k += 1
            if k == len(list_genes) - 1:
                break
        list_genes_int.append(list_genes[i][0])
        list_occur.append([compteur, proba/compteur, list_genes[i][0]])
list_occur.sort(reverse = True)
list_genes_fin = []
for gene in list_occur:
    list_genes_fin.append(gene[2])

print(len(list_genes_fin))
f = open("known_proteins.txt", "w+")
for gene in list_genes_fin[:-1]:
    if len(gene) != 0:
        f.write(gene)
        f.write("\n")
f.write(list_genes_fin[-1])
f.close()