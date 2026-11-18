# CSE422 Lab Mid drill — Lab 1 — Tweak: turn A* into Uniform-Cost Search
# Tag: TWEAK
#
# Same program, but the frontier is ordered by g only (h is ignored). A one-line change in the push — you must know which line.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_04_ucs.py
# Expected output when correct:
#     Expansion order: S -> B -> A -> C -> G
#     Path: S -> A -> C -> G
#     Cost: 5

import heapq

# Graph as an adjacency list: node -> [(neighbour, edge_cost), ...]
graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('S', 2), ('C', 2), ('G', 6)],
    'B': [('S', 1), ('C', 5)],
    'C': [('A', 2), ('B', 5), ('G', 1)],
    'G': [('A', 6), ('C', 1)],
}
# Heuristic values h(n)
h = {'S': 4, 'A': 3, 'B': 5, 'C': 1, 'G': 0}

def reconstruct_path(parent, goal):
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]

def ucs(start, goal):
    open_list = [(0, start)]   # (f, node)
    g = {start: 0}                    # best known cost from start
    parent = {start: None}
    closed = set()
    order = []                        # expansion order
    while open_list:
        f, node = heapq.heappop(open_list)
        if node in closed:
            continue
        closed.add(node)
        order.append(node)
        if node == goal:
            return reconstruct_path(parent, goal), g[goal], order
        # TODO: expand 'node' so that the frontier is ordered by g ONLY
        # (uniform-cost search). Update g/parent exactly as in A*.
        pass
    return None, float('inf'), order

path, cost, order = ucs('S', 'G')
print("Expansion order:", " -> ".join(order))
print("Path:", " -> ".join(path))
print("Cost:", cost)
