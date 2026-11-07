# P06 — Boolean-specific Gram spectral criterion and novelty boundary

## Proposition (exact common-neighbour criterion)
Let f:{0,1}^n→{0,1} and S=f^{-1}(1), |S|=k. Let d_S(x) be the number of neighbours of x inside S, and N(x) the n-cube neighbours. Define a symmetric k×k integer matrix H(S), indexed by S, with H_xx=n−d_S(x) and, for x≠y, H_xy=2−|N(x)∩N(y)∩S| when d_H(x,y)=2, otherwise H_xy=0.

For two functions f,g on the same n variables and with the same k, their full sensitivity graphs are adjacency-cospectral **if and only if** det(tI−H(S_f))=det(tI−H(S_g)). Equivalently, tr(H(S_f)^j)=tr(H(S_g)^j) for every j=1,…,k.

## Proof
Order vertices of Q_n by positive and negative inputs. The sensitivity adjacency matrix is [[0,M],[M^T,0]], with M the k×(2^n−k) incidence matrix of cube edges from S to its complement. Thus H=MM^T. The diagonal H_xx counts the n neighbours of x not in S, yielding n−d_S(x). For x≠y, H_xy counts common cube neighbours outside S. In a hypercube, two distinct vertices have common neighbours iff their Hamming distance is 2, and then exactly two. This yields the stated entries.

The characteristic polynomial of the full 2^n×2^n adjacency matrix is t^(2^n−2k) det(t² I_k−H) when 2^n≥2k, and the same expression is a polynomial identity (with cancellation) for arbitrary k; equivalently use the smaller output fibre to avoid negative exponents. At fixed n,k, equality of full adjacency polynomials is equivalent to equality of the k×k Gram characteristic polynomials because substitution t→t² is injective and the prefactor is fixed. Newton's identities over characteristic zero equate the characteristic coefficients with the first k power traces.

**Caution:** When k>2^(n−1), the displayed t exponent is negative, but the rational-expression identity is still valid after cancellation; for publication state the formula using the smaller fibre or use a determinant identity with formal cancellation.

## Verified five-variable witnesses
A={0,8,16,28,31}; B={0,3,5,8,16}.
H(A)=[[3,0,0,0,0],[0,4,1,2,0],[0,1,4,2,0],[0,2,2,5,2],[0,0,0,2,5]]
H(B)=[[3,2,2,0,0],[2,5,2,0,0],[2,2,5,0,0],[0,0,0,4,1],[0,0,0,1,4]].
Both have characteristic polynomial (t−5)(t−3)^2(t²−10t+13). Their full 32-vertex adjacency polynomials are t^22(t²−5)(t²−3)^2(t⁴−10t²+13). The active-vertex polynomial is t^10 times the nonzero factors.

## Executed falsification and exact tests
A separate local Python/SymPy script reconstructed H both directly from the formula and from M M^T for **all 256 Boolean functions on Q3**. All agreed. For A and B, the matrices and polynomial agreed with direct incidence multiplication. Negative control on Q3: S={1,2} and T={3,4} both have six sensitive edges (tr H=6), but H characteristic polynomials are t²−6t+5 versus t²−6t+9. Thus equality of edge count is insufficient; the criterion is falsifiable. Executable self-contained verifier committed at `code/p06_boolean_gram_criterion.py`.

## Novelty and prior-art boundary
The bipartite block identity, MM^T spectral reduction, common-neighbour counting, and Newton trace criterion are **standard mathematical consequences**, not an independently established novel theorem. The Boolean cube entry formula is a specialized explicit certificate that may be useful exposition, but novelty must be claimed primarily for the verified restricted Boolean sensitivity witness, its exhaustive/minimality certificate under precisely stated conditions, and the parity lift (subject to prior-art audit).

Godsil–McKay (1982) already constructed general cospectral graphs by switching; later switching generalizations exist, including 2020 and 2026 literature. **No proof is provided that the A/B sensitivity graphs cannot arise through GM switching**; do not claim a novel general cospectral construction or independence from GM switching. The special restriction to cube-edge cuts is the relevant distinction.

## References checked on publisher/author-hosted pages
- C. D. Godsil and B. D. McKay, 'Constructing cospectral graphs', Aequationes Mathematicae 25 (1982), 257–268, author-hosted PDF: https://users.cecs.anu.edu.au/~bdm/papers/GodsilMcKayCospectral.pdf
- 'On a theorem of Godsil and McKay concerning the construction of cospectral graphs', Linear Algebra and its Applications (2020), DOI https://doi.org/10.1016/j.laa.2020.05.025
- 'Switching methods of level 2 for the construction of cospectral graphs', Linear Algebra and its Applications (2026), DOI https://doi.org/10.1016/j.laa.2026.08.030
- W. H. Haemers, general cospectral graph context and references summarized at https://www.dwest.web.illinois.edu/regs/cospec.html

No exhaustive literature novelty claim is made. Full bibliographic metadata for the 2020/2026 papers and application of switching to the actual A/B graphs remain to be audited.
