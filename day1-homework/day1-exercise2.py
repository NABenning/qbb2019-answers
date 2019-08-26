#!/usr/bin/env python3

import sys

counter = 0 
for line in open( sys.argv[1]):
    if "NM:i:0" in line:
        counter +=1
print(counter)