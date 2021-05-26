"""
This code selects the proteins that are known to be interacting with the drugs 
of all the .csv files within the same folder.
It only keeps the known targets of the hits.
It creates a .txt file that is suited for g:Profiler.
Note that there is no order of importance of the proteins in the selection.
"""

import os
import csv

list_files = []
for file in os.listdir():
    if file.endswith(".csv"):
        list_files.append(os.path.join(file))

list_genes = []
for file_name in list_files:
    file = open(file_name)
    doc = csv.reader(file)
    var = True
    for line in doc:
        if var == False:
            if line[-1] == "False":
                if line[2] not in list_genes:
                    list_genes.append(line[2])
        var = False
print(len(list_genes))     
f = open("known_proteins.txt", "w+")
for gene in list_genes[:-1]:
    f.write(gene)
    f.write("\n")
f.write(list_genes[-1])
f.close()