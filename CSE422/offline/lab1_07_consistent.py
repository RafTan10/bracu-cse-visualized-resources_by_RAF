# CSE422 Lab Mid drill — Lab 1 — Tweak: consistency checker on a weighted graph
# Tag: TWEAK
#
# Return every edge (u, v) that violates h(u) ≤ c(u, v) + h(v). Check both directions of each undirected edge.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_07_consistent.py
# Expected output when correct:
#     [('B', 'A')]

# graph: node -> [(neighbour, cost), ...]  (undirected: both directions listed)
def inconsistent_edges(graph, h):
    """Return a sorted list of (u, v) pairs with h[u] > cost(u, v) + h[v]."""
    # TODO
    pass

graph = {'S': [('A', 10), ('B', 2)], 'A': [('S', 10), ('B', 2), ('G', 10)],
         'B': [('S', 2), ('A', 2), ('G', 15)], 'G': [('A', 10), ('B', 15)]}
h = {'S': 12, 'A': 7, 'B': 10, 'G': 0}
print(inconsistent_edges(graph, h))
