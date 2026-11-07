#!/usr/bin/env python3
"""Deterministic vector figures for the TAG manuscript."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import networkx as nx

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
A = {0, 8, 16, 28, 31}
B = {0, 3, 5, 8, 16}

def sensitivity_graph(positive):
    graph = nx.Graph()
    graph.add_nodes_from(range(32))
    for x in range(32):
        for coordinate in range(5):
            y = x ^ (1 << coordinate)
            if x < y and ((x in positive) != (y in positive)):
                graph.add_edge(x, y)
    graph.remove_nodes_from(list(nx.isolates(graph)))
    return graph

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8), constrained_layout=True)
for axis, (name, positive) in zip(axes, [('A', A), ('B', B)]):
    graph = sensitivity_graph(positive)
    components = sorted(nx.connected_components(graph), key=len, reverse=True)
    profile = [(len(c), nx.diameter(graph.subgraph(c))) for c in components]
    expected = [(16, 6), (4, 2)] if name == 'A' else [(11, 4), (9, 4)]
    assert profile == expected
    shift = 0.0
    for idx, component in enumerate(components):
        subgraph = graph.subgraph(component)
        unit_positions = nx.spring_layout(subgraph, seed=20261107 + idx, iterations=200)
        scale = 1.4 if idx == 0 else 0.95
        positions = {v: (float(x) * scale + shift, float(y)) for v, (x, y) in unit_positions.items()}
        nx.draw_networkx_edges(subgraph, positions, ax=axis, width=1.2, edge_color='black')
        nx.draw_networkx_nodes(subgraph, positions, ax=axis, node_size=46, node_color='#175a7a')
        shift += 3.3 if idx == 0 else 1.7
    axis.set_title(f'$f_{name}$: components {expected}', fontsize=12, pad=16)
    axis.axis('off')
fig.savefig(OUT / 'figure1_witness_graphs.pdf', bbox_inches='tight')
plt.close(fig)

fig, axis = plt.subplots(figsize=(10.5, 4.5))
axis.set_xlim(0, 10.5)
axis.set_ylim(0, 4.5)
axis.axis('off')
rows = [
    ('Local controls', '21 edges; identical degree histograms'),
    ('Directional controls', 'Identical sorted edge counts (3, 3, 5, 5, 5)'),
    ('Boolean complexity', 'Same $bs$, $D$, certificates, and polynomial degrees'),
    ('Spectral control', 'Same complete adjacency characteristic polynomial'),
]
for idx, (head, detail) in enumerate(rows):
    y = 3.55 - 0.93 * idx
    axis.add_patch(FancyBboxPatch((0.38, y), 9.7, 0.74, boxstyle='round,pad=0.025', facecolor='white', edgecolor='black', linewidth=1))
    axis.text(0.63, y + 0.36, head, ha='left', va='center', fontsize=12, fontweight='bold')
    axis.text(3.65, y + 0.36, detail, ha='left', va='center', fontsize=10)
axis.text(5.25, 0.28, 'Component sizes and diameters still differ', ha='center', fontsize=12, fontweight='bold')
fig.savefig(OUT / 'figure2_invariant_hierarchy.pdf', bbox_inches='tight')
plt.close(fig)

fig, axis = plt.subplots(figsize=(10.5, 3.1))
axis.set_xlim(0, 10.5)
axis.set_ylim(0, 3.1)
axis.axis('off')
for idx, (n, representation) in enumerate([(5, '$G_f$  □  $Q_0$'), (6, '$G_f$  □  $Q_1$'), (7, '$G_f$  □  $Q_2$')]):
    x = 0.4 + 3.45 * idx
    axis.add_patch(FancyBboxPatch((x, 1.2), 2.55, 1.0, boxstyle='round,pad=0.05', facecolor='white', edgecolor='black', linewidth=1))
    axis.text(x + 1.275, 1.86, f'$N={n}$', fontsize=12, ha='center', va='center', fontweight='bold')
    axis.text(x + 1.275, 1.44, representation, fontsize=13, ha='center', va='center')
    if idx < 2:
        axis.annotate('', xy=(x+3.39,1.72), xytext=(x+2.68,1.72), arrowprops={'arrowstyle':'->','color':'black','lw':1.3})
axis.text(5.25, 0.57, 'Each added parity coordinate is sensitive at every lifted input', ha='center', fontsize=11)
fig.savefig(OUT / 'figure3_parity_lift.pdf', bbox_inches='tight')
plt.close(fig)
print('PASS: 3 deterministic vector figures')
