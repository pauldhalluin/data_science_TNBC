"""
The function most_enriched_pathways takes in parameter the name of the .csv file of the
most enriched pathways for the list of known targets and for the list of predicted targets.
The idea is to compare both analyses in order to identify the pathways that DTI prediction
enriched.
It returns one .txt file of the list of pathways ordered by enrichment with prediction.
"""

import csv

def most_enriched_pathways(file_known_enriched_pathways, file_predicted_enriched_pathways):
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
    ls_pathway = []
    var = False
    for ligne in doc_connu:
        if var == True:
            liste_pathway_connu.append(ligne[1])
            ls_pathway.append([ligne[1], ligne[4]])
        var = True

    for i in range(len(liste_pathway_tout) - 1, -1, -1):
        if liste_pathway_tout[i][0] not in liste_pathway_connu:
            liste_pathway_tout.pop(i)

    ls_pathways = []
    for pathway1 in liste_pathway_tout:
        for pathway2 in ls_pathway:
            if pathway1[0] == pathway2[0]:
                ls_pathways.append([float(pathway1[1]) - float(pathway2[1]), pathway1[0]])
    ls_pathways.sort(reverse = True)

    f = open("most_enriched_pathways.txt", "w")
    f.write('Pathway,Diff log')
    f.write('\n')
    for pathway in ls_pathways[:-1]:
        f.write(pathway[1] + ',' + str(pathway[0]))
        f.write('\n')
    f.write(ls_pathways[-1][1] + ',' + str(ls_pathways[-1][0]))
    f.close