#!/usr/bin/env python3

import sys

in_file= open(sys.argv[1])
mapqsum = 0
counter = 0

for line in in_file:
    fields = line.strip().split("\t")
    mapqsum += int(fields[4])
    counter += 1

avg = float(mapqsum) / float(counter)    
print(avg)