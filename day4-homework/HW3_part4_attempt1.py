"""
arg 4 = replicate
arg 5 = stringtie   
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def get_fpkms(sample_file,sex_,ctab_dir):
    fpkms=[]
    for i,line in enumerate(sample_file):
        if == 0:
            continue
        fields = line.rstrip("\n").split(",")
        sample = fields[0]
        sex = fields[1]
        stage = fields[2]
        if sex != sex_:
            continue
        ctab = os.path.join(ctab_dir,sample,"t_data.ctab")
        df = pd.read_csv(ctab,sep="\t,",index_col="t_name")
        fpkms.append(df.loc["FBtr0331261","FPKM"])
    return fpkms
    

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
# male_data_last4 = male_data[4:8]
# female_data_last4 = female_data[4:8]

male_R = get_fpkms(open(sys.argv[4]),"male",sys.argv[5])
female_R = get_fpkms(open(sys.argv[4]),"female",sys.argv[5])

labelz = ["male", "female"]
label2 = ["10","11","12","13","14A","14B","14C","14D"]

fig,ax = plt.subplots()
# ax.plot(male_data_last4, color="blue")
# ax.plot(female_data_last4, color="red")
ax.plot(range(4,8),male_R,"x",label="male_R",color="blue")
ax.plot(range(4,8),female_R,"x",label="female_R",color="red")
plt.legend(loc="center left", bbox_to_anchor=(1,0.5))
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