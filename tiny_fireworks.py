# 2026.10.07
# tiny_fireworks.py

import random

stars = ["*", "+", "x", "o", "."]

for i in range(1, 8):

    space = " " * random.randint(0, 15)
    boom = random.choice(stars) * random.randint(1, i)

    print(space + boom)
