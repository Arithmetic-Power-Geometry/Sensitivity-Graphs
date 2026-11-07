# P07 — parity-lift infinite-family theorem (2026-11-07)

## Base functions
Let A={0,8,16,28,31} and B={0,3,5,8,16}, using 5-bit integers for cube vertices. The indicator functions f_A and f_B have cospectral sensitivity graphs but different active component profiles: A has (size,diameter) (16,6),(4,2), B has (11,4),(9,4), with 12 isolated vertices each. Their shared full 32-vertex adjacency characteristic polynomial is t^22(t^2−5)(t^2−3)^2(t^4−10t^2+13).

For r>=0 let p_r(z)=z_1 XOR ... XOR z_r (p_0=0) and define F_r(x,z)=f_A(x) XOR p_r(z), G_r(x,z)=f_B(x) XOR p_r(z).

## Theorem and proof: graph structure and spectra
The sensitivity graph of f XOR p_r is the Cartesian product Γ(f) □ Q_r: an x-coordinate flip changes the output iff it changes f, and every z-coordinate flip changes parity. Therefore the adjacency matrix is A_f ⊗ I_(2^r)+I_32 ⊗ A_(Q_r). The eigenvalues of Q_r are r−2j, each with multiplicity binom(r,j), for 0<=j<=r. If p_f(t) is the characteristic polynomial of A_f, then the lift has characteristic polynomial product over j of p_f(t−r+2j)^binom(r,j). This holds at r=0. Since the base polynomials coincide, all lifted pairs are cospectral, using exact polynomial identities.

The Cartesian product of connected graphs is connected and has additive distances, so components for F_r are (16·2^r,6+r), (4·2^r,2+r), and twelve copies of (2^r,r). For G_r they are (11·2^r,4+r), (9·2^r,4+r), and twelve copies of (2^r,r). The convention Q_0 is a singleton. In particular, the two lifted graphs are nonisomorphic for every r.

## Exact Boolean measures
At each input, sensitivity is s_f(x)+r: all r parity directions are sensitive. For block sensitivity, any disjoint sensitive-block family has at most r blocks meeting a parity coordinate; all remaining blocks are disjoint sensitive x-blocks for f. Thus bs(F_r;x,z)<=bs(f;x)+r. Taking an optimal disjoint family of x-blocks plus the r singleton parity blocks gives equality. Since both bases have s=bs=5, both lifts have s=bs=5+r.

Every certificate must fix all parity coordinates; otherwise flipping a free z bit changes the output. Once z is fixed, an x-certificate for f is necessary and sufficient. Thus pointwise C(F_r;x,z)=C(f;x)+r. For r>=1, either z parity is possible, so C0(F_r)=C1(F_r)=r+max(C0(f),C1(f))=r+5. At r=0 both bases have (C0,C1)=(3,5).

Querying all parity bits and then an optimal decision tree for f gives D(F_r)<=D(f)+r=5+r. The base has a point with certificate complexity 5, hence its lift has pointwise certificate complexity 5+r, giving D(F_r)>=5+r. Therefore D=5+r for all r>=0.

Over GF(2), F_r=f+z_1+...+z_r, so deg_GF2(F_r)=5 for all r (NOT 5+r). Over the reals, 1−2F_r=(1−2f) product_j (1−2z_j). The base has real degree 5, so the nonzero top-degree coefficient survives, yielding deg_R(F_r)=5+r. All 5+r variables are essential. Every lifted degree is s_f(x)+r, and the base degree histogram is shifted by r and multiplied by 2^r. Base directional edge counts multiply by 2^r; each new parity direction has 32·2^(r−1) sensitive edges for r>=1.

## Executed exact checks and limits
A locally executed Python standard-library program built all sensitivity graphs for r=0,1,2, checked all connected-component sizes and BFS diameters, and checked the degree histograms. It independently enumerated all certificates, block sensitivity packings, deterministic decision-tree depths and real/GF(2) Möbius degrees for r=0,1. All tests passed. The reproducible script is committed as code/p07_parity_lift_verify.py. No numerical eigenvalue computations or GitHub CI run are claimed.

The Cartesian-product spectral rule and parity degree identities are classical mechanisms, not new general theorems. The explicit infinite family of nonisomorphic cospectral Boolean sensitivity graphs is the result being documented; priority/novelty relative to all prior examples still requires a dedicated literature audit. Ordinary deterministic decision-tree depth is used; parity decision-tree depth is a different complexity model.

## References with checked source metadata
- Rahul Jain, Hartmut Klauck and Miklos Santha, "Optimal direct sum results for deterministic and randomized decision tree complexity", Information Processing Letters 110 (2010), 893–897. DOI: 10.1016/j.ipl.2010.07.020. Context only: our depth proof uses pointwise certificates, not a general direct-sum result.
- Zhiqiang Zhang and Yaoyun Shi, "On the parity complexity measures of Boolean functions", Theoretical Computer Science 411 (2010), 2612–2618. DOI: 10.1016/j.tcs.2010.03.027. Distinct parity-decision-tree model.
- Avishay Tal, "Properties and Applications of Boolean Function Composition", ECCC TR12-163 (2012), https://eccc.weizmann.ac.il/report/2012/163/. Composition context.
