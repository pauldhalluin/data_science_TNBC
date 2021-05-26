This folder is organized in two sub-folders which correspond to two different analyses that I made. This distinction comes from the usage of the server g:Profiler for Pathway Enrichment Analysis. The module g:GOSt that I used takes indeed for parameter a list of genes that can be ordered by importance or not. This is an option that has to be chosen at the beginning of the analysis.

The first folder "1 - Analysis of non_ordered gene list" is naturally the analysis that I made with no order in the list of genes. The second one corresponds to the analysis of the ordered list of genes. The results are different, therefore I thought it was a good idea to separate them. The way of ordering the genes and whether or not to do it are two crucial parameters to set.

The two sub-folders are themselves organized in three sub-sub-folders:

- the selection of the proteins for the analysis: after all the predictions for all the hits of the list, there has to be a selection of the main targets. The two algorithms in this folder make this selection (while ordering or not, depending on which analysis it is): one selects all the targets that are known to be existing and the other selects the top predicted proteins. The results of these selections are in the folder in the form of .txt files that are well suited for g:Profiler.

- the results of the PEA: this folder contains the results of the search of enriched pathways, either in the form of .csv file or in the form of .jpg files, for the list of known targets and for the list of predicted targets. The idea behind the fact of doing two analyses (for known and predicted targets) is to be able to compare them and observe in what ways virtual screening helped.

- the analysis of the PEA: this folder contains the python files that make the comparison between the results of the PEA for known and predicted targets and the results in the form of Excel sheets and .txt files.