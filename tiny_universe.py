# 2028.08.29
# tiny_universe.py

import random

words = ["별", "비", "고양이", "커피", "달", "바람", "파이썬"]

a ,b = random.sample(words, 2)

print(f"오늘의 세계에서는 '{a}'와 '{b}'만 존재합니다.")
print(f"그리고 {random.randint(1, 99)}분 뒤, 아무 일도 일어나지 않습니다.")
