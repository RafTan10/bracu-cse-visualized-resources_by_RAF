# CSE422 Lab Mid drill — Lab 1 — Greedy Best-First: the neighbour step
# Tag: REAL ASSESSMENT
#
# The exact TODO from the real assessment "CSE422 Lab 01 section 2". Same skeleton as A*, but the frontier is ordered by h only and a node is pushed once.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_02_gbfs_expand.py
# Expected output when correct:
#     Expansion order: S -> B -> G
#     Path: S -> B -> G
#     Cost: 11

import heapq

graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('S', 2), ('C', 4), ('G', 12)],
    'B': [('S', 4), ('C', 1), ('G', 7)],
    'C': [('A', 4), ('B', 1), ('G', 3)],
    'G': [('A', 12), ('B', 7), ('C', 3)],
}
h = {'S': 6, 'A': 4, 'B': 3, 'C': 3, 'G': 0}

def reconstruct_path(parent, goal):
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]

def greedy_best_first(start, goal):
    open_list = [(h[start], start)]   # (h, node)  <- ordered by h ONLY
    g = {start: 0}                     # cost of the path used (only for printing)
    parent = {start: None}
    closed = set()
    order = []                         # expansion order
    while open_list:
        _, node = heapq.heappop(open_list)
        if node in closed:
            continue
        closed.add(node)
        order.append(node)
        if node == goal:
            return reconstruct_path(parent, goal), g[goal], order
        # ===================== TODO =====================
        # Loop over every neighbour of 'node'.
        # If the neighbour is not in closed and has not
        # been seen yet (not in parent):
        #   - record its path cost in g
        #   - set its parent to 'node'
        #   - push (h, neighbour) into open_list
        # ================================================
        pass
    return None, float('inf'), order

path, cost, order = greedy_best_first('S', 'G')
print("Expansion order:", " -> ".join(order))
if path is None:
    print("NO PATH FOUND")
else:
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
