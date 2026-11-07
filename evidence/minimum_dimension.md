# P05 — minimum-dimension audit for all Boolean functions n<=4 (2026-11-07)

## Exact conclusion
For every n=1,2,3,4, **no two Boolean functions** have sensitivity graphs with different multisets of (nontrivial component size, component diameter) while sharing the exact adjacency spectrum and the strengthened Boolean-complexity signature tested below. In fact, the implemented combined signature distinguishes every equivalence orbit in n<=4.

| n | all functions 2^(2^n) | full NPN orbits | combined-signature classes | geometry-discordant classes |
|---|---:|---:|---:|---:|
| 1 | 4 | 2 | 2 | 0 |
| 2 | 16 | 4 | 4 | 0 |
| 3 | 256 | 14 | 14 | 0 |
| 4 | 65,536 | 222 | 222 | 0 |
| TOTAL | 65,812 | 242 | 242 | 0 |

**Equivalence group:** input automorphisms x ↦ P x ⊕ a, P in S_n and a in {0,1}^n, together with output complementation f ↦ 1−f. Group size 2^(n+1)n!, equal to 4,16,96,768 for n=1,2,3,4. Each transformation preserves sensitivity graph up to cube vertex relabeling. Output complementation swaps C0 and C1; hence their **sorted pair** is the invariant. Input bit flips are included, unlike earlier S5-only fixed-weight enumeration.

**Exact tested signature:** full sensitivity adjacency spectrum encoded by the integer Gram characteristic polynomial on the smaller output fiber (number of vertices 2^n fixed), sensitivity degree histogram, sorted directional edge counts, maximum sensitivity, block sensitivity, deterministic decision-tree depth, sorted one-sided certificate maxima, GF(2) degree, real multilinear degree. Geometry is multiset of (size,diameter) of nontrivial connected components. The polynomial for an empty Gram matrix is 1. Every operation is exact integer arithmetic; no numerical eigenvalues, tolerance, or floating-point pruning.

## Reproduction and independent cross-check
1. A C++17 implementation enumerated every truth-table mask, marked its orbit under all input permutations, bit flips and output complement, and computed exact integer Gram characteristic coefficients using Faddeev–LeVerrier. It produced the table above. Local source SHA256: `726e33f47167a19cace109c25c3613ca67e74f58a11977efc701fb73a47f7ff7`.
2. A separately written Python/SymPy implementation independently performed the same full orbit reduction and exact graph, Gram, BFS, sensitivity, block-sensitivity, certificate, decision-tree and degree calculations. It independently returned **(1,4,2,2,0), (2,16,4,4,0), (3,256,14,14,0), (4,65536,222,222,0)**. Python source committed as `code/p05_minimum_dimension_independent.py`; locally executed source SHA256 `5bb0449db7a73f28980f00987a6f693943ece275647c203acb5a5d5dfa49b6b1`.
3. Raw C++ result CSV SHA256 `f2e0a6d67a7063f0464d0e6cc03e3ca603c68080d5d0a50c06e0489f363613a1`; its contents are committed as `evidence/P05_RESULTS.csv`. The independent Python script is fully executable from GitHub and reproduces the table.

## Proof scope
Every Boolean function is in exactly one enumerated orbit because for each unvisited mask the algorithm applies every element of the finite group and marks both output orientations. The sensitivity graph, exact spectrum, complexity signature and component geometry are invariant under the group (with C0/C1 unordered). Thus testing every orbit representative suffices. The zero discordant-class result proves the **specified finite n<=4 negative statement**, conditional on correct execution of the provided independently implemented exact verifiers.

Combined with the separately verified n=5 witness, this establishes that **five is the minimum dimension for the particular spectrum-and-strengthened-complexity-matched, component-geometry-separated phenomenon**.

## Limitations
- This is a finite exhaustive computational certificate, not a short symbolic classification theorem or a literature novelty proof.
- A broader cospectrality-only question, without the full matched signature, is **not** ruled out by this audit.
- The original n=5,k=4 cheap-bucket discrepancy (31 reported vs 24 under our defined key) is unchanged.
- The C++ source and its binary are included in the downloadable local P05 evidence ZIP but the C++ source is not yet separately committed to GitHub. No GitHub CI run has been claimed.
