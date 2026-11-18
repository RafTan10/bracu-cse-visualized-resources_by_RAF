# CSE422 Lab Mid drill — Lab 2 — Fitness with penalties (course-scheduling GA)
# Tag: TWEAK
#
# From the Summer-24 assignment. Chromosome = T segments of N bits. fitness = −(overlap penalty + consistency penalty).
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab2_09_schedule_fitness.py
# Expected output when correct:
#     -5
#     0

# N courses, T timeslots. Chromosome length N*T. Segment t (bits t*N .. t*N+N-1) = timeslot t,
# bit i inside a segment = whether course i is scheduled in that slot.
def fitness(chromosome, N, T):
    """overlap penalty: for each timeslot, (#courses scheduled - 1) if more than one is scheduled.
    consistency penalty: for each course, 1 if it is not scheduled exactly once.
    Return -(overlap + consistency)."""
    # TODO
    pass

print(fitness("110110010", 3, 3))
print(fitness("100010001", 3, 3))
