# 2026.09.15
# weekday_shift.py

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

shift = 3

for i in range(len(days)):

    print(days[i], "->", days[(i + shift) % len(days)])
