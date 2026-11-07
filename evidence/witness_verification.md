# P02 independent witness verification — 2026-11-07

Independent local Python/SymPy verifier constructed the full 32-vertex sensitivity graphs directly from the two truth sets:
A = {00000,01000,10000,11100,11111};
B = {00000,00011,00101,01000,10000}.

## Exact independently computed results

| Property | A | B |
|---|---|---|
| Sensitive edges | 21 | 21 |
| Active vertices | 20 | 20 |
| Isolates | 12 | 12 |
| Degree histogram | 0:12,1:10,2:4,3:2,4:2,5:2 | identical |
| Sorted direction counts | (3,3,5,5,5) | identical |
| Active component sizes | (16,4) | (11,9) |
| Corresponding diameters | (6,2) | (4,4) |
| Maximum sensitivity | 5 | 5 |
| Block sensitivity | 5 | 5 |
| Deterministic decision-tree depth | 5 | 5 |
| Maximum certificate complexity | 5 | 5 |
| One-sided maxima (C0,C1) | (3,5) | (3,5) |
| Positive-input individual certificate sizes | 4,4,4,5,5 | 4,4,4,5,5 |
| GF(2) degree | 5 | 5 |
| Real multilinear degree | 5 | 5 |
| Essential variables | 5 | 5 |
| Gram characteristic polynomial | (t-5)(t-3)^2(t^2-10t+13) | identical |

Proof mechanism: Let M be the 5-by-27 positive-to-negative cube cut incidence matrix. The sensitivity adjacency matrix is [0 M; M^T 0]. The full adjacency polynomial is lambda^22 * (lambda^2-5)*(lambda^2-3)^2*(lambda^4-10*lambda^2+13), and the active adjacency polynomial is lambda^10 times the same nonzero factors. The equality is exact over the integers.

The verifier used (a) full edge construction; (b) BFS from every vertex in each active component; (c) exact SymPy Gram characteristic polynomial; (d) dynamic programming over all sensitive disjoint blocks for block sensitivity; (e) exact enumeration of subcube certificates; (f) minimax DP on all 3^5 partial assignments for deterministic decision-tree depth; and (g) Möbius transforms for GF(2) and real polynomial degree. Local code SHA256 3eca556e25c2e670684ef8ec14304d15375ded8941f225160d3f52650ee93d86; output JSON SHA256 d3d430ef385d708a2e86def24979e033e134a3ac0baea3f79b58ac5ab692c19d.

**Critical scope:** These results are from one newly written verifier; a separately implemented independent checker has NOT yet been executed. This verifies the explicit pair computationally but does not certify the manuscript's exhaustive 201376-case search, canonical representative counts, global minimality or novelty.

**Important terminology:** The manuscript's {3,5} denotes the one-sided maximum certificate complexities (C0,C1), not the set of positive-input individual certificate sizes, which is {4,5} for both witnesses. Do not silently change this distinction.

**P01 status:** still PARTIAL; original source ZIP, original figures, complete TAG source and PDF remain uncommitted due to local binary-transfer limitation. P02 status: PARTIAL; local exact verification passed, but full verifier source and independent second implementation must be committed/run before closure.
