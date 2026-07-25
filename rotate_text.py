# 2026.07.25
# rotate_text.py

text = input("문장 입력: ")

for i in range(len(text)):

    print(text[i:] + text[:i])
