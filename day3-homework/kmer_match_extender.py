#!/usr/bin/env python3

from fasta import FASTAReader
import sys


k = int(sys.argv[3] )
query = FASTAReader( open( sys.argv[2] ) )
target = FASTAReader( open( sys.argv[1] ) )
target_dictionary = {}
right_ext_kmer = []
left_ext_kmer = []
#kmer_extension = []

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range (0, len(sequence) - k + 1):
        kmer_target = sequence[i:i+k]
        if kmer_target not in target_dictionary:
            target_dictionary[kmer_target] = [(i, ident)]
        else:
            target_dictionary[kmer_target].append((i, ident))

output_list = []
for ident2, sequence2 in query:
    sequence2=sequence2.upper()
    ignore_set = set()
    for j in range(0, len(sequence2) - k + 1):
        kmer_query = sequence2[j:j+k]
        if kmer_query in target_dictionary:
            for target_start, target_id in target_dictionary[kmer_query]:
                if (target_id,target_start) in ignore_set:
                    continue
                match_len = k
                seq = kmer_query
                last_target_start = target_start
                x = j + 1
                while x < len(sequence2) - k + 1:
                    next_kmer = sequence2[x:x+k]
                    if next_kmer in target_dictionary:
                        flag = False
                        for i, ident in target_dictionary[next_kmer]:
                            if ident == target_id and i == last_target_start + 1:
                                match_len += 1
                                last_target_start += 1
                                flag = True
                                seq = seq + next_kmer[-1]
                                ignore_set.add((ident,i))
                        if not flag:
                            break
                    else:
                        break
                    x += 1
                output_list.append((match_len, seq, target_id, target_start, j))
        
       #  x = 0
       #  if kmer_query[j+k+x] == kmer_target[j+k+x]:
       #      x += 1
       #  else:
       #      right_ext_kmer = kmer_target[j:j+k+x]
       #
       #  z = 0
       #  if kmer_query[j+k+z] == kmer_target[j+k+z]:
       #      z -= 1
       #  elif kmer_ques[j] == kmer_query[j+k+z]:
       #      break
       #  else:
       #      left_ext_kmer = kmer_target[j:j+k+z]
       #
       #
       # for x, z in range(0, len(sequence2) - k + 1):
       #     kmer_extension = sequence2[x:x+k+z]
       #     if kmer_query in target_dictionary:
       #         kmer_extension = kmer_extension.append(target_dictionary[kmer_query], str(j), kmer_query, kmer_extension)
       #
       #
for match_len, seq, target_id, target_start, j in sorted(output_list,reverse=True,key =lambda t: t[0]):
    print(match_len, seq, target_id, target_start, j)


