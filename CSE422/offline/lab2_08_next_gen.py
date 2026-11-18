# CSE422 Lab Mid drill — Lab 2 — Next generation with elitism
# Tag: ASSIGNMENT CORE
#
# Keep the best individual, then fill the rest of the population with mutated children of selected parents. Population size must stay constant.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_08_next_gen.py
# Expected output when correct:
#     a list of 4 strings whose first element is '1110'

import random

POPULATION_SIZE = 4
MUTATION_RATE = 0.1

def fitness(c):
    return c.count("1")

def selection(population):
    return random.choice(population)

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutation(c, rate=MUTATION_RATE):
    return "".join(("1" if b == "0" else "0") if random.random() < rate else b for b in c)
def next_generation(population):
    """Elitism: carry the single fittest individual forward unchanged.
    Fill the remaining slots with mutated children (crossover of two selected parents).
    Return a list of exactly POPULATION_SIZE chromosomes."""
    # TODO
    pass

random.seed(6)
print(next_generation(["0000", "1100", "1110", "0011"]))
