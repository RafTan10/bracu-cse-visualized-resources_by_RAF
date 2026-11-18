# CSE422 Lab Mid drill — Lab 2 — Bit-flip mutation with a rate
# Tag: ASSIGNMENT CORE
#
# Every bit flips independently with probability rate. Return the new string.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_07_mutation.py
# Expected output when correct:
#     a 10-bit string with roughly 3 ones (depends on the seed)

import random
def mutation(chromosome, rate):
    """Each bit has a `rate` chance of being flipped (0 -> 1, 1 -> 0)."""
    # TODO
    pass

random.seed(5)
print(mutation("0000000000", 0.3))
