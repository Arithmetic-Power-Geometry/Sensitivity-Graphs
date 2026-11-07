# P03 — independent exact sparse-layer enumeration audit (2026-11-07)

## Reproducible executed checks
Source manuscript: `manuscript/TAG_main.tex` within verified uploaded `TAG_P01_Complete_Source_and_Build (1).zip` (SHA256 `b8f74b26238b5867de9a7853c3f051d8ff2cddf35fe5987b09df3e7582fd4919`). The manuscript reports k=4 (35960,625,31,26,0) and k=5 (201376,2674,63,63,1) for raw sets, canonical, cheap buckets, collision classes, strong separations.

Recompute: `g++ -O3 -std=c++17 code/p03_enumerate.cpp -o enumerate && ./enumerate`; move generated `reps_k4.txt` and `reps_k5.txt` to same directory as `code/p03_cheap_buckets.py`, then `python code/p03_cheap_buckets.py`.

- k=4: 35,960 raw masks; 35,960 visited; **625** distinct orbits under S5 input-coordinate permutations. Orbit size distribution: 5:5, 10:30, 15:15, 20:47, 30:123, 60:297, 120:108.
- k=5: 201,376 raw masks; 201,376 visited; **2674** distinct orbits under S5 input-coordinate permutations. Orbit size distribution: 1:2, 5:14, 10:42, 12:2, 15:20, 20:104, 30:316, 60:1198, 120:976.
- Exact cheap signature defined here as (sensitive edge count, max vertex sensitivity, full degree histogram, sorted directional edge counts, number of essential coordinates). Under THIS reproducible signature, k=4 has **24** cheap buckets, not manuscript's 31, and k=5 has **63**, matching manuscript. All 24 and all 63 buckets respectively contain more than one canonical representative.

## Symmetry audit
The verified orbit counts use **only input-coordinate permutations S5**. Output complementation S↦V\\S sends weight k to 32-k, so is not an internal action on k=4 or k=5 layers. Input bit flips x↦x⊕a are genuine hypercube automorphisms but were NOT included in these canonical counts. Full cube automorphism group is (C2)^5⋊S5; do not call the 625/2674 counts full cube-isomorphism orbit counts. Output complement preserves sensitivity graph but cannot be applied as a within-layer canonical operation here.

## Discrepancy and interpretation
The manuscript's cheap controls are verbally listed but its exact bucket key, implementation, and ordering are not provided in the uploaded source. Under the explicit exact controls as described in the manuscript, k=4 yields 24, not 31. This does **not** prove 31 impossible under some different undocumented bucketing rule; it does mean the claimed 31 is NOT reproduced and must not be represented as verified. Likewise '26 collision classes' and 'one strong separation' have no sufficiently precise published equivalence/refinement criterion in the manuscript and have NOT been independently reproduced. In particular, numerical spectral-radius pruning must never be used to exclude a candidate from an exact cospectrality completeness claim without an independently justified safe bound.

## Minimality scope
The exhaustive **orbit classification** is complete for n=5, k∈{4,5}, under S5 permutations. It does NOT establish that no strong separation exists at n≤4, nor that k=5 is minimal among all five-variable functions. No global minimality theorem is certified.

## Code provenance and remaining gates
Local C++ enumeration ran successfully and finished in under a second. Local Python exact bucket check ran successfully. The two source files have been committed in `code/`; the generated per-orbit representative lists are not yet committed. A full exact spectrum + complete Boolean invariant refinement for every orbit and a rigorous exhaustive negative-control claim are **pending**. Preserve the existing explicit A/B witness theorem; revise the search algorithm/table before submission.

Local original source SHA256: C++ `1959274764a717e69ba1b041c00ffe505f5bf39e3a5796377ac6253ed4c136f0`; Python `b28d2e1a20bb7c73e228bb5c14ec42f9c4483a07c047505674e5854448a5b27f`.
