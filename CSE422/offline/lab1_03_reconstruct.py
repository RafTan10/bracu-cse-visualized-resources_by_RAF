# CSE422 Lab Mid drill — Lab 1 — reconstruct_path from the parent dictionary
# Tag: LIKELY BLANK
#
# The helper every search program has. Follow parent links from the goal back to the start, then reverse.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab1_03_reconstruct.py
# Expected output when correct:
#     ['S', 'A', 'C', 'G']

# parent maps each node to the node it was reached from; the start maps to None
def reconstruct_path(parent, goal):
    # TODO: follow parent links from goal back to the start,
    # then return the path in start -> goal order
    pass

parent = {'S': None, 'A': 'S', 'C': 'A', 'G': 'C', 'B': 'S'}
print(reconstruct_path(parent, 'G'))
