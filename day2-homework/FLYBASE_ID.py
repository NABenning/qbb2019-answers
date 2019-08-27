#!/usr/bin/env python3

"""USAGE: ./FLYBASE_ID <flybase data>. Outputs "organized flybase ID" for use in ID_map.py""" 

import sys


FlyBase_ID = []  
f = open(sys.argv[1])

for i, line in enumerate(f):
    columns = line.split( )
    for field in columns:
                
        if field.endswith("DROME"):
            if "FBgn" not in columns[-1]:
                continue
            print(columns[-1],columns[-2])
        
        
     
      

    
    