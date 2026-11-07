#!/usr/bin/env python3
"""Exact independently reconstructible witness check; Python 3 + SymPy."""
from itertools import combinations
from functools import lru_cache
import sympy as sp

A = {int(x,2) for x in ("00000","01000","10000","11100","11111")}
B = {int(x,2) for x in ("00000","00011","00101","01000","10000")}
V=range(32)

def check(S):
    f=lambda x:int(x in S)
    adj={x:set() for x in V}
    dirs=[0]*5
    for x in V:
        for i in range(5):
            y=x^(1<<i)
            if x<y and f(x)!=f(y):
                adj[x].add(y);adj[y].add(x);dirs[i]+=1
    todo={x for x in V if adj[x]}; components=[]
    while todo:
        q=[min(todo)]; seen={q[0]}
        for u in q:
            for v in adj[u]:
                if v not in seen:seen.add(v);q.append(v)
        todo-=seen
        diameter=0
        for s in seen:
            dist={s:0}; queue=[s]
            for u in queue:
                for v in adj[u]:
                    if v not in dist:dist[v]=dist[u]+1;queue.append(v)
            diameter=max(diameter,max(dist.values()))
        components.append((len(seen),diameter))
    neg=sorted(set(V)-S)
    M=sp.Matrix([[int(y in adj[x]) for y in neg] for x in sorted(S)])
    t=sp.symbols('t')
    gram=sp.factor((M*M.T).charpoly(t).as_expr())
    def bs_at(x):
        blocks=[m for m in range(1,32) if f(x^m)!=f(x)]
        @lru_cache(None)
        def pack(used):
            return max([0]+[1+pack(used|m) for m in blocks if not (used&m)])
        return pack(0)
    def c_at(x):
        for k in range(6):
            for inds in combinations(range(5),k):
                mask=sum(1<<i for i in inds)
                if all(f(y)==f(x) for y in V if x&mask==y&mask):return k
    @lru_cache(None)
    def D(mask,values):
        values&=mask
        ys=[x for x in V if x&mask==values]
        if len({f(x) for x in ys})==1:return 0
        return 1+min(max(D(mask|(1<<i),values),D(mask|(1<<i),values|(1<<i))) for i in range(5) if not (mask>>i&1))
    anf=[f(x) for x in V]; real=anf[:]
    for i in range(5):
        for m in V:
            if m>>i&1:
                anf[m]^=anf[m^(1<<i)]
                real[m]-=real[m^(1<<i)]
    result=dict(edges=sum(map(len,adj.values()))//2,active=sum(bool(adj[x]) for x in V),isolates=sum(not adj[x] for x in V),
                degree_histogram={i:sum(len(adj[x])==i for x in V) for i in range(6)},
                direction_counts=sorted(dirs),components=sorted(components,reverse=True),
                gram_polynomial=str(gram),sensitivity=max(map(len,adj.values())),
                block_sensitivity=max(bs_at(x) for x in V),decision_tree_depth=D(0,0),
                certificate_complexity=max(c_at(x) for x in V),
                C0=max(c_at(x) for x in V if x not in S),
                C1=max(c_at(x) for x in S),
                positive_certificates=sorted(c_at(x) for x in S),
                GF2_degree=max(x.bit_count() for x in V if anf[x]),
                real_degree=max(x.bit_count() for x in V if real[x]))
    return result

if __name__=='__main__':
    import json
    a,b=check(A),check(B)
    print(json.dumps({'A':a,'B':b},indent=2))
    expected='(t - 5)*(t - 3)**2*(t**2 - 10*t + 13)'
    assert a['gram_polynomial']==b['gram_polynomial']==expected
    assert a['components']==[(16,6),(4,2)]
    assert b['components']==[(11,4),(9,4)]
    for z in (a,b):
        assert (z['edges'],z['active'],z['isolates'])==(21,20,12)
        assert (z['sensitivity'],z['block_sensitivity'],z['decision_tree_depth'])==(5,5,5)
        assert (z['C0'],z['C1'],z['certificate_complexity'])==(3,5,5)
        assert z['positive_certificates']==[4,4,4,5,5]
        assert z['direction_counts']==[3,3,5,5,5]
        assert (z['GF2_degree'],z['real_degree'])==(5,5)
    print('PASS: exact witness checks')
