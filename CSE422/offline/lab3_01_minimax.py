# CSE422 Lab Mid drill — Lab 3 — Plain minimax on an implicit binary tree
# Tag: ASSIGNMENT CORE
#
# Leaves are given in a list; node (depth, index) has children 2*index and 2*index+1 one level down. Return the root value.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_01_minimax.py
# Expected output when correct:
#     3
#     3

# leaves: list of 2**depth utility values, left to right
def minimax(depth, index, is_max, leaves):
    """Value of the node at (depth levels above the leaves, index among its level).
    depth == 0 means the node is leaves[index]."""
    # TODO
    pass

print(minimax(3, 0, True, [3, 6, 2, 3, 7, 1, 2, 0]))   # Pacman tree from Lab 3
print(minimax(2, 0, True, [3, 5, 2, 9]))
