# 2026.05.25
# no_more_algorithms_today.py

import random
import time

print("🔮 오늘의 휴식 가이드 🔮")
time.sleep(1)

luck = ["대박! 뭘 해도 될 날", "평온함 그 자체", "조용히 침대와 물아일체 추천"]
food = ["치킨에 맥주", "따뜻한 라면", "달달한 아이스아메리카노"]

print()
print(f"🍀 오늘의 운세: {random.choice(luck)}")
print(f"🍕 추천 야식: {random.choice(food)}")
