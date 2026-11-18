# CSE422 Lab Mid drill — Lab 3 — Gene-sequence utility function
# Tag: THIS SEMESTER
#
# From this semester's Lab 3. utility = −Σ wᵢ · |ASCII(gene[i]) − ASCII(target[i])| over max(len) positions; missing chars count as 0, missing weights as 1.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_06_gene_utility.py
# Expected output when correct:
#     0
#     -54
#     -137

# weights: a list of ints (last n digits of the student ID, n = len(target))
def utility(gene, target, weights):
    # TODO
    pass

print(utility("ATGC", "ATGC", [4, 0, 5, 2]))
print(utility("AGCT", "ATGC", [4, 0, 5, 2]))
print(utility("AGCTS", "ATGC", [4, 0, 5, 2]))
