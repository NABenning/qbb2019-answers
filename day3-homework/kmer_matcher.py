#!/usr/bin/env python3

from fasta import FASTAReader
import sys


k = int(sys.argv[3] )
query = FASTAReader( open( sys.argv[2] ) )
target = FASTAReader( open( sys.argv[1] ) )
target_dictionary = {}

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range (0, len(sequence) - k + 1):
        kmer_target = sequence[i:i+k]
        if kmer_target not in target_dictionary:
            target_dictionary[kmer_target] = [(i, ident)]
        else:
            target_dictionary[kmer_target].append((i, ident))
            
for ident2, sequence2 in query:
    sequence2=sequence2.upper()
    for j in range(0, len(sequence2) - k + 1):
        kmer_query = sequence2[j:j+k]
        if kmer_query in target_dictionary:
            print(target_dictionary[kmer_query], str(j), kmer_query)

        