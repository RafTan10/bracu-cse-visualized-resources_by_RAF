# CSE422 Lab Mid drill — Lab 3 — Alpha-beta: the MAX branch
# Tag: ASSIGNMENT CORE
#
# Fill in what a MAX node does: loop over its two children, keep the best, raise alpha, stop when alpha ≥ beta.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_02_ab_max.py
# Expected output when correct:
#     3
#     4

import math

def alpha_beta(depth, index, is_max, leaves, alpha, beta):
    """Alpha-beta on an implicit binary tree. Returns the node value."""
    if depth == 0:
        return leaves[index]
    if is_max:
        # TODO: best = -inf; for each child (2*index, 2*index+1):
        #   value = alpha_beta(child...), best = max(best, value), alpha = max(alpha, best)
        #   if beta <= alpha: break   (prune)
        # return best
        pass
    else:
        best = math.inf
        for i in range(2):
            value = alpha_beta(depth - 1, 2 * index + i, True, leaves, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print(alpha_beta(3, 0, True, [3, 6, 2, 3, 7, 1, 2, 0], -math.inf, math.inf))
print(alpha_beta(4, 0, True, [8,4,2,7,4,5,3,2,5,1,2,4,6,3,5,7], -math.inf, math.inf))   # Assignment Q17 tree
