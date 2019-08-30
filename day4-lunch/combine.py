#!/usr/bin/env python3

"""
Usage: ./combine.py

"""

import sys
import matplotlib.pyplot as plt 
import numpy as np
import scipy.stats as stats

threshhold = float(sys.argv[1])
criteria = sys.argv[2]

for i in range(3: len(sys.argv[])):
    
    fpkm = {name1 : sys.argv[] :, "FPKM"}
    
    for j, line in enumerate(open(i)):
        if j == 0:
            continue
            fields = line,rstrip("\n").split("\t")
