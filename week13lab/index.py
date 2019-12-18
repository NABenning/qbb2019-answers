#!/usr/bin/env python2

""" ./index.py chr10_rna_binned.bed chr10_activity_binned.bed """

import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

input1 = []
fieldstuple = ()

v = [0]*7000
v2 = [0]*7000


rna_index = []
rna_expression = {}
for i, line in enumerate(f1):
    if i == 0:
        continue        
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index = (int(fields[1])-5000000)/5000
        #v[index] = float(fields[-2])
        rna_index.append(index)
        rna_expression[index] = float(fields[-2]) 
        
activity_index = []
activity_value = {}
for i, line in enumerate(f2):
    if i == 0:
        continue
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:     
        index2 = (int(fields[1])-5000000)/5000
        #v2[index2] = float(fields[-2])
        activity_index.append(index2)
        activity_value[index2] = float(fields[-2])        

import hifive
import numpy
hic = hifive.HiC('PROJECT', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

interaction_activity = {}
for index in rna_index:
    int_act = 0
    for index2 in activity_index:
        int_act += float(activity_value[index2])*data[index][index2]
    interaction_activity[index] = int_act

# data_subset = data[numpy.where(v2 > 0), :]
# sum_data_subset = numpy.sum(data_subset, axis=1)
# R = numpy.corrcoef(sum_data_subset, v2)[0, 1]

rna_expression_list = []
interaction_activity_list = []

for index in rna_index:
    rna_expression_list.append(float(rna_expression[index]))
    interaction_activity_list.append(interaction_activity[index])
rna_array = numpy.array(rna_expression_list)
interaction_activity_array = numpy.array(interaction_activity_list)
R_value = numpy.corrcoef(rna_array, interaction_activity_array)[0, 1]
print "R coefficient =" , R_value

# print(data)
# print(R)
        