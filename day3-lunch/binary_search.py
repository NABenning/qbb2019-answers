#!/usr/bin/env python3

import sys

protein_coding_genes = {}

protein_coding_genes_count = 0 
#str(fields[4]) == gene end
#str(fields[3]) == gene beginning
 
for line in open( sys.argv[1] ):
   fields = line.strip("\n").split()
   if line.startswith( "#" ):
           continue
   
   gene_beginning = int(fields[3])
   gene_end = int(fields[4])
   gene_mid = float(gene_beginning + gene_end) / 2
   for i, mini in enumerate( fields[8:]):
       if "gene_name" in mini:
           gene_name = fields[8 + i + 1]
           break
           
   #gene_mid = (str(fields[4]) + str(fields[3]))/2
   if "protein_coding" in line:
       if fields[0] == "3R" and fields[2] == "gene":
           protein_coding_genes_count +=1
           print(gene_beginning , gene_end , gene_mid , gene_name)  
                                                                            
           protein_coding_genes.update({str(fields[3]): str(fields[4])})    

#print("number of protein coding genes: " + str( protein_coding_genes_count))
"""list of genes moved into ~/day3-lunch/genes.txt for later use as sys.argv[2]""" 



#def ()
 # for i, line in enumerate( open( sys.argv[2] ) ):
  #    fields = line.strip("\n").split("\t")
 # lo = 0
 # hi = len(line)-1
 # mid = 0
 # number_iterations = 0
 # while (lo <= hi):
 #     mid = (hi+lo)/2
 #     number_iterations = number_iterations + 1
 #     if (search_pos < gene_list[mid][0]):
          #pick low range
 #     elif (search_pos > gene_list[mid][1]):
          #pick hi range
  #    else:
  #        gene_list[mid]

        
    