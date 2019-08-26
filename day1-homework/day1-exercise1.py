#!/usr/bin/env python3
#fields = line.split("\t")
import sys

counter = 0
for line in open( sys.argv[1]):
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1

print(counter)