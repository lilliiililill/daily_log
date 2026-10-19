# 2026.10.20
# binary_exponentition.py

def power(base, exp):

    result = 1

    while exp > 0:

        if exp % 2 == 1:

            result *= base

        base *= base
        exp //= 2

    return result

if __name__ == "__main__":

    print(power(2, 10))
    print(power(3, 5))
