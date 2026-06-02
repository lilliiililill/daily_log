# 2026.06.03
# mood_bar.py

import random
import time

mood = random.randint(1, 10)

print("오늘의 컨디션 측정 중...")

for i in range(mood + 1):

    print("" * i)
    time.sleep(0.15)

print(f"\n오늘의 기분 점수: {mood}/10")
