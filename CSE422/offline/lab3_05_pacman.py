# CSE422 Lab Mid drill — Lab 3 — Pacman dark magic decision
# Tag: ASSIGNMENT CORE
#
# Given the fixed 8-leaf tree, compute the normal minimax value and the value of using magic on the left or right ghost (max of that subtree minus cost c). Decide.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_05_pacman.py
# Expected output when correct:
#     The new minimax value is 5. Pacman goes right and uses dark magic
#     The minimax value is 3. Pacman does not use dark magic

LEAVES = [3, 6, 2, 3, 7, 1, 2, 0]
def pacman_game(c):
    """Return (normal_value, best_magic_value, direction, use_magic)
    where direction is 'left' or 'right' (prefer right on a tie) and use_magic is True
    only if best_magic_value > normal_value."""
    # TODO
    pass

for c in (2, 5):
    normal, magic, side, use = pacman_game(c)
    if use:
        print("The new minimax value is " + str(magic) + ". Pacman goes " + side + " and uses dark magic")
    else:
        print("The minimax value is " + str(normal) + ". Pacman does not use dark magic")
