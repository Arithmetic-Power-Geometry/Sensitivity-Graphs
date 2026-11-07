#!/usr/bin/env python3
"""Check all regenerated exact enumeration counts stated in the manuscript."""
from pathlib import Path
import json

root=Path(__file__).resolve().parent.parent
results=json.loads((root/"code"/"p04_exact_results.json").read_text())
expected={"4":(625,24,27,29,0,0),"5":(2674,63,86,92,1,1)}
for k,values in expected.items():
    got=results[k]
    counts=(got["representatives"],got["cheap_buckets"],got["spectral_buckets"],
            got["joint_buckets"],got["discordant_geometry_classes"],got["strong_classes"])
    assert counts==values,(k,counts,values)

strong=results["5"]["strong"]
assert len(strong)==1
assert len(strong[0]["representatives"])==36
assert sorted(strong[0]["geometry_counts"].values())==[18,18]
minimum=[
    "1,4,2,2,0",
    "2,16,4,4,0",
    "3,256,14,14,0",
    "4,65536,222,222,0",
]
rows=(root/"results"/"minimum_dimension.csv").read_text().strip().splitlines()[1:]
assert rows==minimum,(rows,minimum)
print("PASS: all fixed-weight and minimum-dimension counts match the article")
