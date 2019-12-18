#!/usr/bin/env python3

"""USAGE: ./variant_snp_analaysis.py <snpEff_result_file>"""

import sys
import matplotlib.pyplot as plt
import numpy as np

vsp = open(sys.argv[1])
quality = []
freq = []
depth = []
effect = {}

for line in vsp: 
    if line.startswith("#"):
            continue 
    col= line.rstrip("\n").split("\t")
    fields = col[7].rstrip("\n").split(";")
        
    dp = fields[7].rstrip("\n").split("=")
    depth.append(dp[1])
    
    quality.append(int(float(col[5])))
   
    af = fields[3].rstrip("\n").split("=")
    freq.append(af[1])
        
    cola = fields[41].rstrip("\n").split("|")
    ai = cola[1]
    if ai in effect: 
        effect[ai] += 1
    else: 
        effect[ai] = 1
            
# for i, line in enumerate(open(sys.argv[1])):
#     if line.startswith("#"):
#         continue
#
#     depth_slice = line.rstrip("\n").split(";")[7]
#     depth_val = depth_slice.split("=")[1]
#     if "," in depth_val:
#         depth_val = depth_val.split(",")[1]
#     depth.append(float(depth_val))
#
#     #repeat for allele frequencies
#
#     freq_slice = line.rstrip("\n").split(";")[3]
#     freq_val = freq_slice.split("=")[1]
#     if "," in freq_val:
#         freq_val = freq_val.split(",")[1]
#     freq.append(float(freq_val))
#
#     fields = line.rstrip("\n").split()
#     quality.append(float(fields[5]))
#
#     fields = line.split("|")
#     if fields[1] not in effect:
#         effect[fields[1]] = 1
#     elif fields[1] in effect:
#         effect[fields[1]] += 1
#
# #making the 2x2 figure
#
# fig, ax = subplots(2 ,2)
#
# ax[0,0].hist(depths, range = [0,750], bins = 100)
# ax[0,0].set_xlabel("Read Depth")
# ax[0,0].set_ylabel("Frequency")
#
# ax[0,1].hist(quality, range = [0,2000], bins = 100)
# ax[0,1].set_xlabel("Quality of Genotype")
# ax[0,1].set_ylabel("Frequency")
#
# ax[1,0].hist(freq, bins = 100)
# ax[1,0].set_xlabel("Allele")
# ax[1,0].set_ylabel("Frequency")
#
# ax[1,1].bar(effect.keys(), effect.values())
# ax[1,1].set_ylabel("Frequency")
# ax[1,1].set_xticklabels(effect.keys(), rotation = "vertical", fontsize = 4)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

"""Read Depth Histogram"""
ax1.hist(depth, bins = 100, density = True)
ax1.set_title("Read Depth Distribution", size = 15)
ax1.set_xlabel("Read Depth")
for tick in ax1.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(5)

"""Quality Histogram"""
ax2.hist(quality, bins = 50, density = True, range = (0, 2500))
ax2.set_title("Quality Distribution", size = 15)
ax2.set_xlabel("Quality", size = 10)

"""Allele Frequency Histogram"""
ax3.hist(freq, bins = 50, density = True)
ax3.set_title("Allele Frequency Histogram", size = 15)
ax3.set_xlabel("Frequency", size = 10)
for tick in ax3.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(8)


"""Summary of Predicted Effects"""
plt.bar(range(len(effect)), list(effect.values()), align = 'center')
plt.xticks(range(len(effect)), list(effect.keys()), rotation = 'vertical', size = 8)
ax4.set_title("Predicted Effects", size = 15)
ax4.set_xlabel("Effects", size = 10)
ax4.set_ylabel("Frequency", size = 10)

fig.set_size_inches(40, 14)
plt.tight_layout()
fig.savefig("variant_snp_analysis.png")
plt.close(fig)

    