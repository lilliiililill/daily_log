# 2026.10.31
# emirp_numbers.py

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            return False

    return True


def is_emirp(n):

    s = str(n)
    rev = int(s[::-1])
    return s != s[::-1] and is_prime(n) and is_prime(rev)

emirps = [i for i in range(1, 1001) if is_emirp(i)]
print(emirps)
