# 2026.06.13
# tiny_diff.py

def diff_positions(a, b):

    length = max(len(a), len(b))

    for i in range(length):

        ca = a[i] if i < len(a) else "∅"
        cb = b[i] if i < len(b) else "∅"

        if ca != cb:

            yield i, ca, cb

old = "algorithm"
new = "algorxthms"

for idx, before, after in diff_positions(old, new):

    print(f"{idx}: {before} -> {after}")
