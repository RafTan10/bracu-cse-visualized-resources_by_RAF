# CSE422 Lab Mid drill — Lab 1 — Maze A*: generate the four neighbours
# Tag: ASSIGNMENT CORE
#
# From Lab 1 Part 1 (maze solver). Try U, D, L, R; keep a move only if it is inside the grid, on a "0" cell and not visited; push with the new g, f and the path string.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_05_maze_neighbours.py
# Expected output when correct:
#     12
#     DDDLLDDRRRRD

import heapq

def manhattan(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def a_star_maze(n, m, start, goal, maze):
    sr, sc = start
    gr, gc = goal
    # heap entries: (f, g, row, col, path_string)
    heap = [(manhattan(sr, sc, gr, gc), 0, sr, sc, "")]
    visited = {}
    while heap:
        f, g, r, c, path = heapq.heappop(heap)
        if (r, c) in visited:
            continue
        visited[(r, c)] = g
        if (r, c) == (gr, gc):
            return g, path
        # TODO: for each of the four moves (U, D, L, R):
        #   compute the new cell (nr, nc)
        #   skip it if it is outside the maze, is a wall '#', or is already visited
        #   push (new_f, new_g, nr, nc, path + action) onto the heap
        pass
    return -1, None

maze = ["###0####", "#000000#", "###0#00#", "#000#00#", "#0######", "#000000#", "#####0##"]
cost, path = a_star_maze(7, 8, (0, 3), (6, 5), maze)
print(cost)
print(path)
