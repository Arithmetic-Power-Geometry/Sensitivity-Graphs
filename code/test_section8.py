#!/usr/bin/env python3
"""Reproduce the Section 8 spectral-feature and quantum-walk witness tests."""
import csv
from pathlib import Path
import numpy as np
import networkx as nx
from scipy.linalg import expm

A = {0, 8, 16, 28, 31}
B = {0, 3, 5, 8, 16}
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'data'
OUT.mkdir(parents=True, exist_ok=True)

def sensitivity_graph(support):
    g = nx.Graph()
    g.add_nodes_from(range(32))
    for x in range(32):
        for bit in range(5):
            y = x ^ (1 << bit)
            if x < y and ((x in support) != (y in support)):
                g.add_edge(x, y)
    return g

records, matrices, eigs, histograms = [], {}, {}, {}
for name, support in [('A', A), ('B', B)]:
    g = sensitivity_graph(support)
    active = sorted(v for v, degree in g.degree if degree)
    h = g.subgraph(active)
    comps = sorted(nx.connected_components(h), key=len, reverse=True)
    sizes = [len(c) for c in comps]
    diameters = [nx.diameter(h.subgraph(c)) for c in comps]
    assert (len(active), g.number_of_edges(), len(list(nx.isolates(g)))) == (20, 21, 12)
    assert (sizes, diameters) == (([16, 4], [6, 2]) if name == 'A' else ([11, 9], [4, 4]))
    matrices[name] = nx.to_numpy_array(h, nodelist=active)
    eigs[name] = np.linalg.eigvalsh(matrices[name])
    histograms[name] = tuple(nx.degree_histogram(g))
    records.append([name, 20, 21, 12, ';'.join(map(str, sizes)), ';'.join(map(str, diameters)), max(diameters), 1.0])

assert histograms['A'] == histograms['B']
assert np.max(np.abs(eigs['A'] - eigs['B'])) < 1e-12
assert ((6 - 5)**2 + (4 - 5)**2) / 2 == 1
with (OUT / 'section8_exact_witness_results.csv').open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['graph','active_vertices','edges','isolates','component_sizes','component_diameters','max_diameter','minimum_two_sample_MSE'])
    writer.writerows(records)

walk_rows = []
for t in (0, 0.25, 0.5, 1, 2, 3):
    vals = {}
    for name in ('A', 'B'):
        u = expm(-1j * t * matrices[name])
        vals[name] = (np.trace(u) / 20, float(np.mean(np.abs(np.diag(u))**2)))
    delta = abs(vals['A'][0] - vals['B'][0])
    assert delta < 1e-12
    walk_rows.append([t, format(delta, '.16g'), format(vals['A'][1], '.12f'), format(vals['B'][1], '.12f')])
with (OUT / 'section8_quantum_walk_results.csv').open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time','normalized_trace_amplitude_absolute_difference','mean_return_probability_A','mean_return_probability_B'])
    writer.writerows(walk_rows)
assert abs(float(walk_rows[3][2]) - 0.276245) < 1e-5
assert abs(float(walk_rows[3][3]) - 0.283489) < 1e-5
print('PASS: Section 8 witness, MSE bound, and quantum-walk results')
