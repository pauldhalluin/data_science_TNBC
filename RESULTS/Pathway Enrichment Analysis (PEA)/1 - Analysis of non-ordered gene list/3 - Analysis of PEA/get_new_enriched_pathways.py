"""
The function most_enriched_pathways takes in parameter the name of the .csv file of the
most enriched pathways for the list of known targets and for the list of predicted targets.
The idea is to compare both analyses in order to identify the pathways that appeared in the 
list of enriched pathways wwith DTI prediction.
It returns one .txt file of the list of the pathways which appeared with prediction ordered by 
their result p on the statistical test of pathway enrichment analysis.
"""

import csv

def new_enriched_pathways(file_known_enriched_pathways, file_predicted_enriched_pathways):
    file_tout = open(file_predicted_enriched_pathways)
    doc_tout = csv.reader(file_tout)

    liste_pathway_tout = []
    var = False
    for ligne in doc_tout:
        if var == True:
            liste_pathway_tout.append([ligne[1], ligne[4]])
        var = True

    file_connu = open(file_known_enriched_pathways)
    doc_connu = csv.reader(file_connu)

    liste_pathway_connu = []
    var = False
    for ligne in doc_connu:
        if var == True:
            liste_pathway_connu.append(ligne[1])
        var = True

    for i in range(len(liste_pathway_tout) - 1, -1, -1):
        if liste_pathway_tout[i][0] in liste_pathway_connu:
            liste_pathway_tout.pop(i)

    f = open("new_enriched_pathways.txt", "w")
    f.write('Pathway,-log(p)')
    f.write('\n')
    for pathway in liste_pathway_tout[:-1]:
        f.write(pathway[0] + ',' + pathway[1])
        f.write('\n')
    f.write(liste_pathway_tout[-1][0] + ',' + liste_pathway_tout[-1][1])
    f.close