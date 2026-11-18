# CSE422 Lab Mid drill — Lab 2 — Tournament selection
# Tag: HIGH PROBABILITY
#
# Every GA assignment ends with "research tournament selection — might be helpful in the near future". Pick k random individuals, return the fittest of them.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_04_tournament.py
# Expected output when correct:
#     one of the four strings (whichever wins the random tournament)

import random

def fitness(chromosome):
    return chromosome.count("1")
def tournament_selection(population, k=2):
    """Pick k distinct individuals at random; return the one with the highest fitness."""
    # TODO
    pass

random.seed(4)
pop = ["0000", "1100", "1110", "1111"]
print(tournament_selection(pop, 2))
