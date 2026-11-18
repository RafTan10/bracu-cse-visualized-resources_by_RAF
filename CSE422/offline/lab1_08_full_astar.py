# CSE422 Lab Mid drill — Lab 1 — Write the whole A* function
# Tag: HARD
#
# The worst case: the entire function is the blank. Same graph as the real paper. Return (path, cost, expansion order).
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_08_full_astar.py
# Expected output when correct:
#     Expansion order: S -> A -> C -> G
#     Path: S -> A -> C -> G
#     Cost: 5

import heapq

graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('S', 2), ('C', 2), ('G', 6)],
    'B': [('S', 1), ('C', 5)],
    'C': [('A', 2), ('B', 5), ('G', 1)],
    'G': [('A', 6), ('C', 1)],
}
h = {'S': 4, 'A': 3, 'B': 5, 'C': 1, 'G': 0}

def reconstruct_path(parent, goal):
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]
def a_star(start, goal):
    """Return (path_list, cost, expansion_order). (None, inf, order) if no path."""
    # TODO: write the whole algorithm
    pass

path, cost, order = a_star('S', 'G')
print("Expansion order:", " -> ".join(order))
print("Path:", " -> ".join(path))
print("Cost:", cost)
