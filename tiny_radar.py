# 2026.09.06
# tiny_radar.py

import random
import time

target = random.randint(1, 20)

for i in range(1, 21):

    distance = abs(target - i)
    signal = max(0, 10 - distance)

    print(f"{i: 02} | {'█' * signal}")
    time.sleep(0.05)

print("\n📡 신호원 위치: {target}")
