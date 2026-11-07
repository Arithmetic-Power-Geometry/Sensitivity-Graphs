#!/usr/bin/env python3
"""Exact Boolean common-neighbour Gram certificate, Python + SymPy."""
import sympy as sp
def gram(n,positives):
 S=set(positives);X=sorted(S)
 return sp.Matrix(len(X),len(X),lambda i,j:
  n-sum((X[i]^(1<<a)) in S for a in range(n)) if i==j else
  (2-sum((X[i]^(1<<a)) in S for a in range(n)
       if (X[i]^(1<<a)^X[j]).bit_count()==1)
   if (X[i]^X[j]).bit_count()==2 else 0))
def direct(n,S):
 S=set(S);X=sorted(S);Y=sorted(set(range(1<<n))-S)
 M=sp.Matrix([[int((x^y).bit_count()==1) for y in Y] for x in X])
 return M*M.T
A=[0,8,16,28,31];B=[0,3,5,8,16]
for name,S in [('A',A),('B',B)]:
 G=gram(5,S)
 assert G==direct(5,S)
 print(name,G.tolist(),sp.factor(G.charpoly().as_expr()))
assert gram(5,A).charpoly().as_expr()==gram(5,B).charpoly().as_expr()
for mask in range(256):
 S=[x for x in range(8) if mask>>x&1]
 assert gram(3,S)==direct(3,S)
X=[1,2];Y=[3,4]
assert gram(3,X).trace()==gram(3,Y).trace()==6
assert gram(3,X).charpoly().as_expr()!=gram(3,Y).charpoly().as_expr()
print('PASS: all 256 Q3 truth sets and non-cospectral same-edge control')
