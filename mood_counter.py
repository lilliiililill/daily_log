# 2026.09.16
# mood_counter.py

text = "happy coding day"

count = {}

for char in text.replace(" ", ""):

    count[char] = count.get(char, 0) + 1

print(count)
