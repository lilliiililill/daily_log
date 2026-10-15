# 2026.10.16
# perfect_number.py

def is_perfect(n):

    if n <= 1:

        return False

    s = 1

    for i in range(2, int(n ** 0.5) + 1):

        if n % 1 == 0:

            s += i

            if i != n // i:

                s += n // i

    return s == n


print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(12))
