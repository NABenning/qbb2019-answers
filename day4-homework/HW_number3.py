#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs.csv>
Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


t_name = sys.argv[1]
samples = pd.read_csv(sys.argv[2])

def sorter(sex):
    soi=samples.loc[:,"sex"] == sex
    stages = samples.loc[soi,"stage"]
    
    fpkms = pd.read_csv(sys.argv[3],index_col="t_name")

    my_data = []
    for stage in stages:
        my_data.append(fpkms.loc[t_name,sex + "_" + stage])
    return my_data
    
male_data = sorter("male")
female_data = sorter("female")

labelz = ["male", "female"]
label2 = ["10","11","12","13","14A","14B","14C","14D"]

fig,ax = plt.subplots()

ax.plot(male_data, color="green")
ax.plot(female_data, color="orange")
ax.set_title("Homework Exercise 3")
ax.set_xlabel("developmental stage")
ax.set_xticklabels(label2,rotation = "vertical")
ax.set_xticks(np.arange(len(label2)))

ax.set_ylabel("mRNA abundance (FPKM)")
plt.legend( labels = labelz, loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()
fig.savefig( "HW4" )
plt.close( fig )