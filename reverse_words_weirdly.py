# 2026.08.25
# reverse_words_weirdly.py

text = "퇴근 하고 싶다 진짜"

words = text.split()

for i, word in enumerate(words):

    if i % 2 == 1:

        words[i] = word[::-1]

print(" ".join(words))
