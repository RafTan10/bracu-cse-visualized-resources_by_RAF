# CSE422 Lab Mid drill — Lab 2 — Two-point crossover (Part 2 of every GA assignment)
# Tag: ASSIGNMENT CORE
#
# Choose two cut points with the second strictly after the first; swap the middle segment.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_06_two_point.py
# Expected output when correct:
#     e.g. ('000000100', '111111011', 3, 7) for points 3 and 7 — the assignment's own example

import random
def two_point_crossover(p1, p2):
    """Return (child1, child2, pt1, pt2) with 1 <= pt1 < pt2 <= len(p1) - 1.
    The segment [pt1:pt2] is swapped between the parents."""
    # TODO
    pass

random.seed(3)
print(two_point_crossover("000111000", "111000111"))
