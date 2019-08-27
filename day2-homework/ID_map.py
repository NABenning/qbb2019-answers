#!/usr/bin/env python3

"""USAGE: ./ID_map.py <organized flybase ID> <ctab file> <default/nothing>"""

import sys

gene_dictionary = {}
    
for i, line in enumerate( open( sys.argv[1] ) ):
    columns = line.strip("\n").split()
    gene_name = columns[0]
    uniport = columns[1]
    if gene_name in gene_dictionary:
            continue
    else:
        gene_dictionary[gene_name] = uniport
    
for i, line in enumerate( open( sys.argv[2] ) ):
    columns = line.split("\t")
    gene_ID = columns[8]
    if gene_ID in gene_dictionary:
        print(line, gene_dictionary[gene_ID])
    elif gene_ID not in gene_dictionary and sys.argv[3] == "nothing":
        continue
    elif gene_ID not in gene_dictionary and sys.argv[3] == "default":
        print("N/A")
        
            
    