#!/usr/bin/env python3
"""Exact n=5, k=4/5 refinement. No floats. Python standard library.
Run p03_enumerate.cpp in the code/ directory first (writes reps_k4.txt and reps_k5.txt
as 8-digit HEX masks); then run python3 p04_exact_refinement.py.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def characteristic(G):
 n=len(G);B=[[int(i==j) for j in range(n)] for i in range(n)];coeff=[1]
 for k in range(1,n+1):
  P=[[sum(G[i][t]*B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
  trace=sum(P[i][i] for i in range(n))
  assert trace%k==0
  c=-trace//k;coeff.append(c)
  B=[[P[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
 return tuple(coeff)

def graph(mask):
 S={x for x in range(32) if mask>>x&1};adj=[[] for _ in range(32)];directions=[0]*5
 for x in range(32):
  for j in range(5):
   y=x^(1<<j)
   if x<y and ((x in S)!=(y in S)):
    adj[x].append(y);adj[y].append(x);directions[j]+=1
 hist=tuple(Counter(map(len,adj)).get(j,0) for j in range(6))
 cheap=(sum(directions),max(map(len,adj)),hist,tuple(sorted(directions)),sum(d>0 for d in directions))
 positives=sorted(S)
 gram=[[len(set(adj[x]).intersection(adj[y])) for y in positives] for x in positives]
 spectrum=characteristic(gram)
 seen=set();components=[]
 for x in range(32):
  if not adj[x] or x in seen:continue
  q=[x];seen.add(x)
  for u in q:
   for v in adj[u]:
    if v not in seen:seen.add(v);q.append(v)
  diameter=0
  for root in q:
   dist={root:0};queue=[root]
   for u in queue:
    for v in adj[u]:
     if v not in dist:dist[v]=dist[u]+1;queue.append(v)
   diameter=max(diameter,max(dist.values()))
  components.append((len(q),diameter))
 return cheap,spectrum,tuple(sorted(components,reverse=True))

def complexity(mask):
 f=[(mask>>x)&1 for x in range(32)]
 @lru_cache(None)
 def certificate(x):
  for k in range(6):
   for m in range(32):
    if m.bit_count()==k and all(f[y]==f[x] for y in range(32) if x&m==y&m):return k
  raise AssertionError()
 @lru_cache(None)
 def depth(known,ones):
  xs=[x for x in range(32) if x&known==ones]
  if len({f[x] for x in xs})==1:return 0
  return 1+min(max(depth(known|1<<i,ones),depth(known|1<<i,ones|1<<i)) for i in range(5) if not known&(1<<i))
 @lru_cache(None)
 def block_sensitivity(x):
  blocks=[m for m in range(1,32) if f[x^m]!=f[x]]
  @lru_cache(None)
  def pack(used):return max([0]+[1+pack(used|m) for m in blocks if not used&m])
  return pack(0)
 anf=f[:];real=f[:]
 for i in range(5):
  for m in range(32):
   if m&(1<<i):
    anf[m]^=anf[m^(1<<i)];real[m]-=real[m^(1<<i)]
 return (max(block_sensitivity(x) for x in range(32)),depth(0,0),
         max(certificate(x) for x in range(32) if not f[x]),
         max(certificate(x) for x in range(32) if f[x]),
         max(m.bit_count() for m in range(32) if anf[m]),
         max(m.bit_count() for m in range(32) if real[m]))

def run():
 results={}
 for k in (4,5):
  reps=[int(s,16) for s in (HERE/('reps_k%d.txt'%k)).read_text().split()]
  cheap=defaultdict(list);spec=defaultdict(list);joint=defaultdict(list)
  for m in reps:
   c,p,g=graph(m);cheap[c].append(m);spec[p].append(m);joint[(c,p)].append((m,g))
  discordant=[vals for vals in joint.values() if len({g for m,g in vals})>1]
  strong=[]
  for vals in discordant:
   refined=defaultdict(list)
   for m,g in vals:refined[complexity(m)].append((m,g))
   for signature,sub in refined.items():
    if len({g for m,g in sub})>1:
     strong.append({'signature':signature,'representatives':[m for m,g in sub],
                    'geometry_counts':dict(Counter(str(g) for m,g in sub))})
  results[str(k)]={'representatives':len(reps),'cheap_buckets':len(cheap),
   'spectral_buckets':len(spec),'joint_buckets':len(joint),
   'discordant_geometry_classes':len(discordant),'strong_classes':len(strong),
   'strong':strong}
 assert results['4']['representatives']==625 and results['5']['representatives']==2674
 assert results['4']['discordant_geometry_classes']==0
 assert results['5']['discordant_geometry_classes']==1
 assert results['5']['strong_classes']==1
 print(json.dumps(results,indent=2))
 (HERE/'p04_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':run()
