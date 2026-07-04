# 2026.07.05
# life_progress.py

from datetime import datetime

birth = input("생년월일 입력 (YYYY-MM-DD): ")

birth_date = datetime.strptime(birth, "%Y-%m-%d")
now = datetime.now()

life_expectancy = 80

total_seconds = life_expectancy * 365.2425 * 24 * 60 * 60
lived_seconds = (now - birth_date).total_seconds()

progress = max(0, min(100, lived_seconds / total_seconds * 100))

bar = "█" * int(progress // 2) + "-" * (50 - int(progress // 2))

print(f"\n인생 진행도")
print(f"[{bar}]")
print(f"{progress:.2f}%")
