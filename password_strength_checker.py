# 2026.06.27
# password_strength_checker.py

password = input("비밀번호 입력: ")

score = 0

if len(password) >= 8:

    score += 1

if any(c.isupper() for c in password):

    score += 1

if any(c.islower() for c in password):

    score += 1

if any(c.isdigit() for c in password):

    score += 1

special = "!@#$%^&*()-_=+[]{};:,.<>/?"

if any(c in special for c in password):

    score += 1

levels = [

    "매우 약함",
    "약함",
    "보통",
    "좋음",
    "강함",
    "매우 강함"

    ]

print(f"\n점수: {score}/5")
print("강도:", levels[score])
