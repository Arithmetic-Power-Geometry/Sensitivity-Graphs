#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p results
python3 code/p02_verify_witness.py > results/witness_verification.txt
node code/p02_independent_js_check.js > results/javascript_independent.txt
g++ -O3 -std=c++17 code/p03_enumerate.cpp -o code/enumerate
(cd code && ./enumerate) | tee results/orbit_counts.txt
python3 code/p03_cheap_buckets.py | tee results/cheap_class_counts.txt
python3 code/p04_exact_refinement.py > results/exact_refinement.json
printf 'n,all_functions,full_NPN_orbits,exact_spectrum_complexity_classes,geometry_discordant_classes\n' > results/minimum_dimension.csv
python3 code/p05_minimum_dimension_independent.py >> results/minimum_dimension.csv
python3 code/p06_boolean_gram_criterion.py > results/gram_checks.txt
python3 code/p07_parity_lift_verify.py > results/parity_lift_checks.txt
python3 code/verify_expected.py
cp code/reps_k4.txt code/reps_k5.txt results/
echo "Exact reproduction completed; see results/."
