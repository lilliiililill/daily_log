# 2026.05.09
# rock_paper_scissors.py

import random

choices = ["가위", "바위", "보"]
beats = {"가위": "바위", "바위": "보", "보": "가위"}

user = input("가위 / 바위 / 보 중 하나를 입력하세요: ")

com = random.choice(choices)

print(f"컴퓨터: {com}")

if user == com:

    print("비겼어요!")

elif beats[user] == com:

    print("이겼어요! 🎉")

else:

    print("졌어요... 😢")
