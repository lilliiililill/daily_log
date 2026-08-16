# 2026.08.17
# glitch_text.py

import random
import time

text = "오늘은 여기까지만 공부한다."
symbols = "!@#$%^&*?<>/"

for _ in range(20):

    broken = ""

    for char in text:

        if char != " " and random.random() < 0.3:

            broken += random.choice(symbols)

        else:

            broken += char

    print("\r" + broken, end = "", flush = True)
    time.sleep(0.08)

print("\r" + text)
