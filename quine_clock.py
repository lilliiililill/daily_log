# 2026.07.19
# quine_clock.py

import time


while True:

    t = time.strftime("%H:%M:%S")

    print("\r" + "".join(chr(0x2800 + int(d)) if d.isdigit() else d for d in t), end = "")

    time.sleep(1)
    
