# 2026.07.17
# chaos.py

x = 0.1

for _ in range(30):

    x = 3.9 * x * (1 - x)
    print("█" * int(x * 40))
