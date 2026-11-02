# 2026.11.02
# str_str.py

def str_str(haystack: str, needle: str) -> int:

    if not needle:

        return 0

    for i in range(len(haystack) - len(needle) + 1):

        if haystack[i: i + len(needle)] == needle:

            return i

    return -1


print(str_str("hello", "ll"))
print(str_str("aaaaa", "bba"))
print(str_str("", ""))
