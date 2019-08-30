#!/usr/bin/env python3

"""
Usage: ./00-metadata.py <metadata.csv> <ctab_dir>

        <ctab_dir> e.g. ~/qbb2019-answers/results/stringtie

Create all.csv with FPKMs

        t_name, gene_name, sample1, ... , samplen
"""

import sys
import os
import pandas as pd


metadata = sys.argv[1]
ctab_dir = sys.argv[2]
# gene_name = sys.argv[3]
fpkms = {}

for i, line in enumerate( open(metadata)):
    if i == 0:
        continue
    fields = line.strip("\n").split(",")
    srr_id = fields[0]
    srr_sex = fields[1]
    srr_time = fields[2]
    srr_join = srr_sex + "_" + srr_time
    # gene_name_mod = {}
    ctab_path = os.path.join( ctab_dir, srr_id, "t_data.ctab")

    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
        
    # fpkms[str(sys.argv[3])] = df.loc[:,str(sys.argv[3])]
#     fpkms[gene_name_mod] = df.loc
    
    print(fpkms)
    
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[srr_join] = df.loc
    
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[srr_join] = df.loc
    
    """ separate males from females """
    
    males = df.loc[[2,9],:]
    female = df.loc[10,:]
    
    
    samples = pd.read_csv[sys.argv[2]]
    
    samples = pd.read_csv( sys.argv[2])
    females = samples.loc[:,"sex"] == "female"
    
    samples = pd.read_csv( sys.argv[2])
    males= samples.loc[:,"sex"] == "male"
    
    # print(males)
#     print(females)

df_fpkms=pd.DataFrame(fpkms)

pd.DataFrame.to_csv( df_fpkms, "all.csv")