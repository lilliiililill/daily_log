# 2026.10.13
# monte_carlo.py

import random

def estimate_pi(n):

    inside = 0

    for _ in range(n):

        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:

            inside += 1


    return 4 * inside / n

print(estimate_pi(100000))
