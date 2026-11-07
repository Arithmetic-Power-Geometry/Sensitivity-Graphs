"""Independent exact n<=4 audit; Python 3 + SymPy, no floating point."""
from itertools import permutations
from collections import defaultdict
import sympy as sp

def audit(n):
    N=1<<n; full=(1<<N)-1
    maps=[]
    for p in permutations(range(n)):
        for shift in range(N):
            maps.append(tuple(shift ^ sum(((x>>i)&1)<<p[i] for i in range(n)) for x in range(N)))
    visited=bytearray(1<<N); groups=defaultdict(set); reps=0
    for mask in range(1<<N):
        if visited[mask]:continue
        reps+=1
        for mp in maps:
            y=sum(1<<mp[x] for x in range(N) if mask>>x&1)
            visited[y]=visited[y^full]=1
        f=[(mask>>x)&1 for x in range(N)]
        adj=[[] for _ in range(N)];direction=[0]*n
        for x in range(N):
            for j in range(n):
                y=x^(1<<j)
                if x<y and f[x]!=f[y]:
                    adj[x].append(y);adj[y].append(x);direction[j]+=1
        hist=tuple(sum(len(a)==i for a in adj) for i in range(n+1))
        side=[x for x in range(N) if f[x]==(sum(f)<=N//2)]
        if len(side)>N//2:side=[x for x in range(N) if x not in side]
        gram=sp.Matrix([[len(set(adj[x])&set(adj[y])) for y in side] for x in side])
        spectrum=tuple(int(c) for c in gram.charpoly().all_coeffs())
        comps=[];seen=set()
        for x in range(N):
            if x in seen or not adj[x]:continue
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
            comps.append((len(q),diameter))
        cert=[]
        for x in range(N):
            cert.append(next(k for k in range(n+1) if any(m.bit_count()==k and all(f[y]==f[x] for y in range(N) if y&m==x&m) for m in range(N))))
        c0=max((cert[x] for x in range(N) if f[x]==0),default=0)
        c1=max((cert[x] for x in range(N) if f[x]==1),default=0)
        from functools import lru_cache
        @lru_cache(None)
        def depth(known,ones):
            values={f[x] for x in range(N) if x&known==ones}
            if len(values)==1:return 0
            return 1+min(max(depth(known|1<<j,ones),depth(known|1<<j,ones|1<<j)) for j in range(n) if not known>>j&1)
        def bs(x):
            blocks=[m for m in range(1,N) if f[x^m]!=f[x]]
            @lru_cache(None)
            def pack(used):return max([0]+[1+pack(used|m) for m in blocks if not used&m])
            return pack(0)
        anf=f[:];real=f[:]
        for j in range(n):
            for m in range(N):
                if m>>j&1:anf[m]^=anf[m^(1<<j)];real[m]-=real[m^(1<<j)]
        sig=(spectrum,hist,tuple(sorted(direction)),max(map(len,adj)),max(bs(x) for x in range(N)),depth(0,0),tuple(sorted((c0,c1))),max((x.bit_count() for x in range(N) if anf[x]),default=0),max((x.bit_count() for x in range(N) if real[x]),default=0))
        groups[sig].add(tuple(sorted(comps,reverse=True)))
    return (n,1<<N,reps,len(groups),sum(len(v)>1 for v in groups.values()))

if __name__=='__main__':
    for n in range(1,5):print(*audit(n),sep=',',flush=True)
