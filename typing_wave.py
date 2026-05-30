# 2026.05.31
# typing_wave.py

import time

text = "PYTHON IS FUN"

for i in range(30):

    line = ""

    for j, ch in enumerate(text):

        if i % len(text) == j:

            line += ch.lower()

        else:

            line += ch

    print(line)
    time.sleep(0.1)
