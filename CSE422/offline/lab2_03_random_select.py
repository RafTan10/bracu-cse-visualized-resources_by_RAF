# CSE422 Lab Mid drill — Lab 2 — Vault GA: random selection
# Tag: REAL ASSESSMENT
#
# Third TODO of the real GA assessment: pick one chromosome at random, ignoring fitness.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_03_random_select.py
# Expected output when correct:
#     Vault unlocked! Master Key 1111111111 found in generation N.

import random

CHROMOSOME_LENGTH = 10
POPULATION_SIZE = 4
MUTATION_RATE = 0.1
MAX_GENERATIONS = 3000
MASTER_KEY = "1" * CHROMOSOME_LENGTH   # 1111111111

def create_population(size=POPULATION_SIZE, length=CHROMOSOME_LENGTH):
    return ["".join(random.choice("01") for _ in range(length)) for _ in range(size)]

def fitness(chromosome):
    return sum(1 for a, b in zip(chromosome, MASTER_KEY) if a == b)
# ---------------- Selection ----------------
def selection(population):
    """Random selection: pick one chromosome from the population at random,
    without looking at fitness."""
    # TODO
    # (The line below will give an error until you write your code above.)
    return chromosome   # you may change this variable

# ---------------- Step 3a: Single-point crossover ----------------
def crossover(parent1, parent2):
    """Cut both parents at the same random point and swap the tails."""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# ---------------- Step 3b: Mutation ----------------
def mutation(chromosome, rate=MUTATION_RATE):
    """Each bit has a `rate` chance of being flipped."""
    new_chromosome = ""
    for bit in chromosome:
        if random.random() < rate:
            new_chromosome += "1" if bit == "0" else "0"
        else:
            new_chromosome += bit
    return new_chromosome

# ---------------- Main GA loop (do not change) ----------------
def genetic_algorithm():
    population = create_population()
    for generation in range(MAX_GENERATIONS):
        scores = [fitness(c) for c in population]
        if MASTER_KEY in population:
            print("Vault unlocked! Master Key " + MASTER_KEY + " found in generation " + str(generation) + ".")
            return MASTER_KEY, generation
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutation(child1))
            new_population.append(mutation(child2))
        population = new_population[:POPULATION_SIZE]
    best = max(population, key=fitness)
    print("Not found. Best: " + best + " (fitness " + str(fitness(best)) + ")")
    return best, MAX_GENERATIONS

random.seed(1)
genetic_algorithm()
