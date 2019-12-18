#!/usr/bin/env python3

"""
filtering.py 
"""

import scanpy as sc 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts = 1)
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all')

filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)

adata = adata[:, filter_result.gene_subset]
sc.pp.normalize_per_cell(adata) 
sc.pp.log1p(adata)
sc.pp.scale(adata)
#sc.tl.pca(adata,n_comps=50)
#sc.pl.pca(adata)

sc.pp.neighbors(adata)
# sc.tl.umap(adata)
sc.tl.louvain(adata, resolution=0.3)
# sc.pl.umap(adata, color='louvain')
sc.tl.tsne(adata)
sc.pl.tsne(adata, color = ["louvain", "Tsc22d1", "Dbi", "Tubb3", "Lhx6", "Arpp21","Zbtb20", "Dlx6os1", "Hbb-bs", "Arpc1b", "Reln", "Rgs5"], legend_loc="on data" )
sc.tl.rank_genes_groups(adata, 'louvain', groups=['0','1','2','3','4','5','6','7','8','9','10'], method = 'logreg' )
sc.pl.rank_genes_groups(adata)

# sc.pl.tsne(adata, color='louvain')
















