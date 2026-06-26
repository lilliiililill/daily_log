# 2026.06.26
# matrix_rain.py

import random
import time
import shutil


width = shutil.get_terminal_size().columns

chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&*"

drops = [0] * width

while True:

    print("".join(
        random.choice(chars) if random.random() > 0.97 else " "
        for _ in range(width)

    ))

    time.sleep(0.05)
