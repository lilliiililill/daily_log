# 2026.11.03
# first_unique_char.py

def first_unique_char(s):

    freq = {}

    for char in s:

        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):

        if freq[char] == 1:

            return i

    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
