# 2026.10.11
# hamming_dist.py

def hamming(s1, s2):

    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

print(hamming("karolin", "kathrin"))
