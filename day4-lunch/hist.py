#!/usr/bin/env python3

"""
Usage: ./hist.py <ctab> <a> <mu_scew> <sigma_scew> <mu_norm> <sigma_norm>

Plot FPKM
"""

import sys
import matplotlib.pyplot as plt 
import numpy as np
import scipy.stats as stats

fpkms = []
for i, line in enumerate( open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]))
        
print( len(fpkms) )        

my_data = np.log2( fpkms )

a = float(sys.argv[2])
mu_scew = float(sys.argv[3])
sigma_scew = float(sys.argv[4])
mu_norm = float(sys.argv[5])
sigma_norm = float(sys.argv[6])

x = np.linspace( -15, 15, 100)
y = stats.norm.pdf(x, mu_norm, sigma_norm)  
z = stats.skewnorm.pdf(x, a, mu_scew, sigma_scew)

fig, ax = plt.subplots()
ax.hist( my_data, bins=100, density=True )
ax.plot( x, y)
ax.plot( x, z)
plt.suptitle("fkpms")
plt.xlabel("log_2(FPKMs)")
plt.ylabel("percentage of total")
plt.figtext(x = 0.15,y = 0.8,s = "a = -10, mu_scew = 6, sigma_scew = 3.5")
plt.figtext(x = 0.15,y = 0.7,s = "mu_norm = 4, sigma_norm = 2")
fig.savefig("fpkms.png")
plt.close( fig )

