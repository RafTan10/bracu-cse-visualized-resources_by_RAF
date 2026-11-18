# CSE422 Lab Mid drill — Lab 1 — Admissibility checker (BFS from the goal)
# Tag: ASSIGNMENT CORE
#
# Lab 1 Part 2. Compute the true distance of every node to the goal with BFS, then list the nodes whose h is larger than that.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_06_admissible.py
# Expected output when correct:
#     0
#     Here nodes 1, 2, 3, 4, 5 are inadmissible.

from collections import deque

def bfs_from_goal(graph, goal):
    """True (unweighted) distance from every node to the goal."""
    dist = {goal: 0}
    queue = deque([goal])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist
def inadmissible_nodes(graph, heuristics, goal):
    """Return the sorted list of nodes whose heuristic overestimates
    the true distance to the goal. Unreachable nodes have distance infinity."""
    # TODO
    pass

graph = {1: [2, 4], 2: [1, 3], 3: [2, 6, 5], 4: [1, 5], 5: [4, 6, 3], 6: [3, 5]}
heur  = {1: 6, 2: 4, 3: 2, 4: 5, 5: 2, 6: 0}
bad = inadmissible_nodes(graph, heur, 6)
if not bad:
    print("The heuristic values are admissible.")
else:
    print(0)
    print("Here nodes " + ", ".join(str(x) for x in bad) + " are inadmissible.")
