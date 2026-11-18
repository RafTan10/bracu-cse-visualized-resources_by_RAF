# CSE422 Lab Mid drill — Lab 3 — Mortal Kombat: the best-of-3 round loop
# Tag: ASSIGNMENT CORE
#
# Alternate who starts each round; Sub-Zero starting ⇒ MAX root; utility +1 = Sub-Zero wins, −1 = Scorpion. First to two round wins takes the game.
#
# Fill in the TODO block below (and nothing else), then run:
#     python check.py lab3_04_mk_rounds.py
# Expected output when correct:
#     Game Winner: <name>
#     Total Rounds Played: 2 or 3
#     Winner of Round 1: ...   (depends on the random leaves)

import random, math

DEPTH = 5

def alpha_beta(depth, index, is_max, leaves, alpha, beta):
    if depth == 0:
        return leaves[index]
    if is_max:
        best = -math.inf
        for i in range(2):
            best = max(best, alpha_beta(depth - 1, 2 * index + i, False, leaves, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    best = math.inf
    for i in range(2):
        best = min(best, alpha_beta(depth - 1, 2 * index + i, True, leaves, alpha, beta))
        beta = min(beta, best)
        if beta <= alpha: break
    return best

def generate_leaves():
    return [random.choice([-1, 1]) for _ in range(2 ** DEPTH)]
def mortal_kombat(first_player):
    """first_player: 0 = Scorpion starts, 1 = Sub-Zero starts.
    Returns (game_winner, round_winners_list).
    Each round: new random leaves; root is MAX iff Sub-Zero starts; +1 => 'Sub-Zero', -1 => 'Scorpion'.
    The player who did NOT start the previous round starts the next. Stop when someone has 2 round wins."""
    # TODO
    pass

random.seed(7)
winner, rounds = mortal_kombat(0)
print("Game Winner:", winner)
print("Total Rounds Played:", len(rounds))
for i, w in enumerate(rounds, 1):
    print("Winner of Round " + str(i) + ":", w)
