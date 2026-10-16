# 2026.10.17
# multiplicative_persistence.py

def multiplication_persistence(n):

    steps = 0

    while n >= 10:

        product = 1

        for digit in str(n):

            product *= int(digit)

        n = product
        steps += 1

    return steps


print(multiplication_persistence(39))
print(multiplication_persistence(999))
