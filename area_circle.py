# 2026.10.29
# area_circle.py

import math

def circle_area(radius):

    return math.pi * radius ** 2

r = float(input("반지름 입력: "))
print(f"넓이: {circle_area(r):.2f}")
