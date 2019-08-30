#!/usr/bin/env python3

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

# fpkm = {"sample1" : [1,2,3], "sample2" : [4,5,6]}
fpkm = { name1 : ctab1.loc[:,"FPKM"] , name2 : ctab2.loc[:,"FPKM"]}

df = pd.DataFrame( fpkm )
df +=1 

r=df.loc[:,name1]
g=df.loc[:,name2]

m=np.log2(r/g)
a= 0.5*np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter(a,m,alpha=0.2, s=2)
plt.xlabel("Log2 Average Expression")
plt.ylabel("Log2(SRR07894 / SRR07895)")
plt.suptitle("SRR07894 / SRR07895")
fig.savefig("MA_plot.png")
plt.close(fig)