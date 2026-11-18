# CSE422 Lab Mid drill — Lab 3 — Minimax over a shrinking pool (gene game)
# Tag: THIS SEMESTER
#
# Agents alternately take a nucleotide from the pool and append it to the sequence. MAX wants high utility, MIN wants low. Return (best_utility, best_sequence) for the player to move.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_07_gene_minimax.py
# Expected output when correct:
#     (-54, 'AGCT')
#     (-153, 'TGAC')

def utility(gene, target, weights):
    N = max(len(gene), len(target))
    total = 0
    for i in range(N):
        w = weights[i] if i < len(weights) else 1
        a = ord(gene[i]) if i < len(gene) else 0
        b = ord(target[i]) if i < len(target) else 0
        total -= w * abs(a - b)
    return total
def minimax(pool, gene, is_max, target, weights):
    """pool: list of remaining nucleotides; gene: sequence built so far.
    Terminal when the pool is empty: return (utility, gene).
    Otherwise try every nucleotide in the pool (remove it, append it, recurse with the other player)
    and return the (value, sequence) that is best for the current player (first best on ties)."""
    # TODO
    pass

print(minimax(['A', 'T', 'C', 'G'], "", True, "ATGC", [4, 0, 5, 2]))
print(minimax(['A', 'T', 'C', 'G'], "", True, "GCAT", [8, 8, 1, 1]))
