# 2026.09.22
# tiny_password.py

word = "python"

password = ""

for i, char in enumerate(word):

    password += char.upper() if i % 2 == 0 else char

print(password[::-1])
