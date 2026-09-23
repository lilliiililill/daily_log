# 2026.09.23
# unique_chars.py

text = "banana"

result = "".join(char for char in text if text.count(char) == 1)

print(result)
