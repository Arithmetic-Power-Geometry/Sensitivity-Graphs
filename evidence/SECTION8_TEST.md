# Section 8 witness and quantum-walk calculations

Run `python3 code/test_section8.py` from the repository root (or any working directory). The script reconstructs the five-variable sensitivity graphs from the two specified positive supports, checks the matched spectra and degree histograms, verifies the distinct component geometries and the two-observation MSE lower bound, and computes the continuous-time quantum-walk mean vertex-return probabilities at six times. It writes `data/section8_exact_witness_results.csv` and `data/section8_quantum_walk_results.csv`.

Dependencies: NumPy, NetworkX, SciPy. Matrix exponentials are evaluated numerically; the exact cospectrality certificate is supplied by the separate symbolic verification scripts. This is a finite computational illustration, not a trained GNN or a physical experiment. At t=1, the mean vertex-return probabilities are 0.276244566701 (A) and 0.283488994981 (B).
