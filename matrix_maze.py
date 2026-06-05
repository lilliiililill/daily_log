# 2026.06.06
# matrix_maze.py

import random
import time

WALLS = ["/", "|"]

print("무한 미로 생성기를 시작합니다. (종료: Ctrl + C)")
time.sleep(1)

try:

    while True:

        line = "".join(random.choice(WALLS) for _ in range(80))
        print(line)
        time.sleep(0.05)

except KeyboardInterrupt:

    print("\n미로 생성을 종료합니다. 수고하셨습니다!")

