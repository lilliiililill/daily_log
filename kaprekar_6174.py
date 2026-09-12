# 2026.09.13
# kaprekar_6174.py

def kaprekar(n):

    count = 0

    while n != 6174:

        s = f"{n:04d}"

        big = int("".join(sorted(s, reverse = True)))
        small = int("".join(sorted(s)))

        n = big - small
        count += 1

        print(f"{big} - {small:04d} = {n:04d}")

    print(f"\n총 {count}번 만에 6174 도착!")

kaprekar(3524)
