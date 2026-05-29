# 2026.05.30
# random_walk.py

import random

x, y = 0, 0
steps = 30

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

path = [(x, y)]

for _ in range(steps):

    dx, dy = random.choice(moves)

    x += dx
    y += dy

    path.append((x, y))

print("final:", (x, y))
print("path:", path)
