#!/usr/bin/env python3

""" Usage: ./dotplots.py <output of lastz>"""

import sys
import matplotlib.pyplot as plt

start = []
end = []

for line in open(sys.argv[1]):
    if "#" in line:
        continue
    col = line.rstrip("/n").split()
    if col[7] != "-":
        start.append((int(col[5])-int(col[4])))
        end.append(int(col[8]))


# start_target = []
# end_target = []
# count_query = []
# end_query = []
#
# dic = {}
#
# for i,line in enumerate(open(sys.argv[1])):
#      if not line.startswith("#"):
#              fields = line.rstrip("\n").split()
#              if fields[6] != "-" and fields[0] == "0":
#                  dic[int(fields[3])] = [fields[3], fields[4], int(fields[-1]) - int(fields[-2])]
#
# for key in sorted(dic):
#     start_target.append(dic[key][0])
#     end_target.append(dic[key][1])
#     count_query.append(dic[key][2])
#
# x_values = 0

fig,ax = plt.subplots()

# for i in range(len(start_target)):
#     plt.plot([x_values, x_values+count_query[i]],[start_target[i], end_target[i]],'r-')
#     x_values += int(count_query[i])
        
#ax.set_title("Genome Assembly")
# plt.xlabel('Assembled Contigs')
# plt.ylabel('Reference Genome')
# ax.yaxis.set_major_locator(plt.MaxNLocator(8))
# plt.tight_layout()

ax.plot()
fig.suptitle("Genome Assembly")
ax.scatter(x=start, y=end, alpha=0.4)
ax.set_xlabel("K21 Contigs Length (bp)")
ax.set_ylabel("Reference Length (bp)")
fig.savefig("MAP.png")
plt.close(fig)

plt.plot()