# 2026.05.16
# rainbow.py

import time

colors = ["\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m"]
text = "Hello, Python!"

for i, char in enumerate(text):

    print(colors[i % len(colors)] + char, end = "", flush=True)
    time.sleep(0.1)

print("\033[0m")
