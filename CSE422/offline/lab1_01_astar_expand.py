# CSE422 Lab Mid drill — Lab 1 — A*: the neighbour-expansion step
# Tag: REAL ASSESSMENT
#
# The exact TODO from the real lab assessment paper "A* Search Lab Question". Loop over neighbours, compute new g, update g/parent, push (f, neighbour).
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_01_astar_expand.py
# Expected output when correct:
#     Expansion order: S -> A -> C -> G
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

def a_star(start, goal):
    open_list = [(h[start], start)]   # (f, node)
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
        # ===================== TODO =====================
        # Loop over every neighbour of 'node'.
        # Compute the new g value through 'node'.
        # If it is better than the known g value (or the
        # neighbour has not been seen yet), update g and
        # parent, then push (f, neighbour) into open_list.
        # ================================================
        pass
    return None, float('inf'), order

path, cost, order = a_star('S', 'G')
print("Expansion order:", " -> ".join(order))
print("Path:", " -> ".join(path))
print("Cost:", cost)
