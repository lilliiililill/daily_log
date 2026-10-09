# 2026.10.09
# tiny_progress.py

from datetime import date

today = date.today()

messages = [

    "오늘도 한 걸음 전진!",
    "작은 꾸준함이 실력을 만든다.",
    "쉬어가는 것도 공부의 일부!",
    "어제보다 조금만 나아지자."

    ]

index = today.toordinal() % len(messages)

print(f"[{today}] {messages[index]}")
