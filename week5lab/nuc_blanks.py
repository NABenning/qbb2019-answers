#!/usr/bin/env python3

"""USAGE: ./nuc_blanks.py mafft.parsed.tsv blastn-results.tsv"""

from fasta import FASTAReadef
import sys
import matplotlib.pyplot as plt
import numpy as np

f = open(sys.argv[1])
f2 = open(sys.argv[2])

reader = FASTAReader(f)
reader2 = FASTAReader(f2)

count = 0
protein_seq = {}
for ident, seq in reader:
    count += 1
    ident = count
    protein_seq[ident] = seq

count2 = 0  
nt_seq = {}
for ident, seq in reader2:
    count2 += 1
    ident = count2
    nt_seq[ident] = seq

new_seq = {}
for ident in protein_seq:
    pseq = protein_seq[ident]
    nseq = nt_seq[ident]
    newline = ""
    nuc_pos = 0
    for character in pseq:
        if character == "-":
            newline += "---"
        else:
            newline += nseq[nuc_pos:nuc_pos+3]
            nuc_pos += 3
    new_seq[ident] = newline

table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

z_score = {}
d_score = []
for i in range(0,len(new_seq[1]), 3):
    q_codon = new_seq[1][i:i+3]
    ds_count = 0
    dn_count= 0
    for ident in new_seq:
        seq_codon = new_seq[ident][i:i+3]
        if q_codon != seq_codon:
            if q_codon == '---' or seq_codon == '---':
                continue
            if q_codon not in table or seq_codon not in table:
                continue
            if table[q_codon] == table[seq_codon]:
                ds_count += 1
            else:
                dn_count += 1
                
    d = dn_count - ds_count
    d_score.append(d)
std = np.std(d_score)
print(d_score)
for i,d in enumerate(d_score):
    z_score[i] = d/std
    
    
x = []
y = []                
for key in z_score:
    x.append(key)
    value = z_score[key]
    y.append(value)
    

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.xlabel("Sequence Idenitites")
plt.ylabel("Z Scores")
plt.title ("Z Scores")
fig.savefig("zscores.png")
plt.close(fig)

# arg1 = open(sys.argv[1])
# arg2 = open(sys.argv[2])
# prot = {}
# nucleo = {}
# back_to_nuc = {}
#
# table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
#       'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
#       'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
#       'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
#       'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
#       'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
#       'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
#       'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
#       'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
#       'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
#       'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
#       'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
#       'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#       'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
#       'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
#       'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
#
# for line in arg1:
#    col = line.split()
#    Id1 = col[0]
#    Id = col[0].rstrip("1").rstrip('_')
#    seq = col[1]
#    prot[Id] = seq
#
# for line2 in arg2:
#    col2 = line2.split("|")
#    Id2 = col2[3]
#    seq2 = col2[4]
#    nucleo[Id2] = seq2
#
# for seq_ID in prot:
#   nuc_pos = 0
#   nuc_update = ""
#   prot_seq = prot[seq_ID][0]
#   nuc_seq = nucleo[seq_ID][1]
#   for char in prot_seq:
#       if char == "-":
#           nuc_update += "---"
#       else:
#           nuc_update += nuc_seq[nuc_pos:nuc_pos+3]
#           nuc_pos += 3
#
#   back_to_nuc[seq_ID] = nuc_update
#
# for i in range(len(back_to_nuc['query']),3):
#     q_codon = back_to_nuc['query'][i:i+3]
#     dS = 0
#     dN = 0
#     for seq_ID in back_to_nuc:
#         seq_codon = back_to_nuc[seq_id][i: i+3]
#         if seq_codon != q_codon:
#             if table[q_codon] == table[seq_codon]:
#                 dS += 1
#             else:
#                 dN + 1
#
#         print(dS)
#         print(dN)