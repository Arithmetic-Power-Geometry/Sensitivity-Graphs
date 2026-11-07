# Cospectral Boolean sensitivity graphs

This repository contains the LaTeX manuscript, exact computational certificates, exhaustive enumerations, and reproducible vector figures for **Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family**.

The five-variable indicator supports are `A={00000,01000,10000,11100,11111}` and `B={00000,00011,00101,01000,10000}`. Their sensitivity graphs have 21 edges and 12 isolated vertices; the active adjacency spectra coincide, with characteristic polynomial `t^10(t^2-5)(t^2-3)^2(t^4-10t^2+13)`. Their active component sizes differ: `(16,4)` against `(11,9)`; their diameter profiles differ: `(6,2)` against `(4,4)`.

## Exact reproduction

Python 3.10+, Node.js, a C++17 compiler, and the libraries in `requirements.txt` are required.

```bash
python3 -m pip install -r requirements.txt
bash reproduce.sh
```

The script regenerates all five-variable coordinate-permutation representatives for support sizes four and five. The corresponding exact counts are:

| k | Raw sets | S5 representatives | Cheap classes | Gram-polynomial classes | Joint classes | Strong discordant classes |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 35,960 | 625 | 24 | 27 | 29 | 0 |
| 5 | 201,376 | 2,674 | 63 | 86 | 92 | 1 |

The exhaustive exclusion at n≤4 uses the full input-coordinate permutation/translation and output-complement action, not the fixed-layer S5 action. Its orbit counts are 2, 4, 14 and 222; none has discordant component geometry under the matched strengthened signature. The infinite family follows the exact Cartesian-product identity for XOR with parity on fresh variables. No numerical spectral-radius pruning is used.

The generated output files, including the canonical representatives, exact refinement results and regression logs, appear in `results/`. A GitHub Actions workflow executes the same checks and retains its generated results as an artifact.

## Manuscript

```bash
bash build_manuscript.sh
```

This regenerates three vector figures from the actual Boolean witness and structural descriptions, then builds `manuscript/TAG_main.pdf` from `manuscript/TAG_main.tex` and `manuscript/references.bib` with latexmk and Biber. The manuscript suppresses the printed title/author block in accordance with the *Theory & Applications of Graphs* final-form guidelines. Figure descriptions are maintained in `figures/ALT_TEXT.md`.

## Contents

- `code/`: exact witness checks, independent JavaScript comparison, C++ orbit enumeration, exact Gram spectral refinement, n≤4 audit, parity-lift checks and figure generation.
- `data/`: five-variable support records and independent reference totals.
- `evidence/`: exact computation and theorem verification records.
- `references/`: research reference register.
- `manuscript/`: reproducible paper source and verified citation-key bibliography.
- `figures/`: original generated vector figures and descriptive text.
- `.github/workflows/`: automated reproduction.

The search uses no observational or third-party dataset: all instances are mathematically generated Boolean truth sets. The repo supplies the code needed to regenerate those instances and their computed invariants. Mathematical priority and journal acceptance are separate questions from successful reproduction.

## Research provenance

The original verification files and evidence derive from [Physical-Computational-Feasibility](https://github.com/Arithmetic-Power-Geometry/Physical-Computational-Feasibility). The manuscript is taken from the latest supplied source and uses the present repository's URL for its data and code availability statement.
