#!/usr/bin/env Python3

import scipy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from sklearn.cluster import KMeans

hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = "gene", header = 0)

cfu = df["CFU"].values
poly = df["poly"].values

Data = {'x': cfu, 'y': poly}

df2 = pd.DataFrame(Data, columns=['x','y'])

kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_

fig,ax = plt.subplots()
plt.scatter(df2['x'], df2['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=50)

fig.savefig('kmeans.png')
plt.close(fig)