#!/usr/bin/env python3

import sys
import numpy

"""Organize input data"""

protein_coding_genes = {}

mid_list = [] #for use in Binary Search

protein_coding_genes_count = 0 
 
for line in open( sys.argv[1] ):
   fields = line.strip("\n").split()
   if line.startswith( "#" ):
           continue
   
   gene_beginning = int(fields[3])
   gene_end = int(fields[4])
   gene_mid = (gene_beginning + gene_end) / 2
   for i, mini in enumerate( fields[8:]):
       if "gene_name" in mini:
           gene_name = fields[8 + i + 1]
           break
           
   if "protein_coding" in line:
       if fields[0] == "3R" and fields[2] == "gene":
           protein_coding_genes_count +=1
           print(gene_beginning , gene_end , gene_mid , gene_name) 
           
           protein_coding_genes.update({str(fields[3]): str(fields[4])})
           mid_list.append(gene_mid)
           
           for i in range(0, len(mid_list)):
               mid_list[i] = int(mid_list[i])
               


"""Binary Search """           
           

startpos = []

length1 = len(startpos)
mutation = 21378950
#mutation_test = int(input("try:"))

def binary_search(lst, m):
   l = len(lst)
   first = 0
   last = l-1
   flag = 0
   distance = 0
   iteration = 0
   while first <= last:
       mid = int((first + last) / 2)
       iteration += 1
       if lst[mid_list] == m:
           flag = 1
           break
       elif lst[mid_list] > m:
           last = mid_list - 1
       else:
           first = mid_list + 1


   if flag == 0 and mid_list+1 < l:
       if lst[mid_list+1] - m >= m - lst[mid_list]:
           distance = m - lst[mid_list]
           return lst[mid_list], distance, iteration
       else:
           distance = lst[mid_list+1] - m
           return lst[mid_list+1], distance, iteration
   elif mid_list + 1 >= l:
       distance = m - lst[mid_list]
       return lst[mid_list], distance, iteration
   else:
       return lst[mid_list], distance, iteration



answer= binary_search(startpos, mutation)
key = str(answer[0])
dis = int(answer[1])
itera = int(answer[2])

print("nearest gene is ", protein_coding_genes[key],"\n", "disntance=", dis,"bp\n", "iteration=", itera)

        
    