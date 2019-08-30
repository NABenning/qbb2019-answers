#!/usr/bin/env python3

"""
Usage: ./approximator.py <ctab> <tab1> <tab2> <tab3> 
"""
#<SRR072893>

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy
from sklearn.decomposition import PCA


f = open("math.bed", "w+")

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    columns = line.strip("\n").split("\t")
    col_interest = columns[1:6]
    strand = col_interest[1]
    if strand == "-":
        promoter_start = int(col_interest[3]) - 500
        promoter_end = int(col_interest[3]) + 500
        promoter_start = max(promoter_start, 1)
        
    else:
        promoter_start = int(col_interest[2]) - 500
        promoter_end = int(col_interest[2]) + 500
        promoter_start = max(promoter_start, 1)  
        
    f.write(col_interest[0] +"\t" + str(promoter_start) +"\t"+ str(promoter_end) + "\t" + col_interest[4] +"\n")
    
f.close()

""" Preparation for OLS """

df = pd.read_csv(sys.argv[1], index_col = "t_name", sep = "\t")
col_names1 = df.columns.values.tolist()
fpkms = df.loc[:,"FPKM"]

tab1 = pd.read_csv(sys.argv[2], index_col = "name", sep = "\t")
tab1.columns = ['name','size','covered','sum','mean0','mean']
col_names1 = tab1.columns.walues.tolist()
mean1 = tab1.loc[:,"mean0"]

tab2 = pd.read_csv(sys.argv[3], index_col = "name", sep = "\t")
tab2.columns = ['name','size','covered','sum','mean0','mean']
col_names2 = tab2.columns.walues.tolist()
mean2 = tab1.loc[:,"mean0"]

tab3 = pd.read_csv(sys.argv[4], index_col = "name", sep = "\t")
tab2.columns = ['name','size','covered','sum','mean0','mean']
col_names3 = tab3.columns.walues.tolist()
mean3 = tab1.loc[:,"mean0"] 

model = sm.formula.ols(formula = 'fpkms ~ mean1 + mean2 + mean3')
results = model.fit()

print(results.summary())
#histone = predictor
#formula = outcome ~ predictor,prid, data = goi