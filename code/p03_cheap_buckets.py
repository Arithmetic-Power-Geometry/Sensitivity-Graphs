"""Audit cheap exact controls on all coordinate-permutation representatives.
Run after ./enumerate in same directory. Requires Python 3, standard library only.
"""
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for k in (4,5):
 reps=[int(x,16) for x in (ROOT/f'reps_k{k}.txt').read_text().split()]
 buckets=defaultdict(list)
 for mask in reps:
  S={i for i in range(32) if mask>>i&1}
  deg=[0]*32;direction=[0]*5
  for x in range(32):
   for j in range(5):
    y=x^(1<<j)
    if x<y and ((x in S)!=(y in S)):
     deg[x]+=1;deg[y]+=1;direction[j]+=1
  hist=tuple(deg.count(j) for j in range(6))
  cheap=(sum(direction),max(deg),hist,tuple(sorted(direction)),sum(v>0 for v in direction))
  buckets[cheap].append(mask)
 print('k',k,'canonical',len(reps),'cheap buckets',len(buckets),
       'multi-member',sum(len(x)>1 for x in buckets.values()))
 print('bucket size distribution',sorted(Counter(map(len,buckets.values())).items()))
