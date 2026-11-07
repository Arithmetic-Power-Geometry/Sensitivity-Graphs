#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
A={0,8,16,28,31};B={0,3,5,8,16}
def graph(S,r):
 n=5+r;N=1<<n;f=[int(((x&31) in S)^((x>>5).bit_count()%2)) for x in range(N)]
 adj=[[] for _ in range(N)]
 for x in range(N):
  for j in range(n):
   y=x^(1<<j)
   if x<y and f[x]!=f[y]:adj[x].append(y);adj[y].append(x)
 seen=set();comps=[]
 for x in range(N):
  if x in seen:continue
  q=[x];seen.add(x)
  for u in q:
   for v in adj[u]:
    if v not in seen:seen.add(v);q.append(v)
  dia=0
  for root in q:
   dist={root:0};queue=[root]
   for u in queue:
    for v in adj[u]:
     if v not in dist:dist[v]=dist[u]+1;queue.append(v)
   dia=max(dia,max(dist.values()))
  comps.append((len(q),dia))
 return f,adj,Counter(comps)
def complexity(f,n):
 N=1<<n
 C=[min(m.bit_count() for m in range(N) if all(f[y]==f[x] for y in range(N) if y&m==x&m)) for x in range(N)]
 @lru_cache(None)
 def depth(mask,val):
  xs=[x for x in range(N) if x&mask==val]
  if len({f[x] for x in xs})==1:return 0
  return 1+min(max(depth(mask|1<<j,val),depth(mask|1<<j,val|1<<j)) for j in range(n) if not mask>>j&1)
 def bs(x):
  blocks=[m for m in range(1,N) if f[x^m]!=f[x]]
  @lru_cache(None)
  def pack(used):return max([0]+[1+pack(used|m) for m in blocks if not m&used])
  return pack(0)
 anf=f[:];real=f[:]
 for j in range(n):
  for m in range(N):
   if m>>j&1:anf[m]^=anf[m^(1<<j)];real[m]-=real[m^(1<<j)]
 return (max(sum(f[x]!=f[x^(1<<j)] for j in range(n)) for x in range(N)),max(bs(x) for x in range(N)),depth(0,0),max(C[x] for x in range(N) if not f[x]),max(C[x] for x in range(N) if f[x]),max(m.bit_count() for m in range(N) if anf[m]),max(m.bit_count() for m in range(N) if real[m]))
for r in range(3):
 for name,S,large,small,diams in [('A',A,16,4,(6,2)),('B',B,11,9,(4,4))]:
  f,adj,comps=graph(S,r)
  expected=Counter({(2**r,r):12,(large*2**r,diams[0]+r):1,(small*2**r,diams[1]+r):1})
  assert comps==expected,(r,name,comps,expected)
  if r<=1:
   got=complexity(f,5+r)
   want=(5+r,5+r,5+r,3,5,5,5) if r==0 else (5+r,5+r,5+r,5+r,5+r,5,5+r)
   assert got==want,(r,name,got,want)
  print('PASS',name,'r=',r,'components=',dict(comps))
print('ALL P07 EXACT CHECKS PASS')
