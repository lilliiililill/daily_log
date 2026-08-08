# 2026.08.09
# look_and_say.py

s = "1"

for _ in range(10):

    print(s)

    next_s  = ""
    count = 1

    for i in range(1, len(s) + 1):

        if i < len(s) and s[i] == s[i - 1]:

            count += 1

        else:

            next_s += str(count) + s[i - 1]

            count = 1

    s = next_s
