#!/usr/bin/env Python3

import scipy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list

hema = open(sys.argv[1])
df = pd.read_csv(hema, sep = "\t", index_col = 0)



linky = linkage(df, 'single', 'euclidean')
leafy = leaves_list(linky)

# for i, line in enumerate(hema):
#     if i == 0:
#         continue
#
#     column.append(float(line.split("\t")[1]))
    


df3 = df.transpose()
linky2 = linkage(df3, 'single', 'euclidean')
leafy2 = leaves_list(linky2)

df4 = df.iloc[:,leafy2]
df5 = df4.iloc[leafy,:]

fig, ax = plt.subplots()

ax = dendrogram(linky2, truncate_mode = 'level', leaf_rotation = 90, labels = df3.index)

fig.savefig("dendrogram.png")


plt.close(fig)