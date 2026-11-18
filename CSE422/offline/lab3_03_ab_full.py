# CSE422 Lab Mid drill — Lab 3 — Write the whole alpha-beta function (with pruned-count)
# Tag: HARD
#
# Return (value, number_of_branches_pruned). Used in the Mortal Kombat solution.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_03_ab_full.py
# Expected output when correct:
#     (3, 0)

import math
def alpha_beta(depth, index, is_max, leaves, alpha, beta):
    """Return (value, pruned) where pruned counts every child branch that was skipped."""
    # TODO: whole function
    pass

print(alpha_beta(3, 0, True, [3, 6, 2, 3, 7, 1, 2, 0], -math.inf, math.inf))
