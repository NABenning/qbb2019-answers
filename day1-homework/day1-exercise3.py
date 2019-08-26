#!/usr/bin/env python3

import sys

counter = 0 
for line in open( sys.argv[1]):
    fields = line.strip("\n").split("\t")   
    if "NH:i:1" in fields[11:]:
        counter +=1
print(counter)    