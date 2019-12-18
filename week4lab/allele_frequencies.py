#!/usr/bin/env python3

"""USAGE ./allele_frequencies.py <vcf file>"""

import sys
import matplotlib.pyplot as plt

allele_freq = []

for line in open(sys.argv[1]):
   if line.startswith("#"):
       continue
   field = line.rstrip("\n").split()
   info = field[7]
   allele_frequency_split = info.split("=")[1]
   allele_frequency_split = allele_frequency_split.split(",")
   for number in allele_frequency_split:
       allele_freq.append(float(number))
    
fig, ax = plt.subplots()
ax.hist(allele_freq, color = "red", bins = 100, density = True)

plt.tight_layout()

ax.set_xlabel("Allele")
ax.set_ylabel("Frequency")
ax.set_title("Allele Frequency")

fig.savefig("Frequency_Allele.png")
plt.close(fig)