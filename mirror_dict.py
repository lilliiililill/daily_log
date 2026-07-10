# 2026.07.11
# mirror_dict.py

text = "pizza"

d = {c: i for i, c in enumerate(text)}
print(d)
print("".join(text[d[c]] for c in reversed(d)))
