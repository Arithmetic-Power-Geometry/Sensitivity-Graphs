# P04 — exact exhaustive spectral and complexity refinement (2026-11-07)

## Scope and algorithm
All 35,960 weight-4 and 201,376 weight-5 Boolean truth sets on Q5 were enumerated and reduced under **input-coordinate permutations S5 only** (625 and 2,674 representatives). The canonical representatives were checked using exact sensitivity graph construction, BFS component diameters, and exact integer characteristic polynomials of the positive-to-negative Gram matrix MM^T via the Faddeev–LeVerrier recurrence. **No floating point or spectral-radius pruning.**

The cheap key is precisely (sensitive edge count, maximum sensitivity, full 0..5 sensitivity-degree histogram, sorted directional edge counts, essential-variable count). For any joint (cheap, exact spectrum) class whose geometry differs, the verifier computes *exactly* block sensitivity (disjoint sensitive-block packing DP), deterministic decision-tree depth (partial assignment minimax DP), one-sided certificate maxima C0/C1 (subcube enumeration), GF(2) polynomial degree (Möbius XOR), and real multilinear degree (integer Möbius).

## Results actually computed locally

| Statistic | k=4 | k=5 |
|---|---:|---:|
| Raw truth sets | 35,960 | 201,376 |
| S5 representatives | 625 | 2,674 |
| Cheap buckets (defined key) | 24 | 63 |
| Distinct exact Gram spectral keys | 27 | 86 |
| Joint cheap + exact spectrum buckets | 29 | 92 |
| Joint buckets with distinct component geometry | 0 | **1** |
| Geometry-discordant representatives | 0 | **36** |
| Strong classes surviving all Boolean complexity controls | 0 | **1** |

The unique k=5 geometry-discordant joint bucket consists of 18 S5 representatives with component sizes/diameters ((11,4),(9,4)) and 18 with ((16,6),(4,2)). Every one of the 36 shares the complexity tuple (bs,D,C0,C1,deg_GF2,deg_real)=(5,5,3,5,5,5). There are 18×18=324 cross-geometry pairs **at the S5-representative level**, not 324 inequivalent counterexamples. Under full hypercube input automorphisms (coordinate permutations and input bit flips), the 36 collapse to **two** orbits of 18 S5 representatives each, one per geometry. Thus this gives **one inequivalent pairing of two geometric types** within this specific strengthened class.

## Important limits and manuscript changes
1. k=4 cheap buckets=24, **not manuscript's 31**, for the fully specified cheap key. The manuscript's 26 'collision classes' uses an undefined or different refinement; do not assert it was reproduced. The 29 and 92 joint spectral keys are not the manuscript's collision-class counts and must not be substituted without definition.
2. The verified 'one' refers to **one joint cheap+exact-spectrum class with geometry separation** in the fixed-weight k=5 layer, not uniqueness of all possible five-variable examples, not global minimality, and not a proof that n=5 is the smallest possible dimension.
3. n<=4 and other k=5 layers were NOT exhaustively checked here. In particular, no global n<=4 negative theorem has been proved.
4. The exact 5×5 Gram polynomial is a certificate of the full sensitivity adjacency spectrum for a k=5 truth set, since the sensitivity graph is bipartite with block adjacency [0 M;M^T 0] and the number of cube vertices is fixed at 32.
5. The uploaded original source archive remains preserved on GitHub; original manuscript claims are not silently modified.

## Reproducibility
- Generate S5 representatives using committed `code/p03_enumerate.cpp` from the `code/` working directory; it writes `reps_k4.txt` and `reps_k5.txt` in 8-digit hexadecimal.
- Run committed `code/p04_exact_refinement.py` (Python >=3.8, standard library only), from the same directory. This independently reconstructs all cheap, exact spectral and geometry classes and refines the discordant class with Boolean complexities.
- Independently executed local C++/Python programs produced the table above. Original local files and outputs (including both representative lists, JSON reports) are available in the downloadable P04 archive. The GitHub committed script is a consolidated reproducible implementation; its source is logically equivalent to the locally run two-step Python scripts, but the exact GitHub version has not been executed within the GitHub environment. No CI success is claimed.
- Local SHA256 for executed `enumerate.cpp`: `2e28c555ca09e8198eb5aee4c39bf0bf4e3f0c84b2df8dbc4becbd5a2564b712`; `refine.py`: `2a506674105af82b5b2bc5e3d1d4e67bcbabe9ebd6e944da0d9aea5ad24f7b4c`; `complexity_refine.py`: `3b43c924e44c699e6a22cfcedba24d0ff7cd84bf449bf186df23dd0e71635957`; results `spectral_geometry_results.json`: `7941c5e128d8ec8aadc435a9c97eae02ed4c0cf8de2397134063363a0ff513ea`; `complexity_results.json`: `8970b9b0df03c07865d369387dc1ef50cfd8f225df7cd99b4d528a580b784e44`.

## Editorial conclusion
The five-variable fixed-weight k=5 one-class separation claim is now supported under an explicit reproducible equivalence and exact refinement. Correct the k=4 bucketing statement, specify the equivalence group, separate 'class' from pair counts, and refrain from asserting minimal dimension or literature novelty until further audits.
