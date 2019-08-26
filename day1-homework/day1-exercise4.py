#!/usr/bin/env python3

import sys

for i,line in enumerate(open( sys.argv[1])):
    fields = line.strip("\n").split("\t")
    if i >= 10:
        break
    print (fields[2])
        