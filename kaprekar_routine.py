# 2026.09.17
# kaprekar_routine.py

n = int(input("네 자리 숫자 (자릿수 다르게): "))

while n != 6174:

    d = f"{n:04d}"
    n = int("".join(sorted(d, reverse=True))) - int("".join(sorted(d)))

    print(n)
