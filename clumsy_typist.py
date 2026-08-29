# 2026.08.30
# clumsy_typist.py

import random

text = input("문장 입력: ")
result = list(text)

for i in range(1, len(result)):

    if result[i] != " " and random.random() < 0.15:

        result[i - 1], result[i] = result[i], result[i - 1]

print("".join(result))
