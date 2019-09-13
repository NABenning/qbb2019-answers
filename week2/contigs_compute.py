#!/usr/bin/env python3

"""USAGE: ./contigs_compute.py <contigs.fa> <Lastz output>"""

import sys
import matplotlib.pyplot as plt
import numpy as np

class FASTAReader( object ):
    
    def __init__( self, fh ):
        self.fh = fh
        self.last_ident = None
        self.eof = False
        
    def next( self ):
        
        if self.eof:
            return None, None            
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")            
        else:
            ident = self.last_ident
            
        #if we reach this point, ident is set correctly
        
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append( line.strip() )
                
        sequence = "".join( sequences )
        return ident, sequence
        

reader = FASTAReader(open(sys.argv[1]))

num_of_contigs = 0

list_length_of_contigs = []

while True:
    ident, sequence = reader.next()
    list_length_of_contigs.append(len(str(sequence)))
    num_of_contigs += 1
    if ident is None:
         break
    print(ident, sequence)   
print(num_of_contigs) 

list_length_of_contigs = sorted(list_length_of_contigs, reverse=True)

average = (list_length_of_contigs[0]+list_length_of_contigs[-1])/len(list_length_of_contigs)

num_sum = 0
for num in list_length_of_contigs:
    num_sum += num
    if num_sum >= sum(list_length_of_contigs)/2:
        print(str(num))
        break
        
print(list_length_of_contigs[0])
print(list_length_of_contigs[-1])

"""attempting to make dotplots"""

f = open(sys.argv[2])

list_y = []
list_x = []
for i,line in enumerate(f):
    if i == 0:
        continue
    col = line.strip("\n").split("\t")
    start = col[3]
    end = col[4]
    contig = col[8]
    
    list_y.append(int(end) - int(start))
    list_x.append(int(col[8]))    

""" commented out stuff makes a variation on the dotplot """
    
# start1 = []
# end1 = []
# start2 = []
# end2 = []
#
# for line in open(sys.argv[2]):
#     if not line.startswith("#"):
#         fields = line.rstrip("\n").split()
#         if fields[6] != "-" and fields[0] == "0":
#             start1.append(fields[3])
#             end1.append(fields[4])
#             start2.append(fields[7])
#             end2.append(fields[-1])
#
# start1 = sorted(start1)
# end1 = sorted(end1)
# start2 = sorted(start2)
# end2 = sorted(end2)

fig, ax = plt.subplots()
fig.suptitle("Spades1 subplot")

# for i in range(len(start1)):
#     plt.plot(start2[i], start1[i], "ro-")
#     plt.plot(end2[i],end1[i], "ro-")

ax.scatter(list_x, list_y, alpha = 0.2)
ax.set_xlabel("len of reference")
ax.set_ylabel("len of contig")

#ax.plot(start1,start2)
#ax.plot(end1,end2)

    
fig.savefig("dot.png")
plt.close()

