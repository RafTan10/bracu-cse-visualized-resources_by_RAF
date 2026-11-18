# CSE422 Lab Mid drill — Lab 2 — Single-point crossover
# Tag: ASSIGNMENT CORE
#
# Cut both parents at the same random point (1 … len−1) and swap the tails. Return both children and the cut point.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_05_single_point.py
# Expected output when correct:
#     ('110010', '101011', 3)   (the point depends on the seed)

import random
def single_point_crossover(p1, p2):
    """Return (child1, child2, point). point is chosen with random.randint(1, len(p1) - 1)."""
    # TODO
    pass

random.seed(2)
print(single_point_crossover("110011", "101010"))
