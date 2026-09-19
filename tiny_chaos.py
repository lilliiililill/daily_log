# 2026.09.20
# tiny_chaos.py

import random

words = ["집중", "휴식", "버그", "성공", "커피", "퇴근"]


random.shuffle(words)

print("오늘의 개발자 운세:", "-> ".join(words[:3]))
