# 2026.09.30
# quiet_counter.py

words = ["rest", "code", "rest", "type", "code", "rest"]

count = {}

for word in words:

    count[word] = count.get(word, 0) + 1

for word, total in count.items():

    print(f"{word}: {total}")
