#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 code/generate_figures.py
(cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error TAG_main.tex)
pdfinfo manuscript/TAG_main.pdf | grep -E 'Pages:|Page size:'
